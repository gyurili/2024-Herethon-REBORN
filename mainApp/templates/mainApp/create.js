const form = document.querySelector(".fileUpload");
const btn = document.querySelector(".popup-button");

// 초기화 함수
const init = () => {
  form.addEventListener("submit", addfile);
  btn.addEventListener("click", displayForm);
};

// form 표시/숨기기 함수
const displayForm = () => {
  form.style.display === "none"
    ? (form.style.display = "flex")
    : (form.style.display = "none");
};

const addfile = () => {
  event.preventDefault();
};

// 시작 함수
init();
