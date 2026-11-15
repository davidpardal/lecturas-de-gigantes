(function () {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  document.querySelectorAll(".front img").forEach(function (img) {
    const fail = function () { img.parentElement.classList.add("no-cover"); };
    img.addEventListener("error", fail);
    if (img.complete && img.naturalWidth < 2) fail();
  });

  document.querySelectorAll("[role='button'].book3d").forEach(function (book) {
    function toggle() {
      const open = book.classList.toggle("is-open");
      book.setAttribute("aria-pressed", open ? "true" : "false");
    }
    book.addEventListener("click", toggle);
    book.addEventListener("keydown", function (event) {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        toggle();
      }
    });
  });

  const scene = document.querySelector(".shelf-scene");
  const shelf = document.querySelector(".shelf");
  if (scene && shelf && !reduce && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    scene.addEventListener("pointermove", function (event) {
      const rect = scene.getBoundingClientRect();
      const x = (event.clientX - rect.left) / rect.width - 0.5;
      const y = (event.clientY - rect.top) / rect.height - 0.5;
      shelf.style.setProperty("--px", (-18 + x * 16).toFixed(2) + "deg");
      shelf.style.setProperty("--py", (8 + y * -10).toFixed(2) + "deg");
    });
  }

  const hero = document.querySelector(".hero");
  if (hero && !reduce) {
    window.addEventListener("scroll", function () {
      const y = Math.min(window.scrollY, 280);
      if (scene) scene.style.setProperty("--scroll", (y * 0.12).toFixed(1) + "px");
    }, { passive: true });
  }

  const dataNode = document.getElementById("catalog");
  const input = document.getElementById("q");
  if (dataNode && input) {
    const catalog = JSON.parse(dataNode.textContent);
    const results = document.getElementById("results");
    const cards = Array.from(document.querySelectorAll(".people [data-name]"));

    function norm(value) {
      return (value || "").toLocaleLowerCase("es").normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    }

    function render(query) {
      const q = norm(query.trim());
      if (!q) {
        results.hidden = true;
        results.innerHTML = "";
        cards.forEach(function (card) { card.hidden = false; });
        return;
      }
      cards.forEach(function (card) {
        const blob = norm(card.getAttribute("data-name") + " " + card.getAttribute("data-books"));
        card.hidden = !blob.includes(q);
      });
      const hits = catalog.filter(function (item) {
        return norm(item.title + " " + item.original + " " + item.author + " " + item.people).includes(q);
      });
      results.hidden = false;
      if (!hits.length && cards.every(function (card) { return card.hidden; })) {
        results.innerHTML = '<p class="empty">Ningún resultado para «' + escapeHtml(query.trim()) + "».</p>";
        return;
      }
      results.innerHTML = hits.slice(0, 12).map(function (item) {
        return '<a class="result" href="' + item.href + '"><span class="book3d sm" style="--spine:' + item.spine + '"><span class="book3d-box"><span class="face front no-cover"><span class="cloth"><span class="cloth-title">' + escapeHtml(item.title) + '</span></span></span><span class="face spine"><span>' + escapeHtml(item.title) + '</span></span><span class="face pages"></span><span class="face back"></span></span></span><span><strong>' + escapeHtml(item.title) + "</strong><br><span class=\"by\">" + escapeHtml(item.author) + " · " + escapeHtml(item.people) + "</span></span></a>";
      }).join("");
    }

    input.addEventListener("input", function () { render(input.value); });
    const params = new URLSearchParams(location.search);
    if (params.get("q")) {
      input.value = params.get("q");
      render(input.value);
    }
    const form = input.form;
    if (form) form.addEventListener("submit", function (event) { event.preventDefault(); render(input.value); });
  }

  /* La estantería en CSS es la escena principal: se ve sin WebGL y no tapa
     el texto. bootWebGL() queda en el archivo por si se quiere activar el
     lienzo; no se arranca solo porque los libros del fondo se montaban
     sobre la estantería. */

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, function (ch) {
      return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[ch];
    });
  }

  function bootWebGL() {
    const canvas = document.getElementById("hero-gl");
    if (!canvas || reduce) return;
    if (window.matchMedia("(max-width: 880px)").matches) return;
    let supported = false;
    try {
      const probe = document.createElement("canvas");
      supported = !!(probe.getContext("webgl2") || probe.getContext("webgl"));
    } catch (error) { supported = false; }
    if (!supported) return;
    const script = document.createElement("script");
    script.src = "https://cdn.jsdelivr.net/npm/three@0.160.1/build/three.min.js";
    script.async = true;
    script.onload = function () {
      try { startThree(canvas); }
      catch (error) { canvas.remove(); }
    };
    script.onerror = function () { canvas.remove(); };
    document.head.appendChild(script);
  }

  function startThree(canvas) {
    const THREE = window.THREE;
    if (!THREE) throw new Error("three");
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
    camera.position.set(0, 0.2, 7.2);
    const group = new THREE.Group();
    scene.add(group);
    scene.add(new THREE.AmbientLight(0xfff4e4, 0.85));
    const key = new THREE.DirectionalLight(0xffe0b8, 1.1);
    key.position.set(3, 4, 5);
    scene.add(key);

    const titles = Array.from(document.querySelectorAll(".hero .book3d")).slice(0, 6);
    const palette = [0x6e2e2a, 0x234237, 0x8a5a2b, 0x3d3a55, 0x7a3e2e, 0x1f3a4d];
    titles.forEach(function (node, index) {
      const title = node.getAttribute("data-title") || "Libro";
      const material = [
        new THREE.MeshStandardMaterial({ color: palette[index % palette.length], roughness: 0.72 }),
        new THREE.MeshStandardMaterial({ color: palette[index % palette.length], roughness: 0.72 }),
        new THREE.MeshStandardMaterial({ color: 0xe7dcc8, roughness: 0.9 }),
        new THREE.MeshStandardMaterial({ color: 0xe7dcc8, roughness: 0.9 }),
        new THREE.MeshStandardMaterial({ map: coverTexture(THREE, title, palette[index % palette.length]) }),
        new THREE.MeshStandardMaterial({ color: 0x2a211b, roughness: 0.8 })
      ];
      const mesh = new THREE.Mesh(new THREE.BoxGeometry(0.72, 1.12, 0.16), material);
      const angle = (index / Math.max(titles.length, 1)) * Math.PI * 2;
      mesh.position.set(Math.cos(angle) * 3.4, Math.sin(angle * 1.3) * 1.3, Math.sin(angle) * 1.6 - 2.4);
      mesh.rotation.y = -0.4 - index * 0.15;
      group.add(mesh);
    });

    function resize() {
      const width = canvas.clientWidth || canvas.parentElement.clientWidth;
      const height = canvas.clientHeight || canvas.parentElement.clientHeight;
      if (!width || !height) return;
      renderer.setSize(width, height, false);
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
    }
    resize();
    window.addEventListener("resize", resize);

    let frame = 0;
    let running = true;
    function tick() {
      if (!running) return;
      frame = requestAnimationFrame(tick);
      group.rotation.y += 0.0025;
      group.children.forEach(function (mesh, index) {
        mesh.position.y += Math.sin(performance.now() / 900 + index) * 0.0008;
      });
      renderer.render(scene, camera);
    }
    const observer = new IntersectionObserver(function (entries) {
      running = entries.some(function (entry) { return entry.isIntersecting; });
      if (running) tick();
      else cancelAnimationFrame(frame);
    });
    observer.observe(canvas);
    canvas.dataset.webgl = "on";
    tick();
  }

  function coverTexture(THREE, title, color) {
    const canvas = document.createElement("canvas");
    canvas.width = 256;
    canvas.height = 400;
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "#" + color.toString(16).padStart(6, "0");
    ctx.fillRect(0, 0, 256, 400);
    ctx.fillStyle = "rgba(255,244,228,0.92)";
    ctx.font = "600 28px Georgia, serif";
    wrap(ctx, title, 24, 70, 208, 34);
    const texture = new THREE.CanvasTexture(canvas);
    texture.colorSpace = THREE.SRGBColorSpace;
    return texture;
  }

  function wrap(ctx, text, x, y, max, line) {
    const words = text.split(" ");
    let row = "";
    words.forEach(function (word) {
      const trial = row ? row + " " + word : word;
      if (ctx.measureText(trial).width > max) {
        ctx.fillText(row, x, y);
        row = word;
        y += line;
      } else row = trial;
    });
    ctx.fillText(row, x, y);
  }
})();
