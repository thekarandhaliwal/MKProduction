from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about_us(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def service_detail(request):
    return render(request, "service_detail.html")

def studio(request):
    return render(request, "studio.html")

def studio_detail(request):
    return render(request, "studio_detail.html")

def faq(request):
    return render(request, "faq.html")

def appointment(request):
    return render(request, "appointment.html")

def contact(request):
    return render(request, "contact.html")

def date(request):
    return render(request, "date.html")

from django.shortcuts import render

def login_page(request):
    return render(request, "login.html")

def signup_page(request):
    return render(request, "signup.html")

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


# @api_view(['POST'])
# def login_view(request):
#     email = request.data.get("email")
#     password = request.data.get("password")

#     try:
#         user = User.objects.get(email=email)
#     except User.DoesNotExist:
#         return Response({"error": "Invalid email"}, status=400)

#     user = authenticate(username=user.username, password=password)

#     if user is not None:
#         refresh = RefreshToken.for_user(user)

#         return Response({
#             "access": str(refresh.access_token),
#             "refresh": str(refresh)
#         })

#     return Response({"error": "Invalid password"}, status=400)


from rest_framework_simplejwt.tokens import RefreshToken

# @api_view(['POST'])
# def login_view(request):
#     email = request.data.get("email")
#     password = request.data.get("password")

#     try:
#         user = User.objects.get(email=email)
#     except User.DoesNotExist:
#         return Response({"error": "Invalid email"}, status=400)

#     user = authenticate(username=user.username, password=password)

#     if user is not None:
#         refresh = RefreshToken.for_user(user)

#         # ✅ ADD EXTRA DATA IN TOKEN
#         refresh['username'] = user.username
#         refresh['email'] = user.email

#         return Response({
#             "access": str(refresh.access_token),
#             "refresh": str(refresh)
#         })

#     return Response({"error": "Invalid password"}, status=400)

# from django.contrib.auth.models import User
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['POST'])
# def signup(request):
#     try:
#         username = request.data.get('username')
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if User.objects.filter(username=username).exists():
#             return Response({"error": "Username exists"}, status=400)

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password
#         )

#         return Response({"message": "User created"}, status=201)

#     except Exception as e:
#         return Response({"error": str(e)}, status=500)
    
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


# ✅ SIGNUP
@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response({"error": "All fields required"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already exists"}, status=400)

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return Response({"message": "User created successfully"}, status=201)


# ✅ LOGIN WITH EMAIL
@api_view(['POST'])
def login_view(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"error": "Email and password required"}, status=400)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "Invalid email"}, status=400)

    user = authenticate(username=user.username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)

        # ✅ Add extra data in token
        refresh['username'] = user.username
        refresh['email'] = user.email

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })

    return Response({"error": "Invalid password"}, status=400)

import json
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from cashfree_pg.api_client import Cashfree
from cashfree_pg.models.create_order_request import CreateOrderRequest
from cashfree_pg.models.customer_details import CustomerDetails
import json
import uuid
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# @csrf_exempt
# def create_order(request):
#     try:
#         body = json.loads(request.body)

#         amount = float(body.get("amount", 1))
        
#         order_id = f"order_{uuid.uuid4().hex[:10]}"

#         url = "https://sandbox.cashfree.com/pg/orders"

#         headers = {
#             "x-client-id": settings.CASHFREE_APP_ID,
#             "x-client-secret": settings.CASHFREE_SECRET_KEY,
#             "x-api-version": "2022-09-01",
#             "Content-Type": "application/json"
#         }

#         payload = {
#             "order_id": order_id,
#             "order_amount": amount,
#             "order_currency": "INR",

#             "customer_details": {
#                 "customer_id": "cust_001",
#                 "customer_email": "test@gmail.com",
#                 "customer_phone": "9999999999"
#             },

#             # ✅ ADD THIS (IMPORTANT)
#             "order_meta": {
#                 "return_url": f"http://127.0.0.1:8000/payment-success?order_id={order_id}"
#             },

#             # ✅ ADD THIS (VERY IMPORTANT)
#             "order_note": "Studio booking payment"
#         }

#         # response = requests.post(url, headers=headers, json=payload)
#         # data = response.json()

#         # print("Cashfree Response:", data)

#         # return JsonResponse({
#         #     "payment_session_id": data.get("payment_session_id")
#         # })
    
#         response = requests.post(url, headers=headers, json=payload)
#         data = response.json()

#         print("FULL RESPONSE:", data)

#         if not data.get("payment_session_id"):
#             return JsonResponse({"error": data})

#         return JsonResponse({
#             "payment_session_id": data.get("payment_session_id")
#         })

#     except Exception as e:
#         print("ERROR:", str(e))
#         return JsonResponse({"error": str(e)}, status=500)


# views.py


import uuid
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from .models import Order
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    try:
        user = request.user
        amount = float(request.data.get("amount"))

        order_id = f"order_{uuid.uuid4().hex[:10]}"

        order = Order.objects.create(
            user=user,
            order_id=order_id,
            amount=amount
        )

        url = "https://api.cashfree.com/pg/orders"

        headers = {
            "x-client-id": settings.CASHFREE_APP_ID,
            "x-client-secret": settings.CASHFREE_SECRET_KEY,
            "x-api-version": "2022-09-01",
            "Content-Type": "application/json"
        }

        payload = {
            "order_id": order_id,
            "order_amount": amount,
            "order_currency": "INR",
            "customer_details": {
                "customer_id": str(user.id),
                "customer_email": user.email,
                "customer_phone": "8360000717"
            },
            # "order_meta": {
            #     "return_url": f"{settings.BASE_URL}/payment-success?order_id={order_id}"
            # }
            "order_meta": {
                "return_url": f"https://7c12-2401-4900-8fe2-7321-888f-43c4-40a5-12f5.ngrok-free.app/payment-success?order_id={order_id}"
            }
        }

        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        print("FULL RESPONSE:", data)

        if not data.get("payment_session_id"):
            return Response({"error": data}, status=400)

        return Response({
            "payment_session_id": data["payment_session_id"],
            "order_id": order_id
        })

    except Exception as e:
        return Response({"error": str(e)}, status=500)
    


# # views.py
# @csrf_exempt
# def cashfree_webhook(request):
#     try:
#         data = json.loads(request.body)

#         order_id = data.get("order", {}).get("order_id")
#         order_status = data.get("order", {}).get("order_status")

#         order = Order.objects.get(order_id=order_id)

#         if order_status == "PAID":
#             order.status = "PAID"
#         else:
#             order.status = "FAILED"

#         order.save()

#         return JsonResponse({"status": "success"})

#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order
import hashlib
import hmac



@csrf_exempt
def cashfree_webhook(request):
    try:
        print("🔥 WEBHOOK HIT")

        data = json.loads(request.body)
        print("FULL DATA:", data)

        order_data = data.get("data", {}).get("order", {})
        payment_data = data.get("data", {}).get("payment", {})

        order_id = order_data.get("order_id")

        # ✅ FIX HERE
        payment_status = payment_data.get("payment_status")

        print("ORDER:", order_id, payment_status)

        if not order_id:
            return JsonResponse({"status": "no order"}, status=200)

        try:
            order = Order.objects.get(order_id=order_id)

            # ✅ USE payment_status INSTEAD
            if payment_status == "SUCCESS":
                order.status = "PAID"
            elif payment_status in ["FAILED", "USER_DROPPED"]:
                order.status = "FAILED"

            # save transaction id
            order.cf_payment_id = payment_data.get("cf_payment_id")
            order.payment_method = str(payment_data.get("payment_method"))
            order.bank_reference = payment_data.get("bank_reference")
            
            order.save()

            print("✅ UPDATED:", order.order_id, order.status)

        except Order.DoesNotExist:
            print("❌ Order not found:", order_id)

        return JsonResponse({"status": "ok"}, status=200)

    except Exception as e:
        print("❌ WEBHOOK ERROR:", str(e))
        return JsonResponse({"status": "error"}, status=200)
# @csrf_exempt
# def cashfree_webhook(request):
#     try:
#         print("WEBHOOK HIT")

#         # ✅ parse safely
#         try:
#             data = json.loads(request.body)
#         except:
#             data = {}

#         print("WEBHOOK DATA:", data)

#         # ✅ safe extraction
#         order_data = data.get("data", {}).get("order", {})

#         order_id = order_data.get("order_id")
#         order_status = order_data.get("order_status")

#         if order_id:
#             try:
#                 order = Order.objects.get(order_id=order_id)

#                 if order_status == "PAID":
#                     order.status = "PAID"
#                 elif order_status == "FAILED":
#                     order.status = "FAILED"

#                 order.save()

#                 print("UPDATED:", order_id, order.status)

#             except Order.DoesNotExist:
#                 print("Order not found:", order_id)

#         # ✅ ALWAYS return 200 (VERY IMPORTANT)
#         return JsonResponse({"status": "ok"}, status=200)

#     except Exception as e:
#         print("WEBHOOK ERROR:", str(e))

#         # ✅ NEVER fail webhook
#         return JsonResponse({"status": "error"}, status=200)
    


# @csrf_exempt
# def cashfree_webhook(request):
#     try:
#         signature = request.headers.get('x-webhook-signature')
#         body = request.body

#         # ✅ verify signature
#         generated_signature = hmac.new(
#             settings.CASHFREE_WEBHOOK_SECRET.encode(),
#             body,
#             hashlib.sha256
#         ).hexdigest()

#         if signature != generated_signature:
#             return JsonResponse({"error": "Invalid signature"}, status=400)

#         data = json.loads(body)

#         order_id = data["order"]["order_id"]
#         order_status = data["order"]["order_status"]

#         order = Order.objects.get(order_id=order_id)

#         if order_status == "PAID":
#             order.status = "PAID"
#         else:
#             order.status = "FAILED"

#         order.save()

#         return JsonResponse({"status": "success"})

#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verify_payment(request):
    order_id = request.GET.get("order_id")

    try:
        order = Order.objects.get(order_id=order_id, user=request.user)

        return Response({
            "order_id": order.order_id,
            "status": order.status,
            "amount": order.amount
        })

    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)
    

# views.py
from django.shortcuts import render

def payment_success(request):
    return render(request, "payment_success.html")