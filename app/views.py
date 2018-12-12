from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .filters import ItemFilter
from .forms import ItemForm
from .models import Item

# Create your views here.

class ItemFilterView(LoginRequiredMixin, FilterView):

    model = Item

    queryset = Item.objects.all().order_by("-created_at")

    filterset_class = ItemFilter
    strict = False

    paginate_by = 10

    def get(self, request, **kwargs):
        if request.GET:
            request.session["query"] = request.GET
        else:
            request.GET = request.GET.copy()
            if "query" in request.session.keys():
                for key in request.session["query"].keys():
                    request.GET[key] = request.session["query"][key]
        return super().get(request, **kwargs) 

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


class ItemCreateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = Item
    success_url = reverse_lazy("index") 

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy("index")    


class ItemDeleteView(LoginRequiredMixin, DetailView):
    model = Item
    success_url = reverse_lazy("index")