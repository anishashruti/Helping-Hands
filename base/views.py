from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import stripe
import json
# Create your views here.

stripe.api_key ='sk_test_51Gz20rIPDW7FrALVrHaj6LC99kLu5B24hSaFVAwRx4M5nvCNAkeE3oishiarGh6Mho92k9P42kE7A7zlppAiMNRI00z8Klep0N'
# print(stripe.api_key)


def home(request):
	return render(request, 'base/home.html')
     
def donate(request):
	return render(request, 'base/donate.html')

def charge(request):
	if request.method == 'POST':
		d_amount = int(request.POST['amount'])
		email=request.POST['email']
		name=request.POST['name']
		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['name'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=d_amount*100,
			currency='inr',
			description="Donation",
			)
		our_customer=charge.get("customer")

		# invoice_create_item =stripe.InvoiceItem.create(
  		# customer=our_customer,
		# amount=d_amount*100,
		# currency='inr'
		# )

		# invoice = stripe.Invoice.create(
		# customer=our_customer,
		# collection_method='charge_automatically',
		# description="Donation for Helping Hands",
		# )
		payment_intent=stripe.PaymentIntent.create(
			amount=d_amount*100,
			currency='inr',
			payment_method_types=['card'],
			receipt_email=email,
			)
		# print(payment_intent)
	return redirect(reverse('base:thanks', args=[d_amount]))

def thanks(request,args):
	amount = args
	return render(request, 'base/done.html', {'amount':amount})