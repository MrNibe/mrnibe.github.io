/* Homepage: scroll scrubs the Fabry-Pérot assembly from exploded to assembled.
   Without JavaScript, or with reduced motion, the still exploded frame stays
   and every step of the chain is shown at full strength. */
(function () {
  var section = document.querySelector(".assembly");
  if (!section) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  var canvas = section.querySelector(".assembly__canvas");
  var still = section.querySelector(".assembly__still");
  var bar = section.querySelector(".assembly__progress span");
  var steps = section.querySelectorAll(".assembly__chain li");
  var ctx = canvas.getContext && canvas.getContext("2d");
  if (!ctx) return;

  var count = parseInt(section.getAttribute("data-frames"), 10);
  var src = section.getAttribute("data-src");
  var frames = new Array(count);
  var pinned = window.matchMedia("(min-width: 1024px)");
  var current = -1;
  var queued = false;

  function pad(n) { return n < 10 ? "0" + n : "" + n; }

  function progress() {
    var vh = window.innerHeight;
    if (pinned.matches) {
      var r = section.getBoundingClientRect();
      var travel = r.height - vh;
      return travel > 0 ? Math.min(1, Math.max(0, -r.top / travel)) : 0;
    }
    // Stacked layout: start exploded at the top of the page and finish
    // assembling as the stage rises into the upper part of the viewport
    var s = canvas.getBoundingClientRect();
    var mid = s.top + s.height / 2 + window.pageYOffset;
    var travel = Math.max(mid - vh * 0.25, vh * 0.6);
    return Math.min(1, Math.max(0, window.pageYOffset / travel));
  }

  function nearestLoaded(i) {
    for (var d = 0; d < count; d++) {
      if (frames[i - d] && frames[i - d].ready) return frames[i - d];
      if (frames[i + d] && frames[i + d].ready) return frames[i + d];
    }
    return null;
  }

  function render() {
    queued = false;
    var p = progress();
    // hold the exploded view briefly, then assemble over the rest of the scroll
    var q = Math.min(1, Math.max(0, (p - 0.06) / 0.86));
    var i = Math.round(q * (count - 1));
    var img = nearestLoaded(i);
    if (img && img.index !== current) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      current = img.index;
    }
    // Close in on the assembled instrument over the last stretch, so the
    // finished part holds the stage instead of shrinking into it
    var t = Math.min(1, Math.max(0, (q - 0.55) / 0.45));
    var e = t * t * (3 - 2 * t);
    canvas.style.transform = "translate(" + (6 * e).toFixed(3) + "%, " + (10 * e).toFixed(3) + "%) scale(" + (1 + 0.6 * e).toFixed(4) + ")";
    bar.style.transform = "scaleX(" + p.toFixed(4) + ")";
    for (var k = 0; k < steps.length; k++) {
      steps[k].classList.toggle("is-lit", p >= k / steps.length - 0.001);
    }
    section.classList.toggle("is-assembled", p > 0.98);
  }

  function request() {
    if (!queued) { queued = true; window.requestAnimationFrame(render); }
  }

  function load(i, done) {
    var img = new Image();
    img.decoding = "async";
    img.index = i;
    img.onload = function () { img.ready = true; frames[i] = img; request(); done && done(); };
    img.onerror = function () { done && done(); };
    img.src = src + pad(i) + ".webp";
  }

  // Frame 0 is the still already on the page; fetch the rest in order, a few at a time
  function start() {
    still.index = 0;
    still.ready = true;
    frames[0] = still;
    section.classList.add("is-live");
    request();
    var next = 1;
    function pump() { if (next < count) load(next++, pump); }
    pump(); pump(); pump();
  }

  if (still.complete && still.naturalWidth) start();
  else still.addEventListener("load", start);

  window.addEventListener("scroll", request, { passive: true });
  window.addEventListener("resize", request);
})();
