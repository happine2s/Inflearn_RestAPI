from dataclasses import field
from importlib.metadata import files
from pyexpat import model
from unicodedata import category
from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Post, Comment, Category, Tag

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PostListSerializer(serializers.ModelSerializer):
    category=serializers.CharField(source='category.name')
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

# views.py의 PATCH 메소드
# class PostLikeSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Post
    #     #fields='__all__'
    #     fields = ['like']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['name']

class CateTagSerializer(serializers.Serializer):
    #cateList=CategorySerializer(many=True)
    #tagList=TagSerializer(many=True)

    cateList=serializers.ListField(child=serializers.CharField())
    tagList=serializers.ListField(child=serializers.CharField())

class PostSerializerSub(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','title']

class CommentSerializerSub(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','content','update_dt']

class PostSerializerDetail(serializers.Serializer):
    post=PostRetrieveSerializer()
    prevPost=PostSerializerSub()
    nextPost=PostSerializerSub()
    commentList=CommentSerializerSub(many=True)