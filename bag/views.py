from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ Returns view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_backpack(request, item_id):
    """ Add tour to backpack """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # Get varible if already extists if not creates one
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # update quantity if exsists
        bag[item_id] += quantity
    else:
        # Add to bag
        bag[item_id] = quantity

    # Update/create bag on session 
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
