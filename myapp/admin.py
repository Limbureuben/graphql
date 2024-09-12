from django.contrib import admin
from .models import * # type: ignore

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password')
    search_fields = ('username', 'email')
    
admin.site.register(Registration, RegistrationAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'firstName', 'lastName')
    search_fields = ('username', 'email')
    
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'region', 'phone_number', 'application_date')
    search_fields = ('username', 'email')
    
admin.site.register(Application, ApplicationAdmin)