from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.views.generic import(
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    DetailView
)

from .models import Article

# from .forms import ArticleModelForm


class ArticleListView(ListView):
	model = Article
	
class ArticleCreateView(CreateView):
	model = Article
	fields = [
            'title',
            'description',
            'featured'
        ]

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article:article_list')

    # def get_object(self, queryset=None):
    #     return super().get_object(queryset=queryset)

    # def get_success_url(self):
    #     return reverse('article:article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['description']
    template_name_suffix = 'article:article_update_form'
    success_url = reverse_lazy('article:article_list')

	


class ArticleDetailView(DetailView):
	model=Article
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
