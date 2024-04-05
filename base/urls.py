from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('edit/<str:pk>/',views.edit,name='edit'),
    path('delete/<str:pk>/',views.delete_task,name='delete'),
    path('delete-completed/',views.delete_completed,name='delete-completed'),

    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('register/',views.register,name='register'),
]
