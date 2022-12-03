from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['__str__']

# admin.site.register(SpecUser)
@admin.register(Mentor)
class SpecUserAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(Student)
class MentorAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(Leed)
class LeedAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['__str__']