from django.shortcuts import render, redirect

# Create your views here.


from .models import Staff
from .forms import StaffForm


def index(request):
    
    emps = Staff.objects.order_by('id').all()
    
    ctx = {
        'emps': emps,
    }
    return render(request, 'staff/index.html', ctx)






def add_staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                model=form.instance
                return redirect('staff')
            except:
                pass
    else:
        form = StaffForm()

    return render(request, 'staff/add_staff.html', {'form': form})

