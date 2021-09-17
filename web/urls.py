from django.urls import path
from . import views

urlpatterns = [
  path('', views.index_view, name='index'),

  # 
  path('courses/', views.courses_view, name='courses'),
  path('new_course/', views.new_course_view, name='new_course'),
  
  # 
  path('lessons/', views.lessons_view, name='lessons'),
  path('new_lesson/', views.new_lesson_view, name='new_lesson'),

  # 
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),

]