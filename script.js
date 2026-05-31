/* ============================================================
   Digital Dreamsbox — script.js
   Interactions : reveal · nav · process · FAQ · vCard · magnet · cookies · form
   ============================================================ */

(function () {
  'use strict';

  /* ── 0. Animated blob background + scroll-speed acceleration ─ */
  (function () {
    /* Inject 6 blobs */
    var wrap = document.createElement('div');
    wrap.id = 'bg-blobs';
    for (var i = 1; i <= 6; i++) {
      var b = document.createElement('div');
      b.className = 'blob blob-' + i;
      wrap.appendChild(b);
    }
    document.body.insertBefore(wrap, document.body.firstChild);

    /* Scroll velocity → WAAPI playbackRate.
       Faster scroll = faster blobs. When scroll stops, rate decays back to 1. */
    var lastScrollY = window.scrollY;
    var decayTimer  = null;
    var MAX_RATE    = 6.5;

    function getBlobAnims() {
      return Array.prototype.slice.call(
        document.querySelectorAll('#bg-blobs .blob')
      ).reduce(function (acc, el) {
        return acc.concat(el.getAnimations ? el.getAnimations() : []);
      }, []);
    }

    function setRate(r) {
      getBlobAnims().forEach(function (a) { a.playbackRate = r; });
    }

    function decayToNormal() {
      /* Smooth 400ms decay: step down 4 times */
      var steps  = 4;
      var delay  = 100;
      var current = MAX_RATE;
      for (var s = 1; s <= steps; s++) {
        (function (step) {
          setTimeout(function () {
            var r = 1 + (MAX_RATE - 1) * (1 - step / steps);
            setRate(r);
          }, delay * step);
        })(s);
      }
    }

    window.addEventListener('scroll', function () {
      var y     = window.scrollY;
      var delta = Math.abs(y - lastScrollY);
      lastScrollY = y;

      /* Map pixel delta per event to rate: ~25px → max */
      var rate = Math.min(1 + delta / 6.5, MAX_RATE);
      setRate(rate);

      clearTimeout(decayTimer);
      decayTimer = setTimeout(decayToNormal, 120);
    }, { passive: true });
  })();

  /* ── 1. Year update ──────────────────────────────────────── */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ── 2. Scroll-reveal (IntersectionObserver) ─────────────── */
  var revealObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        var el = entry.target;
        var delay = parseFloat(getComputedStyle(el).getPropertyValue('--rd') || '0') * 1000;
        setTimeout(function () { el.classList.add('visible'); }, delay);
        revealObserver.unobserve(el);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach(function (el) {
    revealObserver.observe(el);
  });

  /* ── 3. Header scroll state ──────────────────────────────── */
  var header = document.querySelector('.site-header');
  var lastY = 0;
  if (header) {
    window.addEventListener('scroll', function () {
      var y = window.scrollY;
      if (y > 80) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
      if (y > lastY + 8 && y > 200) {
        header.classList.add('hidden');
      } else if (y < lastY - 4) {
        header.classList.remove('hidden');
      }
      lastY = y;
    }, { passive: true });
  }

  /* ── 4. Mobile nav — premium overlay ────────────────────────── */
  var navToggle = document.querySelector('.nav-toggle');
  var navLinks  = document.querySelector('.nav-links');

  if (navToggle) {
    // Replace static SVG with animated lines
    navToggle.innerHTML =
      '<span class="line"></span>' +
      '<span class="line"></span>' +
      '<span class="line"></span>';

    // Collect page links from desktop nav
    var pageLinks = navLinks ? Array.from(navLinks.querySelectorAll('a')) : [];
    var nums = ['01', '02', '03', '04', '05'];

    // Build overlay links HTML
    var linksHTML = pageLinks.map(function (a, i) {
      return '<a href="' + a.getAttribute('href') + '" style="--i:' + i + '">' +
             '<span class="nav-num">' + (nums[i] || '') + '</span>' +
             a.textContent.trim() +
             '</a>';
    }).join('');

    // Determine path prefix (pages/contact.html vs contact.html)
    var isSubPage = window.location.pathname.indexOf('/pages/') !== -1;
    var contactHref = isSubPage ? 'contact.html' : 'pages/contact.html';
    var telLink = 'tel:+33688848145';

    // Create overlay
    var overlay = document.createElement('div');
    overlay.className = 'nav-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Navigation principale');
    overlay.innerHTML =
      '<div class="nav-overlay-inner">' +
        '<nav class="nav-overlay-links" aria-label="Navigation">' + linksHTML + '</nav>' +
        '<div class="nav-overlay-bottom">' +
          '<a href="' + telLink + '" class="btn btn-ghost">' +
            '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.86 19.86 0 0 1 2.08 4.18 2 2 0 0 1 4.07 2h3a2 2 0 0 1 2 1.72 12.5 12.5 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.5 12.5 0 0 0 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>' +
            '06 88 84 81 45' +
          '</a>' +
          '<a href="' + contactHref + '" class="btn btn-primary">' +
            'Nous contacter' +
            '<svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"/></svg>' +
          '</a>' +
          '<p class="nav-overlay-location">' +
            '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>' +
            'Sarrebourg, Moselle' +
          '</p>' +
        '</div>' +
      '</div>';

    document.body.appendChild(overlay);

    function openMenu() {
      navToggle.setAttribute('aria-expanded', 'true');
      overlay.classList.add('open');
      document.body.classList.add('nav-open');
    }
    function closeMenu() {
      navToggle.setAttribute('aria-expanded', 'false');
      overlay.classList.remove('open');
      document.body.classList.remove('nav-open');
    }

    navToggle.addEventListener('click', function () {
      navToggle.getAttribute('aria-expanded') === 'true' ? closeMenu() : openMenu();
    });

    overlay.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeMenu);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMenu();
    });
  }

  /* ── 5. Magnet button effect ─────────────────────────────── */
  document.querySelectorAll('[data-magnet]').forEach(function (btn) {
    btn.addEventListener('mousemove', function (e) {
      var r  = btn.getBoundingClientRect();
      var x  = e.clientX - (r.left + r.width  / 2);
      var y  = e.clientY - (r.top  + r.height / 2);
      btn.style.transform = 'translate(' + (x * 0.22) + 'px,' + (y * 0.22) + 'px)';
    });
    btn.addEventListener('mouseleave', function () {
      btn.style.transform = '';
    });
  });

  /* ── 6. Process rail — horizontal scroll carousel ─────────── */
  var rail    = document.querySelector('.process-rail');
  var cards   = rail ? Array.from(rail.querySelectorAll('.process-card')) : [];
  var dots    = Array.from(document.querySelectorAll('.pdot'));
  var prevBtn = document.querySelector('[data-proc-prev]');
  var nextBtn = document.querySelector('[data-proc-next]');
  var procIdx = 0;

  function goProc(i) {
    procIdx = Math.max(0, Math.min(cards.length - 1, i));
    dots.forEach(function  (d, idx) { d.classList.toggle('on', idx === procIdx); });
    if (prevBtn) prevBtn.toggleAttribute('disabled', procIdx <= 0);
    if (nextBtn) nextBtn.toggleAttribute('disabled', procIdx >= cards.length - 1);
    if (cards[procIdx]) {
      var card = cards[procIdx];
      var railRect = rail.getBoundingClientRect();
      var cardRect = card.getBoundingClientRect();
      var offset   = cardRect.left - railRect.left + rail.scrollLeft - (rail.offsetWidth - card.offsetWidth) / 2;
      rail.scrollTo({ left: offset, behavior: 'smooth' });
    }
  }

  if (prevBtn) prevBtn.addEventListener('click', function () { goProc(procIdx - 1); });
  if (nextBtn) nextBtn.addEventListener('click', function () { goProc(procIdx + 1); });

  // swipe support
  if (rail) {
    var startX = 0;
    rail.addEventListener('touchstart', function (e) { startX = e.touches[0].clientX; }, { passive: true });
    rail.addEventListener('touchend',   function (e) {
      var dx = e.changedTouches[0].clientX - startX;
      if (Math.abs(dx) > 50) goProc(procIdx + (dx < 0 ? 1 : -1));
    }, { passive: true });

    // dot click
    dots.forEach(function (d, i) { d.addEventListener('click', function () { goProc(i); }); });

    // sync dots when user natively scrolls the rail (trackpad / mouse wheel)
    var scrollSyncTimer;
    rail.addEventListener('scroll', function () {
      clearTimeout(scrollSyncTimer);
      scrollSyncTimer = setTimeout(function () {
        var atEnd   = rail.scrollLeft + rail.clientWidth >= rail.scrollWidth - 4;
        var atStart = rail.scrollLeft <= 4;
        var closest;
        if (atEnd) {
          closest = cards.length - 1;
        } else if (atStart) {
          closest = 0;
        } else {
          var railMid = rail.scrollLeft + rail.offsetWidth / 2;
          closest = 0;
          var closestDist = Infinity;
          cards.forEach(function (card, i) {
            var dist = Math.abs((card.offsetLeft + card.offsetWidth / 2) - railMid);
            if (dist < closestDist) { closestDist = dist; closest = i; }
          });
        }
        if (closest !== procIdx) {
          procIdx = closest;
          dots.forEach(function (d, idx) { d.classList.toggle('on', idx === procIdx); });
          if (prevBtn) prevBtn.toggleAttribute('disabled', procIdx <= 0);
          if (nextBtn) nextBtn.toggleAttribute('disabled', procIdx >= cards.length - 1);
        }
      }, 80);
    }, { passive: true });

    goProc(0);
  }

  /* ── 7. Services stacked cards — sticky scroll ───────────── */
  var stackSection = document.querySelector('.section-services');
  if (stackSection) {
    var stackCards = Array.from(stackSection.querySelectorAll('.service-card'));
    var stackCount = stackCards.length;
    stackCards.forEach(function (card, i) {
      card.style.setProperty('--stack-i', i);
      card.style.setProperty('--stack-n', stackCount);
    });

    var stackObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var card = entry.target;
        card.classList.toggle('in-view', entry.isIntersecting);
      });
    }, { threshold: 0.25 });
    stackCards.forEach(function (c) { stackObserver.observe(c); });
  }

  /* ── 8. FAQ accordion ────────────────────────────────────── */
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var expanded = btn.getAttribute('aria-expanded') === 'true';
      // close others
      document.querySelectorAll('.faq-q[aria-expanded="true"]').forEach(function (b) {
        if (b !== btn) {
          b.setAttribute('aria-expanded', 'false');
          b.parentElement.classList.remove('open');
        }
      });
      btn.setAttribute('aria-expanded', String(!expanded));
      btn.parentElement.classList.toggle('open', !expanded);
    });
  });

  /* ── 9. vCard download ───────────────────────────────────── */
  var vcardContent = [
    'BEGIN:VCARD',
    'VERSION:3.0',
    'FN:Digital Dreamsbox',
    'ORG:Digital Dreamsbox',
    'TEL;TYPE=CELL:+33688848145',
    'EMAIL:contact@digitaldreamsbox.com',
    'URL:https://digitaldreamsbox.com',
    'ADR;TYPE=WORK:;;Sarrebourg;;57400;;FR',
    'NOTE:Agence web & branding — Moselle · Grand Est',
    'END:VCARD'
  ].join('\r\n');

  document.querySelectorAll('[data-vcard]').forEach(function (el) {
    el.addEventListener('click', function (e) {
      e.preventDefault();
      var blob = new Blob([vcardContent], { type: 'text/vcard' });
      var url  = URL.createObjectURL(blob);
      var a    = document.createElement('a');
      a.href     = url;
      a.download = 'digital-dreamsbox.vcf';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    });
  });

  /* ── 10. Cookie consent ──────────────────────────────────── */
  var cookieBanner = document.querySelector('.cookies');
  if (cookieBanner) {
    var saved = localStorage.getItem('ddb-cookies');
    if (saved) {
      cookieBanner.classList.add('hidden');
    } else {
      setTimeout(function () { cookieBanner.classList.add('show'); }, 1800);
    }
    cookieBanner.querySelector('.accept').addEventListener('click', function () {
      localStorage.setItem('ddb-cookies', 'accepted');
      cookieBanner.classList.remove('show');
      cookieBanner.classList.add('hidden');
    });
    cookieBanner.querySelector('.reject').addEventListener('click', function () {
      localStorage.setItem('ddb-cookies', 'rejected');
      cookieBanner.classList.remove('show');
      cookieBanner.classList.add('hidden');
    });
  }

  /* ── 11. Contact form (Formspree endpoint — à configurer) ─── */
  var form    = document.getElementById('contact-form');
  var success = form && form.querySelector('.form-success');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // Honeypot check
      if (form.querySelector('[name="website"]').value) return;

      // Basic validation
      var valid = true;
      form.querySelectorAll('[required]').forEach(function (field) {
        if (!field.value.trim()) {
          field.classList.add('error');
          valid = false;
        } else {
          field.classList.remove('error');
        }
      });
      if (!valid) return;

      var submit = form.querySelector('[type="submit"]');
      submit.disabled = true;
      submit.textContent = 'Envoi…';

      // Replace 'YOUR_FORM_ID' with actual Formspree form ID after setup
      var endpoint = form.getAttribute('action') || 'https://formspree.io/f/YOUR_FORM_ID';
      var data     = new FormData(form);

      fetch(endpoint, {
        method:  'POST',
        body:    data,
        headers: { 'Accept': 'application/json' }
      })
      .then(function (r) { return r.json(); })
      .then(function () {
        form.reset();
        if (success) success.classList.add('visible');
        submit.disabled    = false;
        submit.textContent = 'Envoyer';
      })
      .catch(function () {
        submit.disabled    = false;
        submit.textContent = 'Envoyer';
        alert('Erreur réseau. Réessayez ou appelez-nous directement.');
      });
    });

    // Remove error state on input
    form.querySelectorAll('[required]').forEach(function (field) {
      field.addEventListener('input', function () { field.classList.remove('error'); });
    });
  }

  /* ── 12. Ticker animation (CSS handles it, JS adds pause on hover) ── */
  var ticker = document.querySelector('.ticker-track');
  if (ticker) {
    ticker.addEventListener('mouseenter', function () { ticker.style.animationPlayState = 'paused'; });
    ticker.addEventListener('mouseleave', function () { ticker.style.animationPlayState = 'running'; });
  }

})();
