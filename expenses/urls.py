from django.urls import path

from . import views

app_name = "expenses"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("", views.TransactionListView.as_view(), name="transaction_list"),
    path("add/", views.TransactionCreateView.as_view(), name="transaction_create"),
    path("<int:pk>/edit/", views.TransactionUpdateView.as_view(), name="transaction_update"),
    path("<int:pk>/delete/", views.TransactionDeleteView.as_view(), name="transaction_delete"),
]
