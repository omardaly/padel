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
