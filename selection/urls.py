from django.urls import path

from . import views

urlpatterns = [
    path('offers/', views.OffersListView.as_view()),
    path('offer_create/', views.OfferCreateView.as_view()),
    path('offer_update/<int:pk>/', views.OfferUpdateView.as_view()),
    path('offer_delete/<int:pk>/', views.OfferDeleteView.as_view()),
]


