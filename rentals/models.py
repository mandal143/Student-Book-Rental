from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    page_count = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rented_at = models.DateField(blank=True, null=True)
    due_date = models.DateField(default=date.today() + timedelta(days=30))
    is_returned = models.BooleanField(default=False)

    def rental_fee(self):
        """Calculate the fee if the rental exceeds the free month."""
        if date.today() > self.due_date:
            overdue_days = (date.today() - self.due_date).days
            months_overdue = overdue_days // 30
            return (self.book.page_count // 100) * months_overdue
        return 0