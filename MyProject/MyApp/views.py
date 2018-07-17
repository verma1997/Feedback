from django.shortcuts import render
#from django.http import HttpResponse
from MyApp.forms import NewUserProfile
from MyApp.models import UserProfile


def index(request):
    return render(request,'template/index.html')

def users(request):

    form = NewUserProfile()

    if request.method == "POST":
        form = NewUserProfile(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return thankyou(request)
        else:
            print('ERROR OCCURED')

    return render(request,'template/users.html',{'form':form})

def list(request):

    user_list = UserProfile.objects.order_by('name')
    user_dict = {"list":user_list}
    return render(request,'template/list.html',context=user_dict)

def thankyou(request):
    return render(request,'template/thankyou.html')
