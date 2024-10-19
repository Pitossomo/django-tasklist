from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm

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

    return render(request, 'link/create_category.html', {'form': form})
