from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Guest
from django.urls import reverse
from django.utils import timezone

def index_view (request):
    guests = Guest.objects.all()

    context = {
        'guests': guests
    }
    url = reverse('index')
    return render(request, 'index.html', context)


def guest_view(request, pk):
    guest = Guest.objects.get(pk=pk)
    context = {'guest': guest}
    return render(request, 'guest_view.html', context)
