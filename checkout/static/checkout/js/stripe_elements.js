/*
    core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here:
    https://stripe.com/docs/stripe-js
*/

// pulling the the stripe public key and client secret key
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
// variable created using stripe public key
var stripe = Stripe(stripe_public_key);
// Instance of Stripe element
var elements = stripe.elements();
// 
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