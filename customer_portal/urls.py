from django.urls import path, re_path
from customer_portal.views import *  # Ensure this path is correct and the views exist

urlpatterns = [
    re_path(r'^index/$', index),  # Ensure 'index' view exists in customer_portal.views
    re_path(r'^login/$', login),  # Ensure 'login' view exists in customer_portal.views
    re_path(r'^auth/$', auth_view),  # Ensure 'auth_view' exists in customer_portal.views
    re_path(r'^logout/$', logout_view),  # Ensure 'logout_view' exists in customer_portal.views
    re_path(r'^register/$', register),  # Ensure 'register' view exists in customer_portal.views
    re_path(r'^registration/$', registration),  # Ensure 'registration' view exists in customer_portal.views
    re_path(r'^search/$', search),  # Ensure 'search' view exists in customer_portal.views
    re_path(r'^search_results/$', search_results),  # Ensure 'search_results' view exists in customer_portal.views
    re_path(r'^rent/$', rent_vehicle),  # Ensure 'rent_vehicle' view exists in customer_portal.views
    re_path(r'^confirmed/', confirm),  # Ensure 'confirm' view exists in customer_portal.views
    re_path(r'^manage/', manage),  # Ensure 'manage' view exists in customer_portal.views
    re_path(r'^update/', update_order),  # Ensure 'update_order' view exists in customer_portal.views
    re_path(r'^delete/', delete_order),  # Ensure 'delete_order' view exists in customer_portal.views
]