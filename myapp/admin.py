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

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'published_date', 'text')
    
admin.site.register(Message, MessageAdmin)

class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'employ_status', 'details_month', 'employ_name', 'is_active')
    
admin.site.register(Employment, EmploymentAdmin)

class WeatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'temperature', 'humidity', 'created_at')
    
admin.site.register(Weather, WeatherAdmin)

class FinancialAdmin(admin.ModelAdmin):
    list_display = ('id', 'accountname', 'amount', 'salary', 'passport_path')
    
admin.site.register(Financial, FinancialAdmin)