from django.db import models
from django.utils import timezone
#extending the user model
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model): #model for category
    name = models.CharField(max_length=50, null = False, blank=False, unique=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    #referencing the category of the product 
    Category_name = models.ForeignKey(Category, on_delete = models.CASCADE, null=False, blank=False) #Creating a relationship between the category and product primary key
    #reserved for date of arrival field (written on line 16)
    date_of_arrival = models.DateField(default=timezone.now)
    part_name = models.CharField(max_length=50, null = False, blank=False)
    country_of_orgin = models.CharField(max_length=50, null = False, blank=False)
    total_quantity = models.IntegerField(default=0, null=False, blank=False)
    issued_quantity = models.IntegerField(default=0, null=False, blank= False)
    received_quantity = models.IntegerField(default=0, null=False, blank= False)
    branch_name = models.CharField(max_length=50, null=False, blank= False)
    unit_price = models.IntegerField(default=0, null=False, blank=False)
    
    def __str__(self):
        return self.part_name
    
    
# more models (sales)

class Sale(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.PositiveIntegerField(default=0, null=False, blank=False)
    customers_name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=100, null=False, blank=False, default=0)
    amount_received = models.PositiveIntegerField(default=0, null=False, blank=False)
    unit_price = models.PositiveIntegerField(default=0, null=False, blank=False)
    branch_name = models.CharField(max_length=100,null=False, blank=False)
    date = models.DateField(default=timezone.now)
    
    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)
    
    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))
    
    def __str__(self):
        return self.item.part_name


class UserProfile(models.Model):
    #Creating one to one relationship with the user_profile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.user.username
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Signal to automatically create a UserProfile when a User is created
#this method is not recommended by django 
from django.db.models.signals import post_save
post_save.connect(create_user_profile, sender=User)
