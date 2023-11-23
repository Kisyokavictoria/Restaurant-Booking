from django.db import models


class Table(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reservation_fee = models.DecimalField(max_digits=5, decimal_places=2)
    

# class MenuItem(models.Model):
#     name = models.CharField(max_length=700)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#
#
# class Order(models.Model):
#     name = models.CharField(max_length=500)
#     phone = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     date = models.DateField()
#     time = models.TimeField()
#
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     quantity = models.IntegerField()


