from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings 

from .forms import OrderForm
from bag.contexts import travelbag_contents

import stripe

def checkout(request):
    bag =  request.session.get('bag', {})
    if not bag: 
        message.error(request, "Your Backpack has nothing in")
        return redirect(reverse('tour_products'))

    current_backpack = travelbag_contents(request)
    total = current_backpack['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ml7fSCjpDkomPFsE9pQFhDbnGMuu69Snz9775XVLC2G0leDgTBtKfv0zebk2OUuHgpEFOGP2tHOg8zsKqIGMKaj00fzUwuG7V',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
