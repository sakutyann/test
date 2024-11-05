from django.urls import path
from . import views

urlpatterns = [path('login/', views.loginworldfunction),
               path('main/', views.mainworldfunction),
               path('account/', views.accountworldfunction),
               path('logout/', views.logoutworldfunction),
               path('form/', views.formworldfunction),
               path('quest/', views.questformworldfunction),
               path('coupon/', views.couponformworldfunction),
               
               ]
