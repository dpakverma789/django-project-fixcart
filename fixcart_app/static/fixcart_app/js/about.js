document.addEventListener("DOMContentLoaded", function () {

    const toggle = document.querySelector(".menu-toggle");
    const navLinks = document.querySelector(".nav-links");

    if (toggle) {
        toggle.addEventListener("click", function () {
            navLinks.classList.toggle("active");
        });
    }

});