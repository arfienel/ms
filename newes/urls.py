from django.urls import path,include
from django.conf.urls import url
from .views import *

app_name = 'newes'
urlpatterns = [
    path('', main_page, name='main_page'),
    path('<int:news_id>/', detail, name='detail'),
    path('<int:news_id>/comment/', comment, name='comment'),
    path('<int:news_id>/like/', like, name='like'),
    path('search/', search, name='search_results'),
    path('filter/', filter_result, name='filter_results'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    #serializers
    path('api/list/', NewsListView.as_view(), name='list'),
    path('api/detail/<int:pk>/', NewsDetailView.as_view(), name='api_detail'),
]
