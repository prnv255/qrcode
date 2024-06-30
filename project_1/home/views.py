from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
import qrcode
from io import BytesIO
from base64 import b64encode

def index(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def landing(request):
    patient_details = None
    qr_code = None

    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        dob = request.POST.get('dob')
        immuneel_id = request.POST.get('immuneel_id')
        hospital_id = request.POST.get('hospital_id')
        generate_qr = request.POST.get('generate_qr')

        patient_details = {
            'patient_name': patient_name,
            'dob': dob,
            'immuneel_id': immuneel_id,
            'hospital_id': hospital_id
        }

        if generate_qr:
            data = f'Name: {patient_name}\nDOB: {dob}\nImmuneel Patient ID: {immuneel_id}\nHospital Patient ID: {hospital_id}'
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            buffer = BytesIO()
            img.save(buffer)
            buffer.seek(0)
            qr_code = buffer.getvalue()

    return render(request, 'landing.html', {'patient_details': patient_details, 'qr_code': qr_code})

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('index')
