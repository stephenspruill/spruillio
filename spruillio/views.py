from django import template
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import context
from .models import Project

def index(request):
    return render(request, 'index.html', {'project_list': Project.objects.all})

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project})