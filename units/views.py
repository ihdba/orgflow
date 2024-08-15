from django.shortcuts import render

# Create your views here.

from .models import Unit

def index(request):
    
    units = Unit.objects.order_by('id').all()
    
    ctx = {
        'units':units, 
    }
    return render(request, 'units/index.html', ctx)



# Detail view of Unit with undelying units

def unit_detail(request, pk):
    
    unit = Unit.objects.get(id=pk)
    
    
    sub_units = Unit.objects.filter(parent=pk)
    
    ctx = {
        'unit': unit,
        'sub_units': sub_units,
    }
    
    return render(request, 'units/unit_detail.html', ctx)
    