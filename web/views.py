from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

def context_load(request):
  context = {}
  context['messages'] = []
  print(request.user)
  # context['messages'].append('این نسخه بتا می‌باشد. | motahharmokfi@gmail.com')
  return context

# For Add New Message:
# context['messages'].append('Message')

def index_view(request):
  context = context_load(request)
  return render(request, 'index.html', context)

@login_required(login_url="/login/")
def courses_view(request):
  context = context_load(request)
  coures_models = models.course_model.objects.filter(author=request.user)
  pages = Paginator(coures_models, 5)
  page_num = request.GET.get('page', 1)
  courses = pages.page(page_num)
  context['courses'] = courses
  context['pages'] = pages
  return render(request, 'courses.html', context)

@login_required(login_url="/login/")
def lessons_view(request):
  context = context_load(request)
  if int(request.GET.get('course_id')) is not None:
    courses = models.course_model.objects.filter(author=request.user).get(id=request.GET.get('course_id'))
    lessons = models.lesson_model.objects.filter(course=courses)

  pages = Paginator(lessons, 5)
  page_num = request.GET.get('page', 1)
  lessons = pages.page(page_num)

  context['pages'] = pages
  context['lessons'] = lessons
  context['course'] = courses
  context['course_id'] = request.GET.get('course_id')
  return render(request, 'lessons.html', context)

@login_required(login_url="/login/")
def new_course_view(request):
  context = context_load(request)
  form = forms.create_course_form(request.POST or None)

  if request.method == "POST":

    if form.is_valid():
      title = form.cleaned_data.get("title")
      description = form.cleaned_data.get("description")
      course = models.course_model()
      course.title = title
      course.description = description
      course.author = request.user
      course.save()
      return redirect('../courses/')

  context['form'] = forms.create_course_form
  return render(request, 'new_form.html', context)

@login_required(login_url="/login/")
def new_lesson_view(request):
  context = context_load(request)
  course = models.course_model.objects.filter(author=request.user).get(id=request.GET.get('course_id'))

  form = forms.create_lesson_form(request.POST or None)

  if request.method == "POST":
    if form.is_valid():
      key = form.cleaned_data.get("key")
      value = form.cleaned_data.get("value")
      lesson = models.lesson_model()
      lesson.key = key
      lesson.value = value
      lesson.course = course
      lesson.save()
      return redirect('../lessons/?course_id='+request.GET.get('course_id'))

  context['form'] = forms.create_lesson_form
  context['cta'] = 'ایجاد سوال'
  context['course'] = course
  return render(request, 'new_form.html', context)


def login_view(request):
  context = context_load(request)
  form = forms.LoginForm(request.POST or None)

  if request.method == "POST":

    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect(request.GET.get('next_login', '/'))

  context['login_form'] = forms.LoginForm
  return render(request, 'login.html', context)

def logout_view(request):
  context = context_load(request)
  logout(request)
  return redirect('/')