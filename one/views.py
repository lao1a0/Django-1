import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from one.models import CreateStu


def index(request):
    return HttpResponse("<h1>Hello world!</h1>")

def CreateStudent(request):
    stu = CreateStu()
    stu.name = request.POST.get('name')
    stu.sex = random.randint(0,2)
    stu.classroom = request.POST.get('class')
    stu.save()
    return HttpResponse("成功创建"+request.POST.get('name'))


def PrintTable(request):
    c = CreateStu.objects.all().order_by('classroom')
    cl = {}
    for i in c:
        cl.setdefault(i.classroom, []).append(i.name)
    context = {
        'data': cl
    }
    return render(request,'print.html',context=context)

def stuname(request , classid):
    context={
        'std' : CreateStu.objects.filter(classroom=classid)
    }
    return render(request,'stuname.html',context=context)

def detail(request):
    name = request.POST.get('name')
    c = CreateStu.objects.filter(name=name)
    if not c:
        name='这名学生不存在'
    else:
         c.delete()
    context={
        'name':name
    }
    return render(request,'detail.html',context=context)