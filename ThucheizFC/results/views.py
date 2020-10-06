from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from results.forms import ClubGoalCreationForm, OpponentGoalCreationForm, ResultCreationForm
from results.models import Result


class ResultListView(ListView):
    model = Result
    paginate_by = 3
    context_object_name = 'results'
    template_name = 'results/result_list.html'

    def get_context_data(self, *args,  **kwargs):
        context = super(ResultListView, self).get_context_data(*args, **kwargs)
        return context


class ResultDetailView(DetailView):
    model = Result
    template_name = 'results/result_detail.html'


def add_goals(request):
    if request.method == 'POST':
        club_goal_form = ClubGoalCreationForm(request.POST)
        opponent_goal_form = OpponentGoalCreationForm(request.POST)
        if club_goal_form.is_valid() and opponent_goal_form.is_valid():
            club_goal_form.save()
            opponent_goal_form.save()
            return redirect('/')
    else:
        club_goal_form = ClubGoalCreationForm()
        opponent_goal_form = OpponentGoalCreationForm()
    context = {
        'club_goal_form': club_goal_form,
        'opponent_goal_form': opponent_goal_form
    }
    return render(request, 'results/add_goals.html', context)


class ResultCreateView(CreateView):
    model = Result
    template_name = 'results/create_result.html'
    form_class = ResultCreationForm
    success_url = '/'


class ResultUpdateView(UpdateView):
    model = Result
    template_name = 'results/create_result.html'
    fields = ['result_type', 'club', 'club_goal', 'opponent', 'image',  'opponent_goal', 'stadium', 'date']
    success_message = "The news was changed successfully"


class ResultDeleteView(DeleteView):
    model = Result
    template_name = 'results/delete_result.html'