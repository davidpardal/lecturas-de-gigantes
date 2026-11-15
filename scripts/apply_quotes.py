#!/usr/bin/env python3
"""Añade quoteEs: traducción fiel al castellano de cada cita en inglés."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
T = {
"I credit this book as being the only book in the last decade—except maybe a few of Nassim Taleb’s works and maybe one or two other scattered books—that made me smarter.":
"Considero que este es el único libro de la última década —salvo quizá algunas obras de Nassim Taleb y uno o dos libros sueltos más— que me ha hecho más inteligente.",
"I’m currently stuck in a loop where, at least in science, I’m only going to read The Beginning of Infinity and The Fabric of Reality over and over again until I understand them fully.":
"Estoy metido en un bucle en el que, al menos en ciencia, solo voy a leer The Beginning of Infinity y The Fabric of Reality una y otra vez hasta entenderlos del todo.",
"Taleb’s Skin In The Game is required reading. If you want to get anywhere in modern life and understand how modern systems work, then Skin In The Game would be near the top of my list to read.":
"Skin in the Game, de Taleb, es de lectura obligada. Si quieres llegar a alguna parte en la vida moderna y entender cómo funcionan los sistemas actuales, Skin in the Game estaría casi al principio de mi lista.",
"Instead of reading a business book, pick up Adam Smith’s The Wealth of Nations.":
"En vez de leer un libro de negocios, coge The Wealth of Nations, de Adam Smith.",
"Instead of reading a book on biology or evolution that’s written today, I would pick up Darwin’s Origin of the Species.":
"En vez de leer un libro de biología o de evolución escrito hoy, yo cogería El origen de las especies, de Darwin.",
"Instead of reading advanced books on cosmology […] you can pick up Richard Feynman’s Six Easy Pieces and start with basic physics.":
"En vez de leer libros avanzados de cosmología […] puedes coger Six Easy Pieces, de Richard Feynman, y empezar por la física básica.",
"Sapiens is the best book of the last decade I have read.":
"Sapiens es el mejor libro de la última década que he leído.",
"The most brilliant and enlightening book I've read in years. He has written four of my top 20 books.":
"El libro más brillante y esclarecedor que he leído en años. Ha escrito cuatro de mis veinte libros preferidos.",
"Everything else written by Matt Ridley. Matt is a scientist, optimist, and forward thinker. One of my favorite authors. I’ve read everything of his, and reread everything of his.":
"Todo lo demás que ha escrito Matt Ridley. Matt es científico, optimista y piensa a largo plazo. Es uno de mis autores favoritos. He leído todo lo suyo, y lo he releído todo.",
"I’ve read everything of his, and reread everything of his.":
"He leído todo lo suyo, y lo he releído todo.",
"This is his collection of ancient wisdom.":
"Esta es su colección de sabiduría antigua.",
"He is also famous for The Black Swan, Antifragile, and Fooled by Randomness, all of which are worth reading.":
"También es famoso por The Black Swan, Antifragile y Fooled by Randomness, y los tres merecen leerse.",
"All of which are worth reading.":
"Todos merecen leerse.",
"I would give my kids a copy of Richard Feynman's Six Easy Pieces and Six Not-So-Easy Pieces.":
"Les daría a mis hijos un ejemplar de Six Easy Pieces y de Six Not-So-Easy Pieces, de Richard Feynman.",
"A great book by Randall Munroe. In this book, he explains very complicated concepts while only using the 1,000 most common words in the English language.":
"Un gran libro de Randall Munroe. En él explica conceptos muy complicados usando solo las mil palabras más comunes del inglés.",
"There’s another great book called Thinking Physics. I open this one all the time.":
"Hay otro gran libro que se llama Thinking Physics. Lo abro continuamente.",
"This is a great book I really liked which summarizes some of the larger themes of history, very incisive.":
"Es un gran libro, me gustó mucho: resume algunos de los grandes temas de la historia, y es muy incisivo.",
"This is the best book I've read since Sapiens (far less mainstream, though).":
"Es el mejor libro que he leído desde Sapiens (aunque mucho menos masivo).",
"This masquerades as a business book, but it's really just Charlie Munger's advice on overcoming oneself to live a successful and virtuous life.":
"Se disfraza de libro de negocios, pero en realidad es el consejo de Charlie Munger sobre cómo vencerse a uno mismo para vivir con éxito y con virtud.",
"This is the best book I've read in the last year. Physics, poetry, philosophy, and history packaged in a very accessible form.":
"Es el mejor libro que he leído en el último año. Física, poesía, filosofía e historia, en una forma muy accesible.",
"I’ve read this one at least twice.":
"Este lo he leído al menos dos veces.",
"The first thing I would do is start meditating, and then I would read Objective Knowledge by Karl Popper.":
"Lo primero que haría es ponerme a meditar, y después leería Objective Knowledge, de Karl Popper.",
"For game theory, in addition to playing strategy games, you may want to try The Evolution of Cooperation by Robert Axelrod.":
"Para la teoría de juegos, además de jugar a juegos de estrategia, quizá te convenga probar The Evolution of Cooperation, de Robert Axelrod.",
"Probably the best book is The Book of Life. I'll give my kids a copy.":
"Probablemente el mejor libro es The Book of Life. Les daré un ejemplar a mis hijos.",
"I like this for someone who’s more advanced. A rationalist’s guide to the perils of the human mind. The “spiritual” book I keep returning to.":
"Me gusta para quien ya va más avanzado. Una guía racionalista de los peligros de la mente humana. El libro «espiritual» al que sigo volviendo.",
"I love this as a classic book on philosophy, a good introduction for someone starting out. I’ve given out more copies of this book than any other.":
"Me encanta como clásico de filosofía, una buena introducción para quien empieza. He regalado más ejemplares de este libro que de ningún otro.",
"Marcus Aurelius was absolutely life changing for me. It's the personal diary of the Emperor of Rome.":
"Marco Aurelio me cambió la vida por completo. Es el diario personal del emperador de Roma.",
"My most listened-to audiobook. The most important audiobook I've ever heard.":
"El audiolibro que más he escuchado. El audiolibro más importante que he oído.",
"The next book I would read, if I didn't read it already, is Plato's Allegory of the Cave.":
"El siguiente libro que leería, si no lo hubiera leído ya, es la alegoría de la caverna de Platón.",
"I think it is a brilliant book everybody should read.":
"Creo que es un libro brillante que todo el mundo debería leer.",
"Two more books, kind of introducing you to the idea of psychedelics and altered state of consciousness is Doors of Perception by Aldous Huxley and How to Change Your Mind by Michael Pollan. Two great books.":
"Otros dos libros que te introducen en la idea de los psicodélicos y de los estados alterados de conciencia son The Doors of Perception, de Aldous Huxley, y How to Change Your Mind, de Michael Pollan. Dos grandes libros.",
"Two great books, kind of give you an idea of what you could be facing.":
"Dos grandes libros; te dan una idea de a qué te puedes enfrentar.",
"They complement James Fadiman's book very well.":
"Complementan muy bien el libro de James Fadiman.",
"This is the best book on spirituality I've ever read by far.":
"Es, con diferencia, el mejor libro de espiritualidad que he leído.",
"The Book: The taboo against knowing who you are. That's a great book.":
"The Book: el tabú de saber quién eres. Es un gran libro.",
"The Way of Zen is just awesome. It's a joy to read that book.":
"The Way of Zen es sencillamente magnífico. Es una gozada leer ese libro.",
"Bruce Lee wrote some great philosophy and Striking Thoughts is a good summary of some of his philosophy.":
"Bruce Lee escribió muy buena filosofía, y Striking Thoughts es un buen resumen de parte de ella.",
"I recommend The Prophet to anybody, whether you’re religious or not. I think it’s a beautiful book, and it’s worth reading.":
"Recomiendo El profeta a cualquiera, seas religioso o no. Me parece un libro hermoso, y merece la pena leerlo.",
"His short story collection Ficciones, or Labyrinths, is amazing.":
"Su libro de cuentos Ficciones, o Labyrinths, es asombroso.",
"My current favorite short story: probably “Understand” by Ted Chiang. It’s in a collection called Stories of Your Life and Others.":
"Mi cuento favorito ahora mismo: probablemente «Understand», de Ted Chiang. Está en una colección que se llama Stories of Your Life and Others.",
"This contemplates the marvel of thermodynamics from the best sci-fi short story writer of our age.":
"Contempla la maravilla de la termodinámica, del mejor autor de cuentos de ciencia ficción de nuestra época.",
"Another masterpiece of sci-fi by Ted Chiang.":
"Otra obra maestra de ciencia ficción de Ted Chiang.",
"Snow Crash is an amazing, amazing book. There’s nothing quite similar to Snow Crash. Snow Crash is in a league of its own.":
"Snow Crash es un libro asombroso, asombroso. No hay nada parecido a Snow Crash. Snow Crash está en una liga aparte.",
"I quote The Last Question all of the time. I loved it as a kid.":
"Cito The Last Question continuamente. Me encantó de niño.",
"If you want to run through a bunch of them, you can pick up a book called The Book of Secrets by Osho.":
"Si quieres recorrer un montón de ellas, puedes coger un libro que se llama The Book of Secrets, de Osho.",
"Everything by Jed McKenna. Jed spits raw truth. His style may be off-putting but the dedication to truth is unparalleled.":
"Todo lo de Jed McKenna. Jed escupe la verdad en crudo. Su estilo puede resultar desagradable, pero su dedicación a la verdad no tiene igual.",
"Of all the sci-fi I read as a teenager, Stranger in a Strange Land is my favorite.":
"De toda la ciencia ficción que leí de adolescente, Stranger in a Strange Land es mi favorita.",
"Even if you’re not [a U2 fan], it’s a super fun read about how a boy from the suburbs of Dublin grew up to become a world-famous rock star and philanthropist.":
"Aunque no seas [fan de U2], se lee con muchísimo gusto: cómo un chico de las afueras de Dublín acabó siendo una estrella del rock mundial y un filántropo.",
"I can’t read enough about Abraham Lincoln, and this is one of the best books on the subject.":
"No me canso de leer sobre Abraham Lincoln, y este es uno de los mejores libros sobre el tema.",
"This book from 1974 is a must-read for anyone who plays tennis, but I think even people who have never played will get something out of it.":
"Este libro de 1974 es de lectura obligada para quien juega al tenis, pero creo que incluso quien no ha jugado nunca sacará algo de él.",
"It’s a fascinating look at how science develops and how human curiosity has evolved over the millennia.":
"Es una mirada fascinante a cómo se desarrolla la ciencia y a cómo ha evolucionado la curiosidad humana a lo largo de milenios.",
"In terms of sci-fi books, I think Isaac Asimov is really great. I like the Foundation series, probably one of the all-time best.":
"En ciencia ficción, Isaac Asimov me parece realmente grande. Me gusta la serie de la Fundación; probablemente una de las mejores de todos los tiempos.",
"Robert Heinlein, obviously. I like The Moon Is a Harsh Mistress and I like Stranger in a Strange Land, although it kind of goes off the rails at the end.":
"Robert Heinlein, por supuesto. Me gusta The Moon Is a Harsh Mistress y me gusta Stranger in a Strange Land, aunque hacia el final se desmadra un poco.",
"I like Stranger in a Strange Land, although it kind of goes off the rails at the end.":
"Me gusta Stranger in a Strange Land, aunque hacia el final se desmadra un poco.",
"I read Hitchhikers Guide to the Galaxy which is quite positive I think and it highlighted an important point which is that a lot of times the question is harder than the answer.":
"Leí la Guía del autoestopista galáctico, que me parece bastante positiva, y subrayaba una idea importante: muchas veces la pregunta es más difícil que la respuesta.",
"There’s a good book on structural design called Structures: Or Why Things Don’t Fall Down. It is really, really good if you want a primer on structural design.":
"Hay un buen libro de diseño estructural que se llama Structures: Or Why Things Don’t Fall Down. Es realmente muy bueno si quieres una introducción al diseño estructural.",
"There is a good book on rocket stuff called Ignition! by John Clark that’s a really fun one.":
"Hay un buen libro de cohetes que se llama Ignition!, de John Clark, y es muy divertido.",
"All of the important ideas in investing … are in that book.":
"Todas las ideas importantes de la inversión… están en ese libro.",
"We’ve said exactly what we do.":
"Hemos dicho exactamente lo que hacemos.",
"Those two books were terrific books.":
"Aquellos dos libros eran libros extraordinarios.",
"If you have half as much sense as I think you do, you will immediately order copies for all of your children and several of your friends. You will never make a better investment.":
"Si tienes la mitad del sentido común que creo que tienes, encargarás enseguida ejemplares para todos tus hijos y para varios amigos. No harás nunca una inversión mejor.",
"It’s the best work of its kind I have ever read.":
"Es la mejor obra de este tipo que he leído.",
"My wife got me to read Remains of the Day and I liked that a lot.":
"Mi mujer me hizo leer Los restos del día y me gustó mucho.",
"It used to be Dune. I’m sort of a techno-geek, propeller-head, science-fiction type.":
"Antes era Dune. Soy un poco un obseso de la tecnología, de los de hélice en el gorro, de ciencia ficción.",
"It was profound. It transformed me and many of my friends.":
"Fue profundo. Me transformó a mí y a muchos de mis amigos.",
"I loved King Lear.":
"Me encantaba El rey Lear.",
"That’s when I swore off meat pretty much for good.":
"Ahí fue cuando dejé la carne, prácticamente para siempre.",
"Following the Muqaddimah, which was a history from the perspective of an intellectual in the 1300s, Sapiens is a contemporary exploration of many similar questions.":
"Después de la Muqaddimah, que era una historia desde el punto de vista de un intelectual del siglo XIV, Sapiens es una exploración contemporánea de muchas preguntas parecidas.",
"While much of what was believed then is now disproven after 700 more years of progress, it’s still very interesting to see what was understood at this time and the overall worldview when it’s all considered together.":
"Aunque buena parte de lo que entonces se creía ha quedado desmentido tras setecientos años más de progreso, sigue siendo muy interesante ver qué se entendía en aquella época y cuál era la visión del mundo cuando se mira en conjunto.",
"I’ve been interested in learning about criminal justice reform for a while, and this book was highly recommended by several people I trust.":
"Llevo un tiempo interesado en aprender sobre la reforma de la justicia penal, y este libro me lo recomendaron mucho varias personas en las que confío.",
"The trend towards giving people more power is one I believe in deeply.":
"La tendencia a dar más poder a la gente es algo en lo que creo profundamente.",
"I love reading first-hand accounts about how people build great companies like Pixar and nurture innovation and creativity.":
"Me encanta leer relatos de primera mano sobre cómo se construyen grandes empresas como Pixar y cómo se cuidan la innovación y la creatividad.",
"The science is completely clear: vaccinations work and are important for the health of everyone in our community.":
"La ciencia está del todo clara: las vacunas funcionan y son importantes para la salud de todos en nuestra comunidad.",
"The more we all have a voice to share our perspectives, the more empathy we have for each other and the more we respect each other’s rights.":
"Cuanta más voz tenemos todos para compartir nuestro punto de vista, más empatía hay entre nosotros y más respetamos los derechos de los demás.",
"Over the last 35 years, China has experienced one of the greatest economic and social transformations in human history.":
"En los últimos 35 años, China ha vivido una de las mayores transformaciones económicas y sociales de la historia humana.",
"I have recommended this outstanding book before. […] Zorba reminds us how to live fully.":
"Ya he recomendado antes este libro extraordinario. […] Zorba nos recuerda cómo vivir del todo.",
"I never expected to finish it, and I tore through it in less than two weeks.":
"No esperaba terminarlo, y lo devoré en menos de dos semanas.",
"Ever feel like you don’t quite fit in? Don’t want to follow society’s silly rules? Then you can probably relate to human-born and Martian-raised Valentine Michael Smith.":
"¿Alguna vez te has sentido fuera de lugar? ¿No quieres seguir las reglas absurdas de la sociedad? Entonces probablemente te identifiques con Valentine Michael Smith, nacido humano y criado en Marte.",
"If people ask me, for instance, “Which books should I read on leadership?”, I might reply: “Dune and Ender’s Game.”":
"Si me preguntan, por ejemplo, «¿qué libros debería leer sobre liderazgo?», podría responder: «Dune y El juego de Ender».",
"Dune presents, despite my synopsis, perhaps the most incredibly detailed and oddly believable fictional landscape I’ve ever encountered.":
"Dune presenta, pese a mi resumen, el paisaje de ficción más increíblemente detallado y extrañamente creíble que he encontrado.",
"If you need humor to make the jump to fiction, this might be your gateway drug.":
"Si necesitas humor para dar el salto a la ficción, esta puede ser tu puerta de entrada.",
"This classic work on state censorship remains as relevant in today’s world of digital delights as it was when published in the black-and-white world of 1953.":
"Esta obra clásica sobre la censura del Estado sigue siendo tan pertinente en el mundo actual de los placeres digitales como cuando se publicó, en el mundo en blanco y negro de 1953.",
"Zorba the Greek and Seneca: Letters from a Stoic. These are two of the most readable books of practical philosophies I’ve ever had the fortune to encounter.":
"Zorba el griego y las Cartas de un estoico, de Séneca. Son dos de los libros de filosofía práctica más legibles que he tenido la suerte de encontrar.",
"A comprehensive biography of one of the most important writers and social commentators in American history.":
"Una biografía exhaustiva de uno de los escritores y comentaristas sociales más importantes de la historia de Estados Unidos.",
"A must-read for progressives who want a blueprint for reforming government so it can deliver for working people.":
"De lectura obligada para los progresistas que quieran un plano para reformar el Gobierno de modo que responda a la gente que trabaja.",
"One of my favorite crime fiction writers delivers in this story of family, ambition and corruption in a racially charged and violent South.":
"Uno de mis autores favoritos de novela negra cumple en esta historia de familia, ambición y corrupción en un Sur cargado de raza y de violencia.",
"Amazing true story of a couple surviving crisis in the open seas.":
"Una historia real asombrosa: una pareja que sobrevive a una crisis en alta mar.",
"A timely reminder of the quiet dedication and skill of the people who work every day to make this country work.":
"Un recordatorio oportuno de la dedicación callada y de la destreza de quienes trabajan cada día para que este país funcione.",
"A useful primer on how social media and the attention economy have warped our democracy and reshaped our lives.":
"Una introducción útil a cómo las redes sociales y la economía de la atención han deformado nuestra democracia y han rehecho nuestras vidas.",
"A beautiful fable about migration, memory, and the struggle to recognize our common humanity.":
"Una fábula hermosa sobre la migración, la memoria y el esfuerzo por reconocer nuestra humanidad común.",
"To me, this is not only one of greatest books ever written but perhaps the only book of its kind.":
"Para mí no es solo uno de los mejores libros jamás escritos, sino quizá el único de su especie.",
"After Marcus Aurelius, this is one of my favorite books. […] Seneca’s letters are the best place to start.":
"Después de Marco Aurelio, este es uno de mis libros favoritos. […] Las cartas de Séneca son el mejor sitio por donde empezar.",
"The essays in On the Shortness of Life are excellent as well.":
"Los ensayos de Sobre la brevedad de la vida también son excelentes.",
"Frankl is one of the most profound modern thinkers on meaning and purpose.":
"Frankl es uno de los pensadores modernos más profundos sobre el sentido y el propósito.",
"Even if you’ve never watched a down of football, you’ll get something out of this book.":
"Aunque no hayas visto ni una jugada de fútbol americano, sacarás algo de este libro.",
"This book (and his life) were living proof of his family motto: “Fortitudine vincimus” (By endurance we conquer).":
"Este libro (y su vida) eran la prueba viva del lema de su familia: «Fortitudine vincimus» (vencemos por la resistencia).",
"You can draw a pretty straight line from Seneca […] to the modern day writings of Nassim Nicholas Taleb (read: The Black Swan, Fooled By Randomness and The Bed of Procrustes).":
"Se puede trazar una línea bastante recta desde Séneca […] hasta lo que escribe hoy Nassim Nicholas Taleb (leed: The Black Swan, Fooled by Randomness y The Bed of Procrustes).",
"Read: The Black Swan, Fooled By Randomness and The Bed of Procrustes.":
"Leed: The Black Swan, Fooled by Randomness y The Bed of Procrustes.",
"What I like about this book is that the profiles are not about statesmen or generals but artists.":
"Lo que me gusta de este libro es que los retratos no son de estadistas ni de generales, sino de artistas.",
"You MUST read his books. His work on power and strategy are critical for anyone trying to accomplish anything.":
"TENÉIS que leer sus libros. Su trabajo sobre el poder y la estrategia es imprescindible para cualquiera que intente lograr algo.",
"What Makes Sammy Run? is Ari Gold before Ari Gold existed.":
"What Makes Sammy Run? es Ari Gold antes de que existiera Ari Gold.",
"On why even environmentalists should be pro building, pro cities, pro nuclear, and pro genetic engineering.":
"Sobre por qué hasta los ecologistas deberían estar a favor de construir, de las ciudades, de la nuclear y de la ingeniería genética.",
"On how modern technological economies can build more outputs with less inputs, and why we need all economies to be modern and technological.":
"Sobre cómo las economías tecnológicas modernas pueden producir más con menos insumos, y por qué necesitamos que todas las economías sean modernas y tecnológicas.",
"On the central role cities play in our world and why it’s so important for us to build them — more, bigger, better.":
"Sobre el papel central de las ciudades en nuestro mundo y por qué es tan importante construirlas: más, más grandes, mejores.",
"On perhaps the greatest American builder of all, the builder who brought electricity to us all, Thomas Edison.":
"Sobre quizá el mayor constructor estadounidense de todos, el que nos trajo la electricidad a todos: Thomas Edison.",
"On how four great builders of the 19th century built the world we live in today.":
"Sobre cómo cuatro grandes constructores del siglo XIX edificaron el mundo en el que vivimos hoy.",
"On why we can’t build in great American cities like San Francisco today and what we need to do about it.":
"Sobre por qué hoy no podemos construir en grandes ciudades estadounidenses como San Francisco, y qué hay que hacer al respecto.",
"Girard gives a sweeping view of the whole human experience on this planet — something captured in the title of his masterwork, Things Hidden Since the Foundation of the World.":
"Girard ofrece una visión de conjunto de toda la experiencia humana en este planeta, algo que queda recogido en el título de su obra mayor, Things Hidden Since the Foundation of the World.",
"That one’s particularly good.":
"Ese es particularmente bueno.",
"This is correct—art of war in the Middle Ages.":
"Correcto: el arte de la guerra en la Edad Media.",
"This is an incredible read, and as we sit in the middle of the software revolution it’s worthwhile to see what people thought as the industrial revolution was happening.":
"Es una lectura increíble y, metidos como estamos en la revolución del software, merece la pena ver qué pensaba la gente mientras ocurría la revolución industrial.",
"The best source of information about startups is probably not business books, but histories of particular startups and industries. The most famous is Tracy Kidder’s Soul of a New Machine.":
"La mejor fuente de información sobre startups probablemente no son los libros de negocios, sino las historias de startups y de sectores concretos. La más famosa es The Soul of a New Machine, de Tracy Kidder.",
"The one book we encourage startup founders to read is Dale Carnegie’s How to Win Friends and Influence People.":
"El único libro que animamos a leer a quienes fundan una startup es How to Win Friends and Influence People, de Dale Carnegie.",
"I’d also recommend Franklin’s Autobiography.":
"También recomendaría la Autobiografía de Franklin.",
}

def main():
    path = ROOT / "data/people.json"
    people = json.loads(path.read_text(encoding="utf-8"))
    missing = []
    n = 0
    for person in people:
        for rec in person["recommendations"]:
            quote = rec.get("quote")
            if not quote:
                rec.pop("quoteEs", None)
                continue
            es = T.get(quote)
            if not es:
                missing.append(quote)
                continue
            rec["quoteEs"] = es
            n += 1
    if missing:
        print("FALTAN", len(missing))
        for q in missing:
            print("---")
            print(q)
        raise SystemExit(1)
    path.write_text(json.dumps(people, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("traducidas", n)

if __name__ == "__main__":
    main()
