function scrollToSection(sectionId) {
  document.getElementById(sectionId).scrollIntoView({
    behavior: "smooth",
  });
}

document.getElementById("checkbox").addEventListener("change", function() {
  var contactBar = document.getElementById("contactBar");
  if (this.checked) {
    contactBar.style.right = "120"; // Desplazar la barra hacia la izquierda
  } else {
    contactBar.style.right = "-700px"; // Ocultar la barra hacia la derecha
  }
});
