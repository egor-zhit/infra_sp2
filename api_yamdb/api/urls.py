from django.urls import include, path
from rest_framework import routers

from .views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    Signup,
    TitleViewSet,
    Token,
    UserViewSet,
)

app_name = 'api'
router_v1 = routers.DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register(
    r'^titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

auth_v1 = [
    path('auth/signup/', Signup.as_view(), name='signup'),
    path('auth/token/', Token.as_view(), name='token'),
]

urlpatterns = [
    path('v1/', include(auth_v1)),
    path('v1/', include(router_v1.urls)),
]
