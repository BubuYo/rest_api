# coding=utf-8
"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""


from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from quickstart import views
'''
views中
list类负责实现创建和列表
Detail类负责实现增删改查
考虑到要求是：article增删改查，tag和comment可以新增和列表
所以在下面的urlpatterns中加入三者的list类，加入article的Detail类
'''
urlpatterns = [

    url(r'^$', views.api_root),

    url(r'^articles/$', views.ArticleList.as_view(), name='article-list'),
    url(r'^tags/$', views.TagList.as_view(), name='tag-list'),
    url(r'^comments/$', views.CommentList.as_view(), name='comment-list'),

    url(r'^comments/(?P<pk>[0-9]+)$',
        views.CommentDetail.as_view(), name='comment-detail'),
    url(r'^articles/(?P<pk>[0-9]+)$',
        views.ArticleDetail.as_view(), name='article-detail'),

    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(), name='user-detail'),

    url(r'^api-auth/', include('rest_framework.urls')),

]


# 添加额外的URL模式不是必须的，但使用它我们可以用一种干净，简单的方式来引用某个特定的格式
urlpatterns = format_suffix_patterns(urlpatterns)
