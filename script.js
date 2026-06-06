/* ============================================================
   Digital Dreamsbox — script.js
   Interactions : reveal · nav · process · FAQ · vCard · magnet · cookies · form
   ============================================================ */

(function () {
  'use strict';

  /* ── 0. Animated blob background + scroll-speed acceleration ─ */
  (function () {
    /* Inject 3 blobs grands uniquement */
    var wrap = document.createElement('div');
    wrap.id = 'bg-blobs';
    for (var i = 1; i <= 3; i++) {
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
        var delay = parseFloat(getComputedStyle(el).getPropertyValue('--rd') || '0');
        setTimeout(function () { el.classList.add('in'); }, delay);
        revealObserver.unobserve(el);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach(function (el) {
    revealObserver.observe(el);
  });

  /* ── 3. Header scroll state ──────────────────────────────── */
  var header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', function () {
      var y = window.scrollY;
      if (y > 80) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
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
    'PHOTO;ENCODING=b;TYPE=JPEG:/9j/4AAQSkZJRgABAQABIAEgAAD/4QCARXhpZgAATU0AKgAAAAgABAEaAAUAAAABAAAAPgEbAA',
    ' UAAAABAAAARgEoAAMAAAABAAIAAIdpAAQAAAABAAAATgAAAAAAAAEgAAAAAQAAASAAAAABAAOg',
    ' AQADAAAAAQABAACgAgAEAAAAAQAAAMigAwAEAAAAAQAAAMgAAAAA/+0AOFBob3Rvc2hvcCAzLj',
    ' AAOEJJTQQEAAAAAAAAOEJJTQQlAAAAAAAQ1B2M2Y8AsgTpgAmY7PhCfv/AABEIAMgAyAMBIgAC',
    ' EQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBA',
    ' AAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1',
    ' Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoq',
    ' OkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/',
    ' xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQ',
    ' IDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6',
    ' Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpq',
    ' eoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2wBDAAIC',
    ' AgICAgMCAgMFAwMDBQYFBQUFBggGBgYGBggKCAgICAgICgoKCgoKCgoMDAwMDAwODg4ODg8PDw',
    ' 8PDw8PDw//2wBDAQICAgQEBAcEBAcQCwkLEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQ',
    ' EBAQEBAQEBAQEBAQEBAQEBAQEBD/3QAEAA3/2gAMAwEAAhEDEQA/AP38ooooAKKKKACiiigAoo',
    ' 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',
    ' iigAooooAKKKKACiiigAooooAKKKKAP/2Q==',
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
        if (success) success.classList.add('show');
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

/* ── Page transition ─────────────────────────────────────── */
(function () {
  var STAR_URLS  = [
    'data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTAwIDEwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImciIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPjxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMzQjgyRjYiLz48c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMwMEQ0RDQiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48cGF0aCBkPSJNNTAgMEM1MiAyNSA3NSA0OCAxMDAgNTBDNzUgNTIgNTIgNzUgNTAgMTAwQzQ4IDc1IDI1IDUyIDAgNTBDMjUgNDggNDggMjUgNTAgMFoiIGZpbGw9InVybCgjZykiLz48L3N2Zz4=',
    'data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTAwIDEwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNNTAgMEM1MiAyNSA3NSA0OCAxMDAgNTBDNzUgNTIgNTIgNzUgNTAgMTAwQzQ4IDc1IDI1IDUyIDAgNTBDMjUgNDggNDggMjUgNTAgMFoiIGZpbGw9IiMwMEQ0RDQiLz48L3N2Zz4=',
    'data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTAwIDEwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNNTAgMEM1MiAyNSA3NSA0OCAxMDAgNTBDNzUgNTIgNTIgNzUgNTAgMTAwQzQ4IDc1IDI1IDUyIDAgNTBDMjUgNDggNDggMjUgNTAgMFoiIGZpbGw9IiMxRDlFRTkiLz48L3N2Zz4=',
    'data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTAwIDEwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNNTAgMEM1MiAyNSA3NSA0OCAxMDAgNTBDNzUgNTIgNTIgNzUgNTAgMTAwQzQ4IDc1IDI1IDUyIDAgNTBDMjUgNDggNDggMjUgNTAgMFoiIGZpbGw9IiMzQjVCREIiLz48L3N2Zz4='
  ];
  var STAR_COUNT = 26;
  var SWEEP_MS   = 680;
  var FADE_IN    = 460;
  var FADE_OUT   = 420;
  var running    = false;

  function spawnStars() {
    for (var i = 0; i < STAR_COUNT; i++) {
      (function (i) {
        var delay = (i / STAR_COUNT) * SWEEP_MS * 0.92;
        setTimeout(function () {
          var el = document.createElement('img');
          el.src = STAR_URLS[i % 4];
          el.classList.add('pt-star');
          var size   = 10 + Math.random() * 18;
          var startX = window.innerWidth + size + 5;
          var startY = Math.random() * (window.innerHeight - size);
          var rot    = Math.random() * 50 - 25;
          var tx     = -(window.innerWidth + size * 2 + Math.random() * 60);
          var ty     = window.innerHeight * (0.02 + Math.random() * 0.09);
          var dur    = 350 + Math.random() * 250;
          el.style.cssText = 'left:' + startX + 'px;top:' + startY + 'px;width:' + size + 'px;height:' + size + 'px;transform:rotate(' + rot + 'deg);';
          document.body.appendChild(el);
          requestAnimationFrame(function () {
            requestAnimationFrame(function () {
              el.style.transition = 'transform ' + dur + 'ms cubic-bezier(0.3,0.1,0.4,1),opacity ' + (dur * 0.7) + 'ms ease';
              el.style.opacity    = '1';
              el.style.transform  = 'translate(' + tx + 'px,' + ty + 'px) rotate(' + (rot + Math.random() * 24 - 12) + 'deg)';
              setTimeout(function () {
                el.style.opacity = '0';
                setTimeout(function () { el.remove(); }, 350);
              }, dur * 0.62);
            });
          });
        }, delay);
      })(i);
    }
  }

  function canTransition(link) {
    var href = link.getAttribute('href');
    if (!href) return false;
    if (href.indexOf('http') === 0 || href.indexOf('mailto') === 0 || href.indexOf('tel') === 0 || href.indexOf('#') === 0 || link.target === '_blank') return false;
    return true;
  }

  /* ── Départ : overlay monte + étoiles ── */
  document.addEventListener('click', function (e) {
    var link = e.target.closest('a');
    if (!link || !canTransition(link)) return;
    e.preventDefault();
    if (running) { window.location.href = link.href; return; }
    running = true;
    var ov = document.getElementById('pt-overlay');
    ov.style.transition    = 'opacity ' + FADE_IN + 'ms ease-in';
    ov.style.opacity       = '1';
    ov.style.pointerEvents = 'all';
    spawnStars();
    setTimeout(function () {
      sessionStorage.setItem('pt', '1');
      window.location.href = link.href;
    }, FADE_IN + 40);
  });

  /* ── Arrivée : overlay redescend ── */
  window.addEventListener('load', function () {
    if (!sessionStorage.getItem('pt')) return;
    sessionStorage.removeItem('pt');
    var ov = document.getElementById('pt-overlay');
    ov.style.transition = 'none';
    ov.style.opacity    = '1';
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        ov.style.transition    = 'opacity ' + FADE_OUT + 'ms ease-out';
        ov.style.opacity       = '0';
        ov.style.pointerEvents = 'none';
        setTimeout(function () {
          ov.style.transition = '';
          running = false;
        }, FADE_OUT + 50);
      });
    });
  });

})();
