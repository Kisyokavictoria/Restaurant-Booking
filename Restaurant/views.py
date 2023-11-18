from django.shortcuts import render, redirect
from .models import Table
from .forms import ReservationForm, OrderForm


def available_tables(request):
    tables = Table.objects.filter(is_available=True)
    return render(request, '#', {'tables': tables})


def new_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('#')
    else:
        form = ReservationForm()
    return render(request, 'new_reservation.html', {'form': form})


def new_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'new_order.html', {'form': form})
