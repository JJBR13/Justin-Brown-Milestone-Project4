/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

*/

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
var cardNumber = elements.create('cardNumber', {
    style: style
});
var cardExpiry = elements.create('cardExpiry', {
    style: style
});
var cardCvc = elements.create('cardCvc', {
    style: style
});

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
        errorDiv.textContent = '';
    }
});

// Handles Stripe form submission
const form = document.getElementById('checkout-form');
const submitButton = document.getElementById('submit-button');

// Add the event listener to the form
form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    // Disable all elements
    cardNumber.update({
        'disabled': true
    });
    cardExpiry.update({
        'disabled': true
    });
    cardCvc.update({
        'disabled': true
    });
    submitButton.setAttribute('disabled', true);

    $('#checkout-form').fadeToggle(100);
    $('#loading-container').fadeIn(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    // Confirm card payment using the card number element
    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: cardNumber,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    postal_code: $.trim(form.postcode.value),
                    country: $.trim(form.country.value),
                }
            },
        }).then(function (result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>
                `;
                $(errorDiv).html(html);

                // Re-enable form elements after error
                $('#checkout-form').fadeToggle(100);
                $('#loading-container').fadeOut(100);
                cardNumber.update({
                    'disabled': false
                });
                cardExpiry.update({
                    'disabled': false
                });
                cardCvc.update({
                    'disabled': false
                });
                submitButton.removeAttribute('disabled');
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // reloads the page, with the error in django messages
        location.reload();
    })
});
