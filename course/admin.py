from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .models import Course, Module
from django.contrib.auth.models import User, Group


# Register your models here.
class OrionAdmin(AdminSite):
    site_title = ugettext_lazy("Orion Admin")
    site_header = ugettext_lazy("Admin Panel")
    index_title = ugettext_lazy("Index")
    
admin.site = OrionAdmin()

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Group)
admin.site.register(User)