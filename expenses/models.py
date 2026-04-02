from django.conf import settings
from django.db import models


class Transaction(models.Model):
    class Category(models.TextChoices):
        FOOD = "Food", "Food"
        RENT = "Rent", "Rent"
        SALARY = "Salary", "Salary"
        ENTERTAINMENT = "Entertainment", "Entertainment"
        MISC = "Misc", "Misc"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=32,
        choices=Category.choices,
        default=Category.MISC,
    )
    date = models.DateField()

    class Meta:
        ordering = ["-date", "-pk"]

    def __str__(self) -> str:
        return self.title
