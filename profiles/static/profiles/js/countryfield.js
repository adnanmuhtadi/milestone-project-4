// get the value of the country field as soon as the page laoads 
let countrySelected = $('#id_default_country').val();
// if the country selected is false, then the colour (grey) should be selected)
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
// capturing the event behind it.
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});