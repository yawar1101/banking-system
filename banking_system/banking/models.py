from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sender_transactions')
    receiver = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='receiver_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.sender} to {self.receiver}: {self.amount}'

