#from django.urls import path, include
# from rest_framework import routers
# from .views import CommentViewSet, PostViewSet, UserViewSet

# router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)
# router.register(r'post',PostViewSet)
# router.register(r'comment',CommentViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from api2 import views

urlpatterns=[
    path('post/',views.PostViewSet.as_view(actions={
        'get':'list',
    }),name='post-list'),
    path('post/<int:pk>/',views.PostViewSet.as_view(actions={
        'get':'retrieve',
    }),name='post-detail'),
    path('post/<int:pk>/like/',views.PostViewSet.as_view(actions={
        'get':'like',
    }),name='post-list'),

    path('comment/',views.CommentViewSet.as_view(actions={ 
        'post':'create',
    }),name='comment-list'),
    
    path('catetag/',views.CateTagAPIView.as_view(),name='catetag'),
]
