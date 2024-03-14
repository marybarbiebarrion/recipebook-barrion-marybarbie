from django.shortcuts import render
from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/recipe_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"