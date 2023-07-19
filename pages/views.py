from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    if request.user.username == "racool":
        return render(request, 'home.html')
    else:
        return HttpResponse("<h1>Abeg gettat, You ain't authorized 🥲</h1>")


