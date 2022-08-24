from django.contrib import admin
from .models import Clinic,Children,Antegen




class AntegenInline(admin.TabularInline):
    model = Antegen

class ChildrenAdmin(admin.ModelAdmin):
     inlines = [AntegenInline,]

admin.site.register(Clinic)
admin.site.register(Children,ChildrenAdmin)
admin.site.register(Antegen)
