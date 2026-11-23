/* ==========================================================================
   AHLY MONZOUR BABAR — Portfolio JavaScript
   Animation philosophy: Emil Kowalski's design engineering principles
   - transform/opacity only (composite-layer, GPU-accelerated)
   - Strong ease-out curves for UI
   - Hover gated behind (hover: hover) in CSS; JS handles active states
   - Reduced motion respected via CSS @media query
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  /* ---------- HEADER SCROLL ---------- */
  const header = document.querySelector('.header');
  let lastScroll = 0;
  let ticking = false;

  const scrollHandler = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const scrollY = window.scrollY;
      header?.classList.toggle('scrolled', scrollY > 50);
      document.querySelector('.back-to-top')?.classList.toggle('visible', scrollY > 500);
      lastScroll = scrollY;
      ticking = false;
    });
  };
  window.addEventListener('scroll', scrollHandler, { passive: true });
  scrollHandler();

  /* ---------- MOBILE MENU ---------- */
  const menuToggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  const navOverlay = document.querySelector('.nav-overlay');

  const toggleMenu = () => {
    const isOpen = nav?.classList.toggle('open');
    menuToggle?.classList.toggle('active');
    navOverlay?.classList.toggle('visible');
    document.body.style.overflow = isOpen ? 'hidden' : '';
  };

  menuToggle?.addEventListener('click', toggleMenu);
  navOverlay?.addEventListener('click', toggleMenu);

  // Close menu on nav link click
  document.querySelectorAll('.nav-link:not(.dropdown-toggle)').forEach(link => {
    link.addEventListener('click', () => {
      if (nav?.classList.contains('open')) toggleMenu();
    });
  });

  /* ---------- MOBILE DROPDOWN ---------- */
  document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
    toggle.addEventListener('click', (e) => {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        toggle.closest('.dropdown')?.classList.toggle('open');
      }
    });
  });

  /* ---------- SCROLL REVEAL ----------
     IntersectionObserver triggers .visible class.
     CSS handles the transition with transform + opacity (composite only).
     Threshold/rootMargin tuned for a natural "just entered viewport" feel.
  */
  const revealElements = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.08,
      rootMargin: '0px 0px -60px 0px'
    });
    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    // Fallback: show immediately
    revealElements.forEach(el => el.classList.add('visible'));
  }

  /* ---------- STAGGERED SERVICE CARDS ----------
     One entrance per container (choreograph rule #1).
     The section reveals as one, cards stagger within via CSS.
  */
  const svcCards = document.querySelectorAll('.svc-card');
  svcCards.forEach((card, i) => {
    card.classList.add('stagger-child');
  });

  /* ---------- STAGGERED PORTFOLIO CARDS ---------- */
  const portfolioCards = document.querySelectorAll('.project-showcase-card');
  portfolioCards.forEach((card, i) => {
    card.classList.add('stagger-child');
  });

  /* ---------- STAGGERED ARTICLE CARDS ---------- */
  const articleCards = document.querySelectorAll('.article-preview-card');
  articleCards.forEach((card, i) => {
    card.classList.add('stagger-child');
  });

  /* ---------- COUNT-UP ANIMATION ----------
     Uses requestAnimationFrame — writes to textContent only, no DOM thrash.
     Ease-out cubic for a satisfying deceleration.
  */
  const countUp = (el) => {
    const target = parseFloat(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const prefix = el.dataset.prefix || '';
    const duration = 2000;
    const isDecimal = target % 1 !== 0;
    const start = performance.now();

    const update = (now) => {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      // Ease out cubic — fast start, slow settle
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = target * eased;
      el.textContent = prefix + (isDecimal ? current.toFixed(1) : Math.floor(current)) + suffix;
      if (progress < 1) requestAnimationFrame(update);
    };
    requestAnimationFrame(update);
  };

  const statNumbers = document.querySelectorAll('.stat-number[data-count]');
  if (statNumbers.length && 'IntersectionObserver' in window) {
    const statObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          countUp(entry.target);
          statObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    statNumbers.forEach(el => statObserver.observe(el));
  }

  /* ---------- FAQ ACCORDION ----------
     Height transition handled in CSS (one of the few layout-property
     animations that's acceptable — no transform equivalent for height).
  */
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.faq-item');
      const wasActive = item.classList.contains('active');

      // Close all items in the same list
      item.closest('.faq-list')?.querySelectorAll('.faq-item').forEach(i => {
        i.classList.remove('active');
      });

      if (!wasActive) item.classList.add('active');
    });
  });

  /* ---------- CERTIFICATION FILTERS ---------- */
  document.querySelectorAll('.cert-filter').forEach(btn => {
    btn.addEventListener('click', () => {
      const category = btn.dataset.filter;
      const grid = btn.closest('.section')?.querySelector('.cert-grid');

      // Update active state
      btn.closest('.cert-filters')?.querySelectorAll('.cert-filter').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Filter cards with fade transition
      grid?.querySelectorAll('.cert-card').forEach(card => {
        if (category === 'all' || card.dataset.category === category) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });

  /* ---------- PORTFOLIO FILTERS ---------- */
  document.querySelectorAll('.portfolio-filter').forEach(btn => {
    btn.addEventListener('click', () => {
      const category = btn.dataset.filter;

      btn.closest('.portfolio-filters')?.querySelectorAll('.portfolio-filter').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      document.querySelectorAll('.portfolio-entry').forEach(entry => {
        if (category === 'all' || entry.dataset.category === category) {
          entry.style.display = '';
        } else {
          entry.style.display = 'none';
        }
      });
    });
  });

  /* ---------- CONTACT FORM VALIDATION ---------- */
  const form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      let valid = true;
      const statusEl = form.querySelector('.form-status');

      // Reset errors
      form.querySelectorAll('.form-group').forEach(g => g.classList.remove('has-error'));

      // Validate required fields
      form.querySelectorAll('[required]').forEach(input => {
        const group = input.closest('.form-group');
        if (!input.value.trim()) {
          group?.classList.add('has-error');
          valid = false;
        }
        // Email validation
        if (input.type === 'email' && input.value.trim()) {
          const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailRe.test(input.value.trim())) {
            group?.classList.add('has-error');
            valid = false;
          }
        }
      });

      if (!valid) return;

      const submitBtn = form.querySelector('button[type="submit"]');
      const originalHTML = submitBtn.innerHTML;
      submitBtn.innerHTML = '<span>SENDING...</span>';
      submitBtn.disabled = true;
      submitBtn.style.opacity = '0.7';

      try {
        const formData = new FormData(form);
        const response = await fetch(form.action, {
          method: 'POST',
          body: formData,
          headers: { 'Accept': 'application/json' }
        });

        if (response.ok) {
          statusEl.className = 'form-status success';
          statusEl.textContent = 'Thanks for reaching out! I\'ll get back to you within 24 hours.';
          statusEl.style.display = 'block';
          form.reset();
        } else {
          throw new Error('Form submission failed');
        }
      } catch (err) {
        statusEl.className = 'form-status error';
        statusEl.innerHTML = 'Something went wrong. Please email me directly at <a href="mailto:ahlybabar1188@gmail.com" style="color: var(--accent)">ahlybabar1188@gmail.com</a>';
        statusEl.style.display = 'block';
      }

      submitBtn.innerHTML = originalHTML;
      submitBtn.disabled = false;
      submitBtn.style.opacity = '';
    });
  }

  /* ---------- BACK TO TOP ---------- */
  document.querySelector('.back-to-top')?.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  /* ---------- ACTIVE NAV LINK ---------- */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
    // Check for service sub-pages
    if (currentPage.includes('services/') && href?.includes('services')) {
      link.classList.add('active');
    }
  });

  /* ---------- TESTIMONIAL CAROUSEL NAVIGATION ---------- */
  const carousel = document.getElementById('testimonialsCarousel');
  const prevBtn = document.querySelector('.t-arrow--prev');
  const nextBtn = document.querySelector('.t-arrow--next');

  if (carousel) {
    prevBtn?.addEventListener('click', () => {
      carousel.scrollBy({ left: -(carousel.clientWidth * 0.85), behavior: 'smooth' });
    });
    nextBtn?.addEventListener('click', () => {
      carousel.scrollBy({ left: carousel.clientWidth * 0.85, behavior: 'smooth' });
    });
  }

  /* ---------- MARQUEE DUPLICATE (for seamless loop) ---------- */
  document.querySelectorAll('.marquee-track').forEach(track => {
    const items = track.innerHTML;
    track.innerHTML = items + items;
  });

  /* ---------- SMOOTH ANCHOR SCROLLING ----------
     Offset for fixed header height.
  */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || targetId === '#main') return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const headerHeight = header?.offsetHeight || 80;
        const y = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    });
  });
});
