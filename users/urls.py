from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),  # Landing page view
    path('join-waitlist/', views.join_waitlist, name='join_waitlist'),

]