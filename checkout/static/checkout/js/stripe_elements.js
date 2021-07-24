/*
    core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here:
    https://stripe.com/docs/stripe-js
*/

// Pulling the the stripe public key and client secret key
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
// Variable created using stripe public key
var stripe = Stripe(stripePublicKey);
// Instance of Stripe element
var elements = stripe.elements();
// Styling based around the instance
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
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
    // If any errors, it will be displayed in the card errors div
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
    // Prevent default form action which is to post
    ev.preventDefault();
    // Disabling the card element and submitted button to prevent multiple submissions
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    // To activate the fade out of the form when the checkout button is activated
    $('#payment-form').fadeToggle(100);
    $('#overlay-processing').fadeToggle(100);

    // Checking if the save info box was  
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} that Django generates in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // Object created to past the view and to pass  the client secret for the payment intent
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        // Confirming the card payment method, providing the card to stripe and then execute the results
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                // Billing details for webhooks
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.address_line1.value),
                        line2: $.trim(form.address_line2.value),
                        city: $.trim(form.town_or_city.value),
                        state: $.trim(form.county_state.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            // Shipping details for webhooks
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.address_line1.value),
                    line2: $.trim(form.address_line2.value),
                    city: $.trim(form.town_or_city.value),
                    state: $.trim(form.county_state.value),
                    postal_code: $.trim(form.postcode.value),
                    country: $.trim(form.country.value),
                }
            },
        }).then(function (result) {
            // If there is an error, an error message would appear
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);

                // To activate the fade out of the form when the checkout button is activated
                $('#payment-form').fadeToggle(100);
                $('#overlay-processing').fadeToggle(100);

                // Renable to the card and submit button if there was an issue so it can be fixed
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                // If succeeded, we will submit the form. 
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // Just reload the page, the error will be in django messages
        location.reload();
    })
});