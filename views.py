from django.shortcuts import render

from .models import *
from .forms import *
# Create your views here.
def img(request):
    if request.method=="POST":
        form=Userform(request.POST,request.FILES)
        if form.is_valid:
            user = form.save(commit=False)
           
            user.save()
            images=request.FILES.getlist("images")
            for img in images:
                Multiple.objects.create(images=img)
    else:
       form=Userform()
    img=Multiple.objects.all()
    return render(request,'index.html',{"form":form,'img':img})