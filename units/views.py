from django.shortcuts import render

# Create your views here.

from .models import Unit

def index(request):
    
    units = Unit.objects.order_by('id').all()
    
    ctx = {
        'units':units, 
    }
    return render(request, 'units/index.html', ctx)

