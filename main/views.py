from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import Info, Item
from .forms import CreateNewInfo
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(response, id):
    info = Info.objects.get(id=3)
    if response.method=="POST":
        print("POST")
        # if response.POST.get("save"):
        #     for item in info.item_set.all():
        #             item.save()
        if response.POST.get("newInfo"):
            txt=response.POST.get("new")
		    
            if len(txt) > 2:
                info.item_set.create(text=txt)
                
            else:
                print("invalid")
	        
    return render(response,'main/items.html',{"info":info})
    


def home(response):
    return render(response,'main/index.html',{})
@login_required
def create(response):
    if response.method == "POST":
        form = CreateNewInfo(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            p = form.cleaned_data["topic"]
            t = Info(name=p)
            t.save()
            
        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewInfo()

    return render(response,'main/create.html',{"form":form})