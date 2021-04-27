from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import News, Comment
from .metascore_parse import Parse
from .steam_parse import Parse_steam
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.core.paginator import Paginator
from django.views.generic import ListView, TemplateView
from django.urls import reverse
from .decorators import counted
from django.utils.decorators import method_decorator


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'вы успешно зарегистрировались')
            return redirect('newes:main_page')
        else:
            messages.error(request, 'не успешная попытка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('newes:login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'вы успешно вошли')
            return redirect('newes:main_page')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})



def main_page(request):
    news_list = News.objects.order_by('pub_date')[::-1]
    paginator = Paginator(news_list, 3)
    page = request.GET.get('page')
    news_list = paginator.get_page(page)
    generess = ['action','adventure','simulator','strategy','RPG','puzzle']
    return render(request, 'newos/mainp.html', {'news_list': news_list,'genress':generess})


def filter_result(request):
    quest = request.GET.get('fil')
    print(quest)
    genress = ['action', 'adventure', 'simulator', 'strategy', 'RPG', 'puzzle']
    result = News.objects.filter(genre1__icontains=quest)

    return render(request, 'newos/search-results.html', {'result': result,'genress':genress})


def Search(request):
    quest = request.GET.get('search')
    result = News.objects.filter(title__icontains=quest)
    genress = ['action', 'adventure', 'simulator', 'strategy', 'RPG', 'puzzle']
    return render(request, 'newos/search-results.html', {'result': result,'genress':genress})



@counted
def detail(request, news_id):
    try:
        a = News.objects.get(id=news_id)
    except:
        raise Http404('Нету такой статьи ;(')

    latest_comments_list = a.comment_set.order_by('-id')
    score = a.score()
    metascore = Parse(a.metascore_url)
    steam_price = Parse_steam(a.steam_url)
    steam_discount = 0
    steam_orig = 0
    steam_free = 0
    steam_price_final = 0
    youtube = a.trailer_youtube_url
    youtube = youtube.replace('watch?v=', 'embed/')
    if 'ab_channel' in youtube:
        youtube = youtube.replace(youtube[youtube.find('ab_channel') - 1:], '')
    if steam_price == 'Бесплатно':
        steam_free = 'Бесплатно'
    elif type(steam_price) == int:
        steam_price_final = steam_price
    elif type(steam_price) == list:
        steam_orig = steam_price[1]
        steam_discount = steam_price[2]




    comment_list = a.comment_set.order_by('-id')
    return render(request, 'newos/detail.html',
                  {'news': a, 'latest_comments_list': latest_comments_list, 'score': float(score),
                   'metascore': metascore, 'steam_discount': steam_discount, 'steam_orig': steam_orig,
                   'steam_free': steam_free,
                   'steam_price_final': steam_price_final, 'youtube': youtube,
                   'comment_list': comment_list})





def like(request,news_id):
    news = get_object_or_404(News, id=news_id)
    news.likes.add(request.user)

    return redirect(reverse('newes:detail', args=[news.id]))


def comment(request, news_id):
    try:
        a = News.objects.get(id=news_id)
    except:
        raise Http404('нет такой статьи')
    user = request.user.username
    a.comment_set.create(com_text=request.POST['text'],com_author=user)

    return redirect(reverse('newes:detail', args=[a.id]))
# Create your views here.
