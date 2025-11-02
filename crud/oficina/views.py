from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Oficina
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class OficinaListView(ListView):
    model = Oficina
    template_name = "oficina/lista.html"
    context_object_name = "oficinas"
    paginate_by = 10
    ordering = ['nombre']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(Q(nombre__icontains=query) | Q(nombreCorto__icontains=query))
        return queryset

class OficinaDetailView(DetailView):
    model = Oficina
    template_name = "oficina/detalle.html"
    context_object_name = "oficina"

class OficinaCreateView(LoginRequiredMixin, CreateView):
    model = Oficina
    template_name = "oficina/crear.html"
    fields = ['nombre', 'nombreCorto']
    success_url = reverse_lazy('oficina:lista')

class OficinaUpdateView(LoginRequiredMixin, UpdateView):
    model = Oficina
    template_name = "oficina/crear.html"
    fields = ['nombre', 'nombreCorto']
    success_url = reverse_lazy('oficina:lista')

class OficinaDeleteView(LoginRequiredMixin, DeleteView):
    model = Oficina
    template_name = "oficina/eliminar.html"
    success_url = reverse_lazy('oficina:lista')
    context_object_name = "oficina"