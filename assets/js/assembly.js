/* Homepage: scroll takes the Fabry-Pérot interferometer apart, from the
   assembled part to the exploded view. Without JavaScript the assembled still
   stays; with reduced motion the page shows the exploded still instead, and
   every step of the chain is shown at full strength either way. */
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

  // Frames run exploded (00) to assembled (last); the scroll plays them backwards
  var count = parseInt(section.getAttribute("data-frames"), 10);
  var last = count - 1;
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
    // Stacked layout: come apart over the first half screen of scrolling
    return Math.min(1, Math.max(0, window.pageYOffset / (vh * 0.45)));
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
    // hold the assembled part for a moment, then take it apart
    var q = Math.min(1, Math.max(0, (p - 0.04) / 0.9));
    var i = Math.round((1 - q) * last);
    var img = nearestLoaded(i);
    if (img && img.index !== current) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      current = img.index;
    }
    // The assembled part starts scaled up to hold the stage and settles back
    // to full-frame size as the pieces spread out (matches the still's CSS)
    var t = Math.min(1, Math.max(0, (0.45 - q) / 0.45));
    var e = t * t * (3 - 2 * t);
    canvas.style.transform = "translate(" + (6 * e).toFixed(3) + "%, " + (10 * e).toFixed(3) + "%) scale(" + (1 + 0.6 * e).toFixed(4) + ")";
    bar.style.transform = "scaleX(" + p.toFixed(4) + ")";
    for (var k = 0; k < steps.length; k++) {
      steps[k].classList.toggle("is-lit", p >= k / steps.length - 0.001);
    }
    section.classList.toggle("is-done", p > 0.98);
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

  // The last frame is the still already on the page; fetch the rest from the
  // assembled end outwards, a few at a time
  function start() {
    still.index = last;
    still.ready = true;
    frames[last] = still;
    section.classList.add("is-live");
    request();
    var next = last - 1;
    function pump() { if (next >= 0) load(next--, pump); }
    pump(); pump(); pump();
  }

  if (still.complete && still.naturalWidth) start();
  else still.addEventListener("load", start);

  window.addEventListener("scroll", request, { passive: true });
  window.addEventListener("resize", request);
})();
