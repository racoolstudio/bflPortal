from django.shortcuts import render
from Production.models import Production


# Create your views here.

def production_index_view(request, *args, **kwargs):
    productions = Production.objects.all()
    return render(request, 'index.html', {'productions': productions})
