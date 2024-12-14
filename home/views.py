# Create your views here.
from django.shortcuts import render

# gpt ne add krvaaya
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerDetails
from rest_framework import serializers
# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.contrib.auth.models import User

from home.serializer import UserSerializer
from rest_framework.decorators import api_view

# gpt ne add krvaaya
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerDetails
from rest_framework import serializers


@api_view(['POST'])
def create_user_order(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # Create the customer order in the database
        CustomerDetails.objects.create(**serializer.validated_data)
        return Response({"message": "Customer order created successfully!"}, status=status.HTTP_201_CREATED)
    
@api_view(['PUT'])
def update_order(request):
    # Fetch the order from the database using the ID
    order = CustomerDetails.objects.filter(order_id=request.data['order_id']).first()
    if not order:
        return Response({"message": f"Order with ID {request.data['order_id']} not found."}, status=404)
    # Serialize the existing order and update only the fields that are passed in the request
    serializer = UserSerializer(order, data=request.data, partial=True)  # partial=True allows partial updates
    if serializer.is_valid():
        serializer.save()  # Save the updated order
        return Response({"message": f"Order with ID {request.data['order_id']} has been updated."}, status=200)
    
    return Response(serializer.errors, status=400)  # Return validation errors if serializer is invalid

@api_view(['PATCH'])
def patch_krunga(request):
    # from complete data (payload) fetch the order_id key value for updating 
    order_id = CustomerDetails.objects.filter(order_id=request.data['order_id']).first()
    if not order_id:
        return Response({"message": f"Order with ID {request.data.get('order_id')} not found."}, status=404)
    # partial=True allows partial updates
    serializer = UserSerializer(order_id,data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()  # Save the updated order
        return Response({"message": f"Order with ID {request.data['order_id']} has been updated."}, status=200)
    
    return Response(serializer.errors, status=400)  # Return validation errors if serializer is invalid

# gpt bhaiaya helped with 1-2 lines
# @api_view(['PATCH'])
# def patch_krunga(request):
#     # Fetch the order by order_id
#     order = CustomerDetails.objects.filter(order_id=request.data.get('order_id')).first()
#     # Serialize the existing order and apply partial updates with the payload
#     serializer = UserSerializer(order, data=request.data, partial=True)  # partial=True allows for partial updates
    
#     if serializer.is_valid():
#         serializer.save()  # Save the updated order
#         return Response({"message": f"Order with ID {request.data.get('order_id')} has been updated."}, status=200)
    
#     return Response(serializer.errors, status=400)  # Return validation errors if serializer is invalid

#     # return Response("good boy")

# @api_view(['PUT'])
# def update_order(request,id):
#     update = CustomerDetails.objects.filter(order_id=id)
#     if not update.exists():
#         return Response({"message": f"Order with ID {id} not found."}, status=404)
#     update = UserSerializer(data=request.data())
#     update.save()
#     return Response({"message": f"Order with ID {id} has been updated."}, status=200)

@api_view(['DELETE'])
def delete_order(request, id):
    order = CustomerDetails.objects.filter(order_id=id)
    
    if not order.exists():
        return Response({"message": f"Order with ID {id} not found."}, status=404)

    order.delete()
    return Response({"message": f"Order with ID {id} has been deleted."}, status=200)




@api_view(['GET'])
def read_all_orders(request):
    users = CustomerDetails.objects.all()
    serializer = UserSerializer(users, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def read_unique_order_id(request, id):
    orderid = CustomerDetails.objects.filter(order_id=id)
    serializer = UserSerializer(orderid, many=True)
    return Response(serializer.data)



# def home_view(request):
#     return HttpResponse("<h1>Welcome to the Home Page!</h1>")

# def jai_shree_ram(request):
#     return HttpResponse("<h1> Jai shree ram </h1>")

# @method_decorator(csrf_exempt, name='dispatch')
# def create_user(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)  # Parse JSON body
#             username = data.get('username')
#             password = data.get('password')

#             # Validate required fields
#             if not username or not password:
#                 return JsonResponse({'error': 'Username and password are required'}, status=400)

#             # Create user
#             user = User.objects.create_user(username=username, password=password)
            
#             return JsonResponse({'message': 'User created', 'user_id': user.id}, status=200)
        
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
    
#     return JsonResponse({'error': 'chodu galat method h ye'}, status=200)
