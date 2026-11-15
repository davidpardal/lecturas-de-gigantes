#!/usr/bin/env python3
"""Completa ISBN de edición en español (Open Library) y el enlace de Amazon.es.

El título en español se aplica solo si hay un ISBN de España (978-84) o de
otro país hispanohablante. Si no hay edición localizada, se conserva el
título original y el enlace es de búsqueda.
"""
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOKS = ROOT / "data" / "books.json"
TAG = "14140b-21"
UA = "lecturas-de-gigantes/1.0 (spanish edition lookup; contact: davidpardal)"

# Prefijos ISBN-13 de mercados en español. España primero.
PREFIXES = (
    "97884", "978607", "978968", "978950", "978987", "978956",
    "978958", "978612", "978980", "9789972", "9789974", "9789977",
    "9789978", "978996", "978999",
)

# Títulos comerciales en español, solo si el ISBN confirma la edición.
TITLES = {
    "beginning-of-infinity": "El comienzo del infinito",
    "fabric-of-reality": "La estructura de la realidad",
    "skin-in-the-game": "Jugarse la piel",
    "wealth-of-nations": "La riqueza de las naciones",
    "origin-of-species": "El origen de las especies",
    "six-easy-pieces": "Seis piezas fáciles",
    "stranger-in-a-strange-land": "Forastero en tierra extraña",
    "team-of-rivals": "Equipo de rivales",
    "inner-game-of-tennis": "El juego interior del tenis",
    "foundation": "Fundación",
    "moon-harsh-mistress": "La Luna es una cruel amante",
    "zero-to-one": "De cero a uno",
    "superintelligence": "Superinteligencia",
    "structures": "Estructuras, o por qué las cosas no se caen",
    "hitchhikers": "Guía del autoestopista galáctico",
    "intelligent-investor": "El inversor inteligente",
    "essays-buffett": "Los ensayos de Warren Buffett",
    "common-stocks": "Acciones ordinarias y beneficios extraordinarios",
    "influence": "Influencia",
    "guns-germs-steel": "Armas, gérmenes y acero",
    "remains-of-the-day": "Los restos del día",
    "dune": "Dune",
    "autobiography-yogi": "Autobiografía de un yogui",
    "king-lear": "El rey Lear",
    "diet-small-planet": "Dieta para un planeta pequeño",
    "moby-dick": "Moby Dick",
    "sapiens": "Sapiens. De animales a dioses",
    "muqaddimah": "Introducción a la historia universal",
    "new-jim-crow": "El color de la justicia",
    "end-of-power": "El fin del poder",
    "creativity-inc": "Creatividad, S.A.",
    "zorba": "Zorba el griego",
    "enders-game": "El juego de Ender",
    "fahrenheit-451": "Fahrenheit 451",
    "letters-seneca": "Cartas a Lucilio",
    "shortness-of-life": "Sobre la brevedad de la vida",
    "empire-of-pain": "El imperio del dolor",
    "project-hail-mary": "Proyecto Hail Mary",
    "klara-and-the-sun": "Klara y el Sol",
    "meditations": "Meditaciones",
    "mans-search": "El hombre en busca de sentido",
    "black-swan": "El cisne negro",
    "fooled-by-randomness": "¿Existe la suerte?",
    "antifragile": "Antifrágil",
    "bed-of-procrustes": "El lecho de Procusto",
    "forty-eight-laws": "Las 48 leyes del poder",
    "democracy-in-america": "La democracia en América",
    "thinking-fast": "Pensar rápido, pensar despacio",
    "how-to-win-friends": "Cómo ganar amigos e influir sobre las personas",
    "franklin-autobiography": "Autobiografía",
    "hundred-years": "Cien años de soledad",
    "fight-club": "El club de la lucha",
    "kite-runner": "Cometas en el cielo",
    "outliers": "Fueras de serie",
    "checklist-manifesto": "El efecto checklist",
    "never-eat-alone": "Nunca comas solo",
    "on-the-road": "En el camino",
    "zen-motorcycle": "Zen y el arte del mantenimiento de la motocicleta",
    "old-man-sea": "El viejo y el mar",
    "war-of-art": "La guerra del arte",
    "atlas-shrugged": "La rebelión de Atlas",
    "hero-thousand-faces": "El héroe de las mil caras",
    "singularity-kurzweil": "La singularidad está cerca",
    "cats-cradle": "Cuna de gato",
    "diamond-age": "La era del diamante",
    "right-stuff": "Lo que hay que tener",
    "things-hidden": "Cosas ocultas desde la fundación del mundo",
    "new-atlantis": "La nueva Atlántida",
    "art-of-war-middle-ages": "El arte de la guerra en la Edad Media",
    "soul-new-machine": "El alma de una nueva máquina",
    "medieval-technology": "Tecnología medieval y cambio social",
    "so-good": "Sé tan bueno que no puedan ignorarte",
    "mindset": "Mindset. La actitud del éxito",
    "triumph-of-the-city": "El triunfo de las ciudades",
    "sovereign-individual": "El individuo soberano",
    "spirit-st-louis": "El espíritu de San Luis",
    "man-who-sold-the-moon": "El hombre que vendió la Luna",
    "heros-journey": "El viaje del héroe",
    "social-animal-aronson": "El animal social",
    "fourth-turning": "El cuarto giro",
    "as-a-man-thinketh": "Como piensa un hombre",
    "abundance": "Abundancia",
    "poor-charlie": "El almanaque de Charlie Munger",
    "vasari-lives": "Las vidas de los más excelentes arquitectos, pintores y escultores",
    "be-here-now": "Be Here Now",
    "shantaram": "Shantaram",
    "musashi": "Musashi",
    "tao-te-ching": "Tao Te Ching",
}


def fold(text: str) -> str:
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text


def get(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.loads(res.read().decode("utf-8"))


def isbn13_to_10(isbn13: str):
    digits = re.sub(r"[^0-9Xx]", "", isbn13)
    if len(digits) != 13 or not digits.startswith("978"):
        return None
    core = digits[3:12]
    total = sum(int(ch) * (10 - i) for i, ch in enumerate(core))
    check = (11 - (total % 11)) % 11
    return core + ("X" if check == 10 else str(check))


def rank_isbn(isbn: str) -> int:
    digits = re.sub(r"[^0-9Xx]", "", isbn).upper()
    if len(digits) != 13 or not digits.startswith("978"):
        return 99
    for i, prefix in enumerate(PREFIXES):
        if digits.startswith(prefix):
            return i
    return 99


def last_name(author: str) -> str:
    author = re.sub(r"\(.*?\)", "", author)
    author = author.split(" y ")[0]
    author = author.replace("Jr.", "").replace("jr.", "")
    parts = [p for p in author.replace(",", " ").split() if p]
    return fold(parts[-1]) if parts else ""


def short_title(book) -> str:
    raw = book["originalTitle"].split(":")[0].split("?")[0]
    raw = raw.replace("’", "'").replace("“", "").replace("”", "")
    return fold(raw)


def pick(book):
    q = urllib.parse.quote(f"{short_title(book)} {last_name(book['author'])}")
    url = (
        "https://openlibrary.org/search.json?q="
        + q
        + "&limit=8&fields=title,author_name,isbn,language"
    )
    try:
        data = get(url)
    except Exception as exc:
        print("ERR", book["id"], exc)
        return None
    want = last_name(book["author"]).lower()
    best = None
    best_rank = 99
    for doc in data.get("docs") or []:
        names = " ".join(doc.get("author_name") or [])
        if want and want not in fold(names).lower():
            continue
        for isbn in doc.get("isbn") or []:
            rank = rank_isbn(isbn)
            if rank < best_rank:
                best_rank = rank
                best = re.sub(r"[^0-9Xx]", "", isbn).upper()
    return best


def amazon(book):
    isbn13 = book.get("isbn13")
    isbn10 = isbn13_to_10(isbn13) if isbn13 else None
    if isbn10:
        book["isbn10"] = isbn10
        book["amazon"] = f"https://www.amazon.es/dp/{isbn10}?tag={TAG}"
        book["amazonKind"] = "direct"
        book["cover"] = f"https://covers.openlibrary.org/b/isbn/{isbn13}-L.jpg?default=false"
    else:
        book["isbn10"] = None
        book["cover"] = None
        q = urllib.parse.quote_plus(f"{book['title']} {book['author'].split('(')[0].strip()}")
        book["amazon"] = f"https://www.amazon.es/s?k={q}&tag={TAG}"
        book["amazonKind"] = "search"


def main():
    books = json.loads(BOOKS.read_text(encoding="utf-8"))
    for i, book in enumerate(books):
        isbn = pick(book)
        if isbn and isbn.startswith("978"):
            book["isbn13"] = isbn
            if book["id"] in TITLES:
                book["title"] = TITLES[book["id"]]
            where = "ES" if isbn.startswith("97884") else "HIS"
            print(f"OK {where} {book['id']}: {book['title']} [{isbn}]")
        else:
            book["isbn13"] = None
            book["title"] = book["originalTitle"]
            print(f"—  {book['id']}")
        amazon(book)
        time.sleep(0.18)
        if i and i % 25 == 0:
            time.sleep(1.0)
    BOOKS.write_text(json.dumps(books, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    direct = sum(1 for b in books if b["amazonKind"] == "direct")
    print(f"directos={direct} busqueda={len(books) - direct}")


if __name__ == "__main__":
    main()
