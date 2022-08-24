from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,AboutView,SearchResultsListView


urlpatterns = [
    path('about', AboutView.as_view(), name='about'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='home'),


    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
