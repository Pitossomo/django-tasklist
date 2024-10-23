from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from link.models import Link

SHOW_LAST_LINKS = 5

@login_required
def dashboard(request):

    new_links = Link.objects.filter(created_by=request.user)[0:SHOW_LAST_LINKS]

    return render(request, 'dashboard/dashboard.html', {'new_links': new_links})