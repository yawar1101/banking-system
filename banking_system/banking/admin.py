from django.contrib import admin
from banking.models import Customer, Transaction

admin.site.register(Customer)
admin.site.register(Transaction)
