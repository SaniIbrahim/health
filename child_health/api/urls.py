from rest_framework.routers import SimpleRouter
from api.views import PostViewSet,ChildrenViewSet,UserViewSet


router = SimpleRouter()

router.register('users', UserViewSet, basename='user')
router.register('children', ChildrenViewSet, basename='child')
router.register('posts', PostViewSet, basename='posts')
urlpatterns = router.urls
