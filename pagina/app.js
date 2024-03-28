function scrollToSection(sectionId) {
  document.getElementById(sectionId).scrollIntoView({
    behavior: "smooth",
  });
}

function toggleContactMenu() {
  var menu = document.getElementById("contact-menu");
  if (menu.style.display === "none") {
    menu.style.display = "block";
  } else {
    menu.style.display = "none";
  }
}

document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("formularioCompra")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      alert(
        "¡Gracias por su interés en Innaxys! Nos pondremos en contacto con usted pronto."
      );
      this.reset();
    });
});

function redirectToBuyPage() {
  // Redirige al usuario a la página de compra
  window.location.href = "https://www.example.com/buy";
}
