from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from main.forms import ExtendedUserCreationForm, PlayerForm, PlayerUpdateForm, UserLoginForm, PlayerContractForm, \
    CoachCreationForm, CoachUpdateForm, ContactUsForm
from main.mixins import allowed_users, unauthenticated_user
from main.models import Player, Coach, Contract
from news.models import News


def home(request):
    players = Player.objects.all().count()
    available = Player.objects.available().count()
    injured = Player.objects.injured().count()
    coaches = Coach.objects.all().count()
    context = {
        'players': players,
        'available': available,
        'injured': injured,
        'coaches': coaches,
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
        form = ExtendedUserCreationForm(request.POST)
        player_form = PlayerForm(request.POST, request.FILES)
        if form.is_valid() and player_form.is_valid():
            user = form.save()
            user.is_player = True
            user.save()
            player = player_form.save(commit=False)
            player.user = user
            player.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username} . You are now required to create {username} contract !')
            group = Group.objects.get(name='Squad')
            user.groups.add(group)
            return redirect('player-list')
    else:
        form = ExtendedUserCreationForm()
        player_form = PlayerForm()
    context = {
        'form': form,
        'player_form': player_form
    }
    return render(request, 'players/add_player.html', context)


class PlayerListView(ListView):
    model = Player
    context_object_name = 'players'
    template_name = 'players/player_list.html'
    paginate_by = 6

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
        player = self.get_object()
        messages.success(request, 'The player was deleted successfully!')
        return super().delete(request, *args, **kwargs)


@login_required
@allowed_users(allowed_roles=['Admin'])
def player_contract_create(request):
    if request.method == 'POST':
        form = PlayerContractForm(request.POST or None)

        if form.is_valid():
            form.save()
            player = form.cleaned_data.get('player')
            player.has_contract = True
            player.save()
            messages.success(request, f'Contract created successfully')
            return redirect('/')
    else:
        form = PlayerContractForm()
    return render(request, 'players/add_player_contract.html', {'form': form})


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
