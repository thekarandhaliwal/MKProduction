from django.urls import path
from .views import *
from django.urls import path
from .views import signup
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# urlpatterns = [
#     path('', index, name='index'),
#     path('about-us/', about_us, name='about_us'),
#     path('services/', services, name='services'),
#     path('service-detail/', service_detail, name='service_detail'),
#     path('studio/', studio, name='studio'),
#     path('studio_detail/', studio_detail, name='studio_detail'),
#     path('faq/', faq, name='faq'),
#     path('appointment/', appointment, name='appointment'),
#     path('contact/', contact, name='contact'),
#     path('create-order/', create_order),
#     path('signup/', signup),
#     path('login/', TokenObtainPairView.as_view()),
#     path('refresh/', TokenRefreshView.as_view()),
#     path('login-page/', login_page),
#     path('signup-page/', signup_page),
#     path('login/', login_view),
# ]


# urlpatterns = [
#     path('', index, name='index'),
#     path('about-us/', about_us, name='about_us'),
#     path('services/', services, name='services'),
#     path('service-detail/', service_detail, name='service_detail'),
#     path('studio/', studio, name='studio'),
#     path('studio_detail/', studio_detail, name='studio_detail'),
#     path('faq/', faq, name='faq'),
#     path('appointment/', appointment, name='appointment'),
#     path('contact/', contact, name='contact'),
#     path('create-order/', create_order),

#     path('signup/', signup),

#     # ✅ KEEP THIS
#     path('login/', login_view),

#     # ✅ token refresh still needed
#     path('refresh/', TokenRefreshView.as_view()),

#     path('login-page/', login_page),
#     path('signup-page/', signup_page),
# ]


from django.urls import path
from .views import signup, login_view, login_page, signup_page
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', index, name='index'),
    path('about-us/', about_us, name='about_us'),
    path('services/', services, name='services'),
    path('service-detail/', service_detail, name='service_detail'),
    path('studio/', studio, name='studio'),
    path('studio_detail/', studio_detail, name='studio_detail'),
    path('faq/', faq, name='faq'),
    path('appointment/', appointment, name='appointment'),
    path('contact/', contact, name='contact'),
    path('date/', date, name='date'),
    path('create-order/', create_order),

    path('signup/', signup),
    path('login/', login_view),
    path('refresh/', TokenRefreshView.as_view()),

    path('login-page/', login_page),
    path('signup-page/', signup_page),
    path('create-order/', create_order),
    path('cashfree/webhook/', cashfree_webhook),
    path('payment-success/', payment_success, name='payment_success'),
    path('verify-payment/', verify_payment),
]