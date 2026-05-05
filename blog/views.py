from django.http import HttpResponse
from django.shortcuts import render


def article_list(request):
    return render(request,'blog/article_list.html')


def my_feed(request):
    return render(request,'blog/my_feed.html')


def article_detail(request, article_id):
    return render(request,'blog/article_detail.html')

# 
def article_comment(request, article_id):
    return HttpResponse(f'Добавление комментария к статье #{article_id}')


def article_update(request, article_id):
    return render(request,'blog/article_detail.html')

# 
def article_delete(request, article_id):
    return HttpResponse(f'Удаление статьи #{article_id}')


def article_create(request):
    return render(request,'blog/article_form.html')


def topic_list(request):
    return render(request,'blog/topic_list.html')


def topic_detail(request, topic_id):
    return render(request,'blog/topic_detail.html')

# 
def topic_subscribe(request, topic_id):
    return HttpResponse(f'Подписка на тему #{topic_id}')

# 
def topic_unsubscribe(request, topic_id):
    return HttpResponse(f'Отписка от темы #{topic_id}')


def profile(request):
    return render(request,'blog/profile.html')


def register(request):
    return render(request,'blog/register.html')


def set_password(request):
    return render(request,'blog/set_password.html')


def login_view(request):
    return render(request,'blog/login.html')

# 
def logout_view(request):
    return HttpResponse('Логаут')


def article_archive(request, year, month):
    return render(request, 'blog/article_archive.html')

