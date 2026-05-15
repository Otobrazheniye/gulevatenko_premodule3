from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Topic, Comment
from django.shortcuts import render, get_object_or_404


def article_list(request):
    articles = Article.objects.all().order_by('-created_at')

    context = {
        'articles': articles,
    }

    return render(request, 'blog/article_list.html', context)

def my_feed(request):
    return render(request,'blog/my_feed.html')


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    context = {
        'article': article,
    }

    return render(request, 'blog/article_detail.html', context)

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
    topics = Topic.objects.all().order_by('name')

    context = {
        'topics': topics,
    }

    return render(request, 'blog/topic_list.html', context)


def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id = topic_id)
    articles = topic.articles.all().order_by('-created_at')

    context = {
        'topic': topic,
        'articles': articles,
    }

    return render(request,'blog/topic_detail.html', context)

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

