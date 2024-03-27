function scrollToSection(sectionId) {
  document.getElementById(sectionId).scrollIntoView({
    behavior: "smooth",
  });
}

document.getElementById("checkbox").addEventListener("change", function() {
  var contactBar = document.getElementById("contactBar");
  var overlay = document.getElementById("overlay");
  if (this.checked) {
    contactBar.style.right = "0"; // Desplazar la barra hacia la izquierda
    overlay.style.display = "block"; // Mostrar el fondo oscuro
  } else {
    contactBar.style.right = "-300px"; // Ocultar la barra hacia la derecha
    overlay.style.display = "none"; // Ocultar el fondo oscuro
  }
});