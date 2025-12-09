const cards = document.querySelectorAll('.card');

function revealCards() {
  const trigger = window.innerHeight * 0.85;
  cards.forEach(card => {
    const rect = card.getBoundingClientRect();
    if (rect.top < trigger) {
      card.classList.add('visible');
    }
  });
}

window.addEventListener('scroll', revealCards);
revealCards();
document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("userBtn");
    const dropdown = document.getElementById("dropdown");

    btn.addEventListener("click", () => {
        dropdown.classList.toggle("show");
    });

    // Close when clicking outside
    document.addEventListener("click", (e) => {
        if (!btn.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.classList.remove("show");
        }
    });
});
