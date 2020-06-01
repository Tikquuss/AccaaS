#biling urls, and from #, we have localhost/biling/here
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#use router.register('route',views.function)