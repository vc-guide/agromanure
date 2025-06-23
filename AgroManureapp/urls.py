from django.urls import path
from django.conf import settings
from .import views
from .views import *

urlpatterns= [
  path("",views.home,name="home"),
  path('about',views.about, name="about"),
  path('product',views.product_details, name="Products"),
  path('accounts/login/',views.loginview, name='login'),
  path('accounts/sign_up/', views.signup,name='signup'),
  path('logout/',views.logout_view,name='logout'),
  path('productview/<str:product_name>/',views.productview,name="productview"),
  path('ordering/',views.collect_order,name="ordering"),
  path('vieworders',views.orders,name='vieworders'),
  path('eventsurl/',views.eventview,name="eventsurl"),
  path("contactsurl",views.contactview, name="contactsurl"),
  path("apiview/",APIthings.as_view())
 
] 