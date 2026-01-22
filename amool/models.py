from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator

# amool/models.py
from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    model_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return self.name










# =========================
# مودل السيارات (مرسيدس)
# =========================
class MercedesCar(models.Model):
    name = models.CharField(max_length=50, verbose_name="Car Name")
    model_year = models.PositiveIntegerField(verbose_name="Model Year")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Price")
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# =========================
# الزبون
# =========================
class Customer(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email


# =========================
# الطلب
# =========================
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


# =========================
# عناصر الطلب
# =========================
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    car = models.ForeignKey(MercedesCar, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} × {self.car.name}"


# =========================
# السلة
# =========================
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.customer.email}"


# =========================
# عناصر السلة
# =========================
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    car = models.ForeignKey(MercedesCar, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} × {self.car.name}"
