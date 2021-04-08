from django.urls import path

from . import views

apps_name = 'mysite'

urlpatterns = [
          path('', views.index, name='index'),

]