from django.shortcuts import render, redirect

# Create your views here.

from .forms import ProjectForm
from .models import Project



def index(request):
    
    projects = Project.objects.all()
    
    ctx = {
        'projects': projects,
    }
    return render(request, 'projects/index.html', ctx)


# add new project
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                model=form.instance
                return redirect('projects')
            except:
                pass
    else:
        form = ProjectForm()

    return render(request, 'projects/add_project.html', {'form': form})