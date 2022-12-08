import datetime
from time import gmtime, strftime
from django.shortcuts import render

def index(request):
    context = {
        #  "time": strftime("%Y-%m-%d %H:%M %p", gmtime()) or another way 
           "time": datetime.datetime.now()
    }
    return render(request,'index.html',context)
