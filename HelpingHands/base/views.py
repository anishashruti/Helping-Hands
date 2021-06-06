from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import os
import stripe
import json
# Create your views here.

stripe.api_key =os.environ.get('STRIPE_KEY')

def home(request):
	return render(request, 'base/home.html')
     
def donate(request):
	if request.method == 'POST':
                amount=0
	        print('Data:', request.POST)
	return redirect(reverse('success', args=[amount]))

def thanks(request, args):
	amount = args
	return render(request, 'base/done.html', {'amount':amount})