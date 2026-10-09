// Builds mailto links at runtime so the address isn't sitting in the HTML for scrapers.
document.querySelectorAll(".js-email").forEach(function (a) {
  var addr = a.dataset.u + "@" + a.dataset.d;
  a.href = "mailto:" + addr;
});
