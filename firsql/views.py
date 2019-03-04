from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db import connection

from django.contrib.auth.models import User
from .models import Profile
from .forms import CardNumberForm, MoneyAmountForm


def index(request):
    return render(request, 'firsql/index.html')

def users_all(request):
    print(connection.queries)
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'firsql/users_all.html', context)

def user_detail(request, user_id):
    # user = get_object_or_404(Profile, pk=user_id)
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'firsql/user_detail.html', {'user': user})

def user_detail_by_login(request, user_login):
    user = User.objects.filter(username=user_login)
    if user:
        user = user[0]
        return render(request, 'firsql/user_detail.html', {'user': user})
    else:
        raise Http404("Profile does not exist")

def profile(request):

    if request.method == 'POST':
        # user = request.user.username 
        # ma_form = MoneyAmountForm(data=request.POST)
        # cn_form = CardNumberForm(data=request.POST)

        # # if ma_form.is_valid() and cn_form.is_valid():
        # if ma_form.is_valid():
        #     user.profile.money_amount = ma_form.save()
        #     user.profile.save()

        # if cn_form.is_valid():
        #     user.profile.card_number = cn_form.save()
        #     user.profile.save()

        # if user_form.is_valid() and profile_form.is_valid():
        #     user = user_form.save()
        #     # pwd = user.password 
        #     user.set_password(user.password)
        #     user.save()

        #     profile = profile_form.save(commit=False)
        #     profile.user = user
        #     profile.email = user.email
        #     # profile.password = pwd
        #     if 'picture' in request.FILES:
        #         profile.picture = request.FILES['picture']
        #     profile.save()
        #     registered = True
        #     new_user = authenticate(username=user_form.cleaned_data['username'],
        #                             password=user_form.cleaned_data['password'],
        #                             )
        #     login(request, new_user)
        #     return HttpResponseRedirect('/shop/')
        # else:
        #     print(user_form.errors, profile_form.errors)

        # cn = request.user.profile.card_number
        # card_number_form = CardNumberForm(initial={'card_number': cn})
        # ma = request.user.profile.money_amount
        # money_amount_form= MoneyAmountForm(initial={'money_amount': ma})

        # if request.user.is_authenticated:
        #     username = request.user.username 
        #     return render(request, 'firsql/profile.html', 
        #         {'username': username,
        #         'card_number_form': card_number_form,
        #         'money_amount_form': money_amount_form })
        raise Http404("В разработке :)")
    else:
        cn = request.user.profile.card_number
        card_number_form = CardNumberForm(initial={'card_number': cn})
        ma = request.user.profile.money_amount
        money_amount_form= MoneyAmountForm(initial={'money_amount': ma})

        if request.user.is_authenticated:
            username = request.user.username 
            return render(request, 'firsql/profile.html', 
                {'username': username,
                'card_number_form': card_number_form,
                'money_amount_form': money_amount_form })
        else:
            raise Http404("You have not any permissions to view this page!")