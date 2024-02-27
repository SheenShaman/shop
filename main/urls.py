from django.urls import path
from rest_framework.routers import DefaultRouter

from main.apps import MainConfig
from main.views import CategoryViewSet

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [

] + router.urls
