from home import views
from django.urls import path,include
urlpatterns = [
    
    path('',views.hello),
    path('boutique/',views.boutique)
] 