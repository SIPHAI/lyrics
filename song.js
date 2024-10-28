const texts = document.querySelectorAll('.rotating-text-wrapper h2');
let currentIndex = 0;

document.addEventListener('keydown', function(event) {
  if (event.key === 'ArrowRight') {
    texts[currentIndex].classList.remove('active');
    
    // Move to the next index, or back to the first if at the end
    currentIndex = (currentIndex + 1) % texts.length;
    
    texts[currentIndex].classList.add('active');
  }
});

// Initialize the first text to be visible
texts[currentIndex].classList.add('active');

