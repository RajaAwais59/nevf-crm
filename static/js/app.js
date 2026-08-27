function openModal(id) {
  document.getElementById(id).classList.add("show");
}
function closeModal(id) {
  document.getElementById(id).classList.remove("show");
}
document.addEventListener("click", function (e) {
  if (e.target.classList && e.target.classList.contains("overlay")) {
    e.target.classList.remove("show");
  }
});

function showTab(groupId, tabName, btn) {
  const group = document.getElementById(groupId);
  group.querySelectorAll(".tab").forEach((t) => t.classList.remove("active"));
  group.querySelectorAll(".tab-panel").forEach((p) => p.classList.remove("active"));
  btn.classList.add("active");
  document.getElementById(tabName).classList.add("active");
}

function filterTable(inputEl, tableBodyId) {
  const q = inputEl.value.toLowerCase();
  const rows = document.querySelectorAll("#" + tableBodyId + " tr");
  rows.forEach((row) => {
    row.style.display = row.innerText.toLowerCase().includes(q) ? "" : "none";
  });
}

// Count-up animation for dashboard/stat numbers
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".count-up").forEach(function (el) {
    const target = parseInt(el.getAttribute("data-target")) || 0;
    const duration = 800;
    const startTime = performance.now();

    function tick(now) {
      const progress = Math.min((now - startTime) / duration, 1);
      const value = Math.floor(progress * target);
      el.textContent = value.toLocaleString();
      if (progress < 1) {
        requestAnimationFrame(tick);
      } else {
        el.textContent = target.toLocaleString();
      }
    }
    requestAnimationFrame(tick);
  });
});

// Global search — live dropdown as you type
let searchTimer;
document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.querySelector(".search-box");
  const resultsBox = document.getElementById("searchResults");
  if (!searchInput || !resultsBox) return;

  searchInput.addEventListener("input", function () {
    clearTimeout(searchTimer);
    const q = this.value.trim();
    if (q.length < 2) {
      resultsBox.innerHTML = "";
      resultsBox.classList.remove("show");
      return;
    }
    searchTimer = setTimeout(function () {
      fetch("/search?q=" + encodeURIComponent(q))
        .then((r) => r.json())
        .then((data) => {
          if (!data.results.length) {
            resultsBox.innerHTML = '<div class="search-empty">No matches found.</div>';
          } else {
            resultsBox.innerHTML = data.results
              .map(function (r) {
                return (
                  '<a class="search-result-item" href="' + r.url + '">' +
                  '<span class="search-result-type">' + r.type + "</span>" +
                  '<span class="search-result-label">' + r.label + "</span>" +
                  '<span class="search-result-sub">' + r.sub + "</span></a>"
                );
              })
              .join("");
          }
          resultsBox.classList.add("show");
        });
    }, 300);
  });

  document.addEventListener("click", function (e) {
    if (!e.target.closest(".search-wrap")) {
      resultsBox.classList.remove("show");
    }
  });
});