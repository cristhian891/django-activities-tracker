from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models

# Create your views here.

class ActivityList(ListView):

    model = models.Activity
    template_name = 'index.html'


class CreateActivityView(CreateView):
    model = models.Activity
    fields = ['sport', 'description', 'time', 'duration', 'calories', 'distance']

class ActivityDetails(DetailView):
    model = models.Activity
    template_name = 'activity_detail.html'

class ActivityUpdateView(UpdateView):
    fields = ['sport', 'description', 'duration']
    model = models.Activity

class ActivityDeleteView(DeleteView):
    model = models.Activity
    success_url = reverse_lazy('activity:list')

class MetricsView(TemplateView):
    model = models.Activity
    template_name = 'activity/calories-calculation.html'
    sum = 0
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.total_cal = models.Activity.objects.all()
        for el in self.total_cal:
            self.sum = self.sum + el.calories
        context['total'] = self.sum
        return context

