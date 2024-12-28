from django import forms 
from Monface.models import Person, Student,Employee
class LoginForm(forms.Form):
    email=forms.EmailField(label='Email')
    password=forms.CharField(label='Mot de passe',widget=forms.PasswordInput)
    def clean(self):
        cleaned_data=super().clean()
        email=cleaned_data.get("email")
        password=cleaned_data.get("password")
        if email and password :
            Result= Person.objects.filter(password=password,email=email)
            if len(Result) != 1:
                raise forms.ValidationError("Adresse ou mot de pas incorrects.")
        return cleaned_data

class StudentProfilForm(forms.ModelForm):
    class Meta :
        model = Student
        exclude=('Amis',)

class EmployeeProfilForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ('Amis',)