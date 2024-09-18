// JavaScript to handle scroll event
window.onscroll = function() {
    var nav = document.querySelector('nav');
    if (window.pageYOffset > 100) { // Change background after scrolling 100px
        nav.classList.add('nav-scrolled');
    } else {
        nav.classList.remove('nav-scrolled');
    }
};