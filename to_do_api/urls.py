from django.urls import include, path

from rest_framework import routers

from to_do_api.views import UserViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
   path('', include(router.urls)),
]