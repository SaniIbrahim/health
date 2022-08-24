from rest_framework  import viewsets
from django.contrib.auth import get_user_model 
from posts.models import Post
from children.models import Children
from .permissions import IsAuthorOrReadOnly,IsAuthor_OrReadOnly
from .serializers import PostSerializer,ChildrenSerializer,UserSerializer


class PostViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer



class ChildrenViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthor_OrReadOnly,)
	queryset = Children.objects.all()
	serializer_class = ChildrenSerializer


class UserViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset =  get_user_model().objects.all()
	serializer_class = UserSerializer