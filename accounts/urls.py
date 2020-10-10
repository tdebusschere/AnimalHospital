from django.urls import path

from . import views
from AnimalHospital import settings

urlpatterns = [
                path('signup/', views.SignUpView.as_view(), name='signup')
               ]
