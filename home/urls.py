from django.urls import path, include
from home.views import home_page
from django.contrib import admin

urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('customer_portal/', include('customer_portal.urls')),
    path('car_dealer_portal/', include('car_dealer_portal.urls')),
]