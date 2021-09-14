$(document).ready(function () {
    //This block of code is for the scroll to top button, which becomes visible when a user scrolls down.
    //I used this link https://codepen.io/matthewcain/pen/ZepbeR to help create and then modify the code to suite my needs.
    let backToTopBtn = $('#scroll-to-top-btn');
    $(window).scroll(function () {
        if ($(window).scrollTop() > 50) {
            backToTopBtn.addClass('visible');
        } else {
            backToTopBtn.removeClass('visible');
        }
    });

    //This block of code is for when a user clicks the button 
    //it will then take them back to the top of the page.
    backToTopBtn.on('click', function (event) {
        event.preventDefault();
        $('html, body').scrollTop(0);
    });

});