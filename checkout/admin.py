from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    fk_name = 'order'
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'grand_total', 
                       'original_bag', 'stripe_pid')

    """ Enables ordering of fields not danjo default """
    fields = ('order_number', 'date', 'full_name', 'phone_number', 'country', 
              'postcode', 'town_or_city', 'street_address1', 'street_address2',
              'county', 'order_total', 'grand_total', 'original_bag', 'stripe_pid')
    
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'grand_total')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
