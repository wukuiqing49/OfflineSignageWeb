document.documentElement.classList.add("js");

for (const link of document.querySelectorAll('a[href^="#"]')) {
  link.addEventListener("click", () => {
    const target = document.querySelector(link.getAttribute("href"));
    if (target) target.setAttribute("tabindex", "-1");
  });
}


// Lightweight Universal Lightbox
(function () {
  function initLightbox() {
    let modal = document.querySelector('.lightbox-modal');
    if (!modal) {
      modal = document.createElement('div');
      modal.className = 'lightbox-modal';
      modal.setAttribute('role', 'dialog');
      modal.setAttribute('aria-modal', 'true');
      modal.setAttribute('aria-label', 'Image Preview');
      modal.innerHTML = `
        <div class="lightbox-container">
          <button class="lightbox-close" aria-label="Close image preview">&times;</button>
          <img class="lightbox-image" src="" alt="">
          <p class="lightbox-caption"></p>
        </div>
      `;
      document.body.appendChild(modal);

      const close = () => modal.classList.remove('active');
      modal.querySelector('.lightbox-close').addEventListener('click', close);
      modal.addEventListener('click', (e) => {
        if (e.target === modal || e.target.classList.contains('lightbox-container')) close();
      });
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) close();
      });
    }

    const zoomableImages = document.querySelectorAll(
      '.screenshot-list figure img, .hero-media img, .article-hero-media img, .article-body img'
    );

    zoomableImages.forEach((img) => {
      img.addEventListener('click', () => {
        const modalImg = modal.querySelector('.lightbox-image');
        const modalCaption = modal.querySelector('.lightbox-caption');
        modalImg.src = img.currentSrc || img.src;
        modalImg.alt = img.alt || '';
        
        let captionText = '';
        const fig = img.closest('figure');
        if (fig) {
          const cap = fig.querySelector('figcaption');
          if (cap) captionText = cap.textContent.trim();
        }
        modalCaption.textContent = captionText;
        modalCaption.style.display = captionText ? 'block' : 'none';
        modal.classList.add('active');
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLightbox);
  } else {
    initLightbox();
  }
})();
