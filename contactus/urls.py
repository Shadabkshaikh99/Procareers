from django.urls import path
from .views import create_employee, read_employee, read_employee_pk, update_employee, delete_employee, SignupView, CustomObtainAuthToken

urlpatterns = [
    path('contactus_employees/', create_employee, name='create_employee'),
    path('contactus_get/', read_employee, name='read_employee'),
    path('contactus_get_pk/<int:pk>/', read_employee_pk, name='read_employee_pk'),
    path('contactus_update_pk/<int:pk>/', update_employee, name='update_employee'),
    path('contactus_delete_pk/<int:pk>/', delete_employee, name='delete_employee'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
]