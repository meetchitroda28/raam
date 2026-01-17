from django.http import HttpResponse
from django.shortcuts import render

def abc(a):
    jj = ['vijay','raam','mihir']
    return render(a,'ab.html',{'data':jj})


def pqr(req):
    return render(req,'abc.html')