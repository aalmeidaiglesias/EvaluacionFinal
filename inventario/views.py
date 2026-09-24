from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


def lista_productos(request):

    productos = Producto.objects.all()

    return render(
        request,
        'inventario/lista.html',
        {
            'productos': productos
        }
    )


def crear_producto(request):

    if request.method == 'POST':

        formulario = ProductoForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            return redirect('lista_productos')

    else:

        formulario = ProductoForm()

    return render(
        request,
        'inventario/formulario.html',
        {
            'formulario': formulario,
            'titulo': 'Registrar producto'
        }
    )


def editar_producto(request, id):

    producto = get_object_or_404(
        Producto,
        id=id
    )

    if request.method == 'POST':

        formulario = ProductoForm(
            request.POST,
            instance=producto
        )

        if formulario.is_valid():

            formulario.save()

            return redirect('lista_productos')

    else:

        formulario = ProductoForm(
            instance=producto
        )

    return render(
        request,
        'inventario/formulario.html',
        {
            'formulario': formulario,
            'titulo': 'Editar producto'
        }
    )


def eliminar_producto(request, id):

    producto = get_object_or_404(
        Producto,
        id=id
    )

    if request.method == 'POST':

        producto.delete()

        return redirect('lista_productos')

    return render(
        request,
        'inventario/eliminar.html',
        {
            'producto': producto
        }
    )