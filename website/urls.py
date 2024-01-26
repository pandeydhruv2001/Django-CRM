from django.urls import path
from . import views
# Create actual Template File
# Create a actual HTML page
# Then create a view
urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
]
