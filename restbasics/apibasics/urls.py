from django.urls import path,include
from . import  views
urlpatterns = [

    path('',views.article_list,name='list'),
    path('<str:pk>/',views.articledetail,name='detail'),
]
