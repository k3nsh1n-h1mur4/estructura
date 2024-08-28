import sqlite3
from django.shortcuts import render, redirect, HttpResponse

from .forms import SearchForm 

def index(request):
    return HttpResponse('Index de la página')
    

def list(request):
    error = None
    title = 'Listado General'
    if request.method == 'GET':
        cnx = sqlite3.connect('db.sqlite3')
        cur = cnx.cursor()
        cur.execute('select * from estructurasApp_basep1')
        ctx =  cur.fetchall()
        cur.close()
        cnx.close()
    return render(request, 'listado.html', {'ctx': ctx, 'title': title})


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
