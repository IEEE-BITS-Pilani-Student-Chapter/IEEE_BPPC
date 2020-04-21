$(window).scroll(()=>{
    $('nav').toggleClass('scrolled', $(this).scrollTop() > 660);
});

console.log("hello");