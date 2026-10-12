from django.shortcuts import render
from .models import FoodOrder

def order_list(request):
    # Get model fields for Task 1 table
    fields_info = []
    for i, field in enumerate(FoodOrder._meta.get_fields(), start=1):
        # Skip relation fields if any, and keep normal fields
        if hasattr(field, 'get_internal_type'):
            fields_info.append({
                's_no': len(fields_info) + 1,
                'name': field.name,
                'type': field.get_internal_type()
            })
            
    # Get all orders for Task 2 table
    orders = FoodOrder.objects.all()
    
    context = {
        'fields_info': fields_info,
        'orders': orders
    }
    return render(request, 'canteen/order_list.html', context)

# Create your views here.
