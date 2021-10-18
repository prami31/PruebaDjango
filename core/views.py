from django.shortcuts import render
from core.forms import AutorForm, LibroFormSet

from core.models import Autor, Libro


def autores(request):
    autores_lista = Autor.objects.all()
    context = {'autores': autores_lista}

    return render(request, 'core/autores.html', context)


def ver_librosxx(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    context = {
        'libros': autor.libro_set.all(),
        'autor': autor
    }
    return render(request, 'core/ver-libros.html', context)


def ver_libros(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    libros = Libro.objects.filter(autor_id=autor_id)
    context = {
        'libros': libros,
        'autor': autor
    }
    return render(request, 'core/ver-libros.html', context)


def agregar_autor(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        ciudad = request.POST.get('ciudad')

        titulo = request.POST.getlist('titulo')
        fecha_publicacion = request.POST.getlist('fecha_publicacion')
        numero_hojas = request.POST.getlist('numero_hojas')

        autor = Autor(nombres=nombres, apellidos=apellidos, ciudad=ciudad)

        autor.save()

    return render(request, 'core/agregar.html')


def agregar_autor_eficaz(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        libro_form = LibroFormSet(request.POST)

        if autor_form.is_valid() and libro_form.is_valid():
            autor_nuevo = autor_form.save()
            libro_form.instance = autor_nuevo
            libro_form.save()

    autor_form = AutorForm()
    libro_form = LibroFormSet()
    context = {'autor_form': autor_form, 'libro_form': libro_form}
    return render(request, 'core/agregar-eficaz.html', context)


def editar_autor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)

    if request.method == 'POST':
        autor_form = AutorForm(request.POST, instance=autor)
        libro_form = LibroFormSet(request.POST, instance=autor)

        if autor_form.is_valid() and libro_form.is_valid():
            autor_form.save()
            libro_form.save()

    autor_form = AutorForm(instance=autor)
    libro_form = LibroFormSet(instance=autor)
    context = {'autor_form': autor_form, 'libro_form': libro_form}
    return render(request, 'core/agregar-eficaz.html', context)
