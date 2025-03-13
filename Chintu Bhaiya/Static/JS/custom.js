// Scroll Slide Bar

$(document).ready(function () {
  $('.customer-logos').slick({
    slidesToShow: 6,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1500,
    arrows: false,
    dots: false,
    pauseOnHover: false,
    responsive: [{
      breakpoint: 768,
      setting: {
        slidesToShow: 4
      }
    }, {
      breakpoint: 520,
      setting: {
        slidesToShow: 3
      }
    }]
  });
});




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