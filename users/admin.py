from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from .models import UserProfile, PassedSubjects



class UserProfileAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'30'})},
        models.IntegerField: {'widget': TextInput(attrs={'size':'20'})},
    }


admin.site.register(PassedSubjects)
admin.site.register(UserProfile, UserProfileAdmin)