#!/usr/bin/env python3
"""Añade recomendaciones verificadas (Naval / Collison) a los JSON."""
import json
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAG = "14140b-21"
ALMANACK = "https://www.navalmanack.com/navals-recommended-reading"
LBL = "Capítulo de lecturas recomendadas de The Almanack of Naval Ravikant (navalmanack.com), con citas públicas de Naval."
COLLISON = "https://patrickcollison.com/bookshelf"
CLBL = "Estantería de Patrick Collison: lo marcó entre los libros particularmente buenos."

books = json.loads((ROOT / "data/books.json").read_text(encoding="utf-8"))
people = json.loads((ROOT / "data/people.json").read_text(encoding="utf-8"))
by_id = {b["id"]: b for b in books}
person = {p["id"]: p for p in people}


def search_link(title, author):
    q = urllib.parse.quote_plus(f"{title} {author.split('(')[0].strip()}")
    return f"https://www.amazon.es/s?k={q}&tag={TAG}"


def add_book(bid, original, author, description, title=None):
    if bid in by_id:
        return
    shown = title or original
    book = {
        "id": bid,
        "title": shown,
        "originalTitle": original,
        "author": author,
        "description": description,
        "titleLocked": bool(title),
        "isbn13": None,
        "isbn10": None,
        "amazon": search_link(shown, author),
        "amazonKind": "search",
        "cover": None,
    }
    books.append(book)
    by_id[bid] = book


def add_rec(pid, bid, quote, url, label):
    recs = person[pid]["recommendations"]
    if any(r["bookId"] == bid for r in recs):
        return
    recs.append({
        "bookId": bid,
        "quote": quote,
        "sourceUrl": url,
        "sourceLabel": label,
    })


# --- Libros nuevos citados por Naval ---
add_book("rational-optimist", "The Rational Optimist", "Matt Ridley",
         "Ensayo sobre cómo el intercambio —de bienes y de ideas— ha hecho a las sociedades más prósperas. Ridley recorre la historia como una cadena de especialización, no como un relato de decadencia.",
         "El optimista racional")
add_book("genome-ridley", "Genome", "Matt Ridley",
         "Un capítulo por cada cromosoma humano: qué gen vive ahí y qué dice de nosotros. Ridley usa la genética para hablar de enfermedad, conducta e historia sin convertir el ADN en destino.",
         "Genoma")
add_book("red-queen", "The Red Queen", "Matt Ridley",
         "Por qué el sexo existe, contado como una carrera armamentística evolutiva: hay que correr para quedarse en el mismo sitio. El título viene de la Reina Roja de Carroll.",
         "La reina roja")
add_book("origins-of-virtue", "The Origins of Virtue", "Matt Ridley",
         "De dónde sale la cooperación humana si la selección premia al individuo. Ridley mezcla biología, antropología y el dilema del prisionero.",
         "Los orígenes de la virtud")
add_book("evolution-of-everything", "The Evolution of Everything", "Matt Ridley",
         "Argumento de que el cambio —en la moral, la tecnología, la economía— surge de abajo arriba, no de un plan. Ridley aplica la lógica evolutiva fuera de la biología.",
         "La evolución de todo")
add_book("six-not-so-easy", "Six Not-So-Easy Pieces", "Richard P. Feynman",
         "La continuación de Seis piezas fáciles: relatividad, simetría y el espacio, en las lecciones de Feynman. Sigue siendo física explicada en voz alta, un grado más arriba.",
         "Seis piezas no tan fáciles")
add_book("thing-explainer", "Thing Explainer", "Randall Munroe",
         "Diagramas de cohetes, células y centrales nucleares escritos solo con las mil palabras más comunes del inglés. Munroe, el de xkcd, llama al Saturno V «el que sube cinco».")
add_book("thinking-physics", "Thinking Physics", "Lewis Carroll Epstein",
         "Acertijos de física que se resuelven razonando, sin fórmulas largas. El propio libro presume de usarse tanto en la escuela como en un posgrado.")
add_book("lessons-of-history", "The Lessons of History", "Will y Ariel Durant",
         "Cien páginas que destilan los temas grandes de la historia —geografía, raza, economía, guerra— después de décadas escribiendo la historia universal. Es corto a propósito.",
         "Las lecciones de la historia")
add_book("reality-not-what-it-seems", "Reality Is Not What It Seems", "Carlo Rovelli",
         "Historia de la gravedad cuántica contada desde Demócrito hasta los lazos de espacio. Rovelli escribe física con el tono de quien también lee poesía.",
         "La realidad no es lo que parece")
add_book("seven-brief-lessons", "Seven Brief Lessons on Physics", "Carlo Rovelli",
         "Siete textos breves —relatividad, cuántica, cosmos, calor, tiempo— pensados para leerse en una tarde. Rovelli comprime la física del siglo XX sin el andamiaje del manual.",
         "Siete breves lecciones de física")
add_book("objective-knowledge", "Objective Knowledge", "Karl Popper",
         "Popper defiende que el conocimiento crece por conjeturas y refutaciones, no por inducción. Es uno de sus libros de epistemología, más seco que las obras de divulgación que vinieron después.",
         "Conocimiento objetivo")
add_book("evolution-of-cooperation", "The Evolution of Cooperation", "Robert Axelrod",
         "Qué pasa cuando se repite el dilema del prisionero: un torneo de programas de ordenador en el que gana la estrategia más simple, el toma y daca. Axelrod saca de ahí una teoría de la cooperación.",
         "La evolución de la cooperación")
add_book("book-of-life", "The Book of Life", "Jiddu Krishnamurti",
         "Fragmentos diarios sacados de charlas de Krishnamurti: mirar la propia mente sin convertir esa mirada en otra doctrina. No es un sistema; es un calendario de observaciones.",
         "El libro de la vida")
add_book("total-freedom", "Total Freedom", "Jiddu Krishnamurti",
         "Selección más exigente de Krishnamurti sobre el pensamiento, el miedo y la autoridad interior. Va dirigido a quien ya no busca un método espiritual con instrucciones.")
add_book("siddhartha", "Siddhartha", "Hermann Hesse",
         "Novela corta de un hombre que deja a los ascetas, prueba la riqueza y el amor, y acaba escuchando a un río. Hesse cuenta una búsqueda espiritual sin sermón.",
         "Siddhartha")
add_book("tao-of-seneca", "The Tao of Seneca", "Séneca (ed. Tim Ferriss)",
         "Las cartas de Séneca a Lucilio en una edición de audio y texto preparada por Tim Ferriss, con introducciones breves. Es el estoico romano pensado para escucharse entero.")
add_book("allegory-of-the-cave", "The Allegory of the Cave", "Platón",
         "El pasaje de La República en el que unos prisioneros toman las sombras de una hoguera por la realidad. Platón lo usa para distinguir opinión de conocimiento.",
         "La alegoría de la caverna")
add_book("how-to-change-your-mind", "How to Change Your Mind", "Michael Pollan",
         "Reportaje sobre la ciencia reciente de los psicodélicos y sobre lo que Pollan probó él mismo. El libro habla de la mente y de la investigación clínica, no es un manual de consumo.",
         "Cómo cambiar tu mente")
add_book("doors-of-perception", "The Doors of Perception", "Aldous Huxley",
         "El relato de Huxley de una experiencia con mescalina en 1953, y el ensayo breve que lo acompaña. Pregunta qué parte de la realidad filtra el cerebro para que podamos funcionar.",
         "Las puertas de la percepción")
add_book("know-yourself", "Know Yourself", "Awhad al-Din Balyani",
         "Tratado breve, atribuido a la tradición de Ibn Arabi, sobre la unidad del ser. Cabe en pocas páginas y se lee como un texto de metafísica, no como una guía de autoayuda.")
add_book("book-taboo", "The Book: On the Taboo Against Knowing Who You Are", "Alan Watts",
         "Watts argumenta que la idea de un yo separado del resto del mundo es una convención, no un hecho. Lo escribe con el humor seco de sus charlas.",
         "El libro del tabú")
add_book("way-of-zen", "The Way of Zen", "Alan Watts",
         "Introducción al zen: de dónde sale en China y Japón y qué quiere decir en la práctica. Watts lo cuenta para un lector occidental, sin pedir que uno se haga monje.",
         "El camino del Zen")
add_book("joyous-cosmology", "The Joyous Cosmology", "Alan Watts",
         "Watts describe estados de conciencia alterada y la sensación de actuar sin forzarse —el wu-wei—. Es un ensayo corto, anterior a la ola psicodélica de los años sesenta.")
add_book("striking-thoughts", "Striking Thoughts", "Bruce Lee",
         "Aforismos de Bruce Lee sobre el entrenamiento, el yo y la adaptación, reunidos a partir de sus notas. No es un manual de combate: es filosofía de alguien que peleaba.",
         "Striking Thoughts")
add_book("the-prophet", "The Prophet", "Khalil Gibran",
         "Un hombre a punto de irse de su ciudad responde, en verso, a preguntas sobre el amor, el trabajo, los hijos y la muerte. Gibran lo escribió en inglés en 1923; se lee como un libro de sabiduría laica.",
         "El profeta")
add_book("ficciones", "Ficciones", "Jorge Luis Borges",
         "Cuentos en los que una biblioteca, un mapa o una enciclopedia se vuelven infinitos. Borges mezcla el relato policial con la metafísica en muy pocas páginas.",
         "Ficciones")
add_book("stories-of-your-life", "Stories of Your Life and Others", "Ted Chiang",
         "Relatos de ciencia ficción de Chiang, entre ellos «La historia de tu vida», llevado al cine como Arrival. Cada cuento parte de una idea —el lenguaje, la inteligencia, el libre albedrío— y la lleva hasta el final.",
         "La historia de tu vida")
add_book("exhalation", "Exhalation", "Ted Chiang",
         "Segunda colección de cuentos de Chiang. El que da título al libro imagina un universo de aire y entropía; otros tratan del tiempo, la memoria y las máquinas que crían.",
         "Exhalación")
add_book("lifecycle-software-objects", "The Lifecycle of Software Objects", "Ted Chiang",
         "Novela corta sobre inteligencias digitales que hay que criar durante años, como a un animal, para que lleguen a ser alguien. Chiang pregunta qué debemos a una criatura que hemos enseñado.",
         "El ciclo de vida de los objetos de software")
add_book("snow-crash", "Snow Crash", "Neal Stephenson",
         "Novela de 1992 en la que un repartidor de pizzas y una patinadora se mueven entre un metaversio y un virus que ataca a programadores. Stephenson mezcla lingüística sumeria, corporaciones y espadas.",
         "Snow Crash")
add_book("the-last-question", "The Last Question", "Isaac Asimov",
         "Cuento breve: la humanidad pregunta una y otra vez a un ordenador si se puede invertir la entropía. Asimov lo recorre a escala cósmica, en pocas páginas.",
         "La última pregunta")
add_book("book-of-secrets", "The Book of Secrets", "Osho",
         "Comentario de 112 técnicas de meditación de un texto sánscrito antiguo. Osho las presenta como experimentos para probar, no como un credo único.",
         "El libro de los secretos")
add_book("jed-theory", "Theory of Everything", "Jed McKenna",
         "Primera novela de la trilogía en la que McKenna, un autor enmascarado, desmonta la búsqueda espiritual como otro sueño más. El tono es brusco a propósito.")

# Collison, los que marcó en negrita y aún no estaban
add_book("age-of-ambition", "Age of Ambition", "Evan Osnos",
         "Crónica de la China de después de Mao a través de gente que quiere dinero, fe o voz propia. Osnos, periodista, escribe desde el terreno, no desde el titular.",
         "La edad de la ambición")
add_book("pattern-language", "A Pattern Language", "Christopher Alexander",
         "Un catálogo de patrones para diseñar pueblos, edificios y habitaciones, del tamaño de la plaza al del alféizar. Alexander lo pensó para que lo usara quien construye, no solo el arquitecto.",
         "Un lenguaje de patrones")
add_book("mindstorms", "Mindstorms", "Seymour Papert",
         "Papert, discípulo de Piaget, cuenta cómo los niños pueden aprender matemáticas construyendo con el ordenador, en el lenguaje Logo. Es un libro de 1980 sobre el pensamiento, no sobre aparatos.",
         "Mindstorms")
add_book("fermi-paradox", "If the Universe Is Teeming with Aliens... Where Is Everybody?", "Stephen Webb",
         "Cincuenta respuestas posibles a la paradoja de Fermi: si hay tantas estrellas, por qué no hemos visto a nadie. Webb las ordena, de la más técnica a la más especulativa.",
         "Si el universo está lleno de alienígenas… ¿dónde está todo el mundo?")
add_book("hard-landing", "Hard Landing", "Thomas Petzinger Jr.",
         "Historia de la aviación comercial estadounidense cuando la desregulación convirtió las aerolíneas en una guerra de precios. Petzinger sigue a directivos, pilotos y quiebras.",
         "Hard Landing")
add_book("metamagical-themas", "Metamagical Themas", "Douglas R. Hofstadter",
         "Selección de columnas de Hofstadter sobre el lenguaje, la autorreferencia, el sexo de las palabras y la mente. Es el terreno de Gödel, Escher, Bach, en piezas sueltas.",
         "Metamagical Themas")
add_book("out-of-maos-shadow", "Out of Mao's Shadow", "Philip P. Pan",
         "Reportajes sobre quienes, en la China contemporánea, empujan contra el relato oficial: abogados, periodistas, supervivientes. Pan escribe desde Pekín.",
         "Fuera de la sombra de Mao")

# --- Recomendaciones de Naval ---
N = [
    ("sapiens", "Sapiens is the best book of the last decade I have read.", ALMANACK, LBL),
    ("rational-optimist", "The most brilliant and enlightening book I've read in years. He has written four of my top 20 books.", ALMANACK, LBL),
    ("genome-ridley", "Everything else written by Matt Ridley. Matt is a scientist, optimist, and forward thinker. One of my favorite authors. I’ve read everything of his, and reread everything of his.", ALMANACK, LBL),
    ("red-queen", "I’ve read everything of his, and reread everything of his.", ALMANACK, LBL),
    ("origins-of-virtue", "I’ve read everything of his, and reread everything of his.", ALMANACK, LBL),
    ("evolution-of-everything", "I’ve read everything of his, and reread everything of his.", ALMANACK, LBL),
    ("bed-of-procrustes", "This is his collection of ancient wisdom.", ALMANACK, LBL),
    ("black-swan", "He is also famous for The Black Swan, Antifragile, and Fooled by Randomness, all of which are worth reading.", ALMANACK, LBL),
    ("antifragile", "All of which are worth reading.", ALMANACK, LBL),
    ("fooled-by-randomness", "All of which are worth reading.", ALMANACK, LBL),
    ("six-not-so-easy", "I would give my kids a copy of Richard Feynman's Six Easy Pieces and Six Not-So-Easy Pieces.", ALMANACK, LBL),
    ("thing-explainer", "A great book by Randall Munroe. In this book, he explains very complicated concepts while only using the 1,000 most common words in the English language.", ALMANACK, LBL),
    ("thinking-physics", "There’s another great book called Thinking Physics. I open this one all the time.", ALMANACK, LBL),
    ("lessons-of-history", "This is a great book I really liked which summarizes some of the larger themes of history, very incisive.", ALMANACK, LBL),
    ("sovereign-individual", "This is the best book I've read since Sapiens (far less mainstream, though).", ALMANACK, LBL),
    ("poor-charlie", "This masquerades as a business book, but it's really just Charlie Munger's advice on overcoming oneself to live a successful and virtuous life.", ALMANACK, LBL),
    ("reality-not-what-it-seems", "This is the best book I've read in the last year. Physics, poetry, philosophy, and history packaged in a very accessible form.", ALMANACK, LBL),
    ("seven-brief-lessons", "I’ve read this one at least twice.", ALMANACK, LBL),
    ("objective-knowledge", "The first thing I would do is start meditating, and then I would read Objective Knowledge by Karl Popper.", ALMANACK, LBL),
    ("evolution-of-cooperation", "For game theory, in addition to playing strategy games, you may want to try The Evolution of Cooperation by Robert Axelrod.", ALMANACK, LBL),
    ("book-of-life", "Probably the best book is The Book of Life. I'll give my kids a copy.", ALMANACK, LBL),
    ("total-freedom", "I like this for someone who’s more advanced. A rationalist’s guide to the perils of the human mind. The “spiritual” book I keep returning to.", ALMANACK, LBL),
    ("siddhartha", "I love this as a classic book on philosophy, a good introduction for someone starting out. I’ve given out more copies of this book than any other.", ALMANACK, LBL),
    ("meditations", "Marcus Aurelius was absolutely life changing for me. It's the personal diary of the Emperor of Rome.", ALMANACK, LBL),
    ("tao-of-seneca", "My most listened-to audiobook. The most important audiobook I've ever heard.", ALMANACK, LBL),
    ("allegory-of-the-cave", "The next book I would read, if I didn't read it already, is Plato's Allegory of the Cave.", ALMANACK, LBL),
    ("how-to-change-your-mind", "I think it is a brilliant book everybody should read.", ALMANACK, LBL),
    ("doors-of-perception", "Two more books, kind of introducing you to the idea of psychedelics and altered state of consciousness is Doors of Perception by Aldous Huxley and How to Change Your Mind by Michael Pollan. Two great books.", ALMANACK, LBL),
    ("psychedelic-explorers", "They complement James Fadiman's book very well.", ALMANACK, LBL),
    ("know-yourself", "This is the best book on spirituality I've ever read by far.", ALMANACK, LBL),
    ("book-taboo", "The Book: The taboo against knowing who you are. That's a great book.", ALMANACK, LBL),
    ("way-of-zen", "The Way of Zen is just awesome. It's a joy to read that book.", ALMANACK, LBL),
    ("striking-thoughts", "Bruce Lee wrote some great philosophy and Striking Thoughts is a good summary of some of his philosophy.", ALMANACK, LBL),
    ("the-prophet", "I recommend The Prophet to anybody, whether you’re religious or not. I think it’s a beautiful book, and it’s worth reading.", ALMANACK, LBL),
    ("ficciones", "His short story collection Ficciones, or Labyrinths, is amazing.", ALMANACK, LBL),
    ("stories-of-your-life", "My current favorite short story: probably “Understand” by Ted Chiang. It’s in a collection called Stories of Your Life and Others.", ALMANACK, LBL),
    ("exhalation", "This contemplates the marvel of thermodynamics from the best sci-fi short story writer of our age.", ALMANACK, LBL),
    ("lifecycle-software-objects", "Another masterpiece of sci-fi by Ted Chiang.", ALMANACK, LBL),
    ("snow-crash", "Snow Crash is an amazing, amazing book. There’s nothing quite similar to Snow Crash. Snow Crash is in a league of its own.", ALMANACK, LBL),
    ("the-last-question", "I quote The Last Question all of the time. I loved it as a kid.", ALMANACK, LBL),
    ("book-of-secrets", "If you want to run through a bunch of them, you can pick up a book called The Book of Secrets by Osho.", ALMANACK, LBL),
    ("jed-theory", "Everything by Jed McKenna. Jed spits raw truth. His style may be off-putting but the dedication to truth is unparalleled.", ALMANACK, LBL),
]
for bid, quote, url, label in N:
    add_rec("naval-ravikant", bid, quote, url, label)

for bid in [
    "age-of-ambition", "pattern-language", "mindstorms", "fermi-paradox",
    "hard-landing", "metamagical-themas", "out-of-maos-shadow",
]:
    add_rec("patrick-collison", bid, None, COLLISON, CLBL)

person["naval-ravikant"]["bio"] = (
    "Cofundador de AngelList. En nav.al y en el capítulo de lecturas de The Almanack of Naval Ravikant ha dejado por escrito los libros que regala, relee o considera imprescindibles."
)

# Comprobar
ids = set(by_id)
for p in people:
    seen = set()
    for r in p["recommendations"]:
        if r["bookId"] not in ids:
            raise SystemExit(f"falta {r['bookId']} en {p['id']}")
        if r["bookId"] in seen:
            raise SystemExit(f"duplicado {r['bookId']} en {p['id']}")
        seen.add(r["bookId"])
        assert "tag=14140b-21" in by_id[r["bookId"]]["amazon"]

(ROOT / "data/books.json").write_text(json.dumps(books, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(ROOT / "data/people.json").write_text(json.dumps(people, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("naval", len(person["naval-ravikant"]["recommendations"]))
print("collison", len(person["patrick-collison"]["recommendations"]))
print("libros", len(books))
print("personas", len(people))
