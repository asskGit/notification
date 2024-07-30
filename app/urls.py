from django.urls import path
from .views import *

urlpatterns = [
    path('transactions/', TransactionAPIView.as_view, name='transactions'),
    path('user/', UserAPIView.as_view()),
    path('notifications/', NotificationView.as_view(), name='notification-list'),

]