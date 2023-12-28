from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from api import views

router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'Todos', views.TodosViewSet)
router.register(r'Post', views.PostViewSet)
router.register(r'Comment', views.CommentViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

urlpatterns += router.urls