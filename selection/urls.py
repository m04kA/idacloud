from django.urls import path

from . import views

urlpatterns = [
    path('bank_create/', views.BankCreateView.as_view()),
    path('banks/', views.BankListView.as_view())
]


