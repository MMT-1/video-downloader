const features = document.querySelectorAll(".ugb-feature-grid__item");
[...features].map((feature) => {
  const image = feature.querySelector("img").getAttribute("src");
  const title = feature.querySelector(".ugb-feature-grid__title").textContent;
  const description = feature.querySelector(
    ".ugb-feature-grid__description"
  ).textContent;
  return {
    image,
    title,
    description,
  };
});

const accordions = document.querySelectorAll(".ugb-accordion__item");
[...accordions].map((accordion) => {
  const question = accordion
    .querySelector(".ugb-accordion__heading")
    .textContent.trim();
  const answers = accordion
    .querySelector(".ugb-accordion__content")
    .textContent.trim();
  return {
    question,
    answers,
  };
});
