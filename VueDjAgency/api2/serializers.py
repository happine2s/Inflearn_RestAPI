from importlib.metadata import files
from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Post, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields='__all__'
        fields = ['id','title','image','like','category']

class PostRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude=['create_dt'] #create_dt 빼고 다 보내줌

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields='__all__'
        fields = ['like']