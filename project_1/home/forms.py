# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'gender', 'additional_info')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'gender', 'additional_info')
class PatientDetailsForm(forms.Form):
    patient_name = forms.CharField(label='Patient Name', max_length=100)
    date_of_birth = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    immuneel_patient_id = forms.CharField(label='Immuneel Patient ID', max_length=100)
    hospital_patient_id = forms.CharField(label='Hospital Patient ID', max_length=100)
    generate_qr = forms.BooleanField(label='Generate QR Code', required=False)