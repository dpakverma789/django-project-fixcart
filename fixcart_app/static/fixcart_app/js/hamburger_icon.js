document.addEventListener("DOMContentLoaded", function () {

    const toggle = document.querySelector(".menu-toggle");
    const navLinks = document.querySelector(".nav-links");

    toggle.addEventListener("click", function () {
        navLinks.classList.toggle("active");
    });

});