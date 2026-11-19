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

// Projects dropdown: hover on desktop; on touch screens the first tap opens it, a tap outside closes it
(function () {
  var dd = document.querySelector('.nav-dd');
  if (!dd) return;
  var trigger = dd.querySelector('.dd-trigger');
  var touch = window.matchMedia('(hover: none)').matches;
  function set(open) { dd.classList.toggle('open', open); trigger.setAttribute('aria-expanded', open ? 'true' : 'false'); }
  trigger.addEventListener('click', function (e) {
    if (touch && !dd.classList.contains('open')) { e.preventDefault(); set(true); }
    else set(false);
  });
  document.addEventListener('click', function (e) { if (!dd.contains(e.target)) set(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
  dd.addEventListener('mouseleave', function () { set(false); });
})();

// Case studies: section navigator (left rail, wide screens only)
(function () {
  document.querySelectorAll('.toc').forEach(function (n) { n.remove(); });
  if (window.__tocScroll) { window.removeEventListener('scroll', window.__tocScroll); window.removeEventListener('resize', window.__tocScroll); }
  var story = document.querySelector('.story');
  var head = document.querySelector('.cs-head');
  if (!story || !head) return;
  var sections = [{ el: head, label: 'Overview' }];
  story.querySelectorAll('.chapter:not(.sub)').forEach(function (ch) {
    var pill = ch.querySelector('.pill');
    if (!pill) return;
    var label = pill.cloneNode(true); var n = label.querySelector('.n'); if (n) n.remove();
    sections.push({ el: ch, label: label.textContent.trim() });
  });
  // a section runs until the next one starts (sub-chapters belong to the chapter before them)
  var rail = document.createElement('nav');
  rail.className = 'toc'; rail.setAttribute('aria-label', 'Sections');
  sections.forEach(function (s, i) {
    if (!s.el.id) s.el.id = 'sec-' + i;
    var a = document.createElement('a');
    a.href = '#' + s.el.id;
    a.innerHTML = '<span class="ln"><i></i></span><span class="lb">' + s.label + '</span>';
    a.addEventListener('click', function (e) { e.preventDefault(); s.el.scrollIntoView({ behavior: 'smooth', block: 'start' }); });
    rail.appendChild(a); s.a = a; s.fill = a.querySelector('.ln i');
  });
  document.body.appendChild(rail);
  var foot = document.querySelector('.site-foot'), ticking = false;
  function top(el) { return el.getBoundingClientRect().top + window.scrollY; }
  function update() {
    ticking = false;
    var y = window.scrollY + window.innerHeight * 0.35, end = foot ? top(foot) : document.body.scrollHeight;
    var active = 0;
    sections.forEach(function (s, i) { if (top(s.el) <= y) active = i; });
    sections.forEach(function (s, i) {
      var start = top(s.el), stop = i + 1 < sections.length ? top(sections[i + 1].el) : end;
      var p = i < active ? 1 : i > active ? 0 : Math.min(1, Math.max(0, (y - start) / (stop - start)));
      s.fill.style.transform = 'scaleX(' + p + ')';
      s.a.classList.toggle('on', i === active);
    });
    var footVisible = foot && foot.getBoundingClientRect().top < window.innerHeight * 0.85;
    rail.classList.toggle('show', window.scrollY > 120 && !footVisible);
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(update); } }
  window.__tocScroll = onScroll;
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  update();
})();

// User-flow diagrams: wider than the frame; on desktop the view follows the mouse, on touch it scrolls
(function () {
  document.querySelectorAll('.flow').forEach(function (fig) {
    var box = fig.querySelector('.flow-scroll');
    if (!box) return;
    var target = 0, raf = null;
    function edges() {
      var max = box.scrollWidth - box.clientWidth;
      box.style.setProperty('--fl', box.scrollLeft > 4 ? '48px' : '0px');
      box.style.setProperty('--fr', box.scrollLeft < max - 4 ? '48px' : '0px');
    }
    function step() {
      var d = target - box.scrollLeft;
      if (Math.abs(d) < 0.5) { box.scrollLeft = target; raf = null; edges(); return; }
      box.scrollLeft += d * 0.12; edges();
      raf = requestAnimationFrame(step);
    }
    box.addEventListener('mousemove', function (e) {
      var r = box.getBoundingClientRect();
      var p = Math.min(1, Math.max(0, (e.clientX - r.left - r.width * 0.1) / (r.width * 0.8)));
      target = p * (box.scrollWidth - box.clientWidth);
      fig.classList.add('explored');
      if (!raf) raf = requestAnimationFrame(step);
    });
    box.addEventListener('scroll', function () { edges(); if (box.scrollLeft > 10) fig.classList.add('explored'); }, { passive: true });
    window.addEventListener('resize', edges);
    edges();
  });
})();

// Click-to-enlarge for case-study screens
(function () {
  var imgs = document.querySelectorAll('.feature-shots img');
  if (!imgs.length) return;
  var box = null, last = null;
  function close() {
    if (!box) return;
    box.classList.remove('open');
    var b = box; box = null;
    setTimeout(function () { b.remove(); }, 250);
    document.removeEventListener('keydown', onKey);
    if (last) last.focus();
  }
  function onKey(e) { if (e.key === 'Escape') close(); }
  function open(img) {
    last = img;
    box = document.createElement('div');
    box.className = 'lightbox'; box.setAttribute('role', 'dialog'); box.setAttribute('aria-modal', 'true'); box.setAttribute('aria-label', img.alt || 'Screen');
    box.innerHTML = '<img alt=""><button class="lightbox-close" aria-label="Close">×</button><p class="lightbox-cap"></p>';
    box.querySelector('img').src = img.dataset.full || img.currentSrc || img.src;
    box.querySelector('img').alt = img.alt;
    box.querySelector('.lightbox-cap').textContent = img.alt;
    box.addEventListener('click', close);
    document.body.appendChild(box);
    requestAnimationFrame(function () { box.classList.add('open'); });
    box.querySelector('.lightbox-close').focus();
    document.addEventListener('keydown', onKey);
  }
  imgs.forEach(function (img) {
    img.classList.add('zoomable'); img.tabIndex = 0; img.setAttribute('role', 'button');
    img.addEventListener('click', function () { open(img); });
    img.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(img); } });
  });
})();

/* home: hello popup, once per visit */
(function () {
  var pop = document.getElementById('hello-pop');
  if (!pop || window.matchMedia('(max-width: 760px)').matches) return;
  var KEY = 'helloPopSeen', seen = false;
  try { seen = sessionStorage.getItem(KEY) === '1'; } catch (e) {}
  if (seen) return;
  function close() {
    pop.classList.remove('open');
    try { sessionStorage.setItem(KEY, '1'); } catch (e) {}
    setTimeout(function () { pop.hidden = true; }, 400);
    document.removeEventListener('keydown', onKey);
  }
  function onKey(e) { if (e.key === 'Escape') close(); }
  setTimeout(function () {
    pop.hidden = false;
    requestAnimationFrame(function () { requestAnimationFrame(function () { pop.classList.add('open'); }); });
    document.addEventListener('keydown', onKey);
  }, 2500);
  pop.querySelector('.hello-close').addEventListener('click', close);
  pop.querySelector('.hello-cta').addEventListener('click', close);
})();
