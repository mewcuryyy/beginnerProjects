const navMenu = document.querySelector(".nav-menu");
const navToggle = document.querySelector(".nav-toggle");
const navClose = document.querySelector(".nav-close");

navToggle.addEventListener("click", () =>{
    navMenu.classList.add("show-menu");
});

navClose.addEventListener("click", () =>{
    navMenu.classList.remove("show-menu");
});

// Remove menu

const navLink = document.querySelectorAll(".nav-link");

function linkAction(){
    const navMenu = document.querySelector(".nav-menu");
    navMenu.classList.remove("show-menu");
};

navLink.forEach(n => n.addEventListener("click", linkAction));