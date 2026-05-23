/* ============================================================
   Digital Dreamsbox — interactions (THÈME SOMBRE)
   ============================================================ */

const PHONE_DISPLAY = '06 88 84 81 45';
const PHONE_TEL = '+33688848145';

// ----- Header scroll -----
const header = document.querySelector('.site-header');
const onScroll = () => {
  if (window.scrollY > 12) header.classList.add('scrolled');
  else header.classList.remove('scrolled');
};
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// ----- Reveal on scroll -----
// Only gate visibility once JS is ready (defensive: if IO never fires, content stays visible).
document.documentElement.classList.add('js-ready');

const revealEls = document.querySelectorAll('.reveal');
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

revealEls.forEach((el) => io.observe(el));

// Safety net: if IO hasn't run within 1.6s, reveal everything.
setTimeout(() => {
  document.querySelectorAll('.reveal:not(.in)').forEach((el) => {
    const r = el.getBoundingClientRect();
    if (r.top < window.innerHeight) el.classList.add('in');
  });
}, 1600);

// ----- Magnetic buttons (subtle) -----
document.querySelectorAll('[data-magnet]').forEach((btn) => {
  const strength = 12;
  btn.addEventListener('mousemove', (e) => {
    const r = btn.getBoundingClientRect();
    const x = e.clientX - r.left - r.width / 2;
    const y = e.clientY - r.top - r.height / 2;
    btn.style.transform = `translate(${(x / r.width) * strength}px, ${(y / r.height) * strength}px)`;
  });
  btn.addEventListener('mouseleave', () => {
    btn.style.transform = '';
  });
});

/* ============================================================
   PROCESS — free horizontal scroll
   - mouse drag
   - vertical wheel converted to horizontal scroll WHEN HOVERING
     (but only consumes scroll if there is room to scroll horizontally,
      otherwise lets the page scroll vertically — no hijacking)
   - prev/next buttons
   - active card = closest to viewport center
============================================================ */
const procRail = document.querySelector('.process-rail');
const procCards = procRail ? Array.from(procRail.children) : [];
const procDots = document.querySelectorAll('.process-progress .pdot');
const procPrev = document.querySelector('[data-proc-prev]');
const procNext = document.querySelector('[data-proc-next]');

function updateProcessActive() {
  if (!procRail) return;
  const railRect = procRail.getBoundingClientRect();
  const center = railRect.left + railRect.width / 2;
  let activeIdx = 0;
  let bestDist = Infinity;
  procCards.forEach((card, i) => {
    const r = card.getBoundingClientRect();
    const c = r.left + r.width / 2;
    const d = Math.abs(c - center);
    if (d < bestDist) { bestDist = d; activeIdx = i; }
  });
  procCards.forEach((c, i) => c.classList.toggle('is-active', i === activeIdx));
  procDots.forEach((d, i) => d.classList.toggle('on', i === activeIdx));

  if (procPrev && procNext) {
    procPrev.disabled = procRail.scrollLeft <= 2;
    procNext.disabled = procRail.scrollLeft + procRail.clientWidth >= procRail.scrollWidth - 2;
  }
}

if (procRail) {
  // -- drag to scroll --
  let isDown = false, startX = 0, startScroll = 0, hasMoved = false;
  procRail.addEventListener('pointerdown', (e) => {
    isDown = true; hasMoved = false;
    startX = e.clientX;
    startScroll = procRail.scrollLeft;
    procRail.classList.add('is-grabbing');
    procRail.setPointerCapture(e.pointerId);
  });
  procRail.addEventListener('pointermove', (e) => {
    if (!isDown) return;
    const dx = e.clientX - startX;
    if (Math.abs(dx) > 4) hasMoved = true;
    procRail.scrollLeft = startScroll - dx;
  });
  const endDrag = (e) => {
    if (!isDown) return;
    isDown = false;
    procRail.classList.remove('is-grabbing');
    if (e && e.pointerId !== undefined) {
      try { procRail.releasePointerCapture(e.pointerId); } catch(_) {}
    }
    // snap to nearest card center
    snapToNearest();
  };
  procRail.addEventListener('pointerup', endDrag);
  procRail.addEventListener('pointercancel', endDrag);
  procRail.addEventListener('pointerleave', () => { if (isDown) endDrag(); });

  // prevent click after drag
  procRail.addEventListener('click', (e) => {
    if (hasMoved) { e.preventDefault(); e.stopPropagation(); }
  }, true);

  // -- vertical wheel → horizontal --
  // Only consumes wheel if rail has remaining horizontal room in scroll direction.
  // Otherwise the page scrolls normally (no hijacking).
  procRail.addEventListener('wheel', (e) => {
    // ignore horizontal trackpad swipes — let native handle
    if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) return;

    const goingRight = e.deltaY > 0;
    const max = procRail.scrollWidth - procRail.clientWidth;
    const cur = procRail.scrollLeft;
    const hasRoom = goingRight ? cur < max - 1 : cur > 1;
    if (!hasRoom) return; // let page scroll
    e.preventDefault();
    procRail.scrollLeft = cur + e.deltaY;
  }, { passive: false });

  procRail.addEventListener('scroll', () => {
    requestAnimationFrame(updateProcessActive);
  }, { passive: true });

  function snapToNearest() {
    const railRect = procRail.getBoundingClientRect();
    const center = railRect.left + railRect.width / 2;
    let bestCard = null;
    let bestDist = Infinity;
    procCards.forEach((card) => {
      const r = card.getBoundingClientRect();
      const c = r.left + r.width / 2;
      const d = Math.abs(c - center);
      if (d < bestDist) { bestDist = d; bestCard = card; }
    });
    if (bestCard) {
      const r = bestCard.getBoundingClientRect();
      const offset = (r.left + r.width / 2) - center;
      procRail.scrollTo({ left: procRail.scrollLeft + offset, behavior: 'smooth' });
    }
  }

  function scrollByCard(dir) {
    const railRect = procRail.getBoundingClientRect();
    const center = railRect.left + railRect.width / 2;
    let activeIdx = 0;
    let bestDist = Infinity;
    procCards.forEach((card, i) => {
      const r = card.getBoundingClientRect();
      const c = r.left + r.width / 2;
      const d = Math.abs(c - center);
      if (d < bestDist) { bestDist = d; activeIdx = i; }
    });
    const targetIdx = Math.min(procCards.length - 1, Math.max(0, activeIdx + dir));
    const target = procCards[targetIdx];
    if (!target) return;
    const r = target.getBoundingClientRect();
    const offset = (r.left + r.width / 2) - center;
    procRail.scrollTo({ left: procRail.scrollLeft + offset, behavior: 'smooth' });
  }
  procPrev && procPrev.addEventListener('click', () => scrollByCard(-1));
  procNext && procNext.addEventListener('click', () => scrollByCard(1));

  // initial active state
  requestAnimationFrame(updateProcessActive);
  window.addEventListener('resize', updateProcessActive);
}

// ----- FAQ accordion -----
document.querySelectorAll('.faq-item').forEach((item) => {
  const q = item.querySelector('.faq-q');
  const a = item.querySelector('.faq-a');
  const inner = item.querySelector('.faq-a-inner');
  q.addEventListener('click', () => {
    const open = item.classList.toggle('open');
    q.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) {
      a.style.maxHeight = inner.offsetHeight + 'px';
    } else {
      a.style.maxHeight = '0px';
    }
  });
});

// ----- vCard download -----
function buildVCard() {
  const lines = [
    'BEGIN:VCARD',
    'VERSION:3.0',
    'N:Digital Dreamsbox;;;;',
    'FN:Digital Dreamsbox',
    'ORG:Digital Dreamsbox',
    'TITLE:Agence de communication visuelle',
    'TEL;TYPE=CELL,VOICE:' + PHONE_TEL,
    'EMAIL;TYPE=WORK:contact@digitaldreamsbox.com',
    'ADR;TYPE=WORK:;;;Sarrebourg;Moselle;57400;France',
    'URL:https://digitaldreamsbox.com',
    'NOTE:Branding · Sites web · Google Ads · Signalétique. Sarrebourg, Moselle.',
    'END:VCARD'
  ];
  return lines.join('\r\n');
}
document.querySelectorAll('[data-vcard]').forEach((btn) => {
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    const blob = new Blob([buildVCard()], { type: 'text/vcard;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'Digital-Dreamsbox.vcf';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  });
});

// ----- Mobile nav -----
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
if (navToggle) {
  navToggle.addEventListener('click', () => {
    const open = navLinks.classList.toggle('mobile-open');
    navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}

// ----- Contact form (front-end demo) -----
const form = document.querySelector('#contact-form');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const hp = form.querySelector('[name="website"]');
    if (hp && hp.value) return;
    const success = document.querySelector('.form-success');
    if (success) {
      success.classList.add('show');
      form.reset();
      setTimeout(() => success.classList.remove('show'), 6000);
    }
  });
}

// ----- Cookies banner -----
const cookies = document.querySelector('.cookies');
const COOKIE_KEY = 'ddb_cookie_consent';
function showCookies() {
  if (!cookies) return;
  if (localStorage.getItem(COOKIE_KEY)) return;
  setTimeout(() => cookies.classList.add('show'), 1200);
}
function dismissCookies(val) {
  localStorage.setItem(COOKIE_KEY, val);
  cookies && cookies.classList.remove('show');
}
document.querySelector('.cookies .accept')?.addEventListener('click', () => dismissCookies('accept'));
document.querySelector('.cookies .reject')?.addEventListener('click', () => dismissCookies('reject'));
showCookies();

// ----- Year -----
const y = document.querySelector('[data-year]');
if (y) y.textContent = new Date().getFullYear();
