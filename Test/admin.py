from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')



@admin.register(Test_kits)
class Test_kitsAdmin(admin.ModelAdmin):
    list_display = ('subtest_test',)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('test_kits', 'questions')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(UsersTest)
class UserTestAdmin(admin.ModelAdmin):
    list_display = ('user', 'test_kits')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'question')

@admin.register(UsersResults)
class UsersResultsAdmin(admin.ModelAdmin):
    list_display = ('user', 'test_kits')

