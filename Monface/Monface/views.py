from django.shortcuts import render, redirect
from Monface.forms import EmployeeProfilForm, LoginForm, StudentProfilForm

def login(request):
    if len(request.POST) > 0 :
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/welcome') 
        else:
            return render(request, 'login.html', {'form': form})
    else:
        loginform = LoginForm()
        return render(request, 'login.html', {'form': loginform})

def register(request):
    if request.method == "POST":
        user_type = request.POST.get('user_type')
        if user_type == 'student':
            studentForm = StudentProfilForm(request.POST)
            employeeForm = None
            if studentForm.is_valid():
                studentForm.save()
                return redirect('/login')
            else:
                return render(request, 'user_profile.html', {'studentForm': studentForm, 'user_type': user_type})
        elif user_type == 'employee':
            employeeForm = EmployeeProfilForm(request.POST)
            studentForm = None
            if employeeForm.is_valid():
                employeeForm.save()
                return redirect('/login')
            else:
                return render(request, 'user_profile.html', {'employeeForm': employeeForm, 'user_type': user_type})
    else:
        studentForm = StudentProfilForm()
        employeeForm = EmployeeProfilForm()  # Assurez-vous de créer une instance de EmployeeProfilForm
        return render(request, 'user_profile.html', {'studentForm': studentForm, 'employeeForm': employeeForm})

def welcome(request):
    return render(request, 'welcome.html')
