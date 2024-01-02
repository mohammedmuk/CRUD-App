from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from django.urls import reverse_lazy
from django.views import View

# Create your views here.

class CatList(LoginRequiredMixin ,View):
    def get(self, request):
        bl = models.Breed.objects.count()
        cl = models.Cat.objects.all()
        ctx = {'bread_count' : bl, 'cat_list' : cl}
        return render(request, 'cats/cat_list.html', ctx)


class CatCreate(LoginRequiredMixin, CreateView):
    model = models.Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = models.Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = models.Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreadList(LoginRequiredMixin, ListView):
    model = models.Breed

class BreadCreate(LoginRequiredMixin, CreateView):
    model = models.Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreadUpdate(LoginRequiredMixin, UpdateView):
    model = models.Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreadDelete(LoginRequiredMixin, DeleteView):
    model = models.Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

