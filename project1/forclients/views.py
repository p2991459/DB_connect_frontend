from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Client_Info ##Yaha hamne apne models.py se Client_Info Model ko import kiya
def index(request):
    return render(request,'index.html')

def showname(request):
    name = request.GET.get('fname','default')
    print(name)
    object1 = Client_Info(client_name=name)
    object1.save()
    params = {'name':name}  ##django html template keval key value pair samjhti hai isliye hum usko param me only dict bhej sakte hain
    return render(request,'home.html',params)

def test(request):
    # template = loader.get_template('test.html')
    # return HttpResponse(template.render())
    return render(request,'test.html')