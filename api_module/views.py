
from .models import Post
from rest_framework import viewsets,pagination,throttling
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serilizers import PostSerializer
from rest_framework.filters import SearchFilter


class PostPagination(pagination.PageNumberPagination):
    page_size=2
    page_size_query_param='page_size'
    max_page_size=100

class PostThrottle(throttling.UserRateThrottle):
    rate='200/day'

class PostViewSet(viewsets.ModelViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    pagination_class=PostPagination
    throttle_classes=[PostThrottle]
    
    