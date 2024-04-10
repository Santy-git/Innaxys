function scrollToSection(sectionId) {
  document.getElementById(sectionId).scrollIntoView({
    behavior: "smooth",
  });
}

document.getElementById("checkbox").addEventListener("change", function () {
  var contactBar = document.getElementById("contactBar");
  if (this.checked) {
    contactBar.style.right = "120"; // Desplazar la barra hacia la izquierda
  } else {
    contactBar.style.right = "-100%"; // Ocultar la barra hacia la derecha
  }
});

document.getElementById("idiomas").addEventListener("change", function (e) {
  changeLanguage(e.target.value);
});

function changeLanguage(lang) {
  document.documentElement.lang = lang;
  const elements = document.querySelectorAll("[data-translate]");
  elements.forEach((element) => {
    const key = element.getAttribute("data-translate");
    element.textContent = translations[lang][key];
  });
  localStorage.setItem("language", lang);
  window.location.reload();
}

document.addEventListener("DOMContentLoaded", function () {
  const lang =
    localStorage.getItem("language") || navigator.language.startsWith("es")
      ? "es"
      : "en";
  changeLanguage(lang);
});
