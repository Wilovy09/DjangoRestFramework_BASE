from django.urls import path, include
from rest_framework import routers
from _index import views

routers = routers.DefaultRouter()
routers.register(r'tasks', views.TaskView, 'task')

# GET , POST , PUT , DELETE
urlpatterns = [
    path('v1/', include(routers.urls)),
]