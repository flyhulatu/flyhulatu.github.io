// assets/js/extended/typewriter.js
document.addEventListener('DOMContentLoaded', function() {
  const text = "写作，使我精确！";
  const element = document.getElementById('typewriter-text'); // 假设你的 HTML 中有一个 id="typewriter-text" 的元素
  let index = 0;
  function type() {
    if (index < text.length) {
      element.innerHTML += text.charAt(index);
      index++;
      setTimeout(type, 100); // 打字速度
    }
  }
  type();
});