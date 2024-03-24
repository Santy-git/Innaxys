document.querySelectorAll(".benefits-list li").forEach(function (item) {
  item.addEventListener("click", function () {
    // cierra la descripción cuando se clickea otro
    document.querySelectorAll(".benefit-description").forEach(function (desc) {
      if (desc.style.display === "block") {
        desc.style.display = "none";
        desc.style.opacity = "0";
      }
    });

    // muestra la descripción cuando se clickea
    this.querySelector(".benefit-description").style.display = "block";
    this.querySelector(".benefit-description").style.opacity = "1";
  });
});
