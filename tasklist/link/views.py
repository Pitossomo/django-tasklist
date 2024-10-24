from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Category, Link
from .forms import CategoryForm, LinkForm

@login_required
def links(request):
    links = Link.objects.filter(created_by=request.user)

    return render(request, 'link/links.html', {'links': links})

@login_required
def create_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)

        if form.is_valid():
            link = form.save(commit=False)
            link.created_by = request.user
            link.save()

    else:
        form = LinkForm()
        form.fields['category'].queryset = Category.objects.filter(created_by=request.user)

    title = 'Criar link'
    return render(request, 'link/create_link.html', {'form': form, 'title': title})

@login_required
def edit_link(request, pk):
    link = get_object_or_404(Link, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)

        if form.is_valid():
            link.save()

            return redirect('/links/')
    else:
        form = LinkForm(instance=link)
        form.fields['category'].queryset = Category.objects.filter(created_by=request.user)

    title = 'Editar link'
    return render(request, 'link/create_link.html', {'form': form, 'title': title})

@login_required
def delete_link(request, pk):
    link = get_object_or_404(Link, pk=pk, created_by=request.user)
    link.delete()

    return redirect('/links/')


@login_required
def categories(request):
    categories = Category.objects.filter(created_by=request.user)

    return render(request, 'link/categories.html', {'categories': categories})

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()

            return redirect('/')
    else:
        form = CategoryForm()

    title = 'Criar categoria'
    return render(request, 'link/create_category.html', {'form': form, 'title': title})

@login_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            category.save()
            return redirect('/links/categories/')
    else:
        form = CategoryForm(instance=category)

    title = 'Editar categoria'
    return render(request, 'link/create_category.html', {'form': form, 'title': title})

@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk, created_by=request.user)
    category.delete()

    return redirect('/links/categories/')
