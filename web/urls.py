from django.urls import path
from . import views

urlpatterns = [
  path('', views.index_view),
  path('login/', views.login_view),
]