from django.http import HttpResponse


def article_list(request):
    return HttpResponse('Главная страница: список всех статей')


def my_feed(request):
    return HttpResponse('Моя лента')


def article_detail(request, article_id):
    return HttpResponse(f'Детальная страница статьи #{article_id}')


def article_comment(request, article_id):
    return HttpResponse(f'Добавление комментария к статье #{article_id}')


def article_update(request, article_id):
    return HttpResponse(f'Обновление статьи #{article_id}')


def article_delete(request, article_id):
    return HttpResponse(f'Удаление статьи #{article_id}')


def article_create(request):
    return HttpResponse('Создание новой статьи')


def topic_list(request):
    return HttpResponse('Список всех тем')


def topic_detail(request, topic_id):
    return HttpResponse(f'Статьи по теме #{topic_id}')


def topic_subscribe(request, topic_id):
    return HttpResponse(f'Подписка на тему #{topic_id}')


def topic_unsubscribe(request, topic_id):
    return HttpResponse(f'Отписка от темы #{topic_id}')


def profile(request):
    return HttpResponse('Профиль пользователя')


def register(request):
    return HttpResponse('Регистрация')


def set_password(request):
    return HttpResponse('Смена пароля')


def login_view(request):
    return HttpResponse('Логин')


def logout_view(request):
    return HttpResponse('Логаут')


def article_archive(request, year, month):
    return HttpResponse(f'Архив статей за {year}/{month}')