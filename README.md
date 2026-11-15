# Lecturas de gigantes

Biblioteca estática, en castellano, de libros que personas influyentes han recomendado en público. Cada persona y cada libro tienen su ficha. Un mismo libro es una sola entrada, aunque lo recomienden varias personas.

La web no necesita compilación para publicarse: GitHub Pages puede servir la rama `main` desde la raíz. Las páginas HTML se generan a partir de los JSON para que el título, la descripción y Open Graph existan sin JavaScript.

Dirección prevista: <https://davidpardal.github.io/lecturas-de-gigantes/>

## Verla en local

```bash
python3 -m http.server 8765
```

Abre `http://127.0.0.1:8765/`. Las rutas son relativas y funcionan igual bajo `/lecturas-de-gigantes/`.

## Cómo está organizado

| Ruta | Qué es |
| --- | --- |
| `index.html` | Portada: estantería, buscador y personas |
| `mas-recomendados.html` | Libros recomendados por más de una persona |
| `personas/<id>.html` | Ficha de una persona |
| `libros/<id>.html` | Ficha de un libro, con todas las personas que lo recomiendan |
| `data/people.json` | Personas y sus recomendaciones |
| `data/books.json` | Libros, sin duplicar |
| `css/styles.css`, `js/site.js` | Diseño, búsqueda, libros en 3D |

En la ficha de una persona, cada libro enlaza a su ficha y, si alguien más lo ha recomendado, aparece «También lo recomiendan». En la ficha del libro están la cita y la fuente de cada persona.

Los enlaces «Ver en Amazon» apuntan a amazon.es con `tag=14140b-21`. Si el ISBN-10 de la edición en español está identificado, el enlace es `https://www.amazon.es/dp/<ISBN-10>?tag=14140b-21`. Si no, es una búsqueda: `https://www.amazon.es/s?k=...&tag=14140b-21`. Llevan `rel="sponsored nofollow noopener"`.

Las portadas salen de Open Library (`covers.openlibrary.org`) cuando hay ISBN. Si la imagen no existe, se muestra un lomo de tela con el título.

## Añadir una persona

1. Si hace falta, crea antes los libros en `data/books.json` (ver más abajo). El `id` no se repite.
2. Añade un objeto a `data/people.json`:

```json
{
  "id": "ada-lovelace",
  "name": "Ada Lovelace",
  "role": "Matemática",
  "bio": "Una o dos frases, en castellano, sobre quién es.",
  "initials": "AL",
  "hue": 200,
  "recommendations": [
    {
      "bookId": "origin-of-species",
      "quote": "Cita breve y literal, en el idioma original. null si no hay cita.",
      "sourceUrl": "https://ejemplo.org/entrevista",
      "sourceLabel": "Entrevista en Ejemplo, 1843."
    }
  ]
}
```

`hue` es un número de 0 a 360: el color del avatar. `quote` puede ser `null`. No inventes recomendaciones: cada entrada necesita una fuente pública real (entrevista, blog, discurso, tuit, lista). Si no hay fuente, no añadas el libro.

3. Regenera las páginas:

```bash
node scripts/build.mjs
```

Eso reescribe `index.html`, `mas-recomendados.html`, `personas/`, `libros/`, `sitemap.xml` y `robots.txt`.

## Añadir un libro

Un libro, una ficha. Si ya existe, reutiliza su `id` en la recomendación: no crees otro objeto.

```json
{
  "id": "origin-of-species",
  "title": "El origen de las especies",
  "originalTitle": "On the Origin of Species",
  "author": "Charles Darwin",
  "description": "Dos o tres frases tuyas, en castellano, sobre el libro.",
  "titleLocked": false,
  "isbn13": "9788483061312",
  "isbn10": "8483061312",
  "amazon": "https://www.amazon.es/dp/8483061312?tag=14140b-21",
  "amazonKind": "direct",
  "cover": "https://covers.openlibrary.org/b/isbn/9788483061312-L.jpg?default=false"
}
```

`title` es el título en español si hay edición; si no la hay, repite `originalTitle`. `amazonKind` es `"direct"` o `"search"`. La descripción no se copia de la contraportada: se escribe para esta web.

Para proponer un ISBN español a partir de Open Library:

```bash
python3 scripts/enrich_editions.py
```

Revisa el resultado. Open Library a veces mezcla ediciones, resume libros o devuelve una traducción al catalán. Si el título o la editorial no cuadran, deja `amazonKind` en `"search"` y borra el ISBN.

Después, `node scripts/build.mjs`.

## Criterio editorial

Solo entran recomendaciones comprobadas en la fuente enlazada. Una lista de «libros que posee» no cuenta, salvo que la persona los marque como especialmente buenos (es el caso de la estantería de Patrick Collison: solo los que destacó). Leer un libro no es recomendarlo.

## Diseño

La estantería y las portadas son CSS 3D (lomo, canto y tapas). Al pasar el cursor, o al pulsar el botón de la portada, el libro gira. En pantallas anchas, y solo si hay WebGL y el sistema no pide reducir movimiento, un lienzo con Three.js (desde jsDelivr) añade libros flotando detrás del título. Si WebGL no está, falla la red o el móvil es estrecho, se queda la estantería CSS: el texto no depende del 3D. `prefers-reduced-motion` deja los libros quietos.

## Publicar

En el repositorio, GitHub Pages debe servir la rama `main` desde la raíz (`/`). Hay un `.nojekyll` para que Pages no procese el sitio con Jekyll. Este cambio no modifica la configuración del repositorio: hay que activar Pages a mano si aún no está activa.

## Aviso

Como afiliado de Amazon, obtengo ingresos por las compras adscritas que cumplen los requisitos aplicables. Las recomendaciones proceden de las fuentes públicas enlazadas en cada ficha.
