from django.contrib import admin
from .models import Book, Rental
from django.contrib.auth.models import User
from datetime import timedelta, date

# Book Admin Interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'page_count']
    search_fields = ['title', 'isbn']
    
# Rental Admin Interface
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'rented_at', 'due_date', 'is_returned', 'rental_fee']
    search_fields = ['user__username', 'book__title']
    list_filter = ['is_returned']
    actions = ['prolong_rental']

     # Action to Prolong an Existing Rental
    def prolong_rental(self, request, queryset):
        """Extend the rental by a month and apply charges if applicable."""
        for rental in queryset:
            rental.due_date += timedelta(days=30)
            rental.save()
        self.message_user(request, f'{queryset.count()} rental(s) were extended by one month.')
    prolong_rental.short_description = 'Prolong selected rentals by one month'
    
# Inline Admin for Viewing All Rentals for a Student
class RentalInline(admin.TabularInline):
    model = Rental
    extra = 0
    fields = ('book', 'rented_at', 'due_date', 'rental_fee', 'is_returned')

# User Admin Interface to Show Rentals
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff']
    inlines = [RentalInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
