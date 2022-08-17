from django.urls import path
from .views import contact

app_name='port'

urlpatterns = [
        path('contact',contact, name='contact'),
        
]