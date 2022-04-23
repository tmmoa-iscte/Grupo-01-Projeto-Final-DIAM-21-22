from django.contrib.auth.decorators import login_required, permission_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return HttpResponse("Esta será a página do fórum Espaço ISCTE! :)")


def register(request):
    return HttpResponse("Esta será a página do fórum Espaço ISCTE! :)")


def login_user(request):
    return HttpResponse("Esta será a página do fórum Espaço ISCTE! :)")


def profile(request):
    return HttpResponse("Esta será a página do fórum Espaço ISCTE! :)")


def profile_edit(request):
    return HttpResponse("Esta será a página do fórum Espaço ISCTE! :)")


def section(request, section_simplified_title):
    return HttpResponse("Esta será a página do fórum Espaço ISCTE! :)")


def thread(request, section_simplified_title, thread_simplified_title):
    return HttpResponse("Esta será a página do fórum Espaço ISCTE! :)")


def new_thread(request, section_simplified_title):
    return HttpResponse("Esta será a página do fórum Espaço ISCTE! :)")


def new_comment(request, section_simplified_title, thread_simplified_title):
    return HttpResponse("Esta será a página do fórum Espaço ISCTE! :)")

