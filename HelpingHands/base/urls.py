from django.urls import path
from .import views


app_name ='base'

urlpatterns = [
    path('',views.home,name='home'),
    path('donate/',views.donate,name='donate'),
    path('thanks/',views.thanks,name="thanks")
]