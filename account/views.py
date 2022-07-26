from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .models import Customer

def log_in(request):
    if request.method == 'POST':
        phone_number=request.POST.get('phone_number',None)
        password=request.POST.get('password',None)
        customer = authenticate(
            phone_number=phone_number,
            password=password
        )
        print(customer)
        if customer:
            login(request,customer)
            return redirect('home')

    return render(
        request=request,
        template_name='auth/signin.html'
    )

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

def register(request):
    print(request.POST)
    user_message:str = ''
    password_message:str = ''
    if request.method == 'POST':
        first_name = request.POST.get('first_name',None)
        last_name = request.POST.get('last_name', None)
        phone_number = request.POST.get('phone_number', None)
        gender = request.POST.get('gender', None)
        password = request.POST.get('password', None)
        password1 = request.POST.get('password1', None)
        user:Customer = Customer.objects.filter(phone_number=phone_number)
        if  user:
            user_message = 'This phone number is busy!'
        elif password1 != password:
            password_message = 'Please make sure password fields is same!'
        else:
            user = Customer.objects.create(
                first_name = first_name,
                last_name = last_name,
                phone_number = phone_number,
                gender = gender,
                password = password
            )
            user.set_password(password)
            user.save()
            if user:
                login(request, user)
            return redirect('home')
    return render(
        request=request,
        template_name='auth/signup.html',
        context= {
            'user_message':user_message,
            'password_message':password_message
        }
    )