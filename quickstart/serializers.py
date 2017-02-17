#coding=utf-8
from rest_framework import serializers
from models import Article, Tag, Comment
from models import UserComment as User
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'created', 'title', 'content', 'tag')

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag', 'article_id')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    '''
    source决定了显示user的哪个参数值
    ReadOnlyField这种类型是只读的，用于进行序列化时候的展示，并且反序列化时不会被修改
    这里我们也可以使 用 CharField(read_only=True) 来替代它
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ('created', 'article_id', 'name', 'email', 'content', 'owner')

class UserSerializer(serializers.ModelSerializer):

    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'comments')

