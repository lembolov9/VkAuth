import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('friends')
    else:
        return render(request, 'vk_app/index.html')

@login_required(login_url='/')
def vk_friends_view(request):
    url = 'https://api.vk.com/method/friends.get'
    token = request.user.social_auth.get(provider='vk-oauth2').extra_data['access_token']
    if token:
        url_params = {'v': '5.95', 'access_token': token, 'count': 5, 'order': 'random', 'fields':'nickname, photo_100'}
        r = requests.get(url, url_params).json()
        context = {'friends': r['response']['items']}

    return render(request, 'vk_app/friends.html', context=context)