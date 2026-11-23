import os
import shutil

# Ensure directories exist
os.makedirs('images/clients', exist_ok=True)
os.makedirs('images/portfolio', exist_ok=True)
os.makedirs('services', exist_ok=True)
os.makedirs('css', exist_ok=True)
os.makedirs('js', exist_ok=True)

# Generate placeholder portrait SVG
portrait_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="400" height="500" viewBox="0 0 400 500" fill="none">
  <defs>
    <radialGradient id="glow" cx="50%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#B79CFF" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#131318" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect width="400" height="500" fill="url(#glow)" rx="20"/>
  <rect x="1" y="1" width="398" height="498" rx="19" stroke="#B79CFF" stroke-opacity="0.2"/>
  <circle cx="200" cy="180" r="75" fill="#1C1C26" stroke="#B79CFF" stroke-width="2" stroke-dasharray="6 6"/>
  <circle cx="200" cy="160" r="42" fill="#282838"/>
  <path d="M135 270 C135 215, 265 215, 265 270 Z" fill="#282838"/>
  <!-- Decorative badge -->
  <rect x="120" y="295" width="160" height="28" rx="14" fill="#B79CFF" fill-opacity="0.15" stroke="#B79CFF" stroke-width="1"/>
  <text x="200" y="313" text-anchor="middle" fill="#B79CFF" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="600" letter-spacing="0.05em">AHLY MONZOUR BABAR</text>
  <text x="200" y="360" text-anchor="middle" fill="#FFFFFF" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="600">Digital Marketing &amp; AI Automation</text>
  <text x="200" y="385" text-anchor="middle" fill="#A0A0B0" font-family="'Inter', sans-serif" font-size="13">Mintrix Virtual Assistants</text>
  <text x="200" y="440" text-anchor="middle" fill="#6B6B7B" font-family="'Inter', sans-serif" font-size="11">[Replace with your portrait photo: images/portrait.jpg]</text>
</svg>"""

with open('images/portrait.svg', 'w', encoding='utf-8') as f:
    f.write(portrait_svg)

# Generate Mintrix logo SVG
mintrix_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="180" height="40" viewBox="0 0 180 40" fill="none">
  <rect width="36" height="36" y="2" rx="8" fill="#B79CFF" fill-opacity="0.15" stroke="#B79CFF" stroke-width="1.5"/>
  <path d="M10 26 L14 14 L18 22 L22 14 L26 26" stroke="#B79CFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="46" y="24" fill="#FFFFFF" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" letter-spacing="0.05em">MINTRIX</text>
  <text x="46" y="34" fill="#A0A0B0" font-family="'Inter', sans-serif" font-size="8.5" font-weight="600" letter-spacing="0.12em">VIRTUAL ASSISTANTS</text>
</svg>"""

with open('images/clients/mintrix-logo.svg', 'w', encoding='utf-8') as f:
    f.write(mintrix_svg)

# Copy favicon if downloaded
if os.path.exists('images/clients/melbourne-wide-favicon.png'):
    shutil.copy('images/clients/melbourne-wide-favicon.png', 'images/favicon.png')

# HTML template helpers
def render_header(root="", active_page=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Ahly Monzour Babar — Digital Marketing Assistant &amp; AI Automation Specialist. Social media management, Meta Ads, SEO, n8n workflow automation, and front-end development.">
  <meta name="author" content="Ahly Monzour Babar">
  <meta name="keywords" content="digital marketing, AI automation, n8n, social media management, Meta Ads, SEO, Google Business Profile, front-end developer, virtual assistant, Philippines">

  <!-- Open Graph / Meta -->
  <meta property="og:title" content="Ahly Monzour Babar | Digital Marketing &amp; AI Automation Specialist">
  <meta property="og:description" content="I help businesses grow with strategic social media, 90-day content calendars, Meta Ads, SEO, and custom n8n AI automations.">
  <meta property="og:type" content="website">
  <!-- PLACEHOLDER: Replace og-image.jpg with your preview share image -->
  <meta property="og:image" content="{root}images/portrait.svg">

  <!-- Favicon -->
  <!-- PLACEHOLDER: Replace favicon.png with your custom brand favicon -->
  <link rel="icon" type="image/png" href="{root}images/favicon.png">

  <!-- Google Fonts: Space Grotesk (Headings) & Inter (Body) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">

  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="{root}css/styles.css">

  <title>Ahly Monzour Babar | Digital Marketing &amp; AI Automation Specialist</title>
</head>
<body>
  <!-- Accessibility Skip Link -->
  <a href="#main" class="skip-link">Skip to main content</a>
  <div class="nav-overlay" aria-hidden="true"></div>

  <!-- ==================== HEADER ==================== -->
  <header class="header" role="banner">
    <div class="container">
      <a href="{root}index.html" class="logo" aria-label="Ahly Monzour Babar Home">Ahly<span>.</span></a>
      <nav class="nav" role="navigation" aria-label="Main navigation">
        <a href="{root}index.html" class="nav-link{' active' if active_page=='home' else ''}">Home</a>
        <a href="{root}about.html" class="nav-link{' active' if active_page=='about' else ''}">About</a>
        <a href="{root}portfolio.html" class="nav-link{' active' if active_page=='portfolio' else ''}">Portfolio</a>
        <div class="dropdown">
          <a href="#" class="nav-link dropdown-toggle{' active' if active_page=='services' else ''}" aria-haspopup="true" aria-expanded="false">
            Services
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
          </a>
          <div class="dropdown-menu" role="menu">
            <a href="{root}services/social-media.html" class="dropdown-item" role="menuitem">Social Media Management &amp; Content Calendars</a>
            <a href="{root}services/meta-ads.html" class="dropdown-item" role="menuitem">Meta Ads Management</a>
            <a href="{root}services/seo.html" class="dropdown-item" role="menuitem">SEO &amp; Google Business Profile</a>
            <a href="{root}services/ai-automation.html" class="dropdown-item" role="menuitem">AI Workflow Automation (n8n)</a>
            <a href="{root}services/web-development.html" class="dropdown-item" role="menuitem">Website / Front-End Development</a>
          </div>
        </div>
        <a href="{root}contact.html" class="nav-link{' active' if active_page=='contact' else ''}">Contact</a>
        <a href="{root}articles.html" class="nav-link{' active' if active_page=='articles' else ''}">Articles</a>
      </nav>
      <a href="{root}contact.html" class="btn btn-primary header-cta">Get in touch</a>
      <button class="menu-toggle" aria-label="Toggle navigation menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
"""

def render_footer(root=""):
    return f"""
  <!-- ==================== TOOLS / PLATFORMS MARQUEE ==================== -->
  <section class="logo-strip" aria-label="Tools and platforms I work with">
    <p class="logo-strip-title">Tools &amp; Platforms I Work With</p>
    <div class="marquee">
      <div class="marquee-track">
        <span class="marquee-item">&#9881;&#65039; n8n (AI Automations)</span>
        <span class="marquee-item">&#128241; Meta Business Suite</span>
        <span class="marquee-item">&#128202; Meta Ads Manager</span>
        <span class="marquee-item">&#128200; Google Analytics</span>
        <span class="marquee-item">&#128205; Google Business Profile</span>
        <span class="marquee-item">&#128269; Semrush</span>
        <span class="marquee-item">&#129522; HubSpot</span>
        <span class="marquee-item">&#127912; Figma</span>
        <span class="marquee-item">&#128202; Tableau</span>
        <span class="marquee-item">&#128202; Power BI</span>
        <span class="marquee-item">&#9729;&#65039; Microsoft Azure</span>
        <span class="marquee-item">&#9883;&#65039; React Native</span>
        <span class="marquee-item">&#128295; Laravel</span>
        <span class="marquee-item">&#128187; HTML5 / CSS3 / JavaScript</span>
        <span class="marquee-item">&#128013; Python</span>
        <span class="marquee-item">&#128451;&#65039; MySQL / phpMyAdmin</span>
      </div>
    </div>
  </section>

  <!-- ==================== FOOTER ==================== -->
  <footer class="footer" role="contentinfo">
    <div class="container">
      <!-- Closing Call To Action Box -->
      <div class="footer-cta reveal">
        <h3>Ready to streamline your marketing &amp; save hours?</h3>
        <p>Let's talk about how I can help your business grow with strategic social media, ads, SEO, and custom n8n automations.</p>
        <a href="{root}contact.html" class="btn btn-primary">Get in touch &rarr;</a>
      </div>

      <div class="footer-grid">
        <div class="footer-about">
          <a href="{root}index.html" class="logo">Ahly<span>.</span></a>
          <p>Digital Marketing Assistant &amp; AI Automation Specialist based in Nasugbu, Batangas, Philippines. Dedicated to helping small businesses grow systematically through data-driven campaigns and automated workflows.</p>
          <div class="social-links">
            <a href="https://www.linkedin.com/in/ahly-monzour-babar-473a53365/" class="social-link" aria-label="LinkedIn Profile" target="_blank" rel="noopener">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            </a>
            <!-- PLACEHOLDER: Replace '#' with your actual Facebook or additional social profiles -->
            <a href="#" class="social-link" aria-label="Facebook Profile" target="_blank" rel="noopener">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
            </a>
            <a href="mailto:ahlybabar1188@gmail.com" class="social-link" aria-label="Email Ahly Babar">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Navigation</h4>
          <ul>
            <li><a href="{root}index.html">Home</a></li>
            <li><a href="{root}about.html">About</a></li>
            <li><a href="{root}portfolio.html">Portfolio</a></li>
            <li><a href="{root}contact.html">Contact</a></li>
            <li><a href="{root}articles.html">Articles</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="{root}services/social-media.html">Social Media &amp; Calendars</a></li>
            <li><a href="{root}services/meta-ads.html">Meta Ads Management</a></li>
            <li><a href="{root}services/seo.html">SEO &amp; Google Profile</a></li>
            <li><a href="{root}services/ai-automation.html">AI Automation (n8n)</a></li>
            <li><a href="{root}services/web-development.html">Web Development</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Direct Contact</h4>
          <ul>
            <li><a href="mailto:ahlybabar1188@gmail.com">ahlybabar1188@gmail.com</a></li>
            <li><a href="tel:+639476179440">+63 947 617 9440</a></li>
            <li>Nasugbu, Batangas, Philippines</li>
            <li>Timezone: PHT (UTC+8)</li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 Ahly Monzour H. Babar. All rights reserved.</p>
        <p>Built with clean HTML5, CSS3 &amp; Vanilla JavaScript &middot; <a href="{root}contact.html">Get in touch</a></p>
      </div>
    </div>
  </footer>

  <!-- Back to top button -->
  <button class="back-to-top" aria-label="Back to top">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>
  </button>

  <script src="{root}js/main.js"></script>
</body>
</html>
"""

# ==================== BUILD INDEX.HTML ====================
index_content = render_header(root="", active_page="home") + """
  <main id="main">
    <!-- 1. Hero Section -->
    <section class="hero" aria-label="Introduction">
      <div class="container">
        <div class="hero-content">
          <div class="hero-badge">&#128640; Available for new client partnerships</div>
          <h1>
            Digital Marketing Assistant
            <span class="highlight">&amp; AI Automation Specialist</span>
          </h1>
          <p class="hero-subheading">
            I help small businesses grow with strategic social media management, targeted paid ads, local SEO, and smart n8n automations &mdash; so you can focus on running your business.
          </p>
          <p class="hero-text">
            From building 90-day content calendars and running Meta Ads campaigns to designing AI-powered workflow automations, I take the guesswork out of digital marketing and replace it with consistent execution.
          </p>
          <div class="hero-buttons">
            <a href="contact.html" class="btn btn-primary">Get in touch &rarr;</a>
            <a href="portfolio.html" class="btn btn-outline">View recent work</a>
          </div>
        </div>

        <div class="hero-image">
          <div class="hero-image-wrapper">
            <!-- PLACEHOLDER: Replace images/portrait.svg with your real photo (e.g. images/portrait.jpg) -->
            <img src="images/portrait.svg" alt="Ahly Monzour Babar - Digital Marketing &amp; AI Automation Specialist" width="380" height="460" onerror="this.src='images/portrait.svg'">
          </div>
        </div>
      </div>
    </section>

    <!-- 2. Social-proof badge -->
    <section class="social-proof reveal" aria-label="Client social proof">
      <div class="container">
        <div class="proof-badge">
          <div class="proof-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <div class="proof-text">
            <strong>5.0 Google Rating (700+ Reviews)</strong><br>
            <small style="color:var(--text-muted)">Supporting social media &amp; digital marketing for Melbourne Wide Electrical &amp; Plumbing</small>
          </div>
        </div>
        <!-- PLACEHOLDER: Add your additional client ratings or review metrics here -->
      </div>
    </section>

    <!-- 3. Client logo strip -->
    <section class="logo-strip" aria-label="Clients and brands I support">
      <p class="logo-strip-title">Trusted By Businesses &amp; Organizations</p>
      <div class="marquee">
        <div class="marquee-track">
          <!-- Melbourne Wide Electrical & Plumbing -->
          <!-- NOTE: Used with client permission — CONFIRM before publishing -->
          <span class="marquee-item">
            <img src="images/clients/melbourne-wide-logo.svg" alt="Melbourne Wide Electrical &amp; Plumbing Logo" style="height:34px;width:auto;" onerror="this.style.display='none';this.nextElementSibling.style.display='inline'">
            <span style="display:none;font-weight:700;color:var(--text)">Melbourne Wide Electrical &amp; Plumbing</span>
          </span>

          <!-- Mintrix Virtual Assistants -->
          <span class="marquee-item">
            <img src="images/clients/mintrix-logo.svg" alt="Mintrix Virtual Assistants Logo" style="height:34px;width:auto;">
          </span>

          <!-- BatStateU ARASOF-Nasugbu (Deployed ExcelLens platform) -->
          <span class="marquee-item">
            <span style="font-weight:700;color:var(--text);border:1px solid var(--border);padding:0.4rem 0.9rem;border-radius:8px;font-size:0.9rem;">
              &#127891; Batangas State University (ARASOF-Nasugbu)
            </span>
          </span>

          <!-- PLACEHOLDER: Drop future client logos here -->
          <span class="marquee-item" style="opacity:0.45;border:1px dashed var(--border);padding:0.4rem 0.9rem;border-radius:8px;font-size:0.85rem;">
            + [ADD YOUR CLIENT LOGO]
          </span>
          <span class="marquee-item" style="opacity:0.45;border:1px dashed var(--border);padding:0.4rem 0.9rem;border-radius:8px;font-size:0.85rem;">
            + [ADD YOUR CLIENT LOGO]
          </span>
        </div>
      </div>
    </section>

    <!-- 4. The Problem: 8 pain points each with a quote -->
    <section class="section problem reveal" id="problem" aria-label="Common business pain points">
      <div class="container">
        <span class="section-label">The Problem</span>
        <h2 class="section-title">Sound familiar?</h2>
        <p class="section-subtitle">If you're a small business owner juggling daily operations, marketing often feels like an uphill struggle. Here are the 8 pain points I solve every week:</p>
        <div class="problem-grid">
          <div class="problem-card reveal">
            <div class="problem-card-icon">&#128241;</div>
            <h3>1. Inconsistent Posting</h3>
            <p>&ldquo;I know I should post on Instagram and Facebook, but I never have time and our profiles go dark for weeks.&rdquo;</p>
          </div>
          <div class="problem-card reveal">
            <div class="problem-card-icon">&#128197;</div>
            <h3>2. No Content Strategy</h3>
            <p>&ldquo;We just post random pictures when we remember. There's no 90-day plan and no clear campaign goal.&rdquo;</p>
          </div>
          <div class="problem-card reveal">
            <div class="problem-card-icon">&#128184;</div>
            <h3>3. Wasted Paid Ad Spend</h3>
            <p>&ldquo;I boosted a few posts in Meta Ads Manager, burned money, and have no idea if it generated real phone calls.&rdquo;</p>
          </div>
          <div class="problem-card reveal">
            <div class="problem-card-icon">&#128205;</div>
            <h3>4. Invisible in Local Search</h3>
            <p>&ldquo;When people in our suburb search for local services, our Google Business Profile is buried below competitors.&rdquo;</p>
          </div>
          <div class="problem-card reveal">
            <div class="problem-card-icon">&#128260;</div>
            <h3>5. Tedious Manual Tasks</h3>
            <p>&ldquo;I spend valuable hours every week manually copying leads, sending follow-ups, and building spreadsheets.&rdquo;</p>
          </div>
          <div class="problem-card reveal">
            <div class="problem-card-icon">&#128202;</div>
            <h3>6. Zero Analytics Visibility</h3>
            <p>&ldquo;I have Google Analytics installed but haven't logged in for months. We have no idea which channels bring ROI.&rdquo;</p>
          </div>
          <div class="problem-card reveal">
            <div class="problem-card-icon">&#129335;</div>
            <h3>7. Overwhelmed by Admin Work</h3>
            <p>&ldquo;I'm the technician, salesperson, manager, and marketer. There just aren't enough hours in the day.&rdquo;</p>
          </div>
          <div class="problem-card reveal">
            <div class="problem-card-icon">&#127760;</div>
            <h3>8. Outdated Web Experience</h3>
            <p>&ldquo;Our landing page is clunky on mobile devices and doesn't convert incoming traffic into customer inquiries.&rdquo;</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. The Solution -->
    <section class="section solution reveal" id="solution" aria-label="The complete marketing and automation solution">
      <div class="container">
        <span class="section-label">The Solution</span>
        <h2 class="section-title">A dedicated marketing partner<br>who actually <span class="text-accent">executes &amp; automates</span>.</h2>
        <div class="solution-grid">
          <div>
            <p class="section-subtitle" style="margin-bottom:2rem">
              I don't just hand you theoretical advice and walk away. Through Mintrix Virtual Assistants, I handle your daily digital marketing operations with structured 90-day roadmaps and AI-driven automations.
            </p>
            <div class="solution-features">
              <div class="solution-feature">
                <div class="check">&#10003;</div>
                <p><strong>Strategic 90-Day Content Calendars:</strong> Planned, designed, scheduled, and published across Meta Business Suite aligned with seasonal promotions and brand authority.</p>
              </div>
              <div class="solution-feature">
                <div class="check">&#10003;</div>
                <p><strong>Targeted Meta Ads Management:</strong> Audience targeting, creative testing, and weekly campaign monitoring to turn ad budget into measurable reach and conversions.</p>
              </div>
              <div class="solution-feature">
                <div class="check">&#10003;</div>
                <p><strong>SEO &amp; Google Business Profile:</strong> Local listing updates, regular Google posts, review monitoring, and on-page SEO best practices to dominate local search.</p>
              </div>
              <div class="solution-feature">
                <div class="check">&#10003;</div>
                <p><strong>n8n AI Workflow Automation:</strong> Custom node-based automations connecting forms, CRM, social channels, and APIs to remove manual data entry entirely.</p>
              </div>
              <div class="solution-feature">
                <div class="check">&#10003;</div>
                <p><strong>Clear Google Analytics Insights:</strong> Transparent bi-weekly reporting that shows exactly what's performing, without vanity metrics or confusing technical jargon.</p>
              </div>
              <div class="solution-feature">
                <div class="check">&#10003;</div>
                <p><strong>Front-End Web Enhancements:</strong> Responsive, fast HTML/CSS/JavaScript components that improve user experience and landing page conversion rates.</p>
              </div>
            </div>
            <div style="margin-top:2.5rem">
              <a href="contact.html" class="btn btn-primary">Start your tailored strategy &rarr;</a>
            </div>
          </div>

          <div>
            <!-- PLACEHOLDER: Client Testimonial 1 -->
            <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:2.25rem;margin-bottom:1.5rem">
              <div style="color:#FFD700;font-size:1.1rem;margin-bottom:0.75rem;">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
              <p style="font-size:1.05rem;font-style:italic;color:var(--text-secondary);line-height:1.7;margin-bottom:1.5rem">
                &ldquo;[ADD TESTIMONIAL &mdash; Insert real feedback from Melbourne Wide Electrical &amp; Plumbing or your current client regarding your social media management and weekly wrap-up carousels.]&rdquo;
              </p>
              <div style="display:flex;align-items:center;gap:0.85rem">
                <div style="width:44px;height:44px;border-radius:50%;background:var(--accent-tint);display:flex;align-items:center;justify-content:center;color:var(--accent);font-weight:700;font-family:var(--font-heading)">
                  MW
                </div>
                <div>
                  <strong style="font-size:0.95rem">[Client Representative Name]</strong>
                  <p style="font-size:0.82rem;color:var(--text-muted)">Melbourne Wide Electrical &amp; Plumbing</p>
                </div>
              </div>
            </div>

            <!-- PLACEHOLDER: Client Testimonial 2 -->
            <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:2.25rem">
              <div style="color:#FFD700;font-size:1.1rem;margin-bottom:0.75rem;">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
              <p style="font-size:1.05rem;font-style:italic;color:var(--text-secondary);line-height:1.7;margin-bottom:1.5rem">
                &ldquo;[ADD TESTIMONIAL &mdash; Insert feedback from Mintrix Virtual Assistants leadership or another business partner regarding workflow automation and execution.]&rdquo;
              </p>
              <div style="display:flex;align-items:center;gap:0.85rem">
                <div style="width:44px;height:44px;border-radius:50%;background:var(--accent-tint);display:flex;align-items:center;justify-content:center;color:var(--accent);font-weight:700;font-family:var(--font-heading)">
                  MV
                </div>
                <div>
                  <strong style="font-size:0.95rem">[Colleague or Client Name]</strong>
                  <p style="font-size:0.82rem;color:var(--text-muted)">Mintrix Virtual Assistants</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. Meet your consultant bio -->
    <section class="section consultant reveal" id="consultant" aria-label="Meet your digital marketing consultant">
      <div class="container">
        <span class="section-label">Meet Your Consultant</span>
        <h2 class="section-title">Hi, I&rsquo;m Ahly Babar.</h2>
        <div class="consultant-grid">
          <div class="consultant-image">
            <!-- PLACEHOLDER: Replace with your actual photo in images/portrait.svg -->
            <img src="images/portrait.svg" alt="Ahly Monzour H. Babar" style="width:100%;height:100%;object-fit:cover;">
          </div>
          <div class="consultant-bio">
            <h3>Bridging Developer Logic with Creative Marketing Execution</h3>
            <p>
              I am a digital marketing and AI automation specialist based in Nasugbu, Batangas, Philippines, currently working at <strong>Mintrix Virtual Assistants</strong>. I hold a Bachelor of Science in Information Technology from Batangas State University ARASOF-Nasugbu (graduating with a <strong>GWA of 1.9</strong>) and previously completed a Front-End Developer internship at <strong>CertiCode</strong> in Makati.
            </p>
            <p>
              What makes my approach distinct is technical discipline: I don't just schedule posts; I build reliable systems. Whether it is engineering node-based <strong>n8n AI automations</strong> that bridge disparate APIs, curating 90-day content calendars, or managing the digital footprint of trade companies with 700+ five-star reviews, I focus on precision and verifiable business impact.
            </p>
            <p>
              During my academic career, I led the front-end development of <strong>ExcelLens</strong>, a student performance analytics platform that was successfully deployed and remains in active production use across multiple university colleges.
            </p>

            <!-- Stats row with verified numbers from resume -->
            <div class="stats-row">
              <div class="stat-item">
                <span class="stat-number" data-count="1.9">0</span>
                <span class="stat-label">College GWA</span>
              </div>
              <div class="stat-item">
                <span class="stat-number" data-count="15" data-suffix="+">0</span>
                <span class="stat-label">Certifications</span>
              </div>
              <div class="stat-item">
                <span class="stat-number" data-count="90">0</span>
                <span class="stat-label">Day Content Plans</span>
              </div>
              <div class="stat-item">
                <span class="stat-number" data-count="1" data-suffix=" Platform">0</span>
                <span class="stat-label">ExcelLens in Production</span>
              </div>
            </div>

            <!-- Categories supported -->
            <p style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1.5rem">
              <strong>Core Industry Experience:</strong> Home Services &amp; Trades (Electrical, Plumbing, HVAC), Professional Virtual Assistance, EdTech &amp; Academic Systems.
            </p>

            <a href="about.html" class="btn btn-outline">Read my full background &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. Recent Projects cards -->
    <section class="section reveal" id="projects" aria-label="Recent client projects">
      <div class="container">
        <span class="section-label">Recent Projects</span>
        <h2 class="section-title">Proven execution in the field.</h2>
        <p class="section-subtitle">Real businesses, live platforms, and hands-on deliverables.</p>

        <div class="projects-grid">
          <!-- Melbourne Wide Featured Card -->
          <!-- NOTE: Used with client permission — CONFIRM before publishing -->
          <a href="portfolio.html#melbourne-wide" class="project-card reveal">
            <div class="project-card-image" style="background:#181822;display:flex;align-items:center;justify-content:center;padding:2rem;">
              <img src="images/clients/melbourne-wide-logo.svg" alt="Melbourne Wide Electrical &amp; Plumbing" style="max-height:60px;width:auto;">
            </div>
            <div class="project-card-body">
              <div class="project-tags">
                <span class="project-tag">Social Media Admin</span>
                <span class="project-tag">90-Day Content Plan</span>
                <span class="project-tag">Google Business Profile</span>
              </div>
              <h3>Melbourne Wide Electrical &amp; Plumbing</h3>
              <p>
                Managing ongoing social media operations for a top-tier trade company in Thomastown, VIC (rated 5.0 with 700+ Google reviews). Crafting weekly &ldquo;Another Week. Another Round of Jobs Done Right!&rdquo; carousels, 90-day schedules, and local SEO listings.
              </p>
              <span class="btn-ghost">View case study &rarr;</span>
            </div>
          </a>

          <!-- ExcelLens Featured Card -->
          <a href="portfolio.html#excellens" class="project-card reveal">
            <div class="project-card-image" style="background:#131B2A;display:flex;align-items:center;justify-content:center;padding:2rem;">
              <div style="text-align:center;">
                <div style="font-size:2.5rem;margin-bottom:0.5rem">&#128202;</div>
                <span style="font-family:var(--font-heading);font-weight:700;font-size:1.2rem;color:var(--text)">ExcelLens Analytics</span>
              </div>
            </div>
            <div class="project-card-body">
              <div class="project-tags">
                <span class="project-tag">Academic Analytics</span>
                <span class="project-tag">Front-End Lead</span>
                <span class="project-tag">Live Deployment</span>
              </div>
              <h3>ExcelLens &mdash; Student Performance &amp; Course Analytics</h3>
              <p>
                Led UI engineering for a full-scale academic analytics platform with dynamic grading calculators and one-click registrar report generation. Successfully deployed and actively used across multiple BatStateU ARASOF colleges.
              </p>
              <span class="btn-ghost">View system details &rarr;</span>
            </div>
          </a>

          <!-- CertiCode Internship Card -->
          <a href="portfolio.html#certicode" class="project-card reveal">
            <div class="project-card-image" style="background:#1A1824;display:flex;align-items:center;justify-content:center;padding:2rem;">
              <div style="text-align:center;">
                <div style="font-size:2.5rem;margin-bottom:0.5rem">&#128187;</div>
                <span style="font-family:var(--font-heading);font-weight:700;font-size:1.2rem;color:var(--text)">CertiCode Front-End</span>
              </div>
            </div>
            <div class="project-card-body">
              <div class="project-tags">
                <span class="project-tag">HTML5 / CSS3 / JS</span>
                <span class="project-tag">Git Version Control</span>
                <span class="project-tag">Agile Environment</span>
              </div>
              <h3>Front-End Developer Internship &mdash; CertiCode</h3>
              <p>
                Developed production web application interfaces in Makati, collaborating directly with senior developers to turn UI/UX feedback into pixel-perfect, cross-browser responsive web components.
              </p>
              <span class="btn-ghost">View details &rarr;</span>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- 8. Four guarantee / promise cards with icons (Commitments, not guaranteed results) -->
    <section class="section reveal" aria-label="How I work and professional commitments">
      <div class="container">
        <span class="section-label">How I Work</span>
        <h2 class="section-title">My 4 core commitments to you.</h2>
        <p class="section-subtitle">
          Ethical marketers don't make false promises about overnight fortunes. Instead, here are the non-negotiable operational commitments I bring to every engagement:
        </p>
        <div class="promise-grid">
          <div class="promise-card reveal">
            <div class="promise-card-icon">&#128221;</div>
            <h3>1. Complete Clarity &amp; Transparency</h3>
            <p>No hiding behind complicated technical buzzwords. You get plain-language updates, transparent timesheets, and honest performance assessments.</p>
          </div>
          <div class="promise-card reveal">
            <div class="promise-card-icon">&#9200;</div>
            <h3>2. Strict Deadline Adherence</h3>
            <p>90-day content calendars are submitted ahead of publication cycles. Campaigns go live when planned. Reports arrive exactly when scheduled.</p>
          </div>
          <div class="promise-card reveal">
            <div class="promise-card-icon">&#128202;</div>
            <h3>3. Data-Informed Action</h3>
            <p>Every ad budget tweak, keyword adjustment, and content angle is grounded in real Google Analytics and Meta Business Suite numbers.</p>
          </div>
          <div class="promise-card reveal">
            <div class="promise-card-icon">&#9881;&#65039;</div>
            <h3>4. Constant Optimization</h3>
            <p>I constantly audit manual bottlenecks, replacing repetitive busywork with clean n8n automations so your business gains efficiency over time.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 9. "It's not for everyone though..." Qualification List -->
    <section class="section qualification reveal" aria-label="Client qualification criteria">
      <div class="container">
        <span class="section-label">Expectation Setting</span>
        <h2 class="section-title">It&rsquo;s not for everyone though&hellip;</h2>
        <p class="section-subtitle">A successful working relationship requires mutual alignment. Here is who I work best with &mdash; and who I am not right for:</p>
        <div class="qual-columns">
          <div class="qual-list">
            <h3 class="text-accent">&#10003; We will achieve great things together if you:</h3>
            <ul>
              <li class="good"><span class="icon">&#10003;</span> Are a trade, local business, or service professional who wants consistent marketing without losing operational hours.</li>
              <li class="good"><span class="icon">&#10003;</span> Understand that sustained brand growth requires planned 90-day cycles rather than erratic, sporadic posts.</li>
              <li class="good"><span class="icon">&#10003;</span> Appreciate clear communication and are willing to provide initial brand inputs and job photos/assets.</li>
              <li class="good"><span class="icon">&#10003;</span> Are eager to implement AI and workflow automations to save repetitive admin time.</li>
              <li class="good"><span class="icon">&#10003;</span> View marketing as an ongoing investment backed by real metrics and continuous refinement.</li>
            </ul>
          </div>
          <div class="qual-list">
            <h3 style="color:#ff6b6b">&#10007; We are probably NOT a good match if you:</h3>
            <ul>
              <li class="bad"><span class="icon">&#10007;</span> Expect guaranteed viral fame or flood of customers within 48 hours of launch.</li>
              <li class="bad"><span class="icon">&#10007;</span> Expect to run paid Meta advertising campaigns with zero ad spend allocation.</li>
              <li class="bad"><span class="icon">&#10007;</span> Disappear for weeks without approving content calendars or critical campaign decisions.</li>
              <li class="bad"><span class="icon">&#10007;</span> Want an expensive 10-person corporate agency with multiple account managers.</li>
              <li class="bad"><span class="icon">&#10007;</span> Prefer manual, disorganized copy-pasting over structured digital workflows.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- 10. Closing CTA -->
    <section class="closing-cta reveal" aria-label="Closing call to action">
      <div class="container">
        <h2>Have a project in mind?<br><span class="text-accent">Let&rsquo;s talk.</span></h2>
        <p>Whether you need social media consistency, Meta Ads management, local SEO enhancement, or automated n8n workflows &mdash; I am ready to help.</p>
        <a href="contact.html" class="btn btn-primary">Schedule a consultation &rarr;</a>
      </div>
    </section>
  </main>
""" + render_footer(root="")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)
print("index.html created")

# ==================== BUILD ABOUT.HTML ====================
about_content = render_header(root="", active_page="about") + """
  <main id="main">
    <!-- Page Hero -->
    <section class="page-hero">
      <div class="container">
        <span class="section-label" style="justify-content:center">About Consultant</span>
        <h1>Developer Mindset.<br><span class="text-accent">Marketing Execution.</span></h1>
        <p class="subtitle">
          I am Ahly Monzour H. Babar &mdash; a Digital Marketing Assistant &amp; AI Automation Specialist based in Nasugbu, Batangas, Philippines.
        </p>
      </div>
    </section>

    <!-- Bio & Stats Section -->
    <section class="section">
      <div class="container">
        <div class="consultant-grid reveal">
          <div class="consultant-image">
            <img src="images/portrait.svg" alt="Ahly Monzour Babar" style="width:100%;height:100%;object-fit:cover;">
          </div>
          <div class="consultant-bio">
            <span class="section-label">My Story</span>
            <h2 style="font-family:var(--font-heading);font-size:1.85rem;margin-bottom:1rem">From Front-End Code to Marketing Strategy</h2>
            <p>
              My journey began in technical software development. While completing my Bachelor of Science in Information Technology at <strong>Batangas State University ARASOF-Nasugbu</strong> (graduating with a <strong>GWA of 1.9</strong>), I interned as a <strong>Front-End Developer at CertiCode</strong> in Makati. There, I built responsive UI components using HTML5, CSS3, JavaScript, and Git within an Agile environment.
            </p>
            <p>
              I quickly recognized that great technical products and small businesses often suffer from the same problem: <em>inconsistent marketing and fragmented manual operations</em>. I transitioned into digital marketing and automation, joining <strong>Mintrix Virtual Assistants</strong> in May 2026.
            </p>
            <p>
              Today, I manage social media presence, design 90-day content calendars, configure Meta Ads Manager campaigns, optimize Google Business Profiles for local search, and build sophisticated <strong>n8n workflow automations</strong> connecting APIs, CRMs, and messaging systems.
            </p>

            <div class="stats-row">
              <div class="stat-item">
                <span class="stat-number" data-count="1.9">0</span>
                <span class="stat-label">College GWA</span>
              </div>
              <div class="stat-item">
                <span class="stat-number" data-count="15" data-suffix="+">0</span>
                <span class="stat-label">Certifications</span>
              </div>
              <div class="stat-item">
                <span class="stat-number" data-count="90">0</span>
                <span class="stat-label">Day Content Plans</span>
              </div>
              <div class="stat-item">
                <span class="stat-number" data-count="1" data-suffix=" Platform">0</span>
                <span class="stat-label">ExcelLens in Production</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4-Step Process: Discovery -> Strategy -> Launch -> Optimisation -->
    <section class="section reveal" aria-label="My structured 4-step process">
      <div class="container">
        <span class="section-label">The Process</span>
        <h2 class="section-title">How we go from audit to automated growth.</h2>
        <p class="section-subtitle">A proven 4-stage operational framework that prevents wasted effort and keeps your brand moving forward:</p>
        <div class="process-steps">
          <div class="process-step reveal">
            <h3>1. Discovery &amp; Audit</h3>
            <p>We review your existing social media profiles, Google Business Profile presence, past advertising data, and manual friction points to establish clear baseline metrics.</p>
          </div>
          <div class="process-step reveal">
            <h3>2. Strategy &amp; 90-Day Calendar</h3>
            <p>I map out your 90-day content calendar, identify key promotional themes, draft audience targeting parameters in Meta Ads Manager, and design workflow automation blueprints.</p>
          </div>
          <div class="process-step reveal">
            <h3>3. Launch &amp; Automate</h3>
            <p>Content is produced, reviewed, and scheduled in Meta Business Suite. Paid campaigns are launched, and custom n8n automations go live to handle lead alerts and routine syncs.</p>
          </div>
          <div class="process-step reveal">
            <h3>4. Track, Report &amp; Optimise</h3>
            <p>Using Google Analytics and platform metrics, I provide clear bi-weekly reports detailing what performed best and where to allocate our focus in the next 90-day sprint.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- End Goal Statement -->
    <section class="closing-cta reveal" style="padding-bottom:1rem">
      <div class="container">
        <span class="section-label" style="justify-content:center">The End Goal</span>
        <h2>A marketing engine that operates<br><span class="text-accent">consistently without your constant supervision</span>.</h2>
        <p>
          When you partner with me, you aren't just buying random posts &mdash; you are installing a structured digital workflow that keeps your brand visible, your local rankings strong, and your leads organized while you focus on service delivery.
        </p>
      </div>
    </section>

    <!-- Experience & Education Timeline -->
    <section class="section reveal" aria-label="Experience and education timeline">
      <div class="container">
        <span class="section-label">Professional Timeline</span>
        <h2 class="section-title">Experience &amp; Education</h2>
        <div class="timeline">
          <!-- Mintrix -->
          <div class="timeline-item reveal">
            <div class="timeline-date">May 2026 &mdash; Present</div>
            <div class="timeline-title">Digital Marketing with AI Automation</div>
            <div class="timeline-company">Mintrix Virtual Assistants &middot; Full-Time Virtual Specialist</div>
            <div class="timeline-desc">
              <ul>
                <li>Design, build, and maintain AI-powered workflow automations in <strong>n8n</strong>, connecting applications and APIs to streamline repetitive digital marketing and administrative tasks for client accounts.</li>
                <li>Serve as social media administrator for client accounts: plan, create, schedule, and publish content using <strong>Meta Business Suite</strong>, managing comprehensive <strong>90-day content calendars</strong> aligned with brand and campaign goals.</li>
                <li>Set up, manage, and monitor paid social advertising campaigns in <strong>Meta Ads Manager</strong> to support client customer acquisition and audience growth.</li>
                <li>Apply SEO best practices and actively manage <strong>Google Business Profile</strong> listings to improve local visibility and search performance.</li>
                <li>Track content and campaign performance using <strong>Google Analytics</strong>, extracting actionable insights to continuously steer content strategy.</li>
              </ul>
            </div>
          </div>

          <!-- CertiCode -->
          <div class="timeline-item reveal">
            <div class="timeline-date">2026</div>
            <div class="timeline-title">Front-End Developer (Internship)</div>
            <div class="timeline-company">CertiCode &middot; Makati, Philippines</div>
            <div class="timeline-desc">
              <ul>
                <li>Designed and implemented front-end web components for production web applications, applying HTML, CSS, and JavaScript best practices to deliver responsive, cross-browser compatible user interfaces.</li>
                <li>Collaborated closely with senior developers in an Agile environment to review functional requirements, iterate on UI/UX feedback, and ship polished features on schedule.</li>
                <li>Maintained high code quality through consistent version control practices using Git, contributing to a shared codebase with multiple concurrent developers.</li>
              </ul>
            </div>
          </div>

          <!-- Education -->
          <div class="timeline-item reveal">
            <div class="timeline-date">August 2022 &mdash; July 2026</div>
            <div class="timeline-title">Bachelor of Science in Information Technology</div>
            <div class="timeline-company">Batangas State University ARASOF-Nasugbu Campus &middot; GWA: 1.9</div>
            <div class="timeline-desc">
              <ul>
                <li><strong>Capstone Project: ExcelLens</strong> &mdash; Student Performance &amp; Course Analytics Platform (2025). Led front-end UI engineering, developed dynamic automated grading systems, and successfully deployed the platform for active academic use across multiple university colleges.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Certifications Section (15+ exact certifications from resume) -->
    <section class="section reveal" id="certifications" aria-label="Official certifications and credentials">
      <div class="container">
        <span class="section-label">Verified Credentials</span>
        <h2 class="section-title">Certifications &amp; Accreditations</h2>
        <p class="section-subtitle">15+ verified credentials spanning Digital Marketing, Analytics, Cloud Computing, AI, and Professional Communication:</p>

        <!-- Category Filters -->
        <div class="cert-filters" style="margin-top:2rem">
          <button class="cert-filter active" data-filter="all">All Certifications</button>
          <button class="cert-filter" data-filter="professional">Professional / IT</button>
          <button class="cert-filter" data-filter="marketing">Marketing &amp; Analytics</button>
          <button class="cert-filter" data-filter="cloud">Cloud Computing</button>
          <button class="cert-filter" data-filter="data">Data Science &amp; AI</button>
          <button class="cert-filter" data-filter="ux">UX &amp; Communication</button>
        </div>

        <div class="cert-grid">
          <!-- Professional -->
          <div class="cert-card" data-category="professional">
            <div class="cert-icon">&#127942;</div>
            <div class="cert-info">
              <h4>IT Specialist &ndash; Data Analytics</h4>
              <span class="cert-issuer">Batangas State University ARASOF-Nasugbu</span>
              <span class="cert-date">May 2025</span>
            </div>
          </div>

          <div class="cert-card" data-category="professional">
            <div class="cert-icon">&#127942;</div>
            <div class="cert-info">
              <h4>IT Specialist &ndash; Databases</h4>
              <span class="cert-issuer">Batangas State University ARASOF-Nasugbu</span>
              <span class="cert-date">May 2024</span>
            </div>
          </div>

          <div class="cert-card" data-category="professional">
            <div class="cert-icon">&#127942;</div>
            <div class="cert-info">
              <h4>Microsoft Office Specialist &ndash; Microsoft Word (Office 2019)</h4>
              <span class="cert-issuer">Batangas State University ARASOF-Nasugbu</span>
              <span class="cert-date">Dec 2022</span>
            </div>
          </div>

          <!-- Marketing & Analytics -->
          <div class="cert-card" data-category="marketing">
            <div class="cert-icon">&#128200;</div>
            <div class="cert-info">
              <h4>Digital Skills: Digital Marketing</h4>
              <span class="cert-issuer">Accenture</span>
              <span class="cert-date">Apr 2026</span>
            </div>
          </div>

          <div class="cert-card" data-category="marketing">
            <div class="cert-icon">&#128269;</div>
            <div class="cert-info">
              <h4>SEO Certified</h4>
              <span class="cert-issuer">HubSpot Academy</span>
              <span class="cert-date">Feb 2026</span>
            </div>
          </div>

          <div class="cert-card" data-category="marketing">
            <div class="cert-icon">&#128202;</div>
            <div class="cert-info">
              <h4>Google Analytics Certification</h4>
              <span class="cert-issuer">Google</span>
              <span class="cert-date">Feb 2026</span>
            </div>
          </div>

          <div class="cert-card" data-category="marketing">
            <div class="cert-icon">&#128270;</div>
            <div class="cert-info">
              <h4>On-Page SEO and AI Search Essentials</h4>
              <span class="cert-issuer">Semrush Academy</span>
              <span class="cert-date">Apr 2026</span>
            </div>
          </div>

          <!-- Cloud -->
          <div class="cert-card" data-category="cloud">
            <div class="cert-icon">&#9729;&#65039;</div>
            <div class="cert-info">
              <h4>Introduction to Microsoft Azure</h4>
              <span class="cert-issuer">DataCamp</span>
              <span class="cert-date">Feb 2026</span>
            </div>
          </div>

          <div class="cert-card" data-category="cloud">
            <div class="cert-icon">&#9729;&#65039;</div>
            <div class="cert-info">
              <h4>Understanding Microsoft Azure</h4>
              <span class="cert-issuer">DataCamp</span>
              <span class="cert-date">Feb 2026</span>
            </div>
          </div>

          <!-- Data Science & AI -->
          <div class="cert-card" data-category="data">
            <div class="cert-icon">&#128187;</div>
            <div class="cert-info">
              <h4>Data Analytics Essentials</h4>
              <span class="cert-issuer">Cisco</span>
              <span class="cert-date">Dec 2024</span>
            </div>
          </div>

          <div class="cert-card" data-category="data">
            <div class="cert-icon">&#129504;</div>
            <div class="cert-info">
              <h4>AI Fundamentals</h4>
              <span class="cert-issuer">IBM SkillsBuild</span>
              <span class="cert-date">Nov 2024</span>
            </div>
          </div>

          <div class="cert-card" data-category="data">
            <div class="cert-icon">&#128013;</div>
            <div class="cert-info">
              <h4>Applied Data Science with Python</h4>
              <span class="cert-issuer">IBM SkillsBuild</span>
              <span class="cert-date">Nov 2024</span>
            </div>
          </div>

          <div class="cert-card" data-category="data">
            <div class="cert-icon">&#128451;&#65039;</div>
            <div class="cert-info">
              <h4>Big Data Foundations (Level 1 &amp; 2)</h4>
              <span class="cert-issuer">IBM SkillsBuild</span>
              <span class="cert-date">Nov 2024</span>
            </div>
          </div>

          <!-- UX & Professional -->
          <div class="cert-card" data-category="ux">
            <div class="cert-icon">&#127912;</div>
            <div class="cert-info">
              <h4>Digital Skills: User Experience</h4>
              <span class="cert-issuer">Accenture</span>
              <span class="cert-date">Apr 2026</span>
            </div>
          </div>

          <div class="cert-card" data-category="ux">
            <div class="cert-icon">&#128483;&#65039;</div>
            <div class="cert-info">
              <h4>Strategic Communication &amp; Teamwork</h4>
              <span class="cert-issuer">Santander Open Academy</span>
              <span class="cert-date">Apr 2026</span>
            </div>
          </div>

          <div class="cert-card" data-category="ux">
            <div class="cert-icon">&#127760;</div>
            <div class="cert-info">
              <h4>English for IT 1 &amp; 2</h4>
              <span class="cert-issuer">Cisco</span>
              <span class="cert-date">Nov 2024</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Accordion (9 comprehensive questions) -->
    <section class="section reveal" id="faq" aria-label="Frequently asked questions">
      <div class="container">
        <span class="section-label" style="justify-content:center">Frequently Asked Questions</span>
        <h2 class="section-title" style="text-align:center">Everything you need to know.</h2>
        <div class="faq-list">
          <!-- 1. Pricing & Packages -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              1. What are your pricing and package models?
              <span class="faq-icon">+</span>
            </button>
            <div class="faq-answer"><div class="faq-answer-inner">
              I provide tailored monthly retainer packages depending on your required scope: dedicated Social Media Management (with 90-day content calendars), Meta Ads campaign management, Google Business Profile local SEO, or end-to-end AI workflow automation via n8n. During our initial discovery conversation, I will assess your exact requirements and provide a transparent, flat-fee proposal. <!-- PLACEHOLDER: Insert your specific hourly or monthly retainer pricing tiers here -->
            </div></div>
          </div>

          <!-- 2. Turnaround Time -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              2. What is your typical turnaround time for deliverables?
              <span class="faq-icon">+</span>
            </button>
            <div class="faq-answer"><div class="faq-answer-inner">
              For initial onboardings, a full 90-day content calendar is delivered within 5 to 7 business days following asset handover. Ongoing social posts are scheduled at least 7 to 10 days in advance. Paid ad campaign configurations and n8n workflow automations typically take 3 to 5 business days from strategy approval.
            </div></div>
          </div>

          <!-- 3. Tools Used -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              3. Which tools and software platforms do you work with?
              <span class="faq-icon">+</span>
            </button>
            <div class="faq-answer"><div class="faq-answer-inner">
              My core stack includes: <strong>n8n</strong> for AI workflow automation; <strong>Meta Business Suite &amp; Meta Ads Manager</strong> for social and paid media; <strong>Google Business Profile &amp; Google Analytics</strong> for local visibility and traffic tracking; <strong>Semrush &amp; HubSpot</strong> for SEO analysis and inbound alignment; <strong>Figma</strong> for UI/UX creative; and <strong>HTML5, CSS3, JavaScript, Git, React Native, and Laravel</strong> for front-end development tasks.
            </div></div>
          </div>

          <!-- 4. Working with a VA -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              4. How does collaborating with a dedicated Virtual Assistant work?
              <span class="faq-icon">+</span>
            </button>
            <div class="faq-answer"><div class="faq-answer-inner">
              As a Digital Marketing Specialist at Mintrix Virtual Assistants, I function as an integrated extension of your internal team. You delegate your marketing and automation initiatives to me, and I execute them independently, providing documented workflows, scheduled approvals, and bi-weekly catch-up calls so you retain total control without getting bogged down in daily execution.
            </div></div>
          </div>

          <!-- 5. Reporting -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              5. How do you track and report campaign performance?
              <span class="faq-icon">+</span>
            </button>
            <div class="faq-answer"><div class="faq-answer-inner">
              You receive concise bi-weekly or monthly performance briefs featuring Google Analytics and Meta Business Suite metrics. We track reach, engagement rate, click-through rates, cost per lead, and Google Business Profile interactions. I highlight what worked, what needs refinement, and our prioritized action items for the upcoming cycle.
            </div></div>
          </div>

          <!-- 6. Timezone -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              6. What timezone are you based in and what are your working hours?
              <span class="faq-icon">+</span>
            </button>
            <div class="faq-answer"><div class="faq-answer-inner">
              I am based in Nasugbu, Batangas, Philippines (<strong>Philippine Standard Time, PHT &middot; UTC+8</strong>). This timezone overlaps closely with Australian business hours (AEST/AEDT is only 2&ndash;3 hours ahead) as well as Asian and European morning schedules. All your scheduled posts and ad campaigns are timed strictly to your customers' local timezone.
            </div></div>
          </div>

          <!-- 7. Communication -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              7. How will we communicate on a day-to-day basis?
              <span class="faq-icon">+</span>
            </button>
            <div class="faq-answer"><div class="faq-answer-inner">
              I adapt to your team's preferred communication rhythm &mdash; whether via Slack, Microsoft Teams, WhatsApp, Email, or Zoom/Google Meet for weekly syncs. For non-urgent matters, I respond within 24 business hours; for time-sensitive campaign updates, you have direct priority access.
            </div></div>
          </div>

          <!-- 8. Web Development Services -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              8. Can you build or optimize our company website as well?
              <span class="faq-icon">+</span>
            </button>
            <div class="faq-answer"><div class="faq-answer-inner">
              Yes. Having served as a Front-End Developer intern at CertiCode and led the UI engineering for BatStateU's ExcelLens platform, I build responsive, accessible, mobile-first websites and landing pages in clean HTML5, CSS3, and JavaScript, as well as React Native and Laravel applications.
            </div></div>
          </div>

          <!-- 9. Guarantee & Commitments -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              9. Do you guarantee specific revenue or follower numbers?
              <span class="faq-icon">+</span>
            </button>
            <div class="faq-answer"><div class="faq-answer-inner">
              No genuine marketing professional can legally or ethically guarantee specific sales numbers or overnight virality, as algorithms, market dynamics, and pricing depend on factors outside of marketing alone. What I guarantee is strict operational consistency, clean data reporting, tested technical automations, and proactive optimization.
            </div></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Closing CTA -->
    <section class="closing-cta reveal">
      <div class="container">
        <h2>Ready to streamline your marketing operations?<br><span class="text-accent">Let&rsquo;s talk today.</span></h2>
        <p>Book a direct discovery call and let&rsquo;s design a plan tailored to your business goals.</p>
        <a href="contact.html" class="btn btn-primary">Get in touch &rarr;</a>
      </div>
    </section>
  </main>
""" + render_footer(root="")

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_content)
print("about.html created")

# ==================== BUILD PORTFOLIO.HTML ====================
portfolio_content = render_header(root="", active_page="portfolio") + """
  <main id="main">
    <section class="page-hero">
      <div class="container">
        <span class="section-label" style="justify-content:center">Portfolio &amp; Case Studies</span>
        <h1>Real Work.<br><span class="text-accent">Verifiable Impact.</span></h1>
        <p class="subtitle">
          Explore real client engagements, live deployed applications, and technical front-end development projects.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <!-- Filter Tabs -->
        <div class="portfolio-filters">
          <button class="portfolio-filter active" data-filter="all">All Projects</button>
          <button class="portfolio-filter" data-filter="social-media">Social Media &amp; Content</button>
          <button class="portfolio-filter" data-filter="local-seo">Local SEO &amp; GBP</button>
          <button class="portfolio-filter" data-filter="web-app">Web &amp; Software Development</button>
        </div>

        <div class="portfolio-list">
          <!-- ==================== FEATURED CASE STUDY: MELBOURNE WIDE ==================== -->
          <!-- NOTE: Used with client permission — CONFIRM before publishing -->
          <article class="portfolio-entry reveal" id="melbourne-wide" data-category="social-media">
            <div class="portfolio-entry-image" style="background:#13151F;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:2.5rem;text-align:center;">
              <img src="images/clients/melbourne-wide-logo.svg" alt="Melbourne Wide Electrical &amp; Plumbing" style="max-height:65px;width:auto;margin-bottom:1.5rem;" onerror="this.style.display='none'">
              <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:1rem 1.5rem;">
                <div style="color:#FFD700;font-size:1.1rem;margin-bottom:0.25rem;">&#9733;&#9733;&#9733;&#9733;&#9733; 5.0 Google Rating</div>
                <div style="font-size:0.85rem;color:var(--text-secondary)">Over 700+ Verified Customer Reviews</div>
              </div>
            </div>

            <div class="portfolio-entry-content">
              <div class="project-tags">
                <span class="project-tag">Social Media Admin</span>
                <span class="project-tag">90-Day Content Calendar</span>
                <span class="project-tag">Meta Business Suite</span>
                <span class="project-tag">Google Business Profile</span>
              </div>
              <h3>Featured Client: Melbourne Wide Electrical &amp; Plumbing</h3>
              <p>
                <strong>Client Background:</strong> Melbourne Wide Electrical &amp; Plumbing is a premier licensed trade services provider headquartered in Thomastown, Victoria, serving Melbourne's northern suburbs alongside sister brands Melbourne Wide Plumbing and Melbourne Wide Air Conditioning.
              </p>
              <p>
                <strong>My Hands-On Role (May 2026 &ndash; Present):</strong> As their Digital Marketing Assistant via Mintrix Virtual Assistants, I administer their social media channels:
              </p>
              <ul style="list-style:disc;padding-left:1.25rem;color:var(--text-secondary);font-size:0.92rem;line-height:1.65;margin-bottom:1rem;">
                <li>Planning, organizing, and executing a comprehensive <strong>90-day content calendar</strong> reflecting seasonal demand and trade specializations.</li>
                <li>Designing and publishing their signature weekly wrap-up carousel: <em>&ldquo;Another Week. Another Round of Jobs Done Right!&rdquo;</em>, showcasing real on-site technician workmanship.</li>
                <li>Scheduling multi-channel content through <strong>Meta Business Suite</strong> and actively monitoring post engagement.</li>
                <li>Updating and optimizing their <strong>Google Business Profile</strong> listings with service updates and completed projects to sustain top local search placement.</li>
                <li>Analyzing performance data in <strong>Google Analytics</strong> and delivering structured monthly reporting.</li>
              </ul>

              <!-- Placeholders for verifiable results -->
              <div style="background:var(--bg);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;margin-bottom:1.25rem;">
                <h4 style="font-size:0.85rem;text-transform:uppercase;letter-spacing:0.08em;color:var(--accent);margin-bottom:0.5rem">Documented Performance Metrics:</h4>
                <ul style="list-style:circle;padding-left:1.2rem;font-size:0.88rem;color:var(--text-secondary);line-height:1.6">
                  <li>[ADD RESULT &mdash; e.g. 100% on-time execution across weekly &ldquo;Jobs Done Right!&rdquo; carousels]</li>
                  <li>[ADD RESULT &mdash; e.g. +XX% increase in monthly social post reach and profile visits]</li>
                  <li>[ADD RESULT &mdash; e.g. XX new Google Business Profile photo impressions and call clicks]</li>
                  <li>[ADD RESULT &mdash; e.g. Saved client ~XX hours/month of marketing admin time]</li>
                </ul>
              </div>

              <!-- PLACEHOLDER: Melbourne Wide Testimonial -->
              <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;">
                <p style="font-style:italic;font-size:0.9rem;color:var(--text-secondary);line-height:1.6;">
                  &ldquo;[ADD TESTIMONIAL &mdash; Insert real quote from Melbourne Wide management regarding your consistency and weekly carousel administration.]&rdquo;
                </p>
                <p style="font-size:0.8rem;color:var(--text-muted);margin-top:0.5rem">&mdash; [Client Contact Name], Melbourne Wide Electrical &amp; Plumbing</p>
              </div>
            </div>
          </article>

          <!-- ==================== EXCELLENS CAPSTONE ==================== -->
          <article class="portfolio-entry reveal" id="excellens" data-category="web-app">
            <div class="portfolio-entry-image" style="background:#0F1726;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:2.5rem;text-align:center;">
              <div style="font-size:3rem;margin-bottom:0.75rem">&#128202;</div>
              <h3 style="font-size:1.4rem;margin-bottom:0.25rem">ExcelLens</h3>
              <p style="font-size:0.85rem;color:var(--accent)">BatStateU Academic Analytics</p>
              <div style="margin-top:1rem;background:rgba(76,175,80,0.12);border:1px solid rgba(76,175,80,0.3);color:#4CAF50;padding:0.35rem 0.85rem;border-radius:var(--radius-pill);font-size:0.75rem;font-weight:600;">
                &#9679; Deployed &amp; In Active University Use
              </div>
            </div>

            <div class="portfolio-entry-content">
              <div class="project-tags">
                <span class="project-tag">Capstone Research &middot; 2025</span>
                <span class="project-tag">Front-End Lead</span>
                <span class="project-tag">Data Visualization</span>
                <span class="project-tag">Automated Grading</span>
              </div>
              <h3>ExcelLens &mdash; Student Performance &amp; Course Analytics Platform</h3>
              <p>
                <strong>The Challenge:</strong> Faculty members across Batangas State University ARASOF-Nasugbu relied on manual spreadsheets to calculate multi-criteria course assessments, creating administrative bottlenecks, error risks, and delayed registrar submissions.
              </p>
              <p>
                <strong>My Architecture &amp; Execution:</strong>
              </p>
              <ul style="list-style:disc;padding-left:1.25rem;color:var(--text-secondary);font-size:0.92rem;line-height:1.65;margin-bottom:1rem;">
                <li>Served as <strong>Front-End Lead Developer</strong>, designing intuitive faculty dashboards, grade entry interfaces, and student analytics visualization screens.</li>
                <li>Engineered a <strong>dynamic grading engine</strong> that automated assessment computations according to university grading policies, eliminating manual spreadsheet formulas.</li>
                <li>Implemented an <strong>Excel export utility</strong> enabling one-click generation of institutional grade report sheets compliant with university registrar standards.</li>
                <li>Contributed to back-end implementation and successfully deployed the platform at <strong>Batangas State University ARASOF-Nasugbu</strong>, where it is actively used across multiple colleges for academic data management.</li>
              </ul>
            </div>
          </article>

          <!-- ==================== CERTICODE INTERNSHIP ==================== -->
          <article class="portfolio-entry reveal" id="certicode" data-category="web-app">
            <div class="portfolio-entry-image" style="background:#171524;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:2.5rem;text-align:center;">
              <div style="font-size:3rem;margin-bottom:0.75rem">&#128187;</div>
              <h3 style="font-size:1.4rem;margin-bottom:0.25rem">CertiCode</h3>
              <p style="font-size:0.85rem;color:var(--accent)">Makati, Philippines</p>
              <div style="margin-top:1rem;background:var(--accent-tint);border:1px solid var(--accent);color:var(--accent);padding:0.35rem 0.85rem;border-radius:var(--radius-pill);font-size:0.75rem;font-weight:600;">
                Production Front-End Engineering
              </div>
            </div>

            <div class="portfolio-entry-content">
              <div class="project-tags">
                <span class="project-tag">HTML5 / CSS3 / JavaScript</span>
                <span class="project-tag">Git Version Control</span>
                <span class="project-tag">Agile Development</span>
              </div>
              <h3>Front-End Web Application Components &mdash; CertiCode</h3>
              <p>
                <strong>Internship Scope:</strong> Working within an Agile software team in Makati, I engineered production-ready front-end components for client web applications:
              </p>
              <ul style="list-style:disc;padding-left:1.25rem;color:var(--text-secondary);font-size:0.92rem;line-height:1.65;margin-bottom:1rem;">
                <li>Implemented responsive, accessible, cross-browser compliant UI components adhering strictly to clean HTML, CSS, and modern JavaScript standards.</li>
                <li>Collaborated closely with senior software engineers, participating in code reviews, daily stand-ups, and sprint planning.</li>
                <li>Utilized Git version control consistently to collaborate across multi-developer feature branches without integration conflicts.</li>
              </ul>
              <!-- PLACEHOLDER: Add specific web application screenshots if permitted -->
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Closing CTA -->
    <section class="closing-cta reveal">
      <div class="container">
        <h2>Want similar results for your business?<br><span class="text-accent">Let&rsquo;s talk.</span></h2>
        <p>I bring this exact level of dedication, organization, and technical accuracy to every client engagement.</p>
        <a href="contact.html" class="btn btn-primary">Start a conversation &rarr;</a>
      </div>
    </section>
  </main>
""" + render_footer(root="")

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(portfolio_content)
print("portfolio.html created")

# ==================== BUILD CONTACT.HTML ====================
contact_content = render_header(root="", active_page="contact") + """
  <main id="main">
    <section class="page-hero">
      <div class="container">
        <span class="section-label" style="justify-content:center">Contact &amp; Inquiries</span>
        <h1>Let&rsquo;s Discuss Your Project.</h1>
        <p class="subtitle">
          Ready to establish consistent social media posting, launch targeted Meta Ads, boost your local Google rankings, or automate repetitive tasks? Let's connect.
        </p>
        <div class="availability" style="justify-content:center;margin-top:1.5rem">
          <span class="dot"></span>
          Currently accepting new clients &middot; Fast 24-Hour Response
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="contact-grid reveal">
          <!-- Contact Form with Validation & Fallback -->
          <div>
            <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:2.25rem;">
              <h2 style="font-family:var(--font-heading);font-size:1.4rem;margin-bottom:0.5rem">Send Me a Message</h2>
              <p style="font-size:0.9rem;color:var(--text-secondary);margin-bottom:1.5rem">Fill out the fields below and I'll get back to you within 24 hours.</p>

              <!-- PLACEHOLDER: Formspree endpoint placeholder.
                   Sign up free at https://formspree.io and paste your form ID in action below:
                   e.g. action="https://formspree.io/f/my-form-id" -->
              <form id="contact-form" action="https://formspree.io/f/YOUR_FORMSPREE_ID" method="POST" novalidate>
                <div class="form-group">
                  <label class="form-label" for="name">Your Name *</label>
                  <input type="text" class="form-input" id="name" name="name" placeholder="John Smith" required>
                  <p class="form-error">Please enter your name.</p>
                </div>

                <div class="form-group">
                  <label class="form-label" for="business">Business or Organization Name</label>
                  <input type="text" class="form-input" id="business" name="business" placeholder="e.g. Smith Electrical Services">
                </div>

                <div class="form-group">
                  <label class="form-label" for="email">Email Address *</label>
                  <input type="email" class="form-input" id="email" name="email" placeholder="john@example.com" required>
                  <p class="form-error">Please enter a valid email address.</p>
                </div>

                <div class="form-group">
                  <label class="form-label" for="phone">Phone Number</label>
                  <input type="tel" class="form-input" id="phone" name="phone" placeholder="+61 400 000 000 or +63 900 000 0000">
                </div>

                <div class="form-group">
                  <label class="form-label" for="message">How Can I Help You? *</label>
                  <textarea class="form-textarea" id="message" name="message" placeholder="Tell me about your business, current marketing challenges, and target goals..." required></textarea>
                  <p class="form-error">Please enter your message.</p>
                </div>

                <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center">Send Message &rarr;</button>

                <div class="form-status" role="alert"></div>

                <p style="font-size:0.8rem;color:var(--text-muted);margin-top:1rem;text-align:center">
                  Prefer direct email? Reach me at <a href="mailto:ahlybabar1188@gmail.com" style="color:var(--accent)">ahlybabar1188@gmail.com</a>
                </p>
              </form>
            </div>
          </div>

          <!-- Direct Details & Timezone Info -->
          <div class="contact-info">
            <div class="contact-detail">
              <div class="contact-detail-icon">&#9993;&#65039;</div>
              <div>
                <h4>Direct Email</h4>
                <a href="mailto:ahlybabar1188@gmail.com">ahlybabar1188@gmail.com</a>
                <p style="font-size:0.8rem;color:var(--text-muted);margin-top:0.25rem">Checked daily; 24-hour response turnaround.</p>
              </div>
            </div>

            <div class="contact-detail">
              <div class="contact-detail-icon">&#128222;</div>
              <div>
                <h4>Direct Phone / WhatsApp</h4>
                <a href="tel:+639476179440">+63 947 617 9440</a>
                <p style="font-size:0.8rem;color:var(--text-muted);margin-top:0.25rem">Voice and messaging available.</p>
              </div>
            </div>

            <div class="contact-detail">
              <div class="contact-detail-icon">&#128205;</div>
              <div>
                <h4>Location</h4>
                <p>Nasugbu, Batangas, Philippines</p>
              </div>
            </div>

            <div class="contact-detail">
              <div class="contact-detail-icon">&#128337;</div>
              <div>
                <h4>Timezone &amp; Working Alignment</h4>
                <p>Philippine Standard Time (PHT &middot; UTC+8)</p>
                <p style="font-size:0.82rem;color:var(--text-muted);margin-top:0.25rem">
                  Convenient real-time overlap with Australia (AEST/AEDT), Singapore/Hong Kong, and Europe.
                </p>
              </div>
            </div>

            <div class="contact-detail">
              <div class="contact-detail-icon">&#128188;</div>
              <div>
                <h4>LinkedIn Network</h4>
                <a href="https://www.linkedin.com/in/ahly-monzour-babar-473a53365/" target="_blank" rel="noopener">linkedin.com/in/ahly-monzour-babar</a>
              </div>
            </div>

            <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:1.5rem;margin-top:1rem">
              <h4 style="font-family:var(--font-heading);font-size:0.95rem;margin-bottom:0.5rem">&#128203; What to expect next:</h4>
              <ol style="font-size:0.88rem;color:var(--text-secondary);line-height:1.6;padding-left:1.2rem">
                <li>I review your message and existing online profiles.</li>
                <li>I reply within 24 hours with preliminary thoughts.</li>
                <li>We hold a no-obligation 20-minute discovery call to align on goals.</li>
              </ol>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
""" + render_footer(root="")

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_content)
print("contact.html created")

# ==================== BUILD ARTICLES.HTML ====================
articles_content = render_header(root="", active_page="articles") + """
  <main id="main">
    <section class="page-hero">
      <div class="container">
        <span class="section-label" style="justify-content:center">Articles &amp; Field Notes</span>
        <h1>Practical Marketing &amp; Automation Insights.</h1>
        <p class="subtitle">
          Real lessons, workflow blueprints, and actionable tips from managing social campaigns, Meta Ads, and n8n automations.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="articles-grid">
          <!-- Article 1 Placeholder -->
          <article class="article-card reveal">
            <div class="article-card-body">
              <p class="article-date">[ADD DATE &mdash; e.g. May 2026]</p>
              <h3>[ADD ARTICLE TITLE: Why 90-Day Content Calendars Outperform Daily Guesswork]</h3>
              <p>
                [ADD SHORT DESCRIPTION &mdash; A practical breakdown of how building structured 90-day social content roadmaps helps local service businesses maintain consistent posting, seasonal authority, and customer engagement.]
              </p>
              <span class="btn-ghost" style="margin-top:1rem">[Read Article &rarr;]</span>
            </div>
          </article>

          <!-- Article 2 Placeholder -->
          <article class="article-card reveal">
            <div class="article-card-body">
              <p class="article-date">[ADD DATE &mdash; e.g. May 2026]</p>
              <h3>[ADD ARTICLE TITLE: 5 Essential n8n Workflows Every Digital Marketer Should Automate]</h3>
              <p>
                [ADD SHORT DESCRIPTION &mdash; How to connect your Meta Business Suite, CRM lead forms, and Google Analytics alerts into automated node workflows without coding back-ends.]
              </p>
              <span class="btn-ghost" style="margin-top:1rem">[Read Article &rarr;]</span>
            </div>
          </article>

          <!-- Article 3 Placeholder -->
          <article class="article-card reveal">
            <div class="article-card-body">
              <p class="article-date">[ADD DATE &mdash; e.g. May 2026]</p>
              <h3>[ADD ARTICLE TITLE: Optimizing Your Google Business Profile for Suburb-Level Search]</h3>
              <p>
                [ADD SHORT DESCRIPTION &mdash; The core local SEO steps trade companies and service businesses must take to earn top placement in Google 3-Pack and Google Maps searches.]
              </p>
              <span class="btn-ghost" style="margin-top:1rem">[Read Article &rarr;]</span>
            </div>
          </article>
        </div>

        <div style="text-align:center;margin-top:4rem;background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:3rem;">
          <h3 style="font-family:var(--font-heading);font-size:1.3rem;margin-bottom:0.75rem;">Want me to write about a specific topic?</h3>
          <p style="color:var(--text-secondary);max-width:500px;margin:0 auto 1.5rem;font-size:0.95rem;">
            Whether it's n8n workflow blueprints, Meta Ads testing methods, or local SEO tactics &mdash; send me your questions.
          </p>
          <a href="contact.html" class="btn btn-primary">Suggest a topic &rarr;</a>
        </div>
      </div>
    </section>
  </main>
""" + render_footer(root="")

with open('articles.html', 'w', encoding='utf-8') as f:
    f.write(articles_content)
print("articles.html created")

# ==================== BUILD THE 5 SERVICE PAGES ====================
services_data = [
    {
        'file': 'services/social-media.html',
        'title': 'Social Media Management &amp; 90-Day Content Calendars',
        'subtitle': 'Eliminate erratic posting. Build a planned, brand-aligned presence on Meta platforms that nurtures leads and reinforces credibility.',
        'badge': 'Core Service',
        'intro': 'Most small businesses post only when work slows down, then disappear for months. I install a structured 90-day content calendar system managed through Meta Business Suite, ensuring your audience sees consistent, professional work every week.',
        'features': [
            ('&#128197;', 'Structured 90-Day Content Calendars', 'Comprehensive quarter-by-quarter editorial roadmaps detailing post formats, educational tips, team spotlights, customer reviews, and seasonal promotions.'),
            ('&#128241;', 'Meta Business Suite Administration', 'End-to-end post preparation, graphic formatting, caption copywriting, hashtag alignment, and advance scheduling across Instagram and Facebook.'),
            ('&#128196;', 'Weekly Proof-of-Work Carousels', 'Specialized weekly wrap-up carousels (such as &ldquo;Another Week. Another Round of Jobs Done Right!&rdquo;) that document actual completed client projects.'),
            ('&#128200;', 'Engagement &amp; Growth Monitoring', 'Tracking reach, saves, shares, and audience inquiries to refine what resonates best with your local market.')
        ],
        'cta': 'Get your 90-day content plan'
    },
    {
        'file': 'services/meta-ads.html',
        'title': 'Meta Ads Management',
        'subtitle': 'Strategic paid campaigns across Facebook &amp; Instagram that convert ad spend into measurable customer inquiries.',
        'badge': 'Paid Advertising',
        'intro': 'Random post boosts waste money. I configure structured campaigns inside Meta Ads Manager tailored to your target geographic radius, demographics, and customer intent.',
        'features': [
            ('&#127919;', 'Targeted Campaign Setup', 'Custom audience building based on local suburbs, service interests, lookalike segments, and re-targeting previous website visitors.'),
            ('&#128161;', 'Creative &amp; Copy Testing', 'Testing multiple ad creative formats &mdash; video reels, static graphics, and client work carousels &mdash; with conversion-driven calls to action.'),
            ('&#128202;', 'Continuous Budget Optimization', 'Daily monitoring of cost-per-click, cost-per-lead, and frequency to prevent ad fatigue and maximize your return on ad spend.'),
            ('&#128203;', 'Transparent Bi-Weekly Reporting', 'Plain-English performance summaries explaining exactly how many clicks, calls, or leads your campaigns generated.')
        ],
        'cta': 'Discuss your ad campaign'
    },
    {
        'file': 'services/seo.html',
        'title': 'SEO &amp; Google Business Profile Optimization',
        'subtitle': 'Dominate local suburb searches and Google Maps rankings when nearby customers need your services.',
        'badge': 'Local Search Optimization',
        'intro': 'When high-intent customers search for services &ldquo;near me&rdquo;, your Google Business Profile is your digital storefront. I ensure your profile is fully optimized, active, and outranking competitors.',
        'features': [
            ('&#128205;', 'Google Business Profile Administration', 'Regular post updates, project photos, service category refinements, and active review management to signal trust to Google algorithms.'),
            ('&#128269;', 'On-Page SEO Best Practices', 'Implementing metadata, structured header hierarchies (H1/H2), title tags, and optimized service page copy certified by HubSpot and Semrush.'),
            ('&#128200;', 'Google Analytics Setup &amp; Monitoring', 'Tracking organic traffic trends, bounce rates, and user conversion paths to understand where your most valuable customers originate.'),
            ('&#127942;', 'Local Suburb Visibility', 'Keyword optimization targeting specific northern suburbs, service corridors, and high-value search queries.')
        ],
        'cta': 'Optimize your local search'
    },
    {
        'file': 'services/ai-automation.html',
        'title': 'AI Workflow Automation with n8n',
        'subtitle': 'Bridge your tools, eliminate manual data entry, and automate routine marketing workflows with custom n8n pipelines.',
        'badge': 'Workflow Engineering',
        'intro': 'Stop spending hours manually copying leads from ad forms into spreadsheets, sending email alerts, or generating reports. I build custom, node-based n8n automations that connect your tech stack.',
        'features': [
            ('&#9881;&#65039;', 'Custom n8n Workflow Architecture', 'Designing self-hosted or cloud n8n workflows that listen for events across webhooks, APIs, forms, and databases.'),
            ('&#128279;', 'Seamless API &amp; App Integration', 'Connecting Meta Ads lead forms directly into your CRM, sending instant SMS/email lead alerts to your technicians, and logging details into Google Sheets.'),
            ('&#129504;', 'AI-Powered Content &amp; Triage', 'Integrating modern LLM APIs to draft initial responses, categorize inbound customer requests, and summarize weekly analytics.'),
            ('&#128202;', 'Automated Report Delivery', 'Scheduled reporting workflows that automatically fetch Google Analytics data and email formatted stakeholder summaries.')
        ],
        'cta': 'Automate your workflows'
    },
    {
        'file': 'services/web-development.html',
        'title': 'Website &amp; Front-End Development',
        'subtitle': 'Modern, mobile-first, and ultra-fast websites built with clean semantic code that turns traffic into paying customers.',
        'badge': 'Technical Engineering',
        'intro': 'Drawing on my experience as a Front-End Developer at CertiCode and lead UI architect of BatStateU\'s ExcelLens platform, I engineer responsive, accessible web experiences that look sharp on any device.',
        'features': [
            ('&#128187;', 'Clean HTML5, CSS3 &amp; JavaScript', 'Fast, lightweight websites built without bloated heavy frameworks, optimized for speed, accessibility, and high Google Lighthouse scores.'),
            ('&#127912;', 'UI/UX Design with Figma', 'Creating professional component systems and interface mockups that align with your branding and guide visitors to conversion.'),
            ('&#9883;&#65039;', 'React Native &amp; Laravel Capabilities', 'Capable of building advanced cross-platform mobile interfaces and database-driven backend web applications.'),
            ('&#128204;', 'Conversion-Optimized Landing Pages', 'Tailored landing pages designed specifically to complement your Meta Ads campaigns and capture customer inquiries.')
        ],
        'cta': 'Build your website'
    }
]

for svc in services_data:
    features_html = ""
    for icon, h, desc in svc['features']:
        features_html += f"""
              <div class="service-feature">
                <div class="service-feature-icon">{icon}</div>
                <div>
                  <h4>{h}</h4>
                  <p>{desc}</p>
                </div>
              </div>"""

    svc_content = render_header(root="../", active_page="services") + f"""
  <main id="main">
    <section class="page-hero">
      <div class="container">
        <span class="section-label" style="justify-content:center">{svc['badge']}</span>
        <h1>{svc['title']}</h1>
        <p class="subtitle">{svc['subtitle']}</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="service-content reveal">
          <div>
            <h2 class="section-title" style="font-size:1.85rem">What&rsquo;s Included</h2>
            <p style="color:var(--text-secondary);margin-bottom:2rem;line-height:1.7;">
              {svc['intro']}
            </p>
            <div class="service-features">
              {features_html}
            </div>
            <div style="margin-top:2.5rem">
              <a href="../contact.html" class="btn btn-primary">{svc['cta']} &rarr;</a>
            </div>
          </div>

          <div>
            <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:2.5rem;">
              <h3 style="font-family:var(--font-heading);font-size:1.3rem;margin-bottom:1rem">Why Partner with Ahly Babar?</h3>
              <div class="solution-features">
                <div class="solution-feature">
                  <div class="check">&#10003;</div>
                  <p><strong>Dedicated Virtual Specialist:</strong> Direct personal execution through Mintrix Virtual Assistants &mdash; no delegating to junior contractors.</p>
                </div>
                <div class="solution-feature">
                  <div class="check">&#10003;</div>
                  <p><strong>Dual Technical &amp; Marketing Skill:</strong> Front-end development discipline combined with creative social media management.</p>
                </div>
                <div class="solution-feature">
                  <div class="check">&#10003;</div>
                  <p><strong>15+ Verified Certifications:</strong> Google Analytics, HubSpot SEO, Semrush, Cisco, IBM, and Accenture certified.</p>
                </div>
                <div class="solution-feature">
                  <div class="check">&#10003;</div>
                  <p><strong>Proven Trade Experience:</strong> Supporting marketing for established brands with 700+ five-star Google reviews.</p>
                </div>
              </div>
            </div>

            <!-- PLACEHOLDER: Service-specific Testimonial -->
            <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:2rem;margin-top:1.5rem">
              <p style="font-style:italic;color:var(--text-secondary);line-height:1.7">
                &ldquo;[ADD TESTIMONIAL &mdash; Insert real client feedback specifically highlighting your work on this service.]&rdquo;
              </p>
              <p style="font-size:0.85rem;color:var(--text-muted);margin-top:0.75rem">&mdash; [Client Contact], [Business Name]</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Closing CTA -->
    <section class="closing-cta reveal">
      <div class="container">
        <h2>Ready to get started?<br><span class="text-accent">Let&rsquo;s build your strategy.</span></h2>
        <p>Contact me today for a direct consultation and let's map out your execution roadmap.</p>
        <a href="../contact.html" class="btn btn-primary">Schedule a consultation &rarr;</a>
      </div>
    </section>
  </main>
""" + render_footer(root="../")

    with open(svc['file'], 'w', encoding='utf-8') as f:
        f.write(svc_content)
    print(f"{svc['file']} created")

print("All pages successfully built!")
