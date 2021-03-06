from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Guest
from django.urls import reverse
from webapp.forms import GuestForm, GuestDeleteForm

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

def guest_add_view(request):
    if request.method == "GET": 
        form = GuestForm()
        return render(request, 'guest_add_view.html', context={'form': form})
    elif request.method == "POST": 
        form = GuestForm(data=request.POST)  
        if form.is_valid():  
            guest = Guest.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                booking_details=form.cleaned_data.get('booking_details')
            )
            return redirect('guest', pk=guest.id)  
        return render(request, 'guest_add_view.html', context={'form': form}) 


def guest_update_view(request, pk):
   
    guest = get_object_or_404(Guest, id=pk)  

    if request.method == 'GET':  
        form = GuestForm(initial={ 
            'name': guest.name,
            'email': guest.email,
            'booking_details': guest.booking_details
        })
        return render(request, 'guest_update_view.html', context={'form': form, 'guest': guest})  
    elif request.method == 'POST':  
        form = GuestForm(data=request.POST)  
        if form.is_valid():  
            guest.name = form.cleaned_data.get("name")
            guest.email = form.cleaned_data.get("email")
            guest.booking_details = form.cleaned_data.get("booking_details")
            guest.save()
            return redirect('guest', pk=guest.id)  

        return render(request, 'guest_update_view.html', context={'form': form, 'guest': guest}) 

