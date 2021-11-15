from django.db.models.query_utils import Q
from django.shortcuts import render
from .models import HostelInfo
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'MainApp/home.html')

def Base(request):
    return render(request,'MainApp/base.html')    

def Team(request):
    return render(request,'MainApp/team.html')        



# @login_required(login_url='login')
def Result(request):
    if request.method== 'POST':
        g=request.POST.get('g',False)
        re=request.POST.get('re',False)
        ra=request.POST.get('ra',False)
        searched = request.POST['searched']
        try :
            current_college=request.POST['current_college']
            if current_college != '':
                searched=current_college
        except:
            pass
        
        a=HostelInfo.objects.all()
        a=a.filter(Q(hostel_name__contains=searched )  |Q(college_name__contains=searched ))
        if g is not False:
            a=a.filter(gender=g)
        if re is not False:
            if re=='1':
                a=a.filter(cost_of_living__lte=50000)
            if re=='2':
                a=a.filter(cost_of_living__gte=50000,cost_of_living__lte=100000)
            if re=='3':
                a=a.filter(cost_of_living__gte=100000)
        if ra is not False:
            if ra=='4':
                a=a.filter(radius__lte=500)
            if ra=='5':
                a=a.filter(radius__gte=500,radius__lte=1000)
            if ra=='6':
                a=a.filter(radius__gte=1000)
        # a.filter()
        # print(a)
        # print(g,re)
        
                          
        return render(request,'MainApp/result.html',{'searched':searched ,'res':a})
    else:
         
        return render(request,'MainApp/result.html',{'error':"No Results,Apply different filters",'messages':messages})       