// Menu hambúrguer
const menuIcon = document.getElementById("menu-icon");
const userIcon = document.getElementById("user-icon");
const navbar = document.querySelector("header nav");

menuIcon.addEventListener("click", () => {
  navbar.classList.toggle("active");
  menuIcon.classList.toggle("fa-times");  // Mudar ícone para "X" quando o menu for aberto
  
  // Alternar entre o ícone de hambúrguer e o de usuário
  if (navbar.classList.contains("active")) {
    menuIcon.style.display = 'none';  // Esconde o ícone de hambúrguer
    userIcon.style.display = 'none';  // Garante que o ícone de usuário não apareça
  } else {
    menuIcon.style.display = 'block';  // Exibe o ícone de hambúrguer
    userIcon.style.display = 'block';  // Exibe o ícone de usuário
  }
});

// Fechar menu ao clicar em um link
document.querySelectorAll('header nav a').forEach(link => {
  link.addEventListener('click', () => {
    navbar.classList.remove("active");
    menuIcon.classList.remove("fa-times");
    
    // Alternar novamente para os ícones
    menuIcon.style.display = 'block';
    userIcon.style.display = 'block';
  });
});
