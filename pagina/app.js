const benefitDescriptions = document.querySelectorAll(".benefit-description");

document.querySelectorAll(".benefits-list li").forEach((item) => {
  item.addEventListener("click", () => {
    // Oculta las descripcion
    benefitDescriptions.forEach((desc) => {
      desc.style.display = "none";
      desc.style.opacity = "0";
    });

    //Muestra la descripción
    const description = item.querySelector(".benefit-description");
    description.style.display = "block";
    description.style.opacity = "1";
  });
});

function scrollToSection(sectionId) {
  document.getElementById(sectionId).scrollIntoView({
    behavior: "smooth",
  });
}
