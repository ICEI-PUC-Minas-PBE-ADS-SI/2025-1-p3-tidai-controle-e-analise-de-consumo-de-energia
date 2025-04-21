// Menu hambúrguer
const menuIcon = document.getElementById("menu-icon");
const navbar = document.querySelector(".navbar");

menuIcon.addEventListener("click", () => {
  navbar.classList.toggle("active");
  menuIcon.classList.toggle("fa-times");
});

// Fechar menu ao clicar em um link
document.querySelectorAll('.navbar a').forEach(link => {
  link.addEventListener('click', () => {
    navbar.classList.remove("active");
    menuIcon.classList.remove("fa-times");
  });
});