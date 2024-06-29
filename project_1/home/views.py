
 # Assuming this is your custom user model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 
from .forms import CustomUserCreationForm
from .models import CustomUser
import qrcode
from django.contrib.auth.forms import AuthenticationForm 
from io import BytesIO
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid. Saving user...")
            user = form.save()
            print(f"User {user.username} created successfully.")
            
            # Authenticate and login the user with specific backend
            user = authenticate(request, username=user.username, password=form.cleaned_data['password1'])
            if user is not None:
                print("Authentication successful. Logging in user...")
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                print("User logged in successfully.")
                return redirect('qr_code')  # Redirect to success page
            else:
                print("Authentication failed.")
        else:
            print("Form is not valid:", form.errors)
    else:
        form = CustomUserCreationForm()
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
                return redirect('qr_code')
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
    # Get user details
    user = request.user
    user_details = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        # Add more details as needed
    }

    # Generate QR code with user details
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(str(user_details))
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    qr_img.save(buffer)
    qr_img_binary = buffer.getvalue()

    # Render template with QR code
    
    return render(request, 'home/profile.html', {'qr_code': qr_img_binary})
    