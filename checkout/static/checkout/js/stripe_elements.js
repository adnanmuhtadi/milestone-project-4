/*
    core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here:
    https://stripe.com/docs/stripe-js
*/

// pulling the the stripe public key and client secret key
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
// variable created using stripe public key
var stripe = Stripe(stripePublicKey);
// Instance of Stripe element
var elements = stripe.elements();
// styling based around the instance
var style = {
    base: {
        color: '#000',
        fontFamily: '"", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
// Instance for the card element
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element 
// Everytime it changes, it will check for any errors
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    // if any errors, it will be displayed in the card errors div
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

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    // prevent default form action which is to post
    ev.preventDefault();
    // disabling the card element and submitted button to prevent multiple submissions
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    // confirming the card payment method, providing the card to stripe and then execute the results
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        // if there is an error, an error message would appear
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // renable to the card and submit button if there was an issue so it can be fixed
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            // if succeeded, we will submit the form. 
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});