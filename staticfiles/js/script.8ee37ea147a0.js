// $(window).scroll(()=>{
//     $('nav').toggleClass('scrolled', $(this).scrollTop() > 660);
// });

// $(".navbar-toggler-icon").click(function() {
//     if($(window).width() <=530) {
//         $('nav').toggleClass(function() {
//             $(this).addClass("scrolled");
//         });
//     }
// });

$(document).ready(function() {
    toastr.options = {
        'closeButton': true,
        'debug': false,
        'newestOnTop': false,
        'progressBar': false,
        'positionClass': 'toast-bottom-right',
        'preventDuplicates': false,
        'showDuration': '1000',
        'hideDuration': '1000',
        'timeOut': '2000',
        'extendedTimeOut': '1000',
        'showEasing': 'swing',
        'hideEasing': 'linear',
        'showMethod': 'fadeIn',
        'hideMethod': 'fadeOut',
    }
});

$('.coming-soon').click(function(event) {
    toastr.info('Coming Soon!')
});