from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# This will automatically generate the URLs for your API
router = DefaultRouter()
router.register(r'cvspots', views.CVSpotsViewSet)
router.register(r'cvconfig', views.CVConfigViewSet)
router.register(r'fooditem', views.FoodItemViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('auth/', views.auth, name='auth'),
    path('logout/', views.logout_view, name='logout'),
    path('config/', views.config, name='config'),
    path('api/', include(router.urls)),  # Add this line to include the API URLs
]

