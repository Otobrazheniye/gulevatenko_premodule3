from django.urls import path
from . import views

# path('АДРЕС/', views.ИМЯ_ФУНКЦИИ, name='ИМЯ_МАРШРУТА')
urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('my-feed/', views.my_feed, name='my_feed'),

    path('create/', views.article_create, name='article_create'),

    path('topics/', views.topic_list, name='topic_list'),
    path('topics/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('topics/<int:topic_id>/subscribe/', views.topic_subscribe, name='topic_subscribe'),
    path('topics/<int:topic_id>/unsubscribe/', views.topic_unsubscribe, name='topic_unsubscribe'),

    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('set-password/', views.set_password, name='set_password'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('<int:year>/<int:month>/', views.article_archive, name='article_archive'),

    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/comment/', views.article_comment, name='article_comment'),
    path('<int:article_id>/update/', views.article_update, name='article_update'),
    path('<int:article_id>/delete/', views.article_delete, name='article_delete'),
]