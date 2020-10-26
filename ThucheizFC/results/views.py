from django.shortcuts import redirect, render
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from results.forms import ResultCreationForm, ClubGoalForm
from results.models import Result, GoalsScored, GoalsConceded


class ResultListView(ListView):
    model = Result
    paginate_by = 3
    context_object_name = 'results'
    template_name = 'results/result_list.html'
    ordering = '-date'

    def get_context_data(self, *args,  **kwargs):
        context = super(ResultListView, self).get_context_data(*args, **kwargs)
        return context


class ResultDetailView(DetailView):
    model = Result
    context_object_name = 'result'
    template_name = 'results/result_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ResultDetailView, self).get_context_data(**kwargs)
        return context


class ResultCreateView(CreateView):
    model = Result
    template_name = 'results/create_result.html'
    form_class = ResultCreationForm


class ResultUpdateView(UpdateView):
    model = Result
    template_name = 'results/create_result.html'
    fields = ['result_type', 'club', 'club_goal', 'opponent', 'image',  'opponent_goal', 'stadium', 'date']
    success_message = "The news was changed successfully"


class ResultDeleteView(DeleteView):
    model = Result
    template_name = 'results/delete_result.html'
    success_url = reverse_lazy('result-list')


def add_goals(request, pk):
    GoalFormSET = inlineformset_factory(Result, GoalsScored, fields=('player', 'minute'), extra=3, can_delete=False)
    ConcededFormset = inlineformset_factory(Result, GoalsConceded, fields=('scorer', 'minute'), extra=3, can_delete=False)
    result = Result.objects.get(id=pk)

    formset = GoalFormSET(queryset=GoalsScored.objects.none(), instance=result)
    formset2 = ConcededFormset(queryset=GoalsConceded.objects.none(), instance=result)

    if request.method == 'POST':
        formset = GoalFormSET(request.POST, instance=result)
        formset2 = ConcededFormset(request.POST, instance=result)
        if formset.is_valid() and formset2.is_valid():
            formset.save()
            formset2.save()
            return redirect('result-list')
    context = {
        'form': formset,
        'form2': formset2
    }
    return render(request, 'results/add_goals.html', context)