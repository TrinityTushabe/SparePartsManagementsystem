from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
#here we're importing models (all)
from .models import *  
#here we're importing forms *(all)
from .forms import *  
#here we're importing filters *(all)
from .filters import *  
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from PIL import Image

# Create your views here.
def index(request):
    return render(request,'assets/index.html')

def home(request):  #requesting login
    products = Product.objects.all().order_by('-id') #this querying a database (ordering by id )
    product_filters = ProductFilter(request.GET,queryset=products)
    products = product_filters.qs
    return render(request, 'assets/home.html',{'products':products, 'product_filters':product_filters})

@login_required
def all_sales(request):
    sales = Sale.objects.all()
    total = sum([items.amount_received  for items in sales])
    change = sum([items.get_change() for items in sales])
    gross = total + change
    
    return render(request, 'assets/all_sales.html', {'sales': sales, 'total': total, 'change': change, 'gross': gross})
    


@login_required
def issued_item(request, pk):
    issued_item = Product.objects.get(id=pk)
    sales_form = SaleForm(request.POST)
    
    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            #keeping track of the remaining stock
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()
            
            print(issued_item.part_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)
            
            return redirect('receipt')
    return render(request, 'assets/issue_item.html', {'sales_form':sales_form})

@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request, 'assets/receipt.html', {'sales':sales})

@login_required
def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id=receipt_id)
    return render(request, 'assets/receipt_detail.html', {'receipt':receipt})

@login_required
def add_to_stock(request, pk):
    issued_item = Product.objects.get(id=pk)
    form = AddForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity']) 
            issued_item.total_quantity += added_quantity
            issued_item.save()
            
            #to add to the rmaining stock quantity is reduced
            print(added_quantity)
            print(issued_item.total_quantity)
            return redirect('home') 
        
    return render(request, 'assets/add_to_stock.html',{'form':form})      
        

@login_required
def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request,'assets/product_detail.html',{'product':product})

# The login and logout views are already imported from django.contrib.auth.views
# and can be used directly in urlpatterns as shown in my original code.


@login_required
def user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile.profile_picture = form.cleaned_data['profile_picture']
    
            user_profile.save()
            return redirect('user_profile')

    else:
        form = ProfilePictureForm()

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'assets/user_profile.html', context)
