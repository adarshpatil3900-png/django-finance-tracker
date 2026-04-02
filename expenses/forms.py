from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Transaction

_field = (
    "block w-full rounded-lg border border-slate-300 bg-white px-4 py-2.5 "
    "text-slate-900 shadow-sm placeholder:text-slate-400 "
    "focus:border-emerald-500 focus:outline-none focus:ring-2 focus:ring-emerald-500/20"
)


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ("title", "amount", "category", "date")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": _field,
                    "placeholder": "e.g. Groceries",
                    "autocomplete": "off",
                }
            ),
            "amount": forms.NumberInput(
                attrs={
                    "class": _field,
                    "placeholder": "0.00",
                    "step": "0.01",
                    "min": "0",
                }
            ),
            "category": forms.Select(
                attrs={"class": f"{_field} cursor-pointer bg-white"}
            ),
            "date": forms.DateInput(
                attrs={
                    "class": _field,
                    "type": "date",
                }
            ),
        }


class StyledAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, forms.PasswordInput):
                widget.attrs.setdefault("class", _field)
                widget.attrs.setdefault("autocomplete", "current-password")
            else:
                widget.attrs.setdefault("class", _field)
                widget.attrs.setdefault("autocomplete", "username")


class StyledUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", _field)
            if isinstance(field.widget, forms.PasswordInput):
                field.widget.attrs.setdefault("autocomplete", "new-password")
