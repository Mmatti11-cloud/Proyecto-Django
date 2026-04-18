from django.shortcuts import render
from web.models import Ciudad


def index(request):

    ciudades = Ciudad.objects.all()

    return render(request, 'web/index.html', {'ciudades': ciudades})
