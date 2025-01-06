from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game

# Create your views here.
def index1(request):
    title = 'Мой сайт'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'main_page.html', context)


def index2(request):
    title = 'Магазин'
    text = 'Игры'
    games = Game.objects.all()
    context = {
        'title': title,
        'text': text,
        'games': games
    }
    return render(request, 'games.html', context)


def index3(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'basket.html', context)


def sign_up_by_django(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        context = {}
        users = Buyer.objects.all()
        flag = False
        for user in users:
            if username == user.name:
                flag = True
        if flag:
            context['text'] = 'Пользователь уже существует'
        else:
            if password == repeat_password:
                Buyer.objects.create(name=username, balance=0, age=age)
                text = f'Приветствуем, {username}!'
                context = {'text': text}
            else:
                if password != repeat_password:
                    context['text'] = 'Пароли не совпадают'

        return render(request, 'registration_page.html', context)

    return render(request, 'registration_page.html')
