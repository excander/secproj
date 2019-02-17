from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import User


def index(request):
    return render(request, 'firsql/index.html')

def users_all(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'firsql/users_all.html', context)

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'firsql/user_detail.html', {'user': user})

def user_detail_by_login(request, user_login):
    user = User.objects.filter(login="admin")[0]
    return render(request, 'firsql/user_detail.html', {'user': user})