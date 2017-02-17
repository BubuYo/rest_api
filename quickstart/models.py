#coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class UserComment(User):

    comments = models.ForeignKey('Comment', related_name='quickstart')

    # class Meta:
    #     ordering = ('created',)


class Article(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    tag = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)


class Tag(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=100, blank=True, default='')
    article_id = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)


class Comment(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    article_id = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField()
    content = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='quickstart')
    # highlighted = models.TextField()

    class Meta:
        ordering = ('created',)
