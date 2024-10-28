from django.urls import path
from .views import tests, test, create_test, update_test, delete_test

urlpatterns = [
    path('', tests, name='tests'),
    path('test/<int:pk>', test, name='test'),
    path('create_test/', create_test, name='create_test'),
    path('update_test/<int:pk>', update_test, name='update_test'),
    path('test/delete/<int:pk>', delete_test, name='delete_test'),
]
