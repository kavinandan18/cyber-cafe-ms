from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.EmailBackEnd import EmailBackEnd
from accounts.models import User as CustomUser

User = get_user_model()

def LOGIN(request):
    return render(request, 'accounts\login.html')

def REGISTER(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.save()
        messages.success(request, 'User registered successfully')
        return redirect('login')

    return render(request, 'accounts\\register.html')


def doLogin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password')
                                         )
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'index' with the appropriate URL name after login
        else:
            messages.error(request, 'Email or Password is not valid')
            return redirect('login')
    else:
        messages.error(request, 'Invalid method')
        return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/accounts/login/')
def PROFILE(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    context = {"user": user}
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='/accounts/login/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if profile_pic:
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, "Your profile has been updated successfully")
            return redirect('profile')
        except CustomUser.DoesNotExist:
            messages.error(request, "User does not exist")
        except Exception as e:
            messages.error(request, f"Error updating profile: {e}")

    return redirect('profile')


@login_required(login_url='/')
def CHANGE_PASSWORD(request):
    context = {}
    user = get_object_or_404(User, id=request.user.id)

    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")

        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            login(request, user)
            messages.success(request, 'Password changed successfully!')
        else:
            messages.error(request, 'Current password is incorrect!')

    context["user"] = user
    return render(request, 'accounts\change-password.html', context)
