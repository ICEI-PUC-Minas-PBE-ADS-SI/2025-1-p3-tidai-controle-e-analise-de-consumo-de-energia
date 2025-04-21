document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById("menu-icon");
    const navbar = document.querySelector(".navbar");

    // Menu Hamburguer
    menuIcon.addEventListener("click", function() {
        // Alternar classes
        navbar.classList.toggle("active");
        this.classList.toggle("fa-times");
        this.classList.toggle("fa-bars");
        
        // Bloquear scroll quando menu está aberto
        if (navbar.classList.contains("active")) {
            document.body.style.overflow = "hidden";
        } else {
            document.body.style.overflow = "auto";
        }
    });

    // Fechar menu ao clicar em um link
    document.querySelectorAll('.navbar a').forEach(link => {
        link.addEventListener('click', () => {
            navbar.classList.remove("active");
            menuIcon.classList.remove("fa-times");
            menuIcon.classList.add("fa-bars");
            document.body.style.overflow = "auto";
        });
    });

    // Fechar menu ao redimensionar a tela
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            navbar.classList.remove("active");
            menuIcon.classList.remove("fa-times");
            menuIcon.classList.add("fa-bars");
            document.body.style.overflow = "auto";
        }
    });
});