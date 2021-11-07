# from django.views.generic import ListView
# from .models import Article

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/detail.html"

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/new.html'
    fields = ["title","body", "picture"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "articles/edit.html"
    fields = ["title", "body", "picture"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "articles/delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
