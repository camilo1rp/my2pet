from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from profiles.models import Profile, Client


# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton

# class PerfilInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'
#
#
# class ClientInline(admin.StackedInline):
#     model = Client
#     can_delete = False
#     verbose_name_plural = 'client'
#
#
# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (PerfilInline, ClientInline)
#
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)