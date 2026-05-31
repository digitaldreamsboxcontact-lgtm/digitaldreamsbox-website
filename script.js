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

  /* ── 4. Mobile nav toggle ─────────────────────────────────── */
  var navToggle = document.querySelector('.nav-toggle');
  var navLinks  = document.querySelector('.nav-links');
  var navCta    = document.querySelector('.nav-cta');
  if (navToggle) {
    navToggle.addEventListener('click', function () {
      var open = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!open));
      if (navLinks) navLinks.classList.toggle('open', !open);
      if (navCta)   navCta.classList.toggle('open', !open);
      document.body.classList.toggle('nav-open', !open);
    });
    // close on link click
    document.querySelectorAll('.nav-links a, .nav-cta a').forEach(function (a) {
      a.addEventListener('click', function () {
        navToggle.setAttribute('aria-expanded', 'false');
        if (navLinks) navLinks.classList.remove('open');
        if (navCta)   navCta.classList.remove('open');
        document.body.classList.remove('nav-open');
      });
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
    cards.forEach(function (c, idx) { c.classList.toggle('is-active', idx === procIdx); });
    dots.forEach(function  (d, idx) { d.classList.toggle('on',        idx === procIdx); });
    if (prevBtn) prevBtn.toggleAttribute('disabled', procIdx <= 0);
    if (nextBtn) nextBtn.toggleAttribute('disabled', procIdx >= cards.length - 1);
    // scroll card into view inside the rail
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
