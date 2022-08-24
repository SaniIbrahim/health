from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Post

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'home.html'
    login_url = 'login'

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    login_url = 'login'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'posts/post_new.html'
    fields = '__all__'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'posts/post_edit.html'
    fields = ['title', 'body']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class AboutView(LoginRequiredMixin,TemplateView):
    template_name = 'about.html'
    login_url = 'login'


class SearchResultsListView(ListView):
    model = Post
    context_object_name = 'Post_list'
    template_name = 'posts/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(body__icontains=query) | Q(body__icontains=query) |Q(title__icontains=query) )
