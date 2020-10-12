from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, DeleteView

from injury.forms import InjuryForm, CheckOutForm
from injury.models import Injury


class InjuryUpdateView(CreateView):
    model = Injury
    form_class = InjuryForm
    template_name = 'injury/add_injury.html'
    success_url = reverse_lazy('injury_list')


def add_injury(request):
    if request.method == 'POST':
        form = InjuryForm(request.POST)
        if form.is_valid():
            form.save()
            player = form.cleaned_data.get('player')
            player.available = False
            player.save()

            return redirect('injury_list')
    else:
        form = InjuryForm()
    return render(request, 'injury/add_injury.html', {'form': form})


class InjuryListView(ListView):
    model = Injury
    context_object_name = 'injuries'
    template_name = 'injury/injury_list.html'

    def get_context_data(self, *args,  **kwargs):
        context = super(InjuryListView, self).get_context_data(*args, **kwargs)
        return context


class InjuryDeleteView(SuccessMessageMixin, DeleteView):
    model = Injury
    template_name = 'injury/delete_injury.html'
    success_url = reverse_lazy('injury_list')
    
    def delete(self, request, *args, **kwargs):
        request = self.request
        injury = self.get_object()
        injury.player.available = True
        injury.player.save()
        return super(InjuryDeleteView, self).delete(request, *args, **kwargs)
