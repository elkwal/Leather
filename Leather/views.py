from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Category,Product,Business,User_profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import UploadForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):

    return render(request,'index.html',{})

def group(request):
    
    products=Product.objects.all()

    return render(request,'temps/group.html',{'group':group})  



def allbiz(request):
    business=Business.objects.all()

    return render(request,'temps/allbiz.html',{"business":business})    

def search_results(request):
    
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        business = Business.search_biz(search_term)
        message = f"{search_term}"

        return render(request, 'temps/search.html',{"message":message,"business": business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'temps/search.html',{"message":message})    


@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    title = 'Home | Upload'
    profiles = User_profile.get_profile()
    for profile in profiles:
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.profile = profile
            upload.save()
            
            return redirect('post')
            messages.success(request, 'Status  updated '\
                                      'successfully')
        else:
            form = UploadForm()
    return render(request,'temps/upload.html',{"title":title, "user":current_user,"form":form})
