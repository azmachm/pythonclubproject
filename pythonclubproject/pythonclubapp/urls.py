from . import views
from django.urls import path

# this is acomment
urlpatterns=[
    path('', views.index, name='index'),
]

