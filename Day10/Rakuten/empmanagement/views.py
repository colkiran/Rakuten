from django.shortcuts import render
from .forms import EmployeeRegistration
from .models import User

# Create your views here.

def new_disp(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST)
        emp = []
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = EmployeeRegistration()
    else:
        fm = EmployeeRegistration()
    emp = User.objects.all()
    return render(request, 'newanddisp.html', {'form': fm})
