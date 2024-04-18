// Caché para los elementos traducidos
const translatedElementsCache = new Map();

// todas las traducciones
const translations = {
  es: {
    descubre: "Descubre el poder de la innovación con Innaxys en tu hotel",
    quienesSomos: "¿Quienes somos?",
    quienesSomosDesc:
      "En Innaxys, nos dedicamos a impulsar la excelencia en la gestión hotelera a través de soluciones tecnológicas innovadoras y personalizadas. Con años de experiencia en el sector, entendemos las necesidades únicas de cada hotel y nos comprometemos a ofrecer soluciones que impulsen el éxito y la eficiencia.",
    queOfrecemos: "¿Qué ofrecemos?",
    queOfrecemosDesc1:
      "Ofrecemos un completo sistema de gestión hotelera diseñado para optimizar cada aspecto de tu hotel",
    queOfrecemosDesc2:
      "Desde la reserva de habitaciones hasta la administración de inventarios y la gestión de personal, nuestro software está diseñado para simplificar tus procesos y potenciar tu negocio.",
    beneficios: "Beneficios",
    eficiencia: "Eficiencia",
    eficienciaDesc:
      "Nuestro software automatiza procesos tediosos y optimiza operaciones complejas, permitiéndote centrarte en lo que más importa: brindar una experiencia excepcional a tus huespedes.",
    rentabilidad: "Rentabilidad",
    rentabilidadDesc:
      "Con herramientas avanzadas de análisis y optimización de ingresos, puedes tomar decisiones informadas que maximicen tus ingresos y mejoren tu competitividad en el mercado.",
    persoFlexi: "Personalización y flexibilidad",
    persoFlexiDesc:
      "No importa el tamaño o el tipo de tu hotel, nuestro sistema se adapta a tus necesidades específicas y evoluciona contigo a medida que creces y te expandes.",
    experiencia: "Experiencia con el huésped",
    experienciaDesc:
      "Desde la reserva hasta el check-out, nuestro software ofrece una experiencia perfecta y personalizada que deja una impresión duradera en tus huespedes",
    compatibilidad: "Compatibilidad",
    compatibilidadDesc:
      "Nuestro sistema es compatible con todos los dispositivos",
    compra: "Compra Innaxys",
    solicitarInfo: "Solicitar más información",
    nombre: "Nombre:",
    email: "Correo electrónico:",
    mensaje: "Mensaje:",
    enviar: "Enviar",
    copy: "Copyright © | 2024 Innaxys. Todos los derechos reservados. | Desarrollado por Innaxys",
  },
  en: {
    descubre: "Discover the innovation power with Innaxys in your hotel",
    quienesSomos: "About us",
    quienesSomosDesc:
      "At Innaxys, we dedicate ourselves to propelling excellence in hotel management with innovative and personalized technology solutions. With years of experience in the area, we understand the unique needs of each hotel and commit to offer solutions that propel success and efficiency.",
    queOfrecemos: "Services",
    queOfrecemosDesc1:
      "We offer a complete hotel management system, designed to optimize each aspect of your hotel.",
    queOfrecemosDesc2:
      "From the room reservation until the inventories administration and the personal management as well, our software is designed to simplify your processes and boost your bussines.",
    beneficios: "Benefits",
    eficiencia: "Eficiency",
    eficienciaDesc:
      "Our software automate tedius processes and optimize complex operations, allowing you to focus on the most important issues offer an exceptional experience to your guests",
    rentabilidad: "Rentability",
    rentabilidadDesc:
      "With advanced tools of analysis and income of optimization, you can make informed decisions that maximize your income and improve your competitiveness in the market.",
    persoFlexi: "Customization and flexibility",
    persoFlexiDesc:
      "It doesn't matter the size or the type of your hotel, our system adapts to your specific needs and evolves with you as you grow and expand.",
    experiencia: "Experience with guest",
    experienciaDesc:
      "From reservation to check-out, our software offers a perfect and personalized experience, leaving a lasting impression on your guests",
    compatibilidad: "Compatibility",
    compatibilidadDesc: "Our system is compatible with all devices",
    compra: "Buy Innaxys",
    solicitarInfo: "For more informartion",
    nombre: "Name:",
    email: "Email:",
    mensaje: "Message:",
    enviar: "Send",
    copy: "Copyright © | 2024 Innaxys. All rights reserved. | Powered by Innaxys",
  },
};

function scrollToSection(sectionId) {
  document.getElementById(sectionId).scrollIntoView({
    behavior: "smooth",
  });
}

document.getElementById("checkbox").addEventListener("change", function () {
  var contactBar = document.getElementById("contactBar");
  if (this.checked) {
    console.log("Holaaaaa");
    contactBar.style.right = "5rem"; // Desplazar la barra hacia la izquierda
  } else {
    contactBar.style.right = "-100%"; // Ocultar la barra hacia la derecha
  }
});

function changeLanguage(lang) {
  console.log(`Changing language to: ${lang}`);
  document.documentElement.lang = lang;
  const elements = document.querySelectorAll("[data-translate]");
  elements.forEach((element) => {
    const key = element.getAttribute("data-translate");
    let translatedText = translations[lang] && translations[lang][key];

    if (translatedText) {
      element.textContent = translatedText;
    } else {
      console.error(
        `Translation for key '${key}' not found in language '${lang}'`
      );
    }
  });
  localStorage.setItem("language", lang);
}

document.getElementById("idiomas").addEventListener("change", function (e) {
  changeLanguage(e.target.value);
});

document.addEventListener("DOMContentLoaded", function () {
  const lang =
    localStorage.getItem("language") || navigator.language.startsWith("es")
      ? "es"
      : "en";
  changeLanguage(lang);
});
