from django.db import models

from django.db import models

class User(models.Model):
    login = models.CharField(max_length=255, primary_key=True)
    full_name = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.login


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PickupPoint(models.Model):
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address


class Product(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    article = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    unit = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='products_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.article} - {self.title}"


class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    login = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_point = models.ForeignKey(PickupPoint, on_delete=models.CASCADE)

    order_date = models.DateField()
    delivery_date = models.DateField()
    receive_code = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Заказ №{self.order_number}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Заказ {self.order.order_number} - {self.product.title}"
