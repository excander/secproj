from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import User


def index(request):
    return HttpResponse("The index page!")

def users_all(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'firsql/users_all.html', context)

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'firsql/user_detail.html', {'user': user})