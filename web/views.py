from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from . import models
from django.contrib.auth.decorators import login_required

context = {}
context['messages'] = []
context['messages'].append('این نسخه بتا می‌باشد. | motahharmokfi@gmail.com')

# For Add New Message:
# context['messages'].append('Message')

@login_required(login_url="/login/")
def index_view(request):
  coures_models = models.course_model.objects.filter(author=request.user)
  page = Paginator(coures_models, 5)
  page_num = request.GET.get('page', 1)
  courses = page.page(page_num)
  context['courses'] = courses
  return render(request, 'index.html', context)

def login_view(request):
  from .forms import LoginForm
  form = LoginForm(request.POST or None)

  if request.method == "POST":

    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect(request.GET.get('next_login', '/'))

  context['login_form'] = LoginForm
  return render(request, 'login.html', context)