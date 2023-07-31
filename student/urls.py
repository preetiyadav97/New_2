from django.contrib import admin
from .views import index,about

urlpatterns = [
    path('index/',index ),
    path('about/',about)
]
