from django.http import HttpResponse

class StripeWH_Handler: 
    '''Handle Strip webhooks'''

    def __init__(self,request):
        self.request = request

    def handle_event(self, event):
        ''' 
        Handle generic/unknown/unexpected webhook event
        '''
        return HttpResponse(
            content=f'Unhandled webhook recived: {event["type"]}', 
            status=200)

    def handle_payment_intent_succeeded(self, event):
        ''' 
        Handle the payment_intent.succeeded webhook Stripe
        '''

        return HttpResponse(
            content=f'Webhook recived: {event["type"]}', 
            status=200)
    
    def handle_payment_intent_payment_failed(self, event):
        ''' 
        Handle the payment_intent.payment_failed webhook Stripe
        '''
        return HttpResponse(
            content=f'Webhook recived: {event["type"]}', 
            status=200)
