from django.urls import path,include
from .views import ArticleApi,Articledetail,GenericApi
urlpatterns = [

    path('generic/<str:id>/',GenericApi.as_view()),
    path('',ArticleApi.as_view(),name='list'),
    path('<str:id>/',Articledetail.as_view(),name='detail'),
]
