from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import os
import stripe
import json
# Create your views here.

stripe.api_key ='sk_test_51Gz20rIPDW7FrALVrHaj6LC99kLu5B24hSaFVAwRx4M5nvCNAkeE3oishiarGh6Mho92k9P42kE7A7zlppAiMNRI00z8Klep0N'
# os.environ.get('STRIPE_KEY')
print(stripe.api_key)

def home(request):
	return render(request, 'base/home.html')
     
def donate(request):
	return render(request, 'base/donate.html')

def charge(request):
	if request.method == 'POST':
		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['name'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='inr',
			description="Donation",
			address={
    'line1': '510 Townsend St',
    'postal_code': '98140',
    'city': 'San Francisco',
    'state': 'CA',
    'country': 'US',
  },
			)
	return redirect(reverse('base:thanks', args=[amount]))

def thanks(request, args):
	amount = args
	return render(request, 'base/done.html', {'amount':amount})