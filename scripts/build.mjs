import { readFileSync, writeFileSync, mkdirSync, readdirSync, unlinkSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const BASE = "https://davidpardal.github.io/lecturas-de-gigantes";
const books = JSON.parse(readFileSync(join(root, "data/books.json"), "utf8"));
const people = JSON.parse(readFileSync(join(root, "data/people.json"), "utf8"));
const bookById = new Map(books.map((book) => [book.id, book]));

for (const person of people) {
  for (const rec of person.recommendations) {
    if (!bookById.has(rec.bookId)) throw new Error(`Falta el libro ${rec.bookId}`);
  }
}

const recommenders = new Map();
for (const person of people) {
  for (const rec of person.recommendations) {
    if (!recommenders.has(rec.bookId)) recommenders.set(rec.bookId, []);
    recommenders.get(rec.bookId).push({ person, rec });
  }
}

function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, (ch) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  })[ch]);
}

function spine(id) {
  let hash = 0;
  for (const char of id) hash = (hash * 33 + char.charCodeAt(0)) >>> 0;
  return `hsl(${hash % 360} 34% 28%)`;
}

function book3d(book, size, label) {
  const cover = book.cover
    ? `<img src="${esc(book.cover)}" alt="" ${size === "lg" ? "" : 'loading="lazy"'} decoding="async">`
    : "";
  return `<div role="button" tabindex="0" class="book3d ${size}" style="--spine:${spine(book.id)}" data-title="${esc(book.title)}" aria-pressed="false" aria-label="${esc(label)}">
    <span class="book3d-box">
      <span class="face front">${cover}<span class="cloth"><span class="cloth-title">${esc(book.title)}</span><span class="cloth-author">${esc(book.author)}</span></span></span>
      <span class="face spine"><span>${esc(book.title)}</span></span>
      <span class="face pages"></span>
      <span class="face back"></span>
    </span>
  </div>`;
}

function amazon(book) {
  return `<a class="amazon" href="${esc(book.amazon)}" target="_blank" rel="sponsored nofollow noopener">Ver en Amazon</a>`;
}

function also(bookId, exceptId) {
  const others = (recommenders.get(bookId) || []).filter((item) => item.person.id !== exceptId);
  if (!others.length) return "";
  const links = others.map((item) => `<a href="../personas/${item.person.id}.html">${esc(item.person.name)}</a>`).join(", ");
  return `<p class="also">También lo recomiendan: ${links}.</p>`;
}

function quoteBlock(rec) {
  if (!rec.quote) return "";
  const main = rec.quoteEs || rec.quote;
  const original = rec.quoteEs
    ? `<p class="quote-original" lang="en">${esc(rec.quote)}</p>`
    : "";
  return `<blockquote><p lang="${rec.quoteEs ? "es" : "en"}">${esc(main)}</p>${original}</blockquote>`;
}

function sourceLine(rec) {
  return `<p class="source"><a href="${esc(rec.sourceUrl)}" target="_blank" rel="noopener noreferrer">${esc(rec.sourceLabel)}</a></p>`;
}

function head({ title, description, canonical, pathPrefix, jsonLd }) {
  return `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${esc(title)}</title>
  <meta name="description" content="${esc(description)}">
  <link rel="canonical" href="${canonical}">
  <meta property="og:site_name" content="Lecturas de gigantes">
  <meta property="og:locale" content="es_ES">
  <meta property="og:type" content="website">
  <meta property="og:title" content="${esc(title)}">
  <meta property="og:description" content="${esc(description)}">
  <meta property="og:url" content="${canonical}">
  <meta property="og:image" content="${BASE}/img/og.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${esc(title)}">
  <meta name="twitter:description" content="${esc(description)}">
  <meta name="twitter:image" content="${BASE}/img/og.png">
  <meta name="theme-color" content="#120e0b">
  <link rel="icon" href="${pathPrefix}img/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,520;0,9..144,680;1,9..144,520&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="${pathPrefix}css/styles.css">
  <script type="application/ld+json">${jsonLd}</script>
</head>`;
}

function header(pathPrefix, current) {
  const home = pathPrefix + "index.html";
  const most = pathPrefix + "mas-recomendados.html";
  return `<a class="skip" href="#contenido">Saltar al contenido</a>
<header class="top">
  <a class="brand" href="${home}">Lecturas de gigantes</a>
  <nav>
    <a href="${home}" ${current === "home" ? 'aria-current="page"' : ""}>Personas</a>
    <a href="${most}" ${current === "most" ? 'aria-current="page"' : ""}>Los más recomendados</a>
  </nav>
</header>`;
}

function footer(pathPrefix) {
  return `<footer class="site-footer">
  <div class="wrap">
    <p class="legal">Como afiliado de Amazon, obtengo ingresos por las compras adscritas que cumplen los requisitos aplicables.</p>
    <p>Las recomendaciones proceden de fuentes públicas enlazadas en cada ficha: entrevistas, blogs, discursos, listas y publicaciones de cada persona. El texto descriptivo de los libros es de esta web.</p>
    <p><a href="${pathPrefix}index.html">Portada</a> · <a href="${pathPrefix}mas-recomendados.html">Los más recomendados</a></p>
  </div>
</footer>
<script src="${pathPrefix}js/site.js" defer></script>`;
}

const cloudflareBeacon = `<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "11d95762138f48e8833beed810ad38c4"}'></script><!-- End Cloudflare Web Analytics -->`;

function clearDir(dir) {
  mkdirSync(dir, { recursive: true });
  for (const file of readdirSync(dir)) {
    if (file.endsWith(".html")) unlinkSync(join(dir, file));
  }
}

const ranked = [...recommenders.entries()]
  .map(([id, list]) => ({ book: bookById.get(id), list }))
  .filter((item) => item.list.length > 1)
  .sort((a, b) => b.list.length - a.list.length || a.book.title.localeCompare(b.book.title, "es"));

const homeTitle = "Lecturas de gigantes";
const homeDesc = "Libros recomendados en público por Naval Ravikant, Bill Gates, Warren Buffett, Mario Vargas Llosa y otras personas influyentes. Cada título, con su fuente.";
const catalog = books.map((book) => ({
  title: book.title,
  original: book.originalTitle,
  author: book.author,
  people: (recommenders.get(book.id) || []).map((item) => item.person.name).join(", "),
  href: `libros/${book.id}.html`,
  spine: spine(book.id)
}));

function shelfBook(book) {
  const cover = book.cover ? `<img src="${esc(book.cover)}" alt="" decoding="async">` : "";
  return `<a class="book3d" style="--spine:${spine(book.id)}" data-title="${esc(book.title)}" href="libros/${book.id}.html" aria-label="${esc(book.title)}, ficha del libro">
    <span class="book3d-box">
      <span class="face front">${cover}<span class="cloth"><span class="cloth-title">${esc(book.title)}</span><span class="cloth-author">${esc(book.author)}</span></span></span>
      <span class="face spine"><span>${esc(book.title)}</span></span>
      <span class="face pages"></span>
      <span class="face back"></span>
    </span>
  </a>`;
}

function personCard(person) {
  return `<a class="person-card" href="personas/${person.id}.html" data-name="${esc(person.name + " " + person.role)}" data-books="${esc(person.recommendations.map((rec) => bookById.get(rec.bookId).title + " " + bookById.get(rec.bookId).author).join(" "))}">
          <span class="avatar" style="--hue:${person.hue}">${esc(person.initials)}</span>
          <span>
            <h3>${esc(person.name)}</h3>
            <p>${esc(person.role)}</p>
            <span class="count">${person.recommendations.length} ${person.recommendations.length === 1 ? "libro" : "libros"}</span>
          </span>
        </a>`;
}

const index = `${head({
  title: homeTitle,
  description: homeDesc,
  canonical: BASE + "/",
  pathPrefix: "",
  jsonLd: JSON.stringify({
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: homeTitle,
    url: BASE + "/",
    inLanguage: "es",
    description: homeDesc,
    potentialAction: {
      "@type": "SearchAction",
      target: BASE + "/?q={search_term_string}",
      "query-input": "required name=search_term_string"
    }
  })
})}
<body class="home">
${header("", "home")}
<main id="contenido">
  <section class="hero">
    <canvas id="hero-gl" aria-hidden="true"></canvas>
    <div class="hero-copy">
      <p class="eyebrow">Biblioteca de recomendaciones públicas</p>
      <h1>Lecturas de <em>gigantes</em></h1>
      <p class="lede">Los libros que citan, regalan y releen quienes están dando forma al mundo. Una ficha por persona, una ficha por libro, y la fuente siempre a la vista.</p>
      <ul class="hero-stats">
        <li>${people.length} personas</li>
        <li>${books.length} libros</li>
        <li>${ranked.length} compartidos por varias</li>
      </ul>
      <form class="search" role="search">
        <label class="sr-only" for="q">Buscar por libro, autor o persona</label>
        <input id="q" type="search" placeholder="Busca un libro, un autor o una persona" autocomplete="off" enterkeyhint="search">
        <button type="submit">Buscar</button>
      </form>
    </div>
    <div class="shelf-wrap">
      <div class="shelf-scene">
        <div class="shelf" aria-label="Estantería de los libros más recomendados">
          ${ranked.slice(0, 5).map((item) => shelfBook(item.book)).join("\n")}
        </div>
      </div>
    </div>
  </section>
  <div class="sheet">
    <div class="wrap">
      <div id="results" class="results" hidden></div>
      <div class="section-head">
        <div>
          <h2>Los más recomendados</h2>
          <p>Títulos que aparecen en la lista de más de una persona.</p>
        </div>
        <a href="mas-recomendados.html">Ver el ranking</a>
      </div>
      <div class="rail">
        ${ranked.slice(0, 8).map((item) => `<div class="mini">${book3d(item.book, "sm", "Girar " + item.book.title)}<a href="libros/${item.book.id}.html"><strong>${esc(item.book.title)}</strong></a><p class="who">${item.list.length} personas</p></div>`).join("")}
      </div>
      <div class="section-head">
        <div>
          <h2>Las personas</h2>
          <p>Entra en una ficha para ver qué recomienda y por qué, con el enlace a la fuente.</p>
        </div>
      </div>
      <div class="people" id="people">
        ${people.filter((person) => !person.spanish).map((person) => personCard(person)).join("")}
      </div>
      <div class="section-head">
        <div>
          <h2>Voces en español</h2>
          <p>Escritores, economistas e inversores de habla hispana y lo que recomiendan leer.</p>
        </div>
      </div>
      <div class="people" id="people-es">
        ${people.filter((person) => person.spanish).map((person) => personCard(person)).join("")}
      </div>
    </div>
    ${footer("")}
  </div>
</main>
<script id="catalog" type="application/json">${JSON.stringify(catalog)}</script>
${cloudflareBeacon}
</body>
</html>
`;

const mostDesc = "Libros recomendados por más de una persona, ordenados por número de recomendadores.";
const most = `${head({
  title: "Los más recomendados — Lecturas de gigantes",
  description: mostDesc,
  canonical: BASE + "/mas-recomendados.html",
  pathPrefix: "",
  jsonLd: JSON.stringify({
    "@context": "https://schema.org",
    "@type": "ItemList",
    name: "Los más recomendados",
    itemListElement: ranked.map((item, index) => ({
      "@type": "ListItem",
      position: index + 1,
      url: `${BASE}/libros/${item.book.id}.html`,
      name: item.book.title
    }))
  })
})}
<body>
${header("", "most")}
<main id="contenido" class="page">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Portada</a> / Los más recomendados</p>
    <h1 class="page-title">Los más recomendados</h1>
    <p class="sub">Ordenados por el número de personas de esta biblioteca que los han recomendado en público. Cada ficha reúne sus citas.</p>
    <div class="rank">
      ${ranked.map((item, index) => `<article>
        <span class="n">${index + 1}</span>
        ${book3d(item.book, "sm", "Girar " + item.book.title)}
        <div>
          <h2><a href="libros/${item.book.id}.html">${esc(item.book.title)}</a></h2>
          <p class="by">${esc(item.book.author)} · ${item.list.length} personas</p>
          <div class="faces">
            ${item.list.map(({ person }) => `<a href="personas/${person.id}.html"><span class="avatar" style="--hue:${person.hue}">${esc(person.initials)}</span>${esc(person.name)}</a>`).join("")}
          </div>
        </div>
      </article>`).join("")}
    </div>
    ${footer("")}
  </div>
</main>
${cloudflareBeacon}
</body>
</html>`;

clearDir(join(root, "personas"));
clearDir(join(root, "libros"));
writeFileSync(join(root, "index.html"), index);
writeFileSync(join(root, "mas-recomendados.html"), most);

for (const person of people) {
  const description = `${person.name}, ${person.role}. ${person.recommendations.length} ${person.recommendations.length === 1 ? "libro" : "libros"} que ha recomendado en público, con la fuente de cada uno.`;
  const html = `${head({
    title: `${person.name}: libros que recomienda — Lecturas de gigantes`,
    description: description.slice(0, 180),
    canonical: `${BASE}/personas/${person.id}.html`,
    pathPrefix: "../",
    jsonLd: JSON.stringify({
      "@context": "https://schema.org",
      "@type": "Person",
      name: person.name,
      jobTitle: person.role,
      description: person.bio,
      url: `${BASE}/personas/${person.id}.html`
    })
  })}
<body>
${header("../", "")}
<main id="contenido" class="page">
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Portada</a> / ${esc(person.name)}</p>
    <header class="person-head">
      <span class="avatar lg" style="--hue:${person.hue}">${esc(person.initials)}</span>
      <div>
        <h1>${esc(person.name)}</h1>
        <p class="role">${esc(person.role)} · ${person.recommendations.length} ${person.recommendations.length === 1 ? "libro" : "libros"}</p>
        <p>${esc(person.bio)}</p>
      </div>
    </header>
    <div class="stack">
      ${person.recommendations.map((rec) => {
        const book = bookById.get(rec.bookId);
        const original = book.title !== book.originalTitle ? `<p class="note">Título original: ${esc(book.originalTitle)}</p>` : "";
        return `<article class="card">
          ${book3d(book, "", "Girar el ejemplar de " + book.title)}
          <div>
            <h2><a href="../libros/${book.id}.html">${esc(book.title)}</a></h2>
            <p class="by">${esc(book.author)}</p>
            ${original}
            <p class="desc">${esc(book.description)}</p>
            ${quoteBlock(rec)}
            ${sourceLine(rec)}
            ${also(book.id, person.id)}
            ${amazon(book)}
          </div>
        </article>`;
      }).join("")}
    </div>
    ${footer("../")}
  </div>
</main>
${cloudflareBeacon}
</body>
</html>`;
  writeFileSync(join(root, "personas", person.id + ".html"), html);
}

for (const book of books) {
  const list = recommenders.get(book.id) || [];
  const names = list.map((item) => item.person.name).join(", ");
  const description = `${book.title}, de ${book.author}. Recomendado por ${names}.`;
  const original = book.title !== book.originalTitle ? `<p class="note">Título original: ${esc(book.originalTitle)}</p>` : "";
  const html = `${head({
    title: `${book.title} — Lecturas de gigantes`,
    description: description.slice(0, 180),
    canonical: `${BASE}/libros/${book.id}.html`,
    pathPrefix: "../",
    jsonLd: JSON.stringify({
      "@context": "https://schema.org",
      "@type": "Book",
      name: book.title,
      author: { "@type": "Person", name: book.author },
      inLanguage: book.title === book.originalTitle ? "en" : "es",
      url: `${BASE}/libros/${book.id}.html`,
      description: book.description
    })
  })}
<body>
${header("../", "")}
<main id="contenido" class="page">
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Portada</a> / <a href="../mas-recomendados.html">Libros</a> / ${esc(book.title)}</p>
    <div class="book-layout">
      ${book3d(book, "lg", "Girar el ejemplar de " + book.title)}
      <div class="book-hero">
        <h1>${esc(book.title)}</h1>
        <p class="by">${esc(book.author)}</p>
        ${original}
        <p>${esc(book.description)}</p>
        <p class="count">${list.length} ${list.length === 1 ? "persona lo recomienda" : "personas lo recomiendan"}</p>
        ${amazon(book)}
      </div>
    </div>
    <h2>Quién lo recomienda</h2>
    <div class="stack">
      ${list.map(({ person, rec }) => `<article class="rec">
        <a class="avatar lg" style="--hue:${person.hue}" href="../personas/${person.id}.html">${esc(person.initials)}</a>
        <div>
          <h3><a href="../personas/${person.id}.html">${esc(person.name)}</a></h3>
          <p class="role">${esc(person.role)}</p>
          ${quoteBlock(rec)}
          ${sourceLine(rec)}
        </div>
      </article>`).join("")}
    </div>
    ${footer("../")}
  </div>
</main>
${cloudflareBeacon}
</body>
</html>`;
  writeFileSync(join(root, "libros", book.id + ".html"), html);
}

const urls = ["", "mas-recomendados.html", ...people.map((p) => `personas/${p.id}.html`), ...books.map((b) => `libros/${b.id}.html`)];
const today = "2026-11-15";
writeFileSync(join(root, "sitemap.xml"), `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map((path) => `  <url><loc>${BASE}/${path}</loc><lastmod>${today}</lastmod></url>`).join("\n")}
</urlset>
`);
writeFileSync(join(root, "robots.txt"), `User-agent: *
Allow: /

Sitemap: ${BASE}/sitemap.xml
`);
writeFileSync(join(root, ".nojekyll"), "");

const direct = books.filter((book) => book.amazonKind === "direct").length;
console.log(`páginas personas=${people.length} libros=${books.length} compartidos=${ranked.length} amazon directos=${direct} búsqueda=${books.length - direct}`);
