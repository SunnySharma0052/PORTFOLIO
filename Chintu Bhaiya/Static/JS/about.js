$("#top-button").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1000);

});
$(window).scroll(function () {
    if ($(window).scrollTop() == 0) {
        $('#top-button').hide();
    } else {
        $('#top-button').show();
    }
});


AOS.init();