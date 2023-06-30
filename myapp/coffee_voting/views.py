from django.urls import reverse_lazy
from django.views import generic
from .models import Coffee

class IndexView(generic.ListView):
    model = Coffee

class DetailView(generic.DetailView):
    model = Coffee

class CreateView(generic.edit.CreateView):
    model = Coffee
    fields = '__all__'

class UpdateView(generic.edit.UpdateView):
    model = Coffee
    fields = '__all__'
