# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Receipt

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'gender', 'additional_info')

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'gender', 'additional_info')

class PatientDetailsForm(forms.Form):
    patient_name = forms.CharField(label='Patient Name', max_length=100)
    date_of_birth = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    immuneel_patient_id = forms.CharField(label='Immuneel Patient ID', max_length=100)
    hospital_patient_id = forms.CharField(label='Hospital Patient ID', max_length=100)
    generate_qr = forms.BooleanField(label='Generate QR Code', required=False)
    # Other fields as needed

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['patient_name', 'date_of_birth', 'immuneel_patient_id', 'hospital_patient_id', 'receipt_type']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Retrieve user from kwargs
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'] = forms.ModelChoiceField(queryset=CustomUser.objects.filter(pk=user.pk), initial=user.pk, widget=forms.HiddenInput())