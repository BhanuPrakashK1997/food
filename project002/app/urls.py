from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('home/',views.home,name='home'),
    path('create/', views.create, name='create'),
    path('data/', views.data, name='data'),
    path('register/',views.register,name='register'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('<int:recipe_id>/details/', views.details, name='details'),
    path('check/', views.check, name='check'),
    path('sample/',views.sample,name='sample'),
]