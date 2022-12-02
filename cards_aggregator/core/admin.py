from django.contrib import admin
from .models import Card, Transaction

# Register your models here.
class TransactionInlineAdmin(admin.StackedInline):
    model = Transaction
    extra = 1


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    model = Card
    readonly_fields = ('date_created',)
    inlines = (TransactionInlineAdmin, )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    # readonly_fields = ('card', 'value', 'date')