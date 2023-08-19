#Handling forms to be dispalyed for the users
from django.forms import ModelForm
from .models import *

class AddForm(ModelForm): # workers edit form, addind received
    class Meta:
        model = Product
        fields = [
            'received_quantity',
            
        ]

class SaleForm(ModelForm):
    class Meta:
        model = Sale  
        fields = [
            'customers_name','phone_number', 'quantity',  'branch_name', 'date','amount_received',
        ]      
        
class ProfilePictureForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
        
