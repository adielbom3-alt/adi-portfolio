// Reveal sections as they scroll into view
(function () {
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) { els.forEach(function (e) { e.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
  els.forEach(function (e) { io.observe(e); });
})();

// Floating "Scroll to explore" button: fades out gradually as the visitor scrolls
// (and fades back in if they return to the top); disappears for good once clicked.
(function () {
  var b = document.getElementById('scrollBtn');
  if (!b) return;
  var FADE = 450; // pixels of scrolling to fade out completely
  var clicked = false, ticking = false;
  function update() {
    ticking = false;
    if (clicked) return;
    var o = Math.max(0, 1 - window.scrollY / FADE);
    b.style.opacity = o;
    b.style.pointerEvents = o < 0.1 ? 'none' : '';
    b.style.visibility = o === 0 ? 'hidden' : '';
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(update); } }
  b.addEventListener('click', function (e) {
    e.preventDefault();
    clicked = true;
    window.removeEventListener('scroll', onScroll);
    var w = document.getElementById('work');
    if (w) w.scrollIntoView({ behavior: 'smooth' });
    b.classList.add('gone');
    setTimeout(function () { b.remove(); }, 400);
  });
  window.addEventListener('scroll', onScroll, { passive: true });
  update();
})();

// Live Tel Aviv clock in the footer: time and an icon by time of day
(function () {
  var el = document.getElementById('clock');
  if (!el) return;
  var hh = el.querySelector('.hh'), mm = el.querySelector('.mm');
  var fmt;
  try { fmt = new Intl.DateTimeFormat('en-GB', { timeZone: 'Asia/Jerusalem', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' }); }
  catch (e) { return; }
  function tick() {
    var parts = {}; fmt.formatToParts(new Date()).forEach(function (p) { parts[p.type] = p.value; });
    var h = parseInt(parts.hour, 10) % 24;
    hh.textContent = String(h).padStart(2, '0'); mm.textContent = parts.minute;
    var period = h >= 6 && h < 12 ? 'sunrise' : h >= 12 && h < 17 ? 'sun' : h >= 17 && h < 20 ? 'sunset' : 'moon';
    el.setAttribute('data-period', period);
  }
  tick();
  if (window.__clockTimer) clearInterval(window.__clockTimer);
  window.__clockTimer = setInterval(tick, 15000);
})();
