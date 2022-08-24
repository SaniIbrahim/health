from django.urls import path
from .views import ChildrenList,ChildrenDetail,ChildrenRegister,ChildrenUpdate,ChildrenDelete,AntegenDetail,AntegenAdd
,AntegenDelete,AntegenUpdate


urlpatterns = [
    path('child/<int:pk>/delete/',ChildrenDelete.as_view(),name='child_delete'),
    path('child/<int:pk>/edit/',ChildrenUpdate.as_view(),name='child_edit'),
    path('child/register/',ChildrenRegister.as_view(),name='child_register'),
    path('child/<int:pk>/',ChildrenDetail.as_view(),name='child_detail'),


    path('antegen/<int:pk>/delete/',AntegenDelete.as_view(),name='antegen_delete'),
    path('antegen/<int:pk>/edit/',AntegenUpdate.as_view(),name='antegen_edit'),
    path('antegen/add/',AntegenAdd.as_view(),name='antegen_add'),
    path('childintegen/<int:pk>/',AntegenDetail.as_view(),name='antegen_antegen'),

    path('list',ChildrenList.as_view(),name='children_list'),


]
