from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages



def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allow_users=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allow_users:
                return view_func(request, *args, **kwargs)
            else:
                messages.info(request, 'У вас недостаточно прав')
                return redirect('/')
        return wrapper_func
    return decorators



