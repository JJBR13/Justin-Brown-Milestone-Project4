var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
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

// Handle realtime validation errors

cardNumber.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
            `;
            $(errorDiv).html(html);
    } else {
        errorDiv.textContent ='';
    }
});

// Handles stripe form submission 
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});