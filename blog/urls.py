from django.urls import path
from . import views
from django.urls import include
from rest_framework import routers
from .views import PostViewSet

router = routers.DefaultRouter()
router.register('Post', views.IntruderImage)
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('sign-in', views.sign_in_view, name='sign-in'),
    path('download', views.download_list, name='download_list'),
    path('logout', views.logout, name='logout'),
    path('api_root/', include(router.urls)),

]
