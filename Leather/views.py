from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Category,Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    # current_user = request.user
    # projects = Project.get_all()
    return render(request,'index.html',{})

