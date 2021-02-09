from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleSerializers(articles,many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = ArticleSerializers(data = request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def articledetail(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializers(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializers(article,data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




