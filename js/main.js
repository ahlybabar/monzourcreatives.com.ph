/* ==========================================================================
   MONZOUR CREATIVES — Portfolio JavaScript
   - Smooth native scroll (zero wheel-hijack bounce)
   - GSAP 3 + ScrollTrigger one-shot subtle section choreography
   - Lucide Icons hydration
   - PHP Mailer form submission with local fallback
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  /* ---------- 1. LUCIDE ICONS ---------- */
  if (typeof window.lucide !== 'undefined') {
    window.lucide.createIcons({
      attrs: { 'stroke-width': 2 }
    });
  }

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const header = document.querySelector('.header');
  const backToTop = document.querySelector('.back-to-top');
  const progressBar = document.querySelector('.scroll-progress-bar');

  /* ---------- 2. PASSIVE SCROLL PROGRESS & HEADER STATE ---------- */
  let ticking = false;
  const updateScrollUI = () => {
    ticking = false;
    const scrollY = window.scrollY;
    header?.classList.toggle('scrolled', scrollY > 40);
    backToTop?.classList.toggle('visible', scrollY > 450);

    if (progressBar) {
      const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
      const progress = maxScroll > 0 ? Math.max(0, Math.min(1, scrollY / maxScroll)) : 0;
      progressBar.style.transform = `scaleX(${progress})`;
    }
  };

  window.addEventListener(
    'scroll',
    () => {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(updateScrollUI);
      }
    },
    { passive: true }
  );
  updateScrollUI();

  /* ---------- 3. GSAP + SPLITTYPE KINETIC ANIMATIONS (Zero scroll bounce) ---------- */
  if (!prefersReducedMotion && typeof window.gsap !== 'undefined' && typeof window.ScrollTrigger !== 'undefined') {
    const gsap = window.gsap;
    const ScrollTrigger = window.ScrollTrigger;
    gsap.registerPlugin(ScrollTrigger);

    // SplitType masked word-by-word reveal on Hero Title
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle && typeof window.SplitType !== 'undefined') {
      const split = new window.SplitType(heroTitle, { types: 'words' });
      const masks = [];
      split.words?.forEach((word) => {
        const wrapper = document.createElement('span');
        wrapper.className = 'split-word-mask';
        word.parentNode?.insertBefore(wrapper, word);
        wrapper.appendChild(word);
        masks.push(wrapper);
      });
      gsap.from('.hero-title .word', {
        yPercent: 102,
        duration: 0.55,
        stagger: 0.045,
        ease: 'power3.out',
        clearProps: 'transform',
        onComplete: () => {
          masks.forEach((m) => {
            m.style.overflow = 'visible';
          });
        },
      });
    }

    // Hero supporting stagger (starts high-visibility for instant first paint)
    gsap.from('.hero-animate', {
      y: 12,
      opacity: 0.9,
      duration: 0.45,
      stagger: 0.05,
      ease: 'power3.out',
      clearProps: 'transform,opacity',
    });

    // Subtle one-time section lift on scroll (never stuck at opacity 0)
    gsap.utils.toArray('.reveal').forEach((section) => {
      const rect = section.getBoundingClientRect();
      if (rect.top < window.innerHeight * 0.95) return;

      gsap.from(section, {
        y: 14,
        opacity: 0.85,
        duration: 0.4,
        ease: 'power2.out',
        clearProps: 'transform,opacity',
        scrollTrigger: {
          trigger: section,
          start: 'top 96%',
          once: true,
        },
      });
    });

    // Staggered card entrance inside grids
    ['.services-cards-grid .svc-card', '.work-grid-3 .work-card', '.articles-grid .article-card'].forEach((selector) => {
      const cards = gsap.utils.toArray(selector);
      if (!cards.length) return;
      const firstRect = cards[0].getBoundingClientRect();
      if (firstRect.top < window.innerHeight * 0.95) return;

      gsap.from(cards, {
        y: 16,
        opacity: 0.85,
        duration: 0.45,
        stagger: 0.08,
        ease: 'power2.out',
        clearProps: 'transform,opacity',
        scrollTrigger: {
          trigger: cards[0],
          start: 'top 94%',
          once: true,
        },
      });
    });

    // Desktop-only subtle magnetic CTAs + 3D card micro-tilt (pointer fine only)
    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      document.querySelectorAll('.magnetic-btn, .hdr-pill-btn, .pill-btn--orange').forEach((btn) => {
        const xTo = gsap.quickTo(btn, 'x', { duration: 0.35, ease: 'power3.out' });
        const yTo = gsap.quickTo(btn, 'y', { duration: 0.35, ease: 'power3.out' });

        btn.addEventListener('mousemove', (e) => {
          const rect = btn.getBoundingClientRect();
          const dx = (e.clientX - rect.left - rect.width / 2) * 0.22;
          const dy = (e.clientY - rect.top - rect.height / 2) * 0.22;
          xTo(dx);
          yTo(dy);
        });

        btn.addEventListener('mouseleave', () => {
          xTo(0);
          yTo(0);
        });
      });
    }

    window.addEventListener('load', () => ScrollTrigger.refresh());
  }

  /* ---------- 3B. SERVICES DARK-CARD HOVER TAKEOVER ---------- */
  const servicesGrid = document.querySelector('.services-cards-grid');
  if (servicesGrid) {
    const svcCards = Array.from(servicesGrid.querySelectorAll('.svc-card'));
    const featuredCard = servicesGrid.querySelector('.svc-card--featured') || svcCards[0];
    const setActiveServiceCard = (targetCard) => {
      svcCards.forEach((c) => c.classList.toggle('is-active', c === targetCard));
    };

    if (featuredCard) {
      servicesGrid.setAttribute('data-hover-ready', 'true');
      setActiveServiceCard(featuredCard);

      svcCards.forEach((card) => {
        card.addEventListener('mouseenter', () => setActiveServiceCard(card));
        card.addEventListener('focusin', () => setActiveServiceCard(card));
      });

      servicesGrid.addEventListener('mouseleave', () => setActiveServiceCard(featuredCard));
    }
  }

  /* ---------- 4. MOBILE MENU ---------- */
  const menuToggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  const navOverlay = document.querySelector('.nav-overlay');

  const toggleMenu = (forceClose = false) => {
    const isOpen = forceClose ? false : !nav?.classList.contains('open');
    nav?.classList.toggle('open', isOpen);
    menuToggle?.classList.toggle('active', isOpen);
    menuToggle?.setAttribute('aria-expanded', String(Boolean(isOpen)));
    navOverlay?.classList.toggle('visible', Boolean(isOpen));
    document.body.style.overflow = isOpen ? 'hidden' : '';
  };

  menuToggle?.addEventListener('click', () => toggleMenu());
  navOverlay?.addEventListener('click', () => toggleMenu(true));

  document.querySelectorAll('.nav-link:not(.dropdown-toggle)').forEach((link) => {
    link.addEventListener('click', () => {
      if (nav?.classList.contains('open')) toggleMenu(true);
    });
  });

  /* ---------- 5. MOBILE DROPDOWN ---------- */
  document.querySelectorAll('.dropdown-toggle').forEach((toggle) => {
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      if (window.innerWidth <= 768) {
        const dropdown = toggle.closest('.dropdown');
        const isOpen = dropdown?.classList.toggle('open');
        toggle.setAttribute('aria-expanded', String(Boolean(isOpen)));
      }
    });
  });

  /* ---------- 6. COUNT-UP STATS ---------- */
  const countUp = (el) => {
    const target = parseFloat(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const prefix = el.dataset.prefix || '';
    const duration = 1200;
    const isDecimal = target % 1 !== 0;
    const start = performance.now();

    if (prefersReducedMotion) {
      el.textContent = prefix + (isDecimal ? target.toFixed(1) : target) + suffix;
      return;
    }

    const update = (now) => {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = target * eased;
      el.textContent = prefix + (isDecimal ? current.toFixed(1) : Math.floor(current)) + suffix;
      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        el.textContent = prefix + (isDecimal ? target.toFixed(1) : target) + suffix;
      }
    };
    requestAnimationFrame(update);
  };

  const statNumbers = document.querySelectorAll('[data-count]');
  if (statNumbers.length && 'IntersectionObserver' in window) {
    const statObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            countUp(entry.target);
            statObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.2 }
    );
    statNumbers.forEach((el) => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight) {
        countUp(el);
      } else {
        statObserver.observe(el);
      }
    });
  }

  /* ---------- 7. FAQ ACCORDION ---------- */
  document.querySelectorAll('.faq-question').forEach((btn) => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.faq-item');
      const wasActive = item.classList.contains('active');

      item.closest('.faq-list')?.querySelectorAll('.faq-item').forEach((i) => {
        i.classList.remove('active');
        i.querySelector('.faq-question')?.setAttribute('aria-expanded', 'false');
      });

      if (!wasActive) {
        item.classList.add('active');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ---------- 8. CERTIFICATION & PORTFOLIO FILTERS ---------- */
  document.querySelectorAll('.cert-filter').forEach((btn) => {
    btn.addEventListener('click', () => {
      const category = btn.dataset.filter;
      const grid = btn.closest('.section')?.querySelector('.cert-grid');
      btn.closest('.cert-filters')?.querySelectorAll('.cert-filter').forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');

      grid?.querySelectorAll('.cert-card').forEach((card) => {
        card.classList.toggle('hidden', !(category === 'all' || card.dataset.category === category));
      });
    });
  });

  document.querySelectorAll('.portfolio-filter').forEach((btn) => {
    btn.addEventListener('click', () => {
      const category = btn.dataset.filter;
      btn.closest('.portfolio-filters')?.querySelectorAll('.portfolio-filter').forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');

      document.querySelectorAll('.portfolio-entry').forEach((entry) => {
        const cats = (entry.dataset.category || '').split(' ');
        entry.style.display = category === 'all' || cats.includes(category) ? '' : 'none';
      });
    });
  });

  /* ---------- 9. COPY EMAIL ---------- */
  document.querySelectorAll('.copy-email-btn').forEach((btn) => {
    btn.addEventListener('click', async () => {
      const email = btn.dataset.email || 'monzourcreatives@gmail.com';
      try {
        await navigator.clipboard.writeText(email);
        const labelEl = btn.querySelector('.copy-label');
        if (labelEl) {
          const original = labelEl.textContent;
          labelEl.textContent = 'Copied';
          setTimeout(() => {
            labelEl.textContent = original;
          }, 1800);
        }
      } catch (_) {
        window.location.href = `mailto:${email}`;
      }
    });
  });

  /* ---------- 10. CONTACT FORM (PHP MAILER + SAFE FALLBACK) ---------- */
  const form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      let valid = true;
      const statusEl = form.querySelector('.form-status');
      form.querySelectorAll('.form-group').forEach((g) => g.classList.remove('has-error'));

      form.querySelectorAll('[required]').forEach((input) => {
        const group = input.closest('.form-group');
        if (!input.value.trim()) {
          group?.classList.add('has-error');
          valid = false;
        }
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
      submitBtn.style.opacity = '0.75';

      const firstName = form.querySelector('#cf-first-name')?.value.trim() || '';
      const lastName = form.querySelector('#cf-last-name')?.value.trim() || '';
      const email = form.querySelector('#cf-email')?.value.trim() || '';
      const business = form.querySelector('#cf-business')?.value.trim() || 'Not provided';
      const phone = form.querySelector('#cf-phone')?.value.trim() || 'Not provided';
      const service = form.querySelector('#cf-service')?.value || 'General Inquiry';
      const message = form.querySelector('#cf-message')?.value.trim() || '';

      const subject = encodeURIComponent(`Project Inquiry: ${service} — ${firstName} ${lastName}`);
      const body = encodeURIComponent(
        `Name: ${firstName} ${lastName}\nEmail: ${email}\nBusiness: ${business}\nPhone: ${phone}\nService: ${service}\n\nMessage:\n${message}`
      );
      const mailtoHref = `mailto:monzourcreatives@gmail.com?subject=${subject}&body=${body}`;
      const linkStyle = 'color:#FF9E80;text-decoration:underline;font-weight:700;';

      const showSuccessModal = (msg) => {
        form.reset();
        statusEl.style.display = 'none';
        statusEl.textContent = '';

        if (typeof Swal !== 'undefined') {
          Swal.fire({
            icon: 'success',
            title: 'Message Sent!',
            html: msg || "Thanks for reaching out! I'll reply within 24 hours.",
            confirmButtonText: 'Got it',
            confirmButtonColor: '#D95B38',
            background: '#1A1D25',
            color: '#F7F6F2',
            iconColor: '#4ADE80',
            backdrop: 'rgba(13, 15, 20, 0.78)',
            customClass: {
              popup: 'mc-swal-popup',
              confirmButton: 'mc-swal-confirm',
            },
          });
        } else {
          statusEl.className = 'form-status success';
          statusEl.textContent = msg || "Message sent! I'll reply within 24 hours.";
          statusEl.style.display = 'block';
        }
      };

      const sendViaFormSubmit = async () => {
        const res = await fetch('https://formsubmit.co/ajax/f20b2f8fb00c1fcf8db507d5fef05310', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json',
          },
          body: JSON.stringify({
            name: `${firstName} ${lastName}`.trim(),
            email,
            business,
            phone,
            service,
            message,
            _subject: `New Portfolio Inquiry: ${service} — ${firstName} ${lastName}`,
            _replyto: email,
            _template: 'table',
            _captcha: 'false',
          }),
        });
        if (!res.ok) throw new Error('FormSubmit delivery failed');
        const result = await res.json().catch(() => ({}));
        if (result.success === 'false' || result.success === false) {
          throw new Error(result.message || 'FormSubmit delivery failed');
        }
        return result;
      };

      try {
        if (window.location.protocol === 'file:') {
          throw new Error('local-file-preview');
        }

        const isStaticHost =
          window.location.hostname.endsWith('github.io') ||
          window.location.hostname.endsWith('netlify.app') ||
          window.location.hostname.endsWith('vercel.app') ||
          window.location.hostname.endsWith('pages.dev');

        if (isStaticHost) {
          await sendViaFormSubmit();
          showSuccessModal("Message sent! I'll reply within 24 hours.");
        } else {
          const formData = new FormData(form);
          const response = await fetch(form.getAttribute('action') || 'send-mail.php', {
            method: 'POST',
            body: formData,
            headers: { Accept: 'application/json' },
          });

          const contentType = response.headers.get('content-type') || '';
          if (!contentType.includes('application/json')) {
            await sendViaFormSubmit();
            showSuccessModal("Message sent! I'll reply within 24 hours.");
          } else {
            const data = await response.json();
            if (response.ok && data.ok) {
              showSuccessModal(data.message);
            } else if (data.needs_smtp_key) {
              statusEl.className = 'form-status error';
              statusEl.innerHTML = `PHP Mailer needs a Gmail App Password in <code>mail-config.php</code>. <a href="${mailtoHref}" style="${linkStyle}">Send via email app (pre-filled)</a> or email <a href="mailto:monzourcreatives@gmail.com" style="${linkStyle}">monzourcreatives@gmail.com</a>.`;
              statusEl.style.display = 'block';
            } else {
              throw new Error(data.error || 'Submission failed');
            }
          }
        }
      } catch (err) {
        statusEl.className = 'form-status error';
        statusEl.innerHTML = `${err.message || 'Could not send message right now.'} <a href="${mailtoHref}" style="${linkStyle}">Send via email app instead</a>.`;
        statusEl.style.display = 'block';
      }

      submitBtn.innerHTML = originalHTML;
      submitBtn.disabled = false;
      submitBtn.style.opacity = '';
    });
  }

  /* ---------- 11. ANCHOR SCROLL & BACK TO TOP ---------- */
  backToTop?.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: prefersReducedMotion ? 'auto' : 'smooth' });
  });

  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (!targetId || targetId === '#' || targetId === '#main') return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const headerOffset = header?.offsetHeight || 72;
        const y = target.getBoundingClientRect().top + window.pageYOffset - headerOffset;
        window.scrollTo({ top: y, behavior: prefersReducedMotion ? 'auto' : 'smooth' });
      }
    });
  });

  /* ---------- 12. ACTIVE NAV LINK ---------- */
  const path = window.location.pathname;
  const currentPage = path.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach((link) => {
    const href = link.getAttribute('href');
    if (href === currentPage) link.classList.add('active');
    if (path.includes('/services/') && link.classList.contains('dropdown-toggle')) {
      link.classList.add('active');
    }
  });
});
