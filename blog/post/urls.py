from django.urls import path
from rest_framework import routers
from post.views import post_list, PostViewSet

router = routers.SimpleRouter()
router.register(r'api/posts', PostViewSet)

urlpatterns = [
    path('list/', post_list, name='post_list')
]

urlpatterns += router.urls