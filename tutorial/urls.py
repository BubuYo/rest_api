#coding=utf-8
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


# from django.conf.urls import url, include
# from rest_framework import routers
# from tutorial.quickstart import views
#
# router = routers.DefaultRouter()
# router.register(r'article', views.ArticleViewSet)
# router.register(r'tag', views.TagViewSet)
# router.register(r'comment', views.CommentViewSet)
#
#
# # 使用URL路由来管理我们的API
# # 另外添加登录相关的URL
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^plist/(.+)/$', views.helloParam),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

# from django.conf.urls import url
# from rest_framework_swagger.views import get_swagger_view
#
# schema_view = get_swagger_view(title='article')
#
# urlpatterns = [
#     url(r'^$', schema_view)
# ]


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

    url(r'^articles/$', views.ArticleList.as_view()),
    url(r'^tags/$', views.TagList.as_view()),
    url(r'^comments/$', views.CommentList.as_view()),
    url(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

]
#添加额外的URL模式不是必须的，但使用它我们可以用一种干净，简单的方式来引用某个特定的格式
urlpatterns = format_suffix_patterns(urlpatterns)