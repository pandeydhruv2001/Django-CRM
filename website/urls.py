from django.urls import path
from . import views
# Create actual Template File
# Create a actual HTML page
# Then create a view
urlpatterns = [
    path('',views.home,name='home'),
]
