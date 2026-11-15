#!/usr/bin/env python3
"""Refuerza a Gates, Buffett, Munger y Bezos, añade voces en español
y limita las búsquedas de Amazon a la sección de libros.

Cada recomendación lleva una fuente pública. Se puede ejecutar varias veces:
no duplica libros, personas ni recomendaciones.
"""
import json
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAG = "14140b-21"

books = json.loads((ROOT / "data/books.json").read_text(encoding="utf-8"))
people = json.loads((ROOT / "data/people.json").read_text(encoding="utf-8"))
by_id = {b["id"]: b for b in books}
person = {p["id"]: p for p in people}


def search_link(title, author):
    q = urllib.parse.quote_plus(f"{title} {author.split(' y ')[0].split('(')[0].strip()}")
    return f"https://www.amazon.es/s?k={q}&i=stripbooks&tag={TAG}"


def add_book(bid, title, original, author, description):
    if bid in by_id:
        return
    book = {
        "id": bid,
        "title": title,
        "originalTitle": original,
        "author": author,
        "description": description,
        "titleLocked": True,
        "isbn13": None,
        "isbn10": None,
        "amazon": search_link(title, author),
        "amazonKind": "search",
        "cover": None,
    }
    books.append(book)
    by_id[bid] = book


def add_person(pid, name, role, bio, initials, hue, spanish=False):
    if pid in person:
        return
    p = {"id": pid, "name": name, "role": role, "bio": bio, "initials": initials,
         "hue": hue, "recommendations": []}
    if spanish:
        p["spanish"] = True
    people.append(p)
    person[pid] = p


def add_rec(pid, bid, url, label, quote=None, quote_es=None):
    assert bid in by_id, bid
    recs = person[pid]["recommendations"]
    if any(r["bookId"] == bid for r in recs):
        return
    rec = {"bookId": bid, "quote": quote, "sourceUrl": url, "sourceLabel": label}
    if quote_es:
        rec["quoteEs"] = quote_es
    recs.append(rec)


# ---------------------------------------------------------------- Libros
add_book("enlightenment-now", "En defensa de la Ilustración", "Enlightenment Now", "Steven Pinker",
         "Pinker mide el progreso humano con quince indicadores, de la esperanza de vida a la seguridad laboral, y defiende que la razón y la ciencia explican esa mejora.")
add_book("better-angels", "Los ángeles que llevamos dentro", "The Better Angels of Our Nature", "Steven Pinker",
         "Un estudio de largo recorrido sobre por qué la violencia entre humanos ha caído a lo largo de la historia, con datos de guerras, homicidios y costumbres.")
add_book("business-adventures", "Business Adventures", "Business Adventures", "John Brooks",
         "Doce crónicas del New Yorker de los años sesenta: el fracaso del Edsel, el ascenso de Xerox, un desplome bursátil. Historias de empresa que siguen siendo actuales.")
add_book("factfulness", "Factfulness", "Factfulness", "Hans Rosling",
         "Rosling explica los diez instintos que nos hacen ver el mundo peor de lo que es y propone hábitos sencillos para mirar los datos con calma.")
add_book("little-book-bogle", "El pequeño libro para invertir con sentido común", "The Little Book of Common Sense Investing", "John C. Bogle",
         "El fundador de Vanguard defiende los fondos indexados de bajo coste frente a la gestión activa, con números sobre comisiones y rentabilidad a largo plazo.")
add_book("outsiders-thorndike", "The Outsiders", "The Outsiders", "William N. Thorndike",
         "Ocho consejeros delegados poco conocidos que superaron con creces al mercado. El hilo común: tratar la asignación de capital como su tarea principal.")
add_book("universe-from-nothing", "Un universo de la nada", "A Universe from Nothing", "Lawrence M. Krauss",
         "Divulgación cosmológica sobre cómo la física moderna explica el origen del universo y por qué «la nada» es más complicada de lo que parece.")
add_book("selfish-gene", "El gen egoísta", "The Selfish Gene", "Richard Dawkins",
         "Clásico de la biología evolutiva que mira la selección natural desde el punto de vista del gen y explica desde ahí la cooperación y el altruismo.")
add_book("deep-simplicity", "Deep Simplicity", "Deep Simplicity", "John Gribbin",
         "Introducción al caos y la complejidad: cómo reglas muy simples generan comportamientos complejos en la naturaleza, la economía o los ecosistemas.")
add_book("built-to-last", "Empresas que perduran", "Built to Last", "Jim Collins y Jerry I. Porras",
         "Seis años de investigación comparando empresas visionarias con sus competidoras para encontrar qué hábitos explican su longevidad.")
add_book("good-to-great", "Empresas que sobresalen", "Good to Great", "Jim Collins",
         "Por qué algunas empresas pasan de buenas a excelentes y otras no: liderazgo discreto, disciplina y el efecto «volante» que se refuerza solo.")
add_book("innovators-dilemma", "El dilema de los innovadores", "The Innovator's Dilemma", "Clayton M. Christensen",
         "Cómo las empresas líderes pierden su posición precisamente por hacer bien su trabajo, frente a tecnologías disruptivas que al principio parecen peores.")
add_book("mythical-man-month", "El mítico hombre-mes", "The Mythical Man-Month", "Frederick P. Brooks Jr.",
         "Ensayos sobre la gestión de proyectos de software. Su ley más citada: añadir gente a un proyecto que va con retraso lo retrasa todavía más.")
add_book("the-goal", "La meta", "The Goal", "Eliyahu M. Goldratt",
         "Novela de empresa sobre un director de fábrica que salva su planta aplicando la teoría de las restricciones: el cuello de botella marca el ritmo de todo el sistema.")
add_book("made-in-america", "Made in America", "Sam Walton: Made in America", "Sam Walton",
         "La autobiografía del fundador de Walmart: precios bajos, obsesión por el cliente y frugalidad como sistema para construir la mayor cadena del mundo.")

# Vargas Llosa: novelas de «La verdad de las mentiras»
VLL = [
    ("heart-of-darkness", "El corazón de las tinieblas", "Heart of Darkness", "Joseph Conrad",
     "Un viaje río arriba por el Congo colonial en busca de Kurtz. Conrad retrata la codicia y la brutalidad del imperio europeo en África."),
    ("death-in-venice", "La muerte en Venecia", "Der Tod in Venedig", "Thomas Mann",
     "Un escritor maduro y disciplinado pierde el control durante unas vacaciones en una Venecia amenazada por el cólera."),
    ("dubliners", "Dublineses", "Dubliners", "James Joyce",
     "Quince relatos sobre la vida cotidiana en Dublín a principios del siglo XX, con personajes atrapados entre la rutina y el deseo de escapar."),
    ("mrs-dalloway", "La señora Dalloway", "Mrs Dalloway", "Virginia Woolf",
     "Un solo día de junio en Londres, contado desde la mente de varios personajes mientras Clarissa Dalloway prepara una fiesta."),
    ("great-gatsby", "El gran Gatsby", "The Great Gatsby", "F. Scott Fitzgerald",
     "Jay Gatsby y su fortuna misteriosa en el Long Island de los años veinte: el sueño americano visto desde sus fiestas y sus grietas."),
    ("steppenwolf", "El lobo estepario", "Der Steppenwolf", "Hermann Hesse",
     "Harry Haller, un intelectual solitario dividido entre el hombre civilizado y el «lobo», atraviesa una crisis que lo lleva al Teatro Mágico."),
    ("brave-new-world", "Un mundo feliz", "Brave New World", "Aldous Huxley",
     "Distopía de una sociedad estable y complaciente donde la felicidad se fabrica en laboratorio y la libertad ya no se echa de menos."),
    ("the-stranger", "El extranjero", "L'Étranger", "Albert Camus",
     "Meursault mata a un hombre en una playa de Argel y afronta el juicio con una indiferencia que escandaliza más que el crimen."),
    ("animal-farm", "Rebelión en la granja", "Animal Farm", "George Orwell",
     "Fábula en la que los animales expulsan al granjero y acaban bajo una tiranía peor. Una sátira de la revolución traicionada."),
    ("lolita", "Lolita", "Lolita", "Vladimir Nabokov",
     "Novela narrada por un hombre que intenta justificar lo injustificable. Nabokov hace del lenguaje la trampa que el lector debe desmontar."),
    ("the-leopard", "El gatopardo", "Il Gattopardo", "Giuseppe Tomasi di Lampedusa",
     "La decadencia de la aristocracia siciliana durante la unificación italiana, vista por el príncipe de Salina."),
    ("tin-drum", "El tambor de hojalata", "Die Blechtrommel", "Günter Grass",
     "Oskar Matzerath decide dejar de crecer a los tres años y, con su tambor, cuenta la Alemania del nazismo y la posguerra."),
    ("pereira-maintains", "Sostiene Pereira", "Sostiene Pereira", "Antonio Tabucchi",
     "Un periodista gris de Lisboa, en pleno salazarismo, se ve empujado a tomar partido por un joven colaborador."),
]
for bid, t, o, a, d in VLL:
    add_book(bid, t, o, a, d)

add_book("human-action", "La acción humana", "Human Action", "Ludwig von Mises",
         "El tratado de economía de Mises: parte de la acción individual para explicar precios, dinero, crédito y ciclos económicos.")
add_book("mastering-market-cycle", "Mastering the Market Cycle", "Mastering the Market Cycle", "Howard Marks",
         "Marks explica cómo reconocer en qué punto del ciclo están los mercados y cómo ajustar el riesgo de una cartera según ese punto.")

# --------------------------------------------------------------- Personas
add_person("mario-vargas-llosa", "Mario Vargas Llosa", "Escritor, premio Nobel de Literatura 2010",
           "Novelista peruano y español (1936-2025). En «La verdad de las mentiras» dedicó un ensayo a cada una de las grandes novelas del siglo XX que más admiraba.",
           "VL", 352, spanish=True)
add_person("juan-ramon-rallo", "Juan Ramón Rallo", "Economista",
           "Economista y divulgador nacido en Benicarló, autor de «Liberalismo» y «Anti-Marx». Ha contado qué libro lo convirtió en economista.",
           "JR", 48, spanish=True)
add_person("alvaro-guzman-de-lazaro", "Álvaro Guzmán de Lázaro", "Gestor de fondos, cofundador de Azvalor",
           "Inversor value español, antes gestor en Bestinver junto a Francisco García Paramés. Recomienda lecturas de inversión en prensa económica.",
           "AG", 210, spanish=True)

# --------------------------------------------------------- Recomendaciones
GATES_PINKER = "https://gatesnotes.com/Books/Enlightenment-Now"
add_rec("bill-gates", "enlightenment-now", GATES_PINKER,
        "Reseña de Bill Gates en Gates Notes, «My new favorite book of all time» (2018).",
        "It’s my new favorite book of all time.", "Es mi nuevo libro favorito de todos los tiempos.")
add_rec("bill-gates", "better-angels", GATES_PINKER,
        "Gates Notes (2018): Gates repasa por qué llevaba años recomendándolo.",
        "For years, I’ve been saying Steven Pinker’s The Better Angels of Our Nature was the best book I’d read in a decade.",
        "Durante años he dicho que The Better Angels of Our Nature, de Steven Pinker, era el mejor libro que había leído en una década.")
add_rec("bill-gates", "business-adventures", "https://www.cnbc.com/id/104077340",
        "Texto de Gates en su blog (2014), recogido por CNBC.",
        "Business Adventures remains the best business book I've ever read.",
        "Business Adventures sigue siendo el mejor libro de empresa que he leído.")
add_rec("bill-gates", "factfulness", "https://ti.me/2q0MEaE",
        "Entrevista de Bill Gates en TIME sobre Factfulness (2018).",
        "One of the most important books I’ve ever read.",
        "Uno de los libros más importantes que he leído.")

add_rec("warren-buffett", "little-book-bogle", "https://www.berkshirehathaway.com/letters/2014ltr.pdf",
        "Carta anual de Warren Buffett a los accionistas de Berkshire Hathaway, 2014.",
        "investors – large and small – should instead read Jack Bogle’s The Little Book of Common Sense Investing.",
        "los inversores, grandes y pequeños, deberían leer en su lugar The Little Book of Common Sense Investing, de Jack Bogle.")
add_rec("warren-buffett", "outsiders-thorndike", "https://www.berkshirehathaway.com/letters/2012ltr.pdf",
        "Carta anual de Warren Buffett a los accionistas de Berkshire Hathaway, 2012.",
        "an outstanding book about CEOs who excelled at capital allocation.",
        "un libro extraordinario sobre consejeros delegados que destacaron asignando capital.")
add_rec("warren-buffett", "business-adventures", "https://www.cnbc.com/id/104077340",
        "Bill Gates cuenta que en 1991 Buffett se lo recomendó como su libro de empresa favorito y le prestó su ejemplar (CNBC).")

add_rec("charlie-munger", "universe-from-nothing", "https://fs.blog/worldly-wisdom",
        "Junta de accionistas de Daily Journal, recogida por Farnam Street.",
        "one of the most remarkable books I’ve ever read",
        "uno de los libros más notables que he leído")
add_rec("charlie-munger", "outsiders-thorndike", "https://fs.blog/worldly-wisdom",
        "Recomendado por Munger en la junta de Daily Journal, según Farnam Street.")
add_rec("charlie-munger", "selfish-gene", "https://fs.blog/2014/08/book-recommendations-from-billionaire-charlie-munger/",
        "Lista de libros recomendados por Charlie Munger recopilada por Farnam Street.")
add_rec("charlie-munger", "deep-simplicity", "https://fs.blog/2014/06/charlie-munger-recommended-books/",
        "Recomendado por Munger en la junta de Daily Journal de 2014, según Farnam Street.")

BEZOS = "https://fs.blog/jeff-bezoss-reading-list/"
BEZOS_LBL = "Lista de lecturas de Bezos y de los directivos de Amazon que Brad Stone recoge en «The Everything Store» (vía Farnam Street)."
for bid in ["built-to-last", "good-to-great", "innovators-dilemma", "mythical-man-month",
            "the-goal", "black-swan", "made-in-america"]:
    add_rec("jeff-bezos", bid, BEZOS, BEZOS_LBL)

VLL_URL = "https://www.cnnchile.com/cultura/libros-recomendados-por-mario-vargas-llosa-lolita-rebelion-en-la-granja-y-el-extranjero_20250414/"
VLL_LBL = "Ensayo dedicado a esta novela en «La verdad de las mentiras» (1990; edición ampliada de 2002), según el listado de CNN Chile."
for bid, *_ in VLL:
    add_rec("mario-vargas-llosa", bid, VLL_URL, VLL_LBL)
add_rec("mario-vargas-llosa", "old-man-sea", VLL_URL, VLL_LBL)

add_rec("juan-ramon-rallo", "human-action",
        "https://www.libertaddigital.com/opinion/libros/el-libro-que-me-convirtio-en-economista-1276236938.html",
        "Artículo de Juan Ramón Rallo en Libertad Digital, «El libro que me convirtió en economista» (2009).")

add_rec("alvaro-guzman-de-lazaro", "mastering-market-cycle",
        "https://www.finect.com/grupos/azvalor/articulos/que-lectura-recomienda-alvaro-guzman-lazaro-verano",
        "Recomendación de verano de Guzmán de Lázaro, publicada en Expansión y reproducida por Azvalor (2019).",
        "No deje de acompañar a Howards Marks con la lectura de este libro.")

# ------------------------------------------------ Amazon: solo sección libros
fixed = 0
for b in books:
    if b.get("amazonKind") == "search" and "i=stripbooks" not in b["amazon"]:
        b["amazon"] = b["amazon"].replace("&tag=", "&i=stripbooks&tag=")
        fixed += 1

(ROOT / "data/books.json").write_text(json.dumps(books, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(ROOT / "data/people.json").write_text(json.dumps(people, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"libros={len(books)} personas={len(people)} búsquedas limitadas a libros={fixed}")
