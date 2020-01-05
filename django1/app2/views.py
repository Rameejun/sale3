from django.shortcuts import render
from app2.models import *
import datetime

# Create your views here.
def fun(request):
    a = sale.objects.filter(day__contains=datetime.date(2020, 1, 3))
    #for i in a:
       # print(i.itemname, i.day)
    #print(a)
    return render(request,"home/file.html",{"a1":a})
#def f():
     # a = sale.objects.filter(day__contains=datetime.date(2020, 1, 3))
      #for i in a:
        #    print(i.itemname,i.day)
     # print(a)
      #return (a)
#f()

