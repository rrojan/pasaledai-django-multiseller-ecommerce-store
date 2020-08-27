from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .models import Article
from .forms import ArticleCreateForm


# Create your views here.
# class based views
class ArticleListView(ListView):
    queryset = Article.objects.order_by('-date')
    template_name = 'blogs/article_list.html'


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
    template_name = 'blogs/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = 'blogs/create.html'
    queryset = Article.objects.all()
    form_class = ArticleCreateForm


class ArticleUpdateView(UpdateView):
    template_name = 'blogs/create.html'
    queryset = Article.objects.all()
    form_class = ArticleCreateForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    template_name = 'blogs/delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:list-view')


class ArticleCreateFunctionView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleCreateForm(request.POST or None)
        return render(request, 'blogs/function-create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleCreateForm(request.POST or None)
        template_name = 'blogs/function-create.html'
        if form.is_valid():
            form.save()
            form = ArticleCreateForm()
        return render(request, self.template_name, context={'form': form})
