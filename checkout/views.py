from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings 

from .forms import OrderForm
from .models import Order, OrderLineItem
from tour_products.models import TourProducts
from bag.contexts import travelbag_contents

import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    if request.method == 'POST':
        bag =  request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    tour = TourProducts.objects.get(id=item_id)
                
                    order_line_item = OrderLineItem(
                        order=order,
                        tour=tour,
                        quantity=item_data if isinstance(item_data, int) else item_data['quantity'],
                    )
                    order_line_item.save()

                except TourProducts.DoesNotExist:
                    messages.error(request, (
                        "One of the tours in your bag wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()  
                    return redirect(reverse('view_bag'))

            request.session['save_info'] =  "save-info" in request.POST
            return redirect(reverse("checkout_success", args=[order.order_number]))
        else: 
            messages.error(request,'There is an error with your form. \
                Please double check your information')
    else:
        bag =  request.session.get('bag', {})
        if not bag: 
            messages.error(request, "Your Backpack has nothing in")
            return redirect(reverse('tour_products'))
        current_backpack = travelbag_contents(request)
        total = current_backpack['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warnings(request, 'Stripe public key is missing. \
            Did yoy forget to set it?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful secure checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
