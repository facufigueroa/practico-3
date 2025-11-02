from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Persona
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

class PersonaListView(ListView):
    model = Persona
    template_name = "persona/lista.html"
    context_object_name = "personas"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("q")
        if search_query:
            queryset = queryset.filter(Q(nombre__icontains=search_query) or Q(apellido__icontains=search_query))
        return queryset

class PersonaDetailView(DetailView):
    model = Persona
    template_name = "persona/detalle.html"
    context_object_name = "persona"

class PersonaCreateView(LoginRequiredMixin, CreateView):
    model = Persona
    template_name = "persona/crear.html"
    fields = ['nombre', 'apellido', 'edad', 'oficina']
    success_url = reverse_lazy('persona:lista')

class PersonaUpdateView(LoginRequiredMixin, UpdateView):
    model = Persona
    template_name = "persona/crear.html"
    fields = ['nombre', 'apellido', 'edad', 'oficina']
    success_url = reverse_lazy('persona:lista')

class PersonaDeleteView(LoginRequiredMixin, DeleteView):
    model = Persona
    template_name = "persona/eliminar.html"
    success_url = reverse_lazy('persona:lista')
    context_object_name = "persona"