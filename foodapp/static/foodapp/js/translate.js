let currentLang = localStorage.getItem("lang") || "en";

function changeLanguage(lang) {
  localStorage.setItem("lang", lang);
  loadTranslations(lang);
}

async function loadTranslations(lang) {
  try {
    const res = await fetch(`/static/foodapp/js/translations.json`);
    const translations = await res.json();
    const dict = translations[lang];

    document.querySelectorAll("[data-translate]").forEach(el => {
      const key = el.getAttribute("data-translate");
      if (dict[key]) el.innerHTML = dict[key];
    });

    document.querySelectorAll("[data-translate-placeholder]").forEach(el => {
      const key = el.getAttribute("data-translate-placeholder");
      if (dict[key]) el.placeholder = dict[key];
    });
  } catch (err) {
    console.error("Translation load error:", err);
  }
}

document.addEventListener("DOMContentLoaded", () => loadTranslations(currentLang));
