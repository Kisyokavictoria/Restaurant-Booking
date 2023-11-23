from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'table', 'date', 'time', 'reservation_fee']


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['name', 'form', 'address', 'date', 'time']
#
#
# class OrderItemForm(forms.ModelForm):
#     class Meta:
#         model = OrderItem
#         fields = ['order', 'menu_item', 'quantity']
