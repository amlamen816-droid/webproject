from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Car, MercedesCar

# صفحات عامة
def main(request):
    return render(request, "main.html")

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def offers(request):
    return render(request, "offers.html")

def reservation(request):
    return render(request, "reservation.html")

# دالة التحقق من الأدمين
def is_admin(user):
    return user.is_staff  # أو is_superuser حسب اختيارك

# تسجيل دخول
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect'})
    return render(request, "login.html")

# تسجيل خروج
def logout_view(request):
    logout(request)
    return redirect('login')

# تسجيل مستخدم جديد
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'signup.html')

# =========================
# صفحة الداشبورد (أدمين فقط)
# =========================
@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def dashboard(request):
    cars = MercedesCar.objects.all()
    return render(request, "dashboard.html", {'cars': cars})

# =========================
# السيارات
# =========================
def cars_view(request):
    cars = Car.objects.all()  # تجيب كل السيارات
    return render(request, 'cars.html', {'cars': cars})


@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def add_car(request):
    if request.method == "POST":
        name = request.POST.get('name')
        model_year = request.POST.get('model_year')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        car = MercedesCar.objects.create(
            name=name,
            model_year=model_year,
            price=price,
            description=description,
            image=image
        )
        messages.success(request, f'تمت إضافة السيارة "{car.name}" بنجاح!')
        return redirect('list_car')
    return render(request, 'add_car.html')

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def list_car(request):
    cars = MercedesCar.objects.all()
    return render(request, 'list_car.html', {'cars': cars})

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def edit_car(request, car_id):
    car = get_object_or_404(MercedesCar, id=car_id)
    if request.method == "POST":
        car.name = request.POST.get('name')
        car.model_year = request.POST.get('model_year')
        car.price = request.POST.get('price')
        car.description = request.POST.get('description')
        if request.FILES.get('image'):
            car.image = request.FILES.get('image')
        car.save()
        messages.success(request, f'تم تعديل السيارة "{car.name}" بنجاح!')
        return redirect('list_car')
    return render(request, 'edit_car.html', {'car': car})

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def delete_car(request, car_id):
    car = get_object_or_404(MercedesCar, id=car_id)
    if request.method == 'POST':
        car_name = car.name
        car.delete()
        messages.success(request, f'تم حذف السيارة "{car_name}" بنجاح!')
        return redirect('admin_dashboard')
    return render(request, 'delete_car.html', {'car': car})
