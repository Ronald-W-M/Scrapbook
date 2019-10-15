from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User
from .models import Profile,Hobby,HobbyInterest

class InterestsInline(admin.TabularInline):
    model = HobbyInterest
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information',{'fields' : ['username','first_name','last_name','birth_date','bio']}),
        ('Account Data',{'fields':['email','password','profile_picture']}),
        ('Adminstrative Data',{'fields':['is_active','is_staff','is_superuser'],'classes':['collapse']})
    ]
    
    inlines = [InterestsInline,]

admin.site.register(Hobby)
admin.site.register(Profile,ProfileAdmin)
