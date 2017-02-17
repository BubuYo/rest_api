#coding=utf-8
from django.shortcuts import render

# Create your views here.
# from models import Article, Tag, Comment

'''
使用基于类的视图而不是基于函数的视图来编写API视图。
这是一个强大的模式，允许我们重用通用功能，并帮助我们保持我们的代码DRY
'''

from quickstart.models import Article, Tag, Comment
from quickstart.serializers import ArticleSerializer, TagSerializer, CommentSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])

def api_root(request, format=None):

    return Response({

    'users': reverse('user-list', request=request, format=format),
    'articles': reverse('article-list', request=request, format=format),
    'tags': reverse('tag-list', request=request, format=format),
    'comments': reverse('comment-list', request=request, format=format),

    })

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAdminUser,)

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CommentList(generics.ListCreateAPIView):
    '''
    现在如果我们创建一条评论，是没法和用户进行关联的。
    因为用户信息是通过 request获取而不是以serialized数据传递的。
    为了解决这个问题。我们需要重写snippet视图中 .perform_create() 方法，
    这个 方法准许我们修改实例如何被保存、处理任何由request或requested URL传递进来的隐含数据。
    '''
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList(generics.ListAPIView):
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


