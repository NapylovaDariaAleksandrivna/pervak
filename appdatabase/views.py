from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

# Вывод страниц
def start(request):
    return render(request, 'appdatabase/first.html')

def register_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = UserForm(username=username, password=password)
            #login(request, user)
            return redirect('/home')
    
    return render(request, 'appdatabase/regU.html', {'form': form})

def regiset_group(request):
    return render(request, 'appdatabase/regG.html')
def sign_in(request):#vxod
    return render(request, 'appdatabase/ent.html')
def pay(request):#regis
    return render(request, 'appdatabase/pay.html')

def home(request):
    return render(request, 'appdatabase/account.html')


#Работа с моделью Группы
