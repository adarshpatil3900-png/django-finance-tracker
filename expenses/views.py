from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import StyledAuthenticationForm, StyledUserCreationForm, TransactionForm
from .models import Transaction


class StyledLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = StyledAuthenticationForm


class RegisterView(CreateView):
    form_class = StyledUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "Account created. You can log in now.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please fix the errors below and try again.")
        return super().form_invalid(form)


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    context_object_name = "transactions"
    template_name = "expenses/dashboard.html"

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = (
            self.get_queryset().aggregate(s=Sum("amount"))["s"] or Decimal("0")
        )
        context["total_balance"] = total
        return context


class TransactionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy("expenses:transaction_list")
    success_message = "Transaction “%(title)s” was added successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)


class TransactionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy("expenses:transaction_list")
    success_message = "Transaction “%(title)s” was updated successfully."

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)


class TransactionDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy("expenses:transaction_list")
    success_message = "Transaction “%(title)s” was deleted."

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
