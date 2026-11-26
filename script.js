/* ═══════════════════════════════════════════════════════════════
   AHLY BABAR — Portfolio v2
   GSAP + ScrollTrigger · Parallax · 3D Tilt · Magnetic Cursor
   Performance-optimized · Reduced-motion aware
   ═══════════════════════════════════════════════════════════════ */

(() => {
  'use strict';

  // ── Helpers ──────────────────────────────────────────────
  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];
  const lerp = (a, b, t) => a + (b - a) * t;
  const clamp = (v, min, max) => Math.min(Math.max(v, min), max);
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ── Year ─────────────────────────────────────────────────
  const yearEl = $('#year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // ══════════════════════════════════════════════════════════
  //  1. CURSOR GLOW — follows mouse with smooth lerp
  // ══════════════════════════════════════════════════════════
  const cursorGlow = $('#cursorGlow');
  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let cursorX = mouseX;
  let cursorY = mouseY;

  if (cursorGlow && !prefersReducedMotion && window.innerWidth > 768) {
    document.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
    }, { passive: true });

    function animateCursor() {
      cursorX = lerp(cursorX, mouseX, 0.08);
      cursorY = lerp(cursorY, mouseY, 0.08);
      cursorGlow.style.transform = `translate(${cursorX - 250}px, ${cursorY - 250}px)`;
      requestAnimationFrame(animateCursor);
    }
    animateCursor();

    // Hide on mouse leave
    document.addEventListener('mouseleave', () => { cursorGlow.style.opacity = '0'; });
    document.addEventListener('mouseenter', () => { cursorGlow.style.opacity = '1'; });
  } else if (cursorGlow) {
    cursorGlow.style.display = 'none';
  }

  // ══════════════════════════════════════════════════════════
  //  2. PARTICLE CANVAS — floating gold specks
  // ══════════════════════════════════════════════════════════
  const canvas = $('#particleCanvas');

  if (canvas && !prefersReducedMotion && window.innerWidth > 640) {
    const ctx = canvas.getContext('2d');
    let particles = [];
    const PARTICLE_COUNT = 50;

    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas, { passive: true });

    class Particle {
      constructor() { this.reset(); }
      reset() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 1.5 + 0.3;
        this.speedX = (Math.random() - 0.5) * 0.3;
        this.speedY = (Math.random() - 0.5) * 0.15 - 0.1;
        this.opacity = Math.random() * 0.4 + 0.1;
        this.fadeSpeed = Math.random() * 0.003 + 0.001;
        this.fadingIn = true;
      }
      update() {
        this.x += this.speedX;
        this.y += this.speedY;

        if (this.fadingIn) {
          this.opacity += this.fadeSpeed;
          if (this.opacity >= 0.5) this.fadingIn = false;
        } else {
          this.opacity -= this.fadeSpeed;
          if (this.opacity <= 0) this.reset();
        }

        if (this.x < -10 || this.x > canvas.width + 10 || this.y < -10 || this.y > canvas.height + 10) {
          this.reset();
        }
      }
      draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(184, 134, 11, ${this.opacity})`;
        ctx.fill();
      }
    }

    for (let i = 0; i < PARTICLE_COUNT; i++) {
      particles.push(new Particle());
    }

    function animateParticles() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(p => { p.update(); p.draw(); });
      requestAnimationFrame(animateParticles);
    }
    animateParticles();
  } else if (canvas) {
    canvas.style.display = 'none';
  }

  // ══════════════════════════════════════════════════════════
  //  3. HEADER — scroll state & active link tracking
  // ══════════════════════════════════════════════════════════
  const header = $('#siteHeader');
  const navLinks = $$('.nav-link');
  const sectionIds = ['home', 'resume', 'projects', 'contact'];
  const sections = sectionIds.map(id => document.getElementById(id)).filter(Boolean);

  function setActiveLink(id) {
    navLinks.forEach(a =>
      a.classList.toggle('active', a.getAttribute('href') === `#${id}`)
    );
  }

  function onScroll() {
    // Header style
    if (header) {
      header.classList.toggle('scrolled', window.scrollY > 60);
    }

    // Active section
    const y = window.scrollY + 200;
    let current = sectionIds[0];
    for (const sec of sections) {
      if (sec.offsetTop <= y) current = sec.id;
    }
    setActiveLink(current);
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Smooth scroll for nav links
  navLinks.forEach(a => {
    a.addEventListener('click', (e) => {
      const href = a.getAttribute('href');
      if (!href || !href.startsWith('#')) return;
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      closeMobileNav();
    });
  });

  // ── Mobile nav ────────────────────────────────────────────
  const navToggle = $('#navToggle');
  const primaryNav = $('#primaryNav');

  function openMobileNav() {
    if (!primaryNav || !navToggle) return;
    primaryNav.classList.add('open');
    navToggle.setAttribute('aria-expanded', 'true');
  }
  function closeMobileNav() {
    if (!primaryNav || !navToggle) return;
    primaryNav.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
  }

  if (navToggle && primaryNav) {
    navToggle.addEventListener('click', () => {
      primaryNav.classList.contains('open') ? closeMobileNav() : openMobileNav();
    });
    document.addEventListener('click', (e) => {
      if (!primaryNav.contains(e.target) && !navToggle.contains(e.target)) closeMobileNav();
    });
  }

  // ══════════════════════════════════════════════════════════
  //  4. SCROLL PROGRESS BAR
  // ══════════════════════════════════════════════════════════
  const scrollProgress = $('#scrollProgress');
  function updateScrollProgress() {
    if (!scrollProgress) return;
    const doc = document.documentElement;
    const scrollTop = doc.scrollTop || document.body.scrollTop;
    const height = doc.scrollHeight - doc.clientHeight;
    const pct = height > 0 ? (scrollTop / height) * 100 : 0;
    scrollProgress.style.width = `${pct}%`;
  }
  window.addEventListener('scroll', updateScrollProgress, { passive: true });
  updateScrollProgress();

  // ══════════════════════════════════════════════════════════
  //  5. GSAP + SCROLLTRIGGER — Registration
  // ══════════════════════════════════════════════════════════
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
    console.warn('GSAP or ScrollTrigger not loaded. Falling back to Intersection Observer.');
    document.body.classList.add('no-gsap');
    initFallbackReveal();
  } else {
    gsap.registerPlugin(ScrollTrigger);
    if (!prefersReducedMotion) {
      initGSAPAnimations();
    } else {
      // Immediately show everything
      gsap.set('[data-reveal]', { opacity: 1, y: 0 });
      gsap.set('.title-word', { opacity: 1, y: 0 });
    }
  }

  // ══════════════════════════════════════════════════════════
  //  6. GSAP ANIMATIONS
  // ══════════════════════════════════════════════════════════
  function initGSAPAnimations() {

    // ── Hero entrance ─────────────────────────────────
    const heroTl = gsap.timeline({ delay: 0.3 });

    heroTl
      .from('#heroProfile', {
        opacity: 0,
        scale: 0.8,
        y: 60,
        duration: 1.2,
        ease: 'power3.out',
      })
      .from('.hero-label', {
        opacity: 0,
        x: -30,
        duration: 0.8,
        ease: 'power3.out',
      }, '-=0.7')
      .from('.title-word', {
        opacity: 0,
        y: 80,
        rotationX: -15,
        duration: 1,
        ease: 'power4.out',
        stagger: 0.15,
      }, '-=0.6')
      .from('.hero-text', {
        opacity: 0,
        y: 30,
        filter: 'blur(8px)',
        duration: 0.9,
        ease: 'power3.out',
      }, '-=0.5')
      .from('.cta-btn', {
        opacity: 0,
        y: 20,
        scale: 0.95,
        duration: 0.7,
        ease: 'power3.out',
        stagger: 0.1,
      }, '-=0.5')
      .from('.h-badge', {
        opacity: 0,
        y: 15,
        scale: 0.9,
        duration: 0.5,
        ease: 'power3.out',
        stagger: 0.06,
      }, '-=0.4')
      .from('.profile-status', {
        opacity: 0,
        y: 10,
        duration: 0.6,
        ease: 'power3.out',
      }, '-=0.3')
      .from('#scrollIndicator', {
        opacity: 0,
        y: -20,
        duration: 0.8,
        ease: 'power3.out',
      }, '-=0.2');

    // ── Parallax hero layers ──────────────────────────
    const layerDeep = $('.layer-deep');
    const layerMid = $('.layer-mid');
    const layerFront = $('.layer-front');

    if (layerDeep) {
      gsap.to(layerDeep, {
        y: 200,
        ease: 'none',
        scrollTrigger: {
          trigger: '.hero-section',
          start: 'top top',
          end: 'bottom top',
          scrub: 1.5,
        }
      });
    }

    if (layerMid) {
      gsap.to(layerMid, {
        y: 120,
        ease: 'none',
        scrollTrigger: {
          trigger: '.hero-section',
          start: 'top top',
          end: 'bottom top',
          scrub: 1,
        }
      });
    }

    if (layerFront) {
      gsap.to(layerFront, {
        y: 60,
        ease: 'none',
        scrollTrigger: {
          trigger: '.hero-section',
          start: 'top top',
          end: 'bottom top',
          scrub: 0.5,
        }
      });
    }

    // ── Hero content parallax ─────────────────────────
    gsap.to('#heroProfile', {
      y: -80,
      ease: 'none',
      scrollTrigger: {
        trigger: '.hero-section',
        start: 'top top',
        end: 'bottom top',
        scrub: 1.2,
      }
    });

    gsap.to('.hero-intro', {
      y: -50,
      ease: 'none',
      scrollTrigger: {
        trigger: '.hero-section',
        start: 'top top',
        end: 'bottom top',
        scrub: 1,
      }
    });

    // ── Scroll indicator fade ─────────────────────────
    gsap.to('#scrollIndicator', {
      opacity: 0,
      y: 20,
      scrollTrigger: {
        trigger: '.hero-section',
        start: '15% top',
        end: '30% top',
        scrub: true,
      }
    });

    // ── Section headers — clip-path wipe reveal ───────
    $$('.section-header').forEach(header => {
      const title = header.querySelector('.title-reveal');
      const number = header.querySelector('.section-number');
      const desc = header.querySelector('.section-desc');
      const line = header.querySelector('.section-line');

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: header,
          start: 'top 80%',
          end: 'top 50%',
          toggleActions: 'play none none none',
        }
      });

      if (number) {
        tl.fromTo(number,
          { opacity: 0, x: -20 },
          { opacity: 1, x: 0, duration: 0.6, ease: 'power3.out' }
        );
      }

      if (title) {
        tl.fromTo(title,
          { y: '100%', clipPath: 'inset(0 0 100% 0)' },
          { y: '0%', clipPath: 'inset(0 0 0% 0)', duration: 0.9, ease: 'power4.out' },
          '-=0.3'
        );
      }

      if (desc) {
        tl.fromTo(desc,
          { opacity: 0, y: 20, filter: 'blur(6px)' },
          { opacity: 1, y: 0, filter: 'blur(0px)', duration: 0.7, ease: 'power3.out' },
          '-=0.4'
        );
      }

      if (line) {
        tl.fromTo(line,
          { scaleX: 0, transformOrigin: 'left center' },
          { scaleX: 1, transformOrigin: 'left center', duration: 0.6, ease: 'power3.out' },
          '-=0.3'
        );
      }
    });

    // ── Data-reveal elements — staggered fade-in ──────
    $$('[data-reveal]').forEach((el, i) => {
      // Skip section headers (handled above)
      if (el.classList.contains('section-header') || el.closest('.section-header')) return;

      gsap.fromTo(el,
        { opacity: 0, y: 40 },
        {
          opacity: 1,
          y: 0,
          duration: 0.8,
          ease: 'power3.out',
          scrollTrigger: {
            trigger: el,
            start: 'top 88%',
            toggleActions: 'play none none none',
          }
        }
      );
    });

    // ── Skill bars — animate width on scroll ──────────
    $$('.skill-fill').forEach(fill => {
      const width = fill.getAttribute('data-width');
      if (!width) return;

      gsap.to(fill, {
        width: width + '%',
        duration: 1.2,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: fill,
          start: 'top 90%',
          toggleActions: 'play none none none',
        }
      });
    });

    // ── Project cards — staggered entrance ────────────
    const projectCards = $$('.project-card');
    if (projectCards.length) {
      gsap.fromTo(projectCards,
        { opacity: 0, y: 60, scale: 0.95 },
        {
          opacity: 1,
          y: 0,
          scale: 1,
          duration: 0.8,
          ease: 'power3.out',
          stagger: {
            each: 0.1,
            from: 'start',
          },
          scrollTrigger: {
            trigger: '.projects-grid',
            start: 'top 80%',
            toggleActions: 'play none none none',
          }
        }
      );
    }

    // ── Contact items — stagger ───────────────────────
    const contactItems = $$('.contact-info li');
    if (contactItems.length) {
      gsap.fromTo(contactItems,
        { opacity: 0, x: -30 },
        {
          opacity: 1,
          x: 0,
          duration: 0.7,
          ease: 'power3.out',
          stagger: 0.12,
          scrollTrigger: {
            trigger: '.contact-info',
            start: 'top 85%',
            toggleActions: 'play none none none',
          }
        }
      );
    }

    // ── Capability pills — pop in ─────────────────────
    const capPills = $$('.cap-pill');
    if (capPills.length) {
      gsap.fromTo(capPills,
        { opacity: 0, scale: 0.7, y: 15 },
        {
          opacity: 1,
          scale: 1,
          y: 0,
          duration: 0.5,
          ease: 'back.out(1.7)',
          stagger: 0.05,
          scrollTrigger: {
            trigger: '.capabilities-grid',
            start: 'top 85%',
            toggleActions: 'play none none none',
          }
        }
      );
    }

    // ── Timeline markers — pulse on enter ─────────────
    $$('.tl-marker').forEach(marker => {
      gsap.fromTo(marker,
        { scale: 0 },
        {
          scale: 1,
          duration: 0.4,
          ease: 'back.out(3)',
          scrollTrigger: {
            trigger: marker,
            start: 'top 90%',
            toggleActions: 'play none none none',
          }
        }
      );
    });

    // ── Cert list items — slide up with clip ──────────
    $$('.cert-list li').forEach((li, i) => {
      gsap.fromTo(li,
        { opacity: 0, y: 20, clipPath: 'inset(100% 0 0 0)' },
        {
        opacity: 1,
        y: 0,
        clipPath: 'inset(0% 0 0 0)',
        duration: 0.6,
        delay: i * 0.08,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: li,
          start: 'top 92%',
          toggleActions: 'play none none none',
        }
      });
    });
  }

  // ══════════════════════════════════════════════════════════
  //  7. FALLBACK — Intersection Observer (if GSAP fails)
  // ══════════════════════════════════════════════════════════
  function initFallbackReveal() {
    const revealEls = $$('[data-reveal]');
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    revealEls.forEach(el => io.observe(el));

    // Skill bars
    $$('.skill-fill').forEach(fill => {
      const width = fill.getAttribute('data-width');
      if (width) fill.style.width = width + '%';
    });
  }

  // ══════════════════════════════════════════════════════════
  //  8. 3D TILT — Project cards
  // ══════════════════════════════════════════════════════════
  if (!prefersReducedMotion && window.innerWidth > 768) {
    const tiltCards = $$('[data-tilt]');

    tiltCards.forEach(card => {
      const shimmer = card.querySelector('.card-shimmer');

      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = ((y - centerY) / centerY) * -8;
        const rotateY = ((x - centerX) / centerX) * 8;

        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;

        // Shimmer follow
        if (shimmer) {
          const percentX = (x / rect.width) * 100;
          const percentY = (y / rect.height) * 100;
          shimmer.style.setProperty('--mouse-x', percentX + '%');
          shimmer.style.setProperty('--mouse-y', percentY + '%');
        }
      });

      card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
        card.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
      });

      card.addEventListener('mouseenter', () => {
        card.style.transition = 'transform 0.1s ease-out';
      });
    });
  }

  // ══════════════════════════════════════════════════════════
  //  9. MAGNETIC BUTTON EFFECT
  // ══════════════════════════════════════════════════════════
  if (!prefersReducedMotion && window.innerWidth > 768) {
    const magneticBtns = $$('.magnetic-btn');

    magneticBtns.forEach(btn => {
      btn.addEventListener('mousemove', (e) => {
        const rect = btn.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;

        btn.style.transform = `translate(${x * 0.25}px, ${y * 0.25}px)`;
      });

      btn.addEventListener('mouseleave', () => {
        btn.style.transform = 'translate(0, 0)';
      });
    });
  }

  // ══════════════════════════════════════════════════════════
  //  10. PDF MODAL
  // ══════════════════════════════════════════════════════════
  const pdfModal = $('#pdfModal');
  const openPdfBtn = $('#openPdfBtn');
  const closePdfBtn = $('#closePdfBtn');

  function openModal() {
    if (!pdfModal) return;
    pdfModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    if (typeof gsap !== 'undefined') {
      gsap.fromTo(pdfModal.querySelector('.modal-panel'), {
        opacity: 0,
        scale: 0.9,
        y: 30,
      }, {
        opacity: 1,
        scale: 1,
        y: 0,
        duration: 0.4,
        ease: 'power3.out',
      });
    }
  }

  function closeModal() {
    if (!pdfModal) return;

    if (typeof gsap !== 'undefined') {
      gsap.to(pdfModal.querySelector('.modal-panel'), {
        opacity: 0,
        scale: 0.95,
        y: 20,
        duration: 0.25,
        ease: 'power2.in',
        onComplete: () => {
          pdfModal.setAttribute('aria-hidden', 'true');
          document.body.style.overflow = '';
        }
      });
    } else {
      pdfModal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
  }

  if (openPdfBtn) openPdfBtn.addEventListener('click', openModal);
  if (closePdfBtn) closePdfBtn.addEventListener('click', closeModal);

  if (pdfModal) {
    pdfModal.addEventListener('click', (e) => {
      if (e.target?.getAttribute?.('data-close-modal') === 'true') closeModal();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && pdfModal.getAttribute('aria-hidden') === 'false') closeModal();
    });
  }

  // ══════════════════════════════════════════════════════════
  //  11. SMOOTH SCROLL — CTA buttons in hero
  // ══════════════════════════════════════════════════════════
  $$('.cta-btn, .circle-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const href = btn.getAttribute('href');
      if (!href || !href.startsWith('#')) return;
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  // ══════════════════════════════════════════════════════════
  //  12. BADGE HOVER GLOW — subtle interactive feedback
  // ══════════════════════════════════════════════════════════
  $$('.h-badge, .cap-pill').forEach(badge => {
    badge.addEventListener('mouseenter', () => {
      if (typeof gsap !== 'undefined' && !prefersReducedMotion) {
        gsap.to(badge, {
          scale: 1.08,
          duration: 0.25,
          ease: 'power2.out',
        });
      }
    });
    badge.addEventListener('mouseleave', () => {
      if (typeof gsap !== 'undefined' && !prefersReducedMotion) {
        gsap.to(badge, {
          scale: 1,
          duration: 0.3,
          ease: 'power2.out',
        });
      }
    });
  });

  // ══════════════════════════════════════════════════════════
  //  13. ABSTRACT SHAPE DRIFT — parallax on mousemove
  // ══════════════════════════════════════════════════════════
  if (!prefersReducedMotion && window.innerWidth > 1024) {
    const shapes = $$('.abstract-shape');
    let shapeRAF;

    document.addEventListener('mousemove', (e) => {
      if (shapeRAF) cancelAnimationFrame(shapeRAF);
      shapeRAF = requestAnimationFrame(() => {
        const xFactor = (e.clientX / window.innerWidth - 0.5) * 2;
        const yFactor = (e.clientY / window.innerHeight - 0.5) * 2;

        shapes.forEach((shape, i) => {
          const speed = (i + 1) * 8;
          const x = xFactor * speed;
          const y = yFactor * speed;
          shape.style.transform = `translate(${x}px, ${y}px)`;
        });
      });
    }, { passive: true });
  }

  // ══════════════════════════════════════════════════════════
  //  14. PERFORMANCE — Intersection Observer for off-screen
  // ══════════════════════════════════════════════════════════
  // Pause particle canvas when not in viewport
  if (canvas && !prefersReducedMotion) {
    const canvasObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        canvas.style.opacity = entry.isIntersecting ? '0.6' : '0.2';
      });
    }, { threshold: 0 });
    canvasObserver.observe(document.querySelector('.hero-section') || document.body);
  }

})();
