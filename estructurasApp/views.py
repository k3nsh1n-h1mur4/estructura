import sqlite3
from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from .forms import SearchForm, RegistroForm 
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm 

def index(request):
    return HttpResponse('Index de la página')
    
@login_required
def registro(request):
    title = 'Registro'
    error = None
    form = RegistroForm(request.POST)
    if request.method == 'POST': 
        pass
        

    return render(request, 'register.html', {'title': title, 'form': form, 'error': error})


def login(request):
    title = 'LogIn'
    error = None
    form = AuthenticationForm(request.POST)
    print(form)
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        print(form)
        m = User.objects.get(username=request.POST['username'])
        print(m)
        if m.check_password(request.POST['password']):
            request.session['username'] = m.username
            return redirect('list')
        else: error = 'No logueado'

    username = request.POST.get('username')
    password = request.POST.get('password')
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print(username)
        user = authenticate(request, username=username, password=password)
        login(request)
        print(request)
        if user:
            print('Auth')
    return render(request, 'registration/logint.html', {'title': title, 'error': error, 'form': form, 'user': user})

@login_required
def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


def profile(request):
    title = 'Perfil'
    error = None
    user = request.session['username']
    return redirect(request, 'registration/profile.html', {'title': title, 'error': error, 'user': user})



@login_required
def list(request):
    error = None
    title = 'Listado General'
    if request.method == 'GET':
        print(request.session.get('_auth_user_id'))
        id = request.session.get('_auth_user_id')
        cnx = sqlite3.connect('db.sqlite3')
        cur = cnx.cursor()
        cur.execute('SELECT * FROM estructurasApp_basep1 INNER JOIN auth_user WHERE estructurasApp_basep1.UserID_id = auth_user.id AND auth_user.id=?',[id,])
        ctx =  cur.fetchall()
        cur.close()
        cnx.close()
        paginator = Paginator(ctx, 15)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
    return render(request, 'listado.html', {'ctx': ctx, 'title': title, 'page_obj': page_obj})


@login_required
def info(request, field1):
    field1 = field1
    print(field1)
    title = 'Información'
    error = None
    if request.method == 'GET':
        cnx = sqlite3.connect('db.sqlite3')
        cur = cnx.cursor()
        cur.execute('SELECT * FROM estructurasApp_basep1 WHERE field1 = ?', [field1,])
        ctx = cur.fetchone()
        print(ctx)
        if not ctx:
            error = 'No hay Información que mostrar'
        cur.close()
        cnx.close()
    return render(request, 'info.html', {'ctx': ctx, 'title': title, 'error': error})

@login_required
def search(request):
    title = 'Buscar'
    error = None
    
    form = SearchForm(request.GET)
    q = request.GET.get('q', 'default')
    cnx = sqlite3.connect('db.sqlite3')
    cur = cnx.cursor()
    cur.execute("SELECT * FROM estructurasApp_basep1 WHERE MATRICULA=?", [q,])
    row = cur.fetchone()
    cur.close()
    cnx.close()
    print(row)
    return render(request, 'search.html', {'form': form, 'ctx': row})
