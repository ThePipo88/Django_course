from django.shortcuts import render,HttpResponse

#Models
from .models import Project

# Create your views here.
def profile(request):
    #p1 = Project(title="Curso de HTML",desc="Descripcion de HTML")
    #p1.save()
    
    #p2 = Project(title="Curso de CSS",desc="Descripcion de CSS")
    #p2.save()
    
    #p3 = Project(title="Curso de Django",desc="Descripcion de Django")
    #p3.save()
    
    projects = Project.objects.all()
    return render(request,'profile.html')