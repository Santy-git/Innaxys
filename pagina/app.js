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
      "Ofrecemos un completo sistema de gestión hotelera diseñado para optimizar cada aspecto de tu operación..",
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
      "Desde la reserva hasta el check-out, nuestro software ofrece una experiencia perfecta y personalizada que deja una impresión duradera en tus huespedes y fomenta la fidelidad a tu marca.",
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
    descubre: "subtitulo del logo",
    quienesSomos: "quienes somos",
    quienesSomosDesc: "descripcion del quienes somo",
    queOfrecemos: "que ofrecemos",
    queOfrecemosDesc1: "descripcion de que ofrecemos",
    queOfrecemosDesc2: "descripcion de que ofrecemos 2",
    beneficios: "beneficios",
    eficiencia: "eficiencia",
    eficienciaDesc: "descripcion eficiencia",
    rentabilidad: "rentabilidad",
    rentabilidadDesc: "descripcion de rentabilidad",
    persoFlexi: "flexibilidad y personalización",
    persoFlexiDesc: "descripcion de flexibilidad y perso",
    experiencia: "experiencia",
    experienciaDesc: "descripcion de experiencia",
    compatibilidad: "compatibilidad",
    compatibilidadDesc: "descripcion compatibilidad",
    compra: "comprar",
    solicitarInfo: "mas informacion",
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
