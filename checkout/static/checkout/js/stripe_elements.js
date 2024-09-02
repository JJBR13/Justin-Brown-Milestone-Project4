var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();


// Create separate elements for card number, expiry, and CVC
var style = {
    base: {
        color: '#005792',
        fontFamily: '"Fredoka One", cursive',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        backgroundColor: '#FFE6EB',
        '::placeholder': {
            color: '#aab7c4'
        },
        iconColor: '#005792'
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
// Create separate elements for card number, expiry, and CVC
var cardNumber = elements.create('cardNumber', { style: style });
var cardExpiry = elements.create('cardExpiry', { style: style });
var cardCvc = elements.create('cardCvc', { style: style });

// Mount the elements to the respective divs
cardNumber.mount('#card-number-element');
cardExpiry.mount('#card-expiry-element');
cardCvc.mount('#card-cvc-element');