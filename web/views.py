from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
context = {}
context['message'] = 'این نسخه بتا می‌باشد. | motahharmokfi@gmail.com'

def index_view(request):
  coures_models = models.course_model.objects.all()
  page = paginator.Paginator(coures_models, 5)
  page_num = request.GET.get('page', 1)
  courses = page.page(page_num)
  context['courses'] = courses
  return render(request, 'index.html', context)
  return render(request, 'index.html', context)