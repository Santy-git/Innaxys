// Caché para los elementos traducidos
const translatedElementsCache = new Map();

// todas las traducciones
const translations = {
  es: {
    descubre: "Descubre el poder de la innovación con Innaxys en tu hotel",
    quienesSomos: "¿Quienes somos?",
    quienesSomosDesc:
      "En Innaxys, nos dedicamos a impulsar la excelencia en la gestión de reservas a través de soluciones tecnológicas innovadoras y personalizadas. Con años de experiencia en el sector, entendemos las necesidades únicas de cada hotel y nos comprometemos a ofrecer soluciones que impulsen el éxito y la eficiencia.",
    queOfrecemos: "¿Qué ofrecemos?",
    queOfrecemosDesc1:
      "Ofrecemos un completo sistema de gestión de reservas, diseñado para optimizar cada aspecto de tu hotel",
    queOfrecemosDesc2:
      "Desde la reserva de habitaciones hasta la gestión de personal, nuestro software está diseñado para simplificar tus procesos y potenciar tu negocio.",
    beneficios: "Beneficios",
    eficiencia: "Eficiencia",
    eficienciaDesc:
      "Nuestro software automatiza procesos tediosos y optimiza operaciones complejas, permitiéndote centrarte en lo que más importa: brindar una experiencia excepcional a tus huespedes.",
    rentabilidad: "Rentabilidad",
    rentabilidadDesc:
      "Con herramientas avanzadas de análisis y optimización puedes maximizar tus ingresos y mejorar tu competitividad en el mercado.",
    persoFlexi: "Personalización y flexibilidad",
    persoFlexiDesc:
      "No importa el tamaño o el tipo de tu hotel, nuestro sistema se adapta a tus necesidades específicas y evoluciona contigo a medida que creces y te expandes.",
    experiencia: "Experiencia con el huésped",
    experienciaDesc:
      "Desde la reserva hasta el check-out, nuestro software ofrece una experiencia perfecta y personalizada que deja una impresión duradera en tus huespedes",
    compatibilidad: "Compatibilidad",
    compatibilidadDesc:
      "Nuestro sistema es compatible con todos los dispositivos",

    nombre1: "Jesus Moreto",
    comentario1: "Excelente programa, muy bueno y bien optimizado. Es de mucha utilidad en mi hotel y todos mis empleados están conformes con el sistema.",
    nombre2: "Mateo Silvestrin",
    comentario2: "He estado usando este software durante algún tiempo y estoy satisfecho con sus características y funcionalidades.",
    nombre3: "Luna Graneros",
    comentario3: "Buen programa, es increible lo intuitivo y facil de usar.",
    nombre4: "Abigail Lopez",
    comentario4: "El programa es fácil de usar y gracias a eso puedo realizar reservas, gestionar inventarios y generar informes.",

    contactanos: "Contactanos",
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
      "At Innaxys, we dedicate ourselves to propelling excellence in booking management with innovative and personalized technology solutions. With years of experience in the area, we understand the unique needs of each hotel and commit to offer solutions that propel success and efficiency.",
    queOfrecemos: "Services",
    queOfrecemosDesc1:
      "We offer a complete booking management system, designed to optimize each aspect of your hotel.",
    queOfrecemosDesc2:
      "From the room booking until the personal management, our software is designed to simplify your processes and boost your bussines.",
    beneficios: "Benefits",
    eficiencia: "Eficiency",
    eficienciaDesc:
      "Our software automate tedius processes and optimize complex operations, allowing you to focus on the most important issues offer an exceptional experience to your guests",
    rentabilidad: "Rentability",
    rentabilidadDesc:
      "With advanced tools of analysis and optimization you can maximize your income and improve your competitiveness in the market.",
    persoFlexi: "Customization and flexibility",
    persoFlexiDesc:
      "It doesn't matter the size or the type of your hotel, our system adapts to your specific needs and evolves with you as you grow and expand.",
    experiencia: "Experience with guest",
    experienciaDesc:
      "From booking to check-out, our software offers a perfect and personalized experience, leaving a lasting impression on your guests",
    compatibilidad: "Compatibility",
    compatibilidadDesc: "Our system is compatible with all devices",

    nombre1: "Jesus Moreto",
    comentario1: "Excellent program, very good and well optimized, it is very useful in my hotel and all my employees are conform with the system.",
    nombre2: "Mateo Silvestrin",
    comentario2: "I have been using this software for some time and am satisfied with its characteristics and functionalities.",
    nombre3: "Luna Graneros",
    comentario3: "Good program, it is incredible how intuitive and easy to use.",
    nombre4: "Abigail Lopez",
    comentario4: "The program is easy to use and thanks to it I can make reservations, manage inventories and generate reports.",

    contactanos: "Contact us",
    compra: "Buy Innaxys",
    solicitarInfo: "For more information",
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
    contactBar.style.display = "flex";
  } else {
    contactBar.style.display = "none";
  }
});

function changeLanguage(lang) {
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

// la flecha para volver al inicio
document.addEventListener("DOMContentLoaded", function () {
  const scrollTopBtn = document.getElementById("scrollTopBtn");

  // Función para mostrar el botón de flecha cuando el usuario se desplace hacia abajo
  function showScrollTopBtn() {
    if (window.pageYOffset > 200) {
      scrollTopBtn.style.display = "block";
    } else {
      scrollTopBtn.style.display = "none";
    }
  }

  // Función para hacer scroll hacia arriba al hacer clic en el botón de flecha
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }

  window.addEventListener("scroll", showScrollTopBtn);

  scrollTopBtn.addEventListener("click", scrollToTop);
});
