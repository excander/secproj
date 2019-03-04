from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db import connection

from django.contrib.auth.models import User
from .models import Profile


def index(request):
    return render(request, 'firsql/index.html')

def users_all(request):
    print(connection.queries)
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'firsql/users_all.html', context)

def user_detail(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)
    return render(request, 'firsql/user_detail.html', {'user': user})

def user_detail_by_login(request, user_login):
    user = Profile.objects.filter(login=user_login)
    if user:
        user = user[0]
        return render(request, 'firsql/user_detail.html', {'user': user})
    else:
        raise Http404("Profile does not exist")