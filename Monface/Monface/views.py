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

from django.shortcuts import render, redirect
from .forms import StudentProfilForm, EmployeeProfilForm

def register(request):
    if request.method == "POST":
        user_type = request.POST.get("user_type")
        if not user_type:
            print("Erreur: aucun type d'utilisateur sélectionné")
            return render(request, "user_profile.html", {"error": "Veuillez sélectionner un type d'utilisateur"})

        studentForm = StudentProfilForm(request.POST)
        employeeForm = EmployeeProfilForm(request.POST)

        if user_type == "student" and studentForm.is_valid():
            studentForm.save()  # Enregistrer les données de l'étudiant
            return redirect("/login/")

        elif user_type == "employee" and employeeForm.is_valid():
            employeeForm.save()  # Enregistrer les données de l'employé
            return redirect("/login/")

        else:
            print("Formulaire invalid:", studentForm.errors if user_type == "student" else employeeForm.errors)

    else:
        studentForm = StudentProfilForm()
        employeeForm = EmployeeProfilForm()

    return render(request, "user_profile.html", {
        "studentForm": studentForm,
        "employeeForm": employeeForm,
    })

def welcome(request):
    return render(request, 'welcome.html')
