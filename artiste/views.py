from django.shortcuts import render
from .models import Biography

def biography_list(request):
    biographies = Biography.objects.all()
    return render(request, 'biography.html', {'biographies': biographies})
