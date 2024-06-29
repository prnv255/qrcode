from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            generate_qr = request.POST.get('generate_qr', False)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if generate_qr:
                    return redirect('qr_code')
                else:
                    return redirect('landing_page')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def qr_code_view(request):
    user = request.user
    data = f'Name: {user.username}\nAge: {user.age}\nGender: {user.gender}\nAdditional Info: {user.additional_info}'
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')

@login_required
def profile(request):
    user = request.user
    user_details = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=2,
    )
    qr.add_data(str(user_details))
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    qr_img.save(buffer)
    qr_img_binary = buffer.getvalue()
    return render(request, 'home/profile.html', {'qr_code': qr_img_binary})

def index(request):
    return render(request, 'index.html')

@login_required
def landing_page_view(request):
    return render(request, 'landing_page.html')
