from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  ListView ,DetailView,TemplateView
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Children,Antegen


class ChildrenList(LoginRequiredMixin,ListView):
    model = Children
    template_name = 'children/children_list.html'
    login_url = 'login'


class ChildrenDetail(LoginRequiredMixin,DetailView):
    model = Children
    template_name = 'children/children_detail.html'
    login_url = 'login'


class ChildrenRegister(LoginRequiredMixin,CreateView):
     model = Children
     fields = '__all__'
     template_name = 'children/children_form.html'
     login_url = 'login'


class ChildrenUpdate(LoginRequiredMixin,UpdateView):
     model = Children
     template_name = 'children/children_edit_form.html'
     fields = '__all__'
     login_url = 'login'
     def dispatch(self, request, *args, **kwargs):
         obj = self.get_object()
         if obj.registrar != self.request.user:
             raise PermissionDenied
             return("You are not the creator of the content")
         return super().dispatch(request, *args, **kwargs)

class ChildrenDelete(DeleteView):
     model = Children
     template_name = 'children/children_confirm_delete.html'
     success_url =  reverse_lazy('children_list')
     def dispatch(self, request, *args, **kwargs):
         obj = self.get_object()
         if obj.registrar != self.request.user:
             raise PermissionDenied
         return super().dispatch(request, *args, **kwargs)




class AntegenDetail(LoginRequiredMixin,DetailView):
    model = Antegen
    template_name = 'antegen/children_antegen.html'
    login_url = 'login'


class AntegenAdd(LoginRequiredMixin,CreateView):
     model = Antegen
     fields = '__all__'
     template_name = ''
     login_url = 'login'

class AntegenUpdate(LoginRequiredMixin,UpdateView):
     model = Children
    # template_name = 'children/children_edit_form.html'
     fields = '__all__'
     login_url = 'login'
     def dispatch(self, request, *args, **kwargs):
         obj = self.get_object()
         if obj.registrar != self.request.user:
             raise PermissionDenied
             return("You are not the creator of the content")
         return super().dispatch(request, *args, **kwargs)

class AntegenDelete(DeleteView):
     model = Children
     template_name = 'children/children_confirm_delete.html'
     success_url =  reverse_lazy('children_list')
     def dispatch(self, request, *args, **kwargs):
         obj = self.get_object()
         if obj.registrar != self.request.user:
             raise PermissionDenied
         return super().dispatch(request, *args, **kwargs)


