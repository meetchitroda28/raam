from django.shortcuts import render,redirect
from .forms import ContactForm

daraa= [
    # {
    #     'id':1,
    #     'name':'vijay',
    #     'number':234567
    # },
    #  {
    #     'id':2,
    #     'name':'raam',
    #     'number':345678
    # }
]

def form(req):
    if req.method == 'GET':
        return render(req,'form.html',{'form':ContactForm,'list':daraa})
    else:
        gg = req.POST.dict()
        daraa.append(gg)
        return redirect('/admin/form')
    
def index(req):
    return render(req,'adminhome.html',{'data':daraa})

def about(req):
    return render(req,'adminabout.html')