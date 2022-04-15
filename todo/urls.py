from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router=DefaultRouter()
router.register('todo',TodoViewSet,'todo')

urlpatterns=[
  path('v1/',include(router.urls)),
]