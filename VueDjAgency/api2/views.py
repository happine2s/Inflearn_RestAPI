# from django.contrib.auth.models import User
# from rest_framework import viewsets
# from .serializers import CommentSerializer, PostSerializer, UserSerializer
# from blog.models import Post, Comment

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

from collections import OrderedDict
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import CateTagSerializer, CommentSerializer, PostListSerializer, PostRetrieveSerializer
from blog.models import Post,Comment,Category, Tag
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination

class PostListAPIView(ListAPIView):
    #ListAPIView는 many=True
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostRetrieveAPIView(RetrieveAPIView):
    #RetrieveAPIView는 many=False
    #cdrf.co 참고
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# class PostLikeAPIView(UpdateAPIView):
#     queryset=Post.objects.all()
#     serializer_class=PostLikeSerializer

#     #PATCH method
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         #data=instance.like+1
#         data={'like':instance.like+1}
#         serializer = self.get_serializer(instance, data=data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         if getattr(instance, '_prefetched_objects_cache', None):
#             # If 'prefetch_related' has been applied to a queryset, we need to
#             # forcibly invalidate the prefetch cache on the instance.
#             instance._prefetched_objects_cache = {}

#         return Response(data['like'])

class PostLikeAPIView(GenericAPIView):
    queryset=Post.objects.all()

    #GET method
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like+=1
        instance.save()
        return Response(instance.like)

class CateTagAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cateList=Category.objects.all()
        tagList=Tag.objects.all()
        data={
            'cateList': cateList,
            'tagList': tagList
        }
        serializer=CateTagSerializer(instance=data)
        return Response(serializer.data)

class PostPageNumberPagination(PageNumberPagination):
    page_size=3
    #page_size_query_param='page_size'
    #max_page_size=1000

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('postList',data),
            ('pageCnt',self.page.paginator.num_pages),
            ('curPage',self.page.number),
        ]))

class PostListAPIView(ListAPIView):
    #ListAPIView는 many=True
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class=PostPageNumberPagination

    def get_serializer_context(self):
        return {
            'request': None,
            'format': self.format_kwarg,
            'view': self
        }