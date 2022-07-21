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

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from .serializers import CommentSerializer, PostLikeSerializer, PostListSerializer, PostRetrieveSerializer
from blog.models import Post,Comment
from rest_framework.response import Response

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

class PostLikeAPIView(UpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostLikeSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        #data=instance.like+1
        data={'like':instance.like+1}
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(data['like'])