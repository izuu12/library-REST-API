

from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'books', views.BookViewSet, basename='books')
router.register(r'item', views.ItemViewSet, basename='item')
#router.register(r'books/<int:id>', views.BookoneViewSet, basename='book')


urlpatterns = [
    path('', include(router.urls)),
]
