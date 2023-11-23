from django.shortcuts import render, redirect
from .models import Table
from .forms import ReservationForm


def homepage(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'about.html')


def menu(request):
    return render(request, 'menu.html')


def service(request):
    return render(request, 'service.html')


def available_tables(request):
    tables = Table.objects.filter(is_available=True)
    return render(request, 'tables.html', {'tables': tables})


def contact(request):
    return render(request, 'contact.html')


def team(request):
    return render(request, 'team.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def new_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ReservationForm()
    return render(request, 'booking.html', {'form': form})

# def new_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = OrderForm()
#     return render(request, 'new_order.html', {'form': form})
