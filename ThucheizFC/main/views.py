from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError
from django.forms import inlineformset_factory
from django.http import HttpResponse, Http404
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from main.forms import ExtendedUserCreationForm, PlayerForm, \
    PlayerUpdateForm, UserLoginForm, CoachCreationForm, CoachUpdateForm, ContactUsForm, PlayerContractCreationForm, \
    InjuryForm

from main.mixins import allowed_users, unauthenticated_user
from main.models import Player, Coach, Contract, Contact, Injury, CoachContract
from training.models import TrainingSession


def home(request):
    players = Player.objects.all().count()
    contracts = Contract.objects.all().order_by('end_date')
    available = Player.objects.available().count()
    injured = Player.objects.injured().count()
    coaches = Coach.objects.all().count()
    contacts = Contact.objects.all().order_by('email')[:3]
    sessions = TrainingSession.objects.all()
    context = {
        'players': players,
        'contracts': contracts,
        'available': available,
        'injured': injured,
        'coaches': coaches,
        'contacts': contacts,
        'sessions': sessions
    }
    return render(request, 'home.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user.is_player:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse("invalid login")
    else:
        form = UserLoginForm()
    context = {
        'form': form
        }
    return render(request, 'login.html', context)


def admin_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user.is_admin:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse("invalid login")
    else:
        form = UserLoginForm()
    context = {
        'form': form
        }
    return render(request, 'login.html', context)


@login_required
@allowed_users(allowed_roles=['Admin'])
def add_player(request):
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        player_form = PlayerForm(request.POST, request.FILES)
        contract_form = PlayerContractCreationForm(request.POST)
        if user_form.is_valid() and player_form.is_valid() and contract_form.is_valid():
            user = user_form.save()
            user.is_player = True
            user.save()
            player = player_form.save(commit=False)
            player.user = user
            player.save()
            contract = contract_form.save(commit=False)
            contract.player = player
            contract.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username} !')
            group = Group.objects.get(name='Squad')
            user.groups.add(group)
            return redirect('player-list')
    else:
        user_form = ExtendedUserCreationForm()
        player_form = PlayerForm()
        contract_form = PlayerContractCreationForm

    context = {
        'user_form': user_form,
        'player_form': player_form,
        'contract_form': contract_form
    }
    return render(request, 'players/add_player.html', context)


class PlayerListView(ListView):
    model = Player
    context_object_name = 'players'
    template_name = 'players/player_list.html'
    paginate_by = 6
    ordering = 'jersey_no'

    def get_context_data(self, *args, **kwargs):
        context = super(PlayerListView, self).get_context_data(*args, **kwargs)
        return context


class PlayerDetailView(DetailView):
    model = Player
    template_name = 'players/player_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PlayerDetailView, self).get_context_data(*args, **kwargs)
        context['contracts'] = Contract.objects.filter(player=self.object)
        return context


class PlayerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = Player
    template_name = 'players/player_update.html'
    form_class = PlayerUpdateForm
    success_message = 'Player information was changed successfully'


class PlayerDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = Player
    context_object_name = 'player'
    template_name = 'players/player_delete.html'
    success_url = reverse_lazy('player-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'The player was deleted successfully!')
        return super().delete(request, *args, **kwargs)


class ContractListView(ListView):
    model = Contract
    template_name = 'home.html'
    context_object_name = 'contracts'


@login_required
@allowed_users(allowed_roles=['Admin'])
def coach_register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = CoachCreationForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username} !')

            return redirect('/')
    else:
        form = ExtendedUserCreationForm()
        profile_form = CoachCreationForm()
    context = {
        'form': form,
        'profile_form': profile_form
    }
    return render(request, 'coaches/coach-register.html', context)


class CoachListView(ListView):
    model = Coach
    context_object_name = 'coaches'
    template_name = 'coaches/coach_list.html'
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        context = super(CoachListView, self).get_context_data(*args, **kwargs)
        return context


class CoachDetailView(DetailView):
    model = Coach
    template_name = 'coaches/coach_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CoachDetailView, self).get_context_data(**kwargs)
        context['contracts'] = CoachContract.objects.filter(coach=self.object)
        return context


class CoachUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = Coach
    template_name = 'coaches/coach-update.html'
    form_class = CoachUpdateForm
    success_message = "Coach information was updated successfully"


class CoachDeleteView(LoginRequiredMixin, DeleteView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = Coach
    template_name = 'coaches/coach_delete.html'
    success_url = reverse_lazy('coach-list')

    def delete(self, request, *args, **kwargs):
        coach = self.get_object()
        messages.success(request, 'The coach %s was deleted successfully!' % coach.user)
        return super().delete(request, *args, **kwargs)


def add_injury(request, pk):
    InjuryFormSET = inlineformset_factory(Player, Injury, fields=('injury_type',), extra=1, can_delete=False)
    player = Player.objects.get(jersey_no=pk)

    formset = InjuryFormSET(queryset=Injury.objects.none(), instance=player)

    if request.method == 'POST':
        formset = InjuryFormSET(request.POST, instance=player)
        if formset.is_valid():
            formset.save()
            player.available = False
            player.save()
            return redirect('player-list')
    context = {
        'form': formset,
    }
    return render(request, 'players/add_injury.html', context)


class InjuryDetailView(DetailView):
    model = Injury
    template_name = 'players/injury_detail.html'
    context_object_name = 'injury'


def updateInjury(request, pk):
    injury = Injury.objects.get(id=pk)
    form = InjuryForm(instance=injury)
    if request.method == 'POST':
        form = InjuryForm(request.POST, instance=injury)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'players/update_injury.html', context)


def deleteInjury(request, pk):
    injury = Injury.objects.get(id=pk)
    if request.method == 'POST':
        injury.delete()
        injury.player.available = True
        injury.player.save()
        return redirect('/')
    context = {
        'injury': injury
    }
    return render(request, 'players/delete_injury.html', context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, f'thanks for contacting us , we will get back to you soon')
            return redirect('/')
    else:
        form = ContactUsForm()
        context = {
            'form': form
        }
    return render(request, 'contact/contact_create.html', context)


class ContactUsListView(ListView):
    model = Contact
    template_name = 'contact/contact_list.html'
    context_object_name = 'contact_us'


class ContactUsDetailView(DetailView):
    model = Contact
    template_name = 'contact/contact_detail.html'


class ContactUsUpdateView(UpdateView):
    model = Contact
    fields = ['name', 'email', 'subject']
    template_name = 'contact/contact_create.html'


class ContactUsDeleteView(DeleteView):
    model = Contact
    template_name = 'contact/contact_delete.html'
    success_url = 'contact-list'