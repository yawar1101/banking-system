from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from banking.models import Customer, Transaction
from decimal import Decimal

def home(request):
    return render(request, 'banking/home.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'banking/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'banking/customer_detail.html', {'customer': customer})


@transaction.atomic
def transfer_money(request):
    customers = Customer.objects.all()

    if request.method == 'POST':
        sender_id = request.POST.get('sender')
        receiver_id = request.POST.get('recipient')
        amount = float(request.POST.get('amount'))

        sender = get_object_or_404(Customer, pk=sender_id)
        receiver = get_object_or_404(Customer, pk=receiver_id)


        with transaction.atomic():

            if amount <= Decimal('0') or sender.current_balance < amount:
                return render(request, 'banking/transfer.html', {'customers': customers, 'error': 'Invalid amount or insufficient balance'})

            sender.current_balance -= Decimal(amount)
            receiver.current_balance += Decimal(amount)

            sender.save()
            receiver.save()

            # Create a transfer record
            transfer = Transaction.objects.create(sender=sender, receiver=receiver, amount=amount)
            transfer.save()

        return redirect('transfer_success')
    


    return render(request, 'banking/transfer.html', {'customers': customers})


# def make_transfer(request, sender_pk, receiver_pk):
#     sender = Customer.objects.get(pk=sender_pk)
#     receiver = Customer.objects.get(pk=receiver_pk)
#     amount = float(request.POST['amount'])
#     if sender.current_balance >= amount:
#         sender.current_balance -= amount
#         receiver.current_balance += amount
#         sender.save()
#         receiver.save()
#         transaction = Transaction.objects.create(sender=sender, receiver=receiver, amount=amount)
#         transaction.save()
#         return render(request, 'banking/success.html')
#     else:
#         return render(request, 'banking/insufficient.html')

def transfer_success(request):
    return render(request, 'banking/transfer_success.html')
