from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Multivendors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.PositiveBigIntegerField()
    restaurant_lic = models.ImageField(upload_to='images/', blank=True, null=True)
    restaurant_img = models.ImageField(upload_to='images/', blank=True, null=True)
    user_type = models.CharField(max_length=50, default='vendor', editable=False)
    approved = models.BooleanField(default=False)
    password = models.CharField(max_length=100)
    franchise = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

class Franchise(models.Model):
    vendor = models.ForeignKey(Multivendors, related_name='franchises', on_delete=models.CASCADE)
    total_investment = models.DecimalField(max_digits=10, decimal_places=2)
    aggr_years = models.PositiveIntegerField()
    profit_sharing = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=255)
    def __str__(self):
        return f"Franchise of {self.vendor.restaurant_name}"

class Userreg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Fooditems(models.Model):
    vendor = models.ForeignKey(Multivendors, related_name='fooditems', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_desc = models.TextField()
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    item_img = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.item_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Fooditems, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name} for {self.user.username}"