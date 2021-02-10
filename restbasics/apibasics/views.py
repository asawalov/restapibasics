from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated




class GenericApi(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self,request):
        return self.create(request)

    def put(self,request,id = None):
        return self.update(request,id)
    def delete(self,request,id):
        return self.delete(request,id)



class ArticleApi(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializers = ArticleSerializers(articles,many=True)
        return Response(serializers.data)

    def post(self,request):
        serializers = ArticleSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.data,status=status.HTTP_400_BAD_REQUEST)



class Articledetail(APIView):

    def get_object(self,id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExists:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        article = Article.objects.get(id = id)
        serializers = ArticleSerializers(article)
        return Response(serializers.data)

    def put(self,request,id):
        article = Article.objects.get(id=id)
        serializers = ArticleSerializers(article,data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = Article.objects.get(id=id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET','POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializers = ArticleSerializers(articles,many=True)
#         return Response(serializers.data)
#
#     elif request.method == 'POST':
#         serializers = ArticleSerializers(data = request.data)
#
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','DELETE'])
# def articledetail(request,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializers(article)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ArticleSerializers(article,data = request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#
