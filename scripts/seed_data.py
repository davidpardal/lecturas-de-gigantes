#!/usr/bin/env python3
"""Genera data/books.json y data/people.json. El JSON es la fuente de verdad."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
books = {}

def B(i, original, author, description, title=None):
    books[i] = {
        "id": i,
        "title": title or original,
        "originalTitle": original,
        "author": author,
        "description": description,
        "titleLocked": bool(title),
    }

# --- Libros ---
B("beginning-of-infinity", "The Beginning of Infinity", "David Deutsch",
  "Ensayo sobre el conocimiento como proceso que no tiene un techo natural. Deutsch defiende que las buenas explicaciones —no la autoridad ni la tradición— son lo que permite a una sociedad resolver problemas sin fin.")
B("fabric-of-reality", "The Fabric of Reality", "David Deutsch",
  "Intento de unir cuatro hebras —la física cuántica, la epistemología de Popper, la teoría de la computación y la evolución— en una sola imagen del mundo. Es un libro exigente, escrito por un físico que no separa la ciencia de la filosofía.")
B("skin-in-the-game", "Skin in the Game", "Nassim Nicholas Taleb",
  "Argumento de que quien decide debe cargar con las consecuencias. Taleb recorre el derecho, la religión y los mercados para mostrar qué sistemas aguantan cuando hay algo que perder y cuáles se pudren cuando el riesgo se traslada a otros.")
B("wealth-of-nations", "The Wealth of Nations", "Adam Smith",
  "Tratado de 1776 sobre cómo se crea la riqueza: división del trabajo, intercambio y los límites del gobernante. Sigue siendo el texto fundacional para entender el mercado sin quedarse en el eslogan.")
B("origin-of-species", "On the Origin of Species", "Charles Darwin",
  "La exposición original de la selección natural, escrita como una larga argumentación con pruebas de criadores, islas y fósiles. Darwin construye el caso con paciencia, no con un manifiesto.")
B("six-easy-pieces", "Six Easy Pieces", "Richard P. Feynman",
  "Seis capítulos de las lecciones de física de Feynman pensados para quien empieza: átomos, física básica, la relación de la física con las otras ciencias, energía, gravitación y cuántica. La claridad es el lujo del libro.")
B("stranger-in-a-strange-land", "Stranger in a Strange Land", "Robert A. Heinlein",
  "Novela de un humano criado en Marte que regresa a la Tierra y mira nuestras costumbres —propiedad, sexo, religión— como si fueran extraterrestres. De ahí salió el verbo «grok», entender algo hasta fundirse con ello.")
B("surrender", "Surrender", "Bono",
  "Memorias del cantante de U2: Dublín, la banda, la fama y décadas de activismo. Es un relato en primera persona de cómo se sostiene una lealtad —a los compañeros, a la familia— cuando el escenario lo ocupa todo.")
B("team-of-rivals", "Team of Rivals", "Doris Kearns Goodwin",
  "Biografía política de Lincoln centrada en el gabinete que formó con quienes habían sido sus rivales. Goodwin muestra el arte de gobernar en una guerra civil sin convertir al presidente en una estatua.")
B("inner-game-of-tennis", "The Inner Game of Tennis", "W. Timothy Gallwey",
  "Libro de tenis que en realidad habla de la atención. Gallwey distingue al yo que critica del yo que ejecuta, y propone dejar de pelearse con el propio juicio mientras se aprende un gesto.")
B("mendeleyevs-dream", "Mendeleyev’s Dream", "Paul Strathern",
  "Historia de la química contada a través de sus personajes, hasta el sueño en el que Mendeléyev ordenó los elementos. Strathern sigue la curiosidad desde los griegos hasta la tabla periódica.")
B("foundation", "Foundation", "Isaac Asimov",
  "Primera novela del ciclo de la Fundación: un científico prevé la caída de un imperio galáctico y diseña un plan para acortar la edad oscura que vendrá. Asimov convierte la historia y la sociología en materia de ciencia ficción.")
B("moon-harsh-mistress", "The Moon Is a Harsh Mistress", "Robert A. Heinlein",
  "Revolución en una colonia lunar penal, narrada por un técnico que conversa con un ordenador que acaba de despertar. Heinlein mezcla ingeniería, humor y una teoría política de la libertad muy suya.")
B("franklin-isaacson", "Benjamin Franklin: An American Life", "Walter Isaacson",
  "Biografía del impresor que se hizo científico, diplomático e inventor de instituciones. Isaacson sigue a Franklin como empresario que empieza sin capital ni nombre.")
B("zero-to-one", "Zero to One", "Peter Thiel y Blake Masters",
  "Notas de un curso de Thiel sobre cómo crear algo que no existía, en lugar de competir copiando. El eje es la diferencia entre ir de cero a uno —inventar— e ir de uno a ene —repetir.")
B("superintelligence", "Superintelligence", "Nick Bostrom",
  "Ensayo sobre qué ocurriría si una máquina superara la inteligencia humana en casi todas las tareas. Bostrom ordena riesgos, incentivos y el problema de controlar un sistema más capaz que sus diseñadores.")
B("structures", "Structures: Or Why Things Don’t Fall Down", "J. E. Gordon",
  "Introducción a por qué puentes, huesos y barcos aguantan o se rompen, escrita con un humor poco habitual en un manual de ingeniería. Gordon explica tensión, compresión y diseño sin esconderse detrás del cálculo.")
B("hitchhikers", "The Hitchhiker’s Guide to the Galaxy", "Douglas Adams",
  "Arthur Dent pierde la Tierra —demolida para una autopista hiperespacial— y recorre el universo con una guía que aconseja no entrar en pánico. Debajo del absurdo hay una idea: a menudo la pregunta importa más que la respuesta.")
B("ignition", "Ignition!: An Informal History of Liquid Rocket Propellants", "John D. Clark",
  "Crónica, escrita por un químico que estuvo dentro, de los combustibles líquidos con los que se intentó hacer volar cohetes. Es técnica y, a la vez, un relato de explosiones, manías y prueba y error.")
B("intelligent-investor", "The Intelligent Investor", "Benjamin Graham",
  "El manual de inversión que separa al inversor del especulador. Graham presenta al señor Mercado, un socio maniaco-depresivo, y la idea de comprar con un margen de seguridad.")
B("essays-buffett", "The Essays of Warren Buffett", "Warren Buffett (ed. Lawrence A. Cunningham)",
  "Las cartas anuales de Buffett a los accionistas de Berkshire, reordenadas por temas: gobierno de la empresa, contabilidad, fusiones, inversión. Cunningham no añade una teoría: recompone las propias palabras de Buffett.")
B("common-stocks", "Common Stocks and Uncommon Profits", "Philip A. Fisher",
  "Método para estudiar una empresa hablando con clientes, competidores y exempleados —lo que Fisher llamó «rumor de pasillo»— antes de comprar y no soltar. Influyó en quien buscaba negocios extraordinarios, no gangas contables.")
B("influence", "Influence", "Robert B. Cialdini",
  "Catálogo de los resortes con los que nos hacen decir que sí: reciprocidad, compromiso, prueba social, autoridad, escasez y simpatía. Cialdini los documenta con experimentos y con el oficio de vendedores y recaudadores.")
B("guns-germs-steel", "Guns, Germs, and Steel", "Jared Diamond",
  "Pregunta por qué unas sociedades conquistaron a otras y responde con geografía, plantas domesticables y gérmenes, no con una supuesta superioridad de los pueblos. Es una historia de largo plazo escrita por un geógrafo.")
B("remains-of-the-day", "The Remains of the Day", "Kazuo Ishiguro",
  "Un mayordomo inglés recorre el país y, mientras conduce, revisa una vida entregada al servicio y al deber. Ishiguro escribe lo que el narrador no se atreve a decir del todo: la lealtad mal puesta y el tiempo que no vuelve.")
B("dune", "Dune", "Frank Herbert",
  "En un planeta desértico del que sale la especia que hace posible el viaje interestelar, un heredero aprende a sobrevivir entre casas nobles, religión y ecología. Herbert construyó un mundo con política, lengua y clima propios.")
B("be-here-now", "Be Here Now", "Ram Dass",
  "Libro de 1971, a medio camino entre manual de meditación, álbum gráfico y relato de un profesor de Harvard que se fue a la India. Mezcla ejercicios de atención con la cultura psicodélica de aquellos años.")
B("autobiography-yogi", "Autobiography of a Yogi", "Paramahansa Yogananda",
  "Relato de un yogui indio que llevó el kriya yoga a Occidente, publicado en 1946. Combina encuentros con santos y científicos con una defensa de la meditación como disciplina, no como adorno.")
B("king-lear", "King Lear", "William Shakespeare",
  "Tragedia de un rey que reparte el reino según quien lo adule y descubre demasiado tarde qué hija decía la verdad. El poder, la vejez y la ceguera voluntaria ocupan cada acto.")
B("diet-small-planet", "Diet for a Small Planet", "Frances Moore Lappé",
  "Ensayo de 1971 que explica cómo obtener proteína de las plantas y cuestiona el coste de alimentar ganado para comer carne. Lappé lo escribió como argumento ecológico y práctico, con recetas incluidas.")
B("moby-dick", "Moby-Dick", "Herman Melville",
  "La persecución de una ballena blanca contada por un marinero que se embarca en el Pequod. Melville mete sermones, taxonomía de cetáceos y una obsesión que acaba con el barco.")
B("sapiens", "Sapiens: A Brief History of Humankind", "Yuval Noah Harari",
  "Recorrido por la historia de Homo sapiens: la revolución cognitiva, la agricultura, los imperios y la ciencia. Harari sostiene que cooperamos en grande porque compartimos ficciones —dioses, naciones, dinero—.")
B("muqaddimah", "The Muqaddimah", "Ibn Jaldún",
  "Introducción a la historia escrita en 1377 por un erudito del norte de África. Ibn Jaldún busca pautas en el ascenso y la caída de las dinastías: cohesión del grupo, lujo y el desgaste del poder.")
B("new-jim-crow", "The New Jim Crow", "Michelle Alexander",
  "Ensayo jurídico sobre cómo la guerra contra las drogas y el sistema penal de Estados Unidos producen una exclusión racial después de la cárcel: empleo, voto y vivienda. Alexander lo argumenta como abogada, con casos y cifras.")
B("end-of-power", "The End of Power", "Moisés Naím",
  "Naím describe cómo el poder —de Estados, ejércitos, iglesias y grandes empresas— se ha vuelto más fácil de obtener y más difícil de usar. Los recién llegados estorban a quien antes mandaba sin discusión.")
B("creativity-inc", "Creativity, Inc.", "Ed Catmull",
  "El cofundador de Pixar cuenta cómo protegieron las ideas frágiles: críticas francas, dirección que no humilla y un miedo consciente a la autocomplacencia. Es un libro de gestión escrito desde una productora, no desde una escuela de negocios.")
B("on-immunity", "On Immunity", "Eula Biss",
  "Ensayo literario sobre las vacunas, el miedo al cuerpo y la metáfora de la pureza. Biss, que escribe como madre y como lectora, revisa por qué la duda prende aunque la evidencia clínica esté clara.")
B("gang-leader", "Gang Leader for a Day", "Sudhir Venkatesh",
  "Un sociólogo entra en un bloque de Chicago y acaba siguiendo a un jefe de banda durante años. El libro muestra la economía cotidiana de ese edificio, con sus reglas, sus rentas y su violencia, vista desde dentro.")
B("dealing-with-china", "Dealing with China", "Henry M. Paulson",
  "Memoria del exsecretario del Tesoro estadounidense sobre décadas de negociación con China, primero desde Goldman Sachs y luego desde el Gobierno. Paulson cuenta la transformación económica sin esconder los roces políticos.")
B("zorba", "Zorba the Greek", "Nikos Kazantzakis",
  "Un intelectual tímido y un obrero vital se meten en una mina de lignito en Creta. Zorba baila, improvisa y empuja al narrador a vivir con el cuerpo, no solo con la cabeza.")
B("musashi", "Musashi", "Eiji Yoshikawa",
  "Novela larga sobre Miyamoto Musashi, el espadachín que pasa de buscavidas a maestro. Yoshikawa convierte duelos y errancia en una educación del carácter: cuándo atacar y cuándo no hace falta.")
B("enders-game", "Ender’s Game", "Orson Scott Card",
  "A un niño lo entrenan en una escuela de combate orbital porque temen una nueva invasión alienígena. La novela habla de estrategia, soledad y del precio de ganar cuando no te han contado el juego entero.")
B("fahrenheit-451", "Fahrenheit 451", "Ray Bradbury",
  "En una ciudad donde los bomberos queman libros, un incinerador empieza a esconder lo que debería destruir. Bradbury escribió sobre la censura y sobre una sociedad que prefiere la pantalla a la frase incómoda.")
B("letters-seneca", "Letters from a Stoic", "Séneca",
  "Selección de las cartas que Séneca escribió a Lucilio: grief, riqueza, tiempo y la muerte. El estoico romano da consejo concreto, a menudo en una página, sin montar un sistema cerrado.")
B("shortness-of-life", "On the Shortness of Life", "Séneca",
  "Ensayo breve: la vida no es corta, dice Séneca, sino que la malgastamos. Discute el ocio, la ambición y la manía de aplazar el momento en que uno vive de verdad.")
B("mark-twain", "Mark Twain", "Ron Chernow",
  "Biografía extensa del escritor que inventó una voz americana y acabó atrapado en deudas, giras y fama. Chernow sigue al hombre detrás de Huck Finn, con sus negocios fallidos y su ojo para la hipocresía.")
B("abundance", "Abundance", "Ezra Klein y Derek Thompson",
  "Argumento de que la escasez de vivienda, energía e infraestructuras en Estados Unidos es, en buena parte, una elección política. Klein y Thompson piden a la izquierda que se tome en serio construir, no solo repartir.")
B("king-of-ashes", "King of Ashes", "S. A. Cosby",
  "Novela negra de Cosby, ambientada en un Sur marcado por la raza y la violencia, en torno a una familia, la ambición y la corrupción. El autor viene de la novela criminal y escribe con ese pulso.")
B("marriage-at-sea", "A Marriage at Sea", "Sophie Elmhirst",
  "Crónica real de una pareja que sobrevive a un naufragio en mar abierto. Elmhirst cuenta la crisis, la espera y lo que el episodio deja en quienes lo viven.")
B("who-is-government", "Who Is Government?", "Michael Lewis",
  "Retratos de funcionarios que hacen funcionar cosas poco visibles —salud, seguridad, datos— sin salir en el titular. Lewis aplica al sector público el mismo ojo que ha usado con los mercados.")
B("sirens-call", "The Sirens’ Call", "Chris Hayes",
  "Ensayo sobre la economía de la atención: cómo las pantallas y las redes secuestran el foco y qué le hace eso a la conversación pública. Hayes escribe desde el periodismo político.")
B("book-of-records", "The Book of Records", "Madeleine Thien",
  "Fábula de Thien sobre migración, memoria y la dificultad de reconocer una humanidad común. La autora, conocida por su novela sobre la Revolución Cultural, vuelve aquí a la historia que las personas cargan encima.")
B("empire-of-pain", "Empire of Pain", "Patrick Radden Keefe",
  "Investigación sobre la familia Sackler y el papel de su fortuna en la crisis de los opioides. Keefe sigue el medicamento, la filantropía que lo tapaba y las víctimas.")
B("project-hail-mary", "Project Hail Mary", "Andy Weir",
  "Un profesor de ciencias despierta solo en una nave, sin recordar la misión, mientras el Sol se apaga por una amenaza interestelar. Weir, el de The Martian, resuelve el problema con ciencia de pizarra y un compañero inesperado.")
B("klara-and-the-sun", "Klara and the Sun", "Kazuo Ishiguro",
  "Una amiga artificial observa a la familia que podría comprarla y trata de entender el amor, la enfermedad y el Sol, que para ella es una divinidad. Ishiguro usa la voz de la máquina para hablar de lo que damos por humano.")
B("meditations", "Meditations", "Marco Aurelio",
  "Apuntes privados de un emperador romano que se recuerda cómo actuar: justo, breve en la ira, atento a lo que depende de él. No se escribieron para publicarse; por eso no hay pose.")
B("mans-search", "Man’s Search for Meaning", "Viktor E. Frankl",
  "Un psiquiatra cuenta los campos de concentración y la idea que sacó de ellos: quien tiene un para qué puede soportar casi cualquier cómo. La segunda parte expone la logoterapia, su método clínico.")
B("score-takes-care", "The Score Takes Care of Itself", "Bill Walsh",
  "El entrenador que levantó a los San Francisco 49ers explica su «estándar de rendimiento»: cómo se entrena, cómo se viste, dónde se coloca cada jugador. La tesis es que el marcador llega si el proceso no se negocia.")
B("endurance-lansing", "Endurance: Shackleton’s Incredible Voyage", "Alfred Lansing",
  "Relato de la expedición de Shackleton atrapada en el hielo de la Antártida y del viaje en un bote abierto para buscar rescate. Lansing lo escribió a partir de los diarios de la tripulación.")
B("black-swan", "The Black Swan", "Nassim Nicholas Taleb",
  "Ensayo sobre los sucesos raros, de enorme impacto, que los modelos dan por imposibles hasta que ocurren. Taleb ataca la soberbia de quien extrapola el pasado y cree haber domado el azar.")
B("fooled-by-randomness", "Fooled by Randomness", "Nassim Nicholas Taleb",
  "Libro anterior al Cisne Negro, centrado en cómo confundimos suerte con talento en los mercados y en la vida. Taleb escribe desde el oficio de quien ha vivido de la incertidumbre.")
B("antifragile", "Antifragile", "Nassim Nicholas Taleb",
  "Taleb distingue lo frágil, lo robusto y lo que sale reforzado del desorden. Propone sistemas —cuerpo, carrera, inversiones— que ganan con la volatilidad en lugar de pedir que el mundo se esté quieto.")
B("bed-of-procrustes", "The Bed of Procrustes", "Nassim Nicholas Taleb",
  "Colección de aforismos: frases cortas sobre el conocimiento, la ética y la modernidad. El título alude al mito de quien cortaba o estiraba a los huéspedes para que cupieran en la cama.")
B("vasari-lives", "Lives of the Most Excellent Painters, Sculptors, and Architects", "Giorgio Vasari",
  "Biografías de artistas del Renacimiento escritas en 1550 por un pintor que los trató. Vasari habla del oficio —el taller, la envidia, el encargo— y no solo de la obra colgada.")
B("forty-eight-laws", "The 48 Laws of Power", "Robert Greene",
  "Compendio de estrategias de poder ilustradas con escenas históricas, de cortes europeas a conspiraciones modernas. Greene describe cómo se obtiene y se pierde influencia, sin presentarlo como un manual moral.")
B("rise-fall-growth", "The Rise and Fall of American Growth", "Robert J. Gordon",
  "El economista argumenta que el gran salto del nivel de vida en Estados Unidos ocurrió entre 1870 y 1970 —agua corriente, electricidad, motor— y que las innovaciones posteriores no se le comparan. Es una historia económica con tesis fuerte.")
B("poor-charlie", "Poor Charlie’s Almanack", "Charles T. Munger (ed. Peter D. Kaufman)",
  "Discursos y comentarios de Charlie Munger, reunidos por Kaufman: modelos mentales, psicología del error y el oficio de invertir. Funciona como biografía intelectual más que como manual de bolsa.")
B("dream-machine", "The Dream Machine", "M. Mitchell Waldrop",
  "Historia de J. C. R. Licklider y de la gente que imaginó el ordenador personal y la red antes de que existieran. Waldrop sigue el dinero de investigación, los laboratorios y las manías de esos pioneros.")
B("hamming", "The Art of Doing Science and Engineering", "Richard W. Hamming",
  "Lecciones de un matemático de los Bell Labs sobre cómo se elige un problema que importe y cómo se trabaja en él. Hamming habla de estilo, de gusto y de no desperdiciar la carrera en lo trivial.")
B("democracy-in-america", "Democracy in America", "Alexis de Tocqueville",
  "Observación de un aristócrata francés sobre la democracia estadounidense en los años 1830: asociaciones, prensa, igualdad y el riesgo de la tiranía de la mayoría. Sigue siendo el clásico para pensar ese experimento político.")
B("whole-earth-discipline", "Whole Earth Discipline", "Stewart Brand",
  "Brand, veterano del ecologismo, defiende ciudades densas, energía nuclear, transgénicos y geoingeniería como herramientas para un planeta habitable. Es un alegato pragmático, escrito contra una parte de su propio campo.")
B("more-from-less", "More from Less", "Andrew McAfee",
  "McAfee sostiene que las economías ricas han empezado a crecer usando menos materiales, no más, gracias a la tecnología. El libro pide que ese desacople llegue al resto del mundo.")
B("triumph-of-the-city", "Triumph of the City", "Edward Glaeser",
  "Defensa de la ciudad como invento que nos hace más ricos, sanos y verdes de lo que admite el tópico. Glaeser, economista urbano, explica por qué la densidad y la vivienda importan.")
B("edison-morris", "Edison", "Edmund Morris",
  "Biografía de Thomas Edison escrita por el biógrafo de Theodore Roosevelt. Morris sigue al inventor del foco y del fonógrafo en el taller, no solo en el mito.")
B("the-tycoons", "The Tycoons", "Charles R. Morris",
  "Retrato de Carnegie, Rockefeller, Gould y J. P. Morgan, los constructores de la economía industrial estadounidense. Morris cuenta cómo montaron ferrocarriles, acero y finanzas a una escala nueva.")
B("golden-gates", "Golden Gates", "Conor Dougherty",
  "Reportaje sobre la crisis de la vivienda en California y sobre quién puede ya vivir en sus ciudades. Dougherty sigue a inquilinos, políticos y constructores en la pelea por el suelo.")
B("things-hidden", "Things Hidden Since the Foundation of the World", "René Girard",
  "Obra mayor de Girard sobre el deseo mimético: queremos lo que quiere otro, y de ahí salen la rivalidad, el chivo expiatorio y lo sagrado. Es filosofía y antropología en un solo volumen denso.")
B("sovereign-individual", "The Sovereign Individual", "James Dale Davidson y Lord William Rees-Mogg",
  "Libro de 1997 que anticipa un mundo donde la información debilita al Estado-nación y el individuo puede llevarse el capital fuera de su alcance. Acertó en parte, exageró en otra, y marcó a quien lo leyó en los noventa.")
B("diamond-age", "The Diamond Age", "Neal Stephenson",
  "Novela en un futuro de nanotecnología donde una niña pobre recibe un libro ilustrado que la educa mejor que cualquier escuela. Stephenson imagina cómo la técnica cambia la clase social y el aprendizaje.")
B("right-stuff", "The Right Stuff", "Tom Wolfe",
  "Crónica de los pilotos de pruebas que se convirtieron en los primeros astronautas estadounidenses. Wolfe pregunta qué tipo de persona se sienta sobre un cohete y espera a que enciendan la mecha.")
B("new-atlantis", "New Atlantis", "Francis Bacon",
  "Fábula de 1627 sobre una isla donde la ciencia se organiza para mejorar la vida humana. Bacon imagina laboratorios, inventos y una sociedad que toma el conocimiento como oficio.")
B("thinking-fast", "Thinking, Fast and Slow", "Daniel Kahneman",
  "El psicólogo resume décadas de trabajo sobre dos modos de pensar: uno rápido e intuitivo y otro lento y deliberado. El libro pone nombre a sesgos —anclaje, disponibilidad, exceso de confianza— que aparecen al decidir.")
B("dealers-of-lightning", "Dealers of Lightning", "Michael Hiltzik",
  "Historia de Xerox PARC, el laboratorio donde se inventaron el ratón, la interfaz gráfica y la impresora láser, y de cómo la empresa no supo convertirlos en negocio. Hiltzik cuenta el talento y el fallo de no llevarlo al mercado.")
B("the-supermen", "The Supermen", "Charles J. Murray",
  "Relato de Seymour Cray y de los ingenieros que construyeron los superordenadores. Murray se detiene en el oficio de diseñar máquinas al límite, no en el eslogan de la innovación.")
B("beak-of-the-finch", "The Beak of the Finch", "Jonathan Weiner",
  "Crónica de los biólogos que midieron, año tras año, los pinzones de las Galápagos y vieron la selección natural en tiempo real. Weiner convierte un estudio de campo en un relato de cómo cambia un pico cuando cambia el clima.")
B("pandaemonium", "Pandaemonium", "Humphrey Jennings",
  "Antología, montada por el documentalista británico, de voces contemporáneas a la llegada de la máquina entre 1660 y 1886. Se lee para ver cómo se vivió una revolución industrial desde dentro, sin el resumen del manual.")
B("art-of-war-middle-ages", "The Art of War in the Middle Ages", "Charles Oman",
  "Ensayo clásico de un historiador militar sobre cómo se combatía entre la caída de Roma y el siglo XVI: caballería, castillos e infantería. Oman escribe para quien quiere la táctica, no la leyenda.")
B("soul-new-machine", "The Soul of a New Machine", "Tracy Kidder",
  "Reportaje de 1981 sobre un equipo que diseña un miniordenador a contrarreloj. Kidder enseña cómo trabajan los ingenieros cuando el plazo aprieta y la máquina aún no existe.")
B("how-to-win-friends", "How to Win Friends and Influence People", "Dale Carnegie",
  "Manual de 1936 sobre trato humano: no humillar, escuchar, hablar de lo que le importa al otro. Carnegie lo escribió para vendedores y mandos; se lee como un curso de fricción social.")
B("franklin-autobiography", "The Autobiography of Benjamin Franklin", "Benjamin Franklin",
  "El propio Franklin cuenta su aprendizaje de impresor, sus proyectos cívicos y el método con el que intentaba corregirse. Es una autobiografía incompleta y, aun así, el modelo del self-made estadounidense.")
B("medieval-technology", "Medieval Technology and Social Change", "Lynn White Jr.",
  "Tesis famosa: el estribo, el arado pesado y otras técnicas reorganizaron la sociedad medieval. White, historiador, ata el objeto cotidiano al poder y a la cosecha.")
B("cats-cradle", "Cat’s Cradle", "Kurt Vonnegut",
  "Sátira sobre un científico y una sustancia, el hielo-nueve, capaz de congelar el agua del mundo. Vonnegut se ríe de la religión inventada, de la bomba y de la fe en que la ciencia se controla sola.")
B("psychedelic-explorers", "The Psychedelic Explorer’s Guide", "James Fadiman",
  "Guía, escrita por un psicólogo, sobre usos terapéuticos y rituales de las sustancias psicodélicas, con protocolos y advertencias. Fadiman recoge décadas de investigación interrumpida y de práctica supervisada.")
B("johnny-bunko", "The Adventures of Johnny Bunko", "Daniel H. Pink",
  "Consejos de carrera en formato de cómic: un oficinista recibe seis lecciones de una mentora inesperada. Pink resume ideas sobre el trabajo —elige el aprendizaje, no el título— en pocas páginas.")
B("so-good", "So Good They Can’t Ignore You", "Cal Newport",
  "Newport discute el consejo de «sigue tu pasión» y propone lo contrario: construye una habilidad rara y valiosa, y la pasión llega después. El libro es un alegato por el oficio deliberado.")
B("shantaram", "Shantaram", "Gregory David Roberts",
  "Novela, basada en la vida del autor, de un fugitivo australiano que se refugia en el Bombay de los años ochenta: barriada, mafia y una ciudad contada calle a calle. Es larga, excesiva y muy física.")
B("as-a-man-thinketh", "As a Man Thinketh", "James Allen",
  "Opúsculo de 1903: el carácter y la circunstancia, dice Allen, siguen a los pensamientos que uno cultiva. Cabe en un rato y ha circulado durante un siglo como manual de actitud.")
B("fourth-turning", "The Fourth Turning", "William Strauss y Neil Howe",
  "Teoría de que la historia anglosajona se mueve en ciclos de cuatro generaciones, de la crisis a la reconstrucción. Strauss y Howe predicen el clima de cada «turno» más que el titular de mañana.")
B("mindset", "Mindset", "Carol S. Dweck",
  "La psicóloga contrasta la mentalidad fija —la habilidad es un don— con la de crecimiento: la habilidad se entrena. Dweck apoya la distinción en estudios sobre alumnos, deportistas y empresas.")
B("spirit-st-louis", "The Spirit of St. Louis", "Charles A. Lindbergh",
  "El propio Lindbergh narra el vuelo en solitario de Nueva York a París en 1927. Es un diario de cabina: sueño, instrumentación y la decisión de no dar la vuelta.")
B("atlas-shrugged", "Atlas Shrugged", "Ayn Rand",
  "Novela de tesis en la que los productores de una sociedad se retiran y el país se detiene. Rand defiende un individualismo radical; el libro es tan largo como su argumento.")
B("man-who-sold-the-moon", "The Man Who Sold the Moon", "Robert A. Heinlein",
  "Relatos de un futuro próximo en el que empresarios privados abren el camino al espacio. El cuento que da título al libro sigue a un magnate empeñado en financiar el primer viaje a la Luna.")
B("singularity-kurzweil", "The Singularity Is Near", "Ray Kurzweil",
  "Pronóstico de que el ritmo de la computación llevará a una inteligencia no biológica que cambie las reglas de la historia. Kurzweil apila curvas exponenciales —chips, genoma, energía— para fechar ese umbral.")
B("hero-thousand-faces", "The Hero with a Thousand Faces", "Joseph Campbell",
  "Campbell compara mitos de muchas culturas y describe un viaje del héroe: llamada, prueba, regreso con un don. Es el esquema que luego adoptaron guionistas de medio mundo.")
B("heros-journey", "The Hero’s Journey", "Joseph Campbell",
  "Conversaciones con Campbell en las que repasa, de forma más oral, la misma idea del viaje del héroe y su lectura de los mitos. Sirve como puerta de entrada a la obra más densa.")
B("one-monster", "One Monster After Another", "Mercer Mayer",
  "Álbum ilustrado infantil de monstruos que se pasan una carta de mano en mano. Es un cuento breve, de los que se leen en voz alta, y Catmull lo señaló entre sus favoritos.")
B("fight-club", "Fight Club", "Chuck Palahniuk",
  "Un oficinista insomne y un vendedor de jabón fundan un club de peleas que deriva en algo más destructivo. Palahniuk escribe el malestar de una generación que consume y no encuentra a qué agarrarse.")
B("outliers", "Outliers", "Malcolm Gladwell",
  "Gladwell argumenta que el éxito extraordinario depende de oportunidad, cultura y horas de práctica, no solo de talento. Usa casos —hockey, Beatles, genios— para bajar del pedestal al individuo solitario.")
B("kite-runner", "The Kite Runner", "Khaled Hosseini",
  "Novela sobre dos niños en el Kabul anterior a la guerra, una traición y el regreso del narrador décadas después. Hosseini cruza la culpa personal con la historia de Afganistán.")
B("checklist-manifesto", "The Checklist Manifesto", "Atul Gawande",
  "Un cirujano explica por qué una lista breve reduce errores en quirófanos, cabinas y obras. Gawande no glorifica el genio: muestra que la complejidad se domina con un papel que no se salta pasos.")
B("never-eat-alone", "Never Eat Alone", "Keith Ferrazzi",
  "Manual de relaciones profesionales: ayudar primero, no pedir favores en frío y tratar la red de contactos como un oficio. Ferrazzi lo cuenta con anécdotas de ventas y de salas de juntas.")
B("social-animal-aronson", "The Social Animal", "Elliot Aronson",
  "Manual clásico de psicología social: conformidad, prejuicio, atracción y cómo nos justificamos. Aronson explica experimentos famosos sin perder el hilo de por qué hacemos lo que hacen los demás.")
B("on-the-road", "On the Road", "Jack Kerouac",
  "Novela de viajes por Estados Unidos en los años cuarenta, escrita de un tirón vital. Kerouac sigue a un grupo que huye de la vida estable en coches, jazz y carreteras.")
B("tao-te-ching", "Tao Te Ching", "Lao Tse",
  "Poemas breves de la tradición taoísta sobre el poder de no forzar, el vacío y el gobierno de uno mismo. Se lee en fragmentos; cada edición depende mucho de quién traduce.")
B("zen-motorcycle", "Zen and the Art of Motorcycle Maintenance", "Robert M. Pirsig",
  "Un viaje en moto de padre e hijo sirve de marco a una indagación sobre la calidad: qué hace que un trabajo esté bien hecho. Pirsig mezcla taller, filosofía y una crisis mental.")
B("old-man-sea", "The Old Man and the Sea", "Ernest Hemingway",
  "Un pescador cubano engancha un pez enorme y pasa días solo con él en el bote. Hemingway reduce la historia a la resistencia, el oficio y lo que queda cuando se vuelve a puerto.")
B("what-makes-sammy", "What Makes Sammy Run?", "Budd Schulberg",
  "Novela sobre un trepa de Hollywood que asciende pisando a quien haga falta. Schulberg, que conocía el cine por dentro, retrata la ambición sin romanticismo.")
B("war-of-art", "The War of Art", "Steven Pressfield",
  "Ensayo corto sobre la resistencia que aparece en cuanto uno intenta hacer un trabajo creativo en serio. Pressfield propone tratarse como un profesional: presentarse cada día, con o sin ganas.")
B("hundred-years", "One Hundred Years of Solitude", "Gabriel García Márquez",
  "Saga de la familia Buendía en el pueblo imaginario de Macondo, donde lo fantástico y la historia de Colombia ocurren en la misma calle. García Márquez escribió el realismo mágico que marcó la novela del siglo XX.")

assert len(books) == len(set(books))

people = []

def P(i, name, role, bio, hue, recs):
    initials = "".join(w[0] for w in name.replace(".", "").split() if w[0].isalpha())
    # Evita iniciales de tres o más cuando el nombre es largo: usa nombre y apellido.
    parts = [w for w in name.replace(".", "").split() if w[0].isupper()]
    if len(parts) >= 2:
        initials = parts[0][0] + parts[-1][0]
    people.append({
        "id": i,
        "name": name,
        "role": role,
        "bio": bio,
        "initials": initials.upper(),
        "hue": hue,
        "recommendations": recs,
    })

def R(book, quote, url, label):
    return {"bookId": book, "quote": quote, "sourceUrl": url, "sourceLabel": label}

# Fuentes reutilizables
NAV_THINK = "https://nav.al/think"
NAV_READ = "https://nav.al/read"
NAV_SKIN = "https://nav.al/accountability-equity"
NAV_LOVE = "https://nav.al/love-read"
GATES = "https://www.gatesnotes.com/holiday-books-2022"
MUSK = "https://fs.blog/elon-musk-book-recommendations/"
CNBC = "https://buffett.cnbc.com/2018/04/20/the-berkshire-hathaway-reading-list.html"
MUNGER_SPEECH = "https://jamesclear.com/great-speeches/psychology-of-human-misjudgment-by-charlie-munger"
BEZOS_1996 = "https://eriklundegaard.com/item/from-the-archives-my-1996-interview-with-jeff-bezos---part-ii"
BEZOS_KUNC = "https://www.kunc.org/2003-06-07/summer-reading-jeff-bezos"
JOBS = "https://www.huffpost.com/entry/the-steve-jobs-reading-list-the-books_n_1024021"
ZUCK = "https://www.businessinsider.com/mark-zuckerberg-book-recommendations-2015-4"
FERRISS_FIC = "https://tim.blog/2012/02/24/the-top-10-fiction-books-for-non-fiction-addicts/"
FERRISS_2008 = "https://tim.blog/2008/12/31/things-ive-learned-and-loved-in-2008/"
FERRISS_GIFTS = "https://tim.blog/2014/10/29/the-books-that-shaped-billionaires-mega-bestselling-authors-and-other-prodigies/"
OBAMA_2025 = "https://www.obama.org/stories/president-obamas-favorite-books-summer-2025/"
OBAMA_2021 = "https://barackobama.medium.com/my-summer-2021-lists-f522aac3b97c"
HOLIDAY = "https://ryanholiday.net/the-reading-list/"
COLLISON = "https://patrickcollison.com/bookshelf"
ANDREESSEN = "https://threadreaderapp.com/thread/1251634412334141440.html"
THIEL_FERRISS = "https://tim.blog/2014/09/09/peter-thiel/"
THIEL_WEEK = "https://theweek.com/articles/443683/peter-thiels-6-favorite-books-that-predict-future"
ALTMAN_HN = "https://news.ycombinator.com/item?id=10423017"
ALTMAN_YC = "https://www.ycombinator.com/blog/ycs-winter-reading-list"
PG_FAQ = "https://paulgraham.com/startupfaq.html"
PG_RAQ = "https://paulgraham.com/raq.html"

LBL_GIFT = "Libros que señaló como favoritos al responder en The Tim Ferriss Show qué libro regala más; recopilación en el blog de Ferriss (2014)."

P("naval-ravikant", "Naval Ravikant", "Emprendedor e inversor",
  "Cofundador de AngelList. Publica en nav.al conversaciones sobre riqueza, conocimiento y cómo decidir qué merece leerse entero.",
  28, [
    R("beginning-of-infinity",
      "I credit this book as being the only book in the last decade—except maybe a few of Nassim Taleb’s works and maybe one or two other scattered books—that made me smarter.",
      NAV_THINK, "Conversación de Naval Ravikant en nav.al, «This Book Changed the Way I Think» (2021)."),
    R("fabric-of-reality",
      "I’m currently stuck in a loop where, at least in science, I’m only going to read The Beginning of Infinity and The Fabric of Reality over and over again until I understand them fully.",
      NAV_READ, "Conversación de Naval Ravikant en nav.al, «Read the Best 100 Books Over and Over Again» (2021)."),
    R("skin-in-the-game",
      "Taleb’s Skin In The Game is required reading. If you want to get anywhere in modern life and understand how modern systems work, then Skin In The Game would be near the top of my list to read.",
      NAV_SKIN, "Conversación de Naval Ravikant en nav.al, «Take Accountability to Earn Equity» (2019)."),
    R("wealth-of-nations",
      "Instead of reading a business book, pick up Adam Smith’s The Wealth of Nations.",
      NAV_LOVE, "Conversación de Naval Ravikant en nav.al, «Read What You Love Until You Love to Read»."),
    R("origin-of-species",
      "Instead of reading a book on biology or evolution that’s written today, I would pick up Darwin’s Origin of the Species.",
      NAV_LOVE, "Conversación de Naval Ravikant en nav.al, «Read What You Love Until You Love to Read»."),
    R("six-easy-pieces",
      "Instead of reading advanced books on cosmology […] you can pick up Richard Feynman’s Six Easy Pieces and start with basic physics.",
      NAV_LOVE, "Conversación de Naval Ravikant en nav.al, «Read What You Love Until You Love to Read»."),
])

P("bill-gates", "Bill Gates", "Cofundador de Microsoft",
  "Cofundador de Microsoft y copresidente de la Fundación Gates. Desde hace años publica en Gates Notes reseñas de lo que recomienda a familia y amigos.",
  205, [
    R("stranger-in-a-strange-land",
      "Of all the sci-fi I read as a teenager, Stranger in a Strange Land is my favorite.",
      "https://www.gatesnotes.com/stranger-in-a-strange-land",
      "Reseña de Bill Gates en Gates Notes (21 de noviembre de 2022)."),
    R("surrender",
      "Even if you’re not [a U2 fan], it’s a super fun read about how a boy from the suburbs of Dublin grew up to become a world-famous rock star and philanthropist.",
      GATES, "Lista de cinco libros favoritos de todos los tiempos, Gates Notes (2022)."),
    R("team-of-rivals",
      "I can’t read enough about Abraham Lincoln, and this is one of the best books on the subject.",
      GATES, "Lista de cinco libros favoritos de todos los tiempos, Gates Notes (2022)."),
    R("inner-game-of-tennis",
      "This book from 1974 is a must-read for anyone who plays tennis, but I think even people who have never played will get something out of it.",
      GATES, "Lista de cinco libros favoritos de todos los tiempos, Gates Notes (2022)."),
    R("mendeleyevs-dream",
      "It’s a fascinating look at how science develops and how human curiosity has evolved over the millennia.",
      GATES, "Lista de cinco libros favoritos de todos los tiempos, Gates Notes (2022)."),
])

P("elon-musk", "Elon Musk", "Empresario",
  "Al frente de Tesla y SpaceX, entre otras compañías. Ha contado en entrevistas que aprendió a hacer cohetes leyendo, y ha citado con nombre los libros que le sirvieron.",
  8, [
    R("foundation",
      "In terms of sci-fi books, I think Isaac Asimov is really great. I like the Foundation series, probably one of the all-time best.",
      MUSK, "Citas de Elon Musk reunidas por Farnam Street."),
    R("moon-harsh-mistress",
      "Robert Heinlein, obviously. I like The Moon Is a Harsh Mistress and I like Stranger in a Strange Land, although it kind of goes off the rails at the end.",
      MUSK, "Citas de Elon Musk reunidas por Farnam Street."),
    R("stranger-in-a-strange-land",
      "I like Stranger in a Strange Land, although it kind of goes off the rails at the end.",
      MUSK, "Citas de Elon Musk reunidas por Farnam Street."),
    R("hitchhikers",
      "I read Hitchhikers Guide to the Galaxy which is quite positive I think and it highlighted an important point which is that a lot of times the question is harder than the answer.",
      MUSK, "Entrevista de Elon Musk con Alison van Diggelen, citada por Farnam Street."),
    R("structures",
      "There’s a good book on structural design called Structures: Or Why Things Don’t Fall Down. It is really, really good if you want a primer on structural design.",
      MUSK, "Citas de Elon Musk reunidas por Farnam Street."),
    R("ignition",
      "There is a good book on rocket stuff called Ignition! by John Clark that’s a really fun one.",
      MUSK, "Citas de Elon Musk reunidas por Farnam Street."),
    R("zero-to-one",
      None,
      MUSK, "Farnam Street recoge que Musk recomienda Zero to One, de su antiguo colega Peter Thiel."),
    R("superintelligence",
      None,
      MUSK, "Farnam Street recoge el tuit de Musk sobre Superintelligence, donde advertía de que la IA podía ser «potentially more dangerous than nukes»."),
    R("franklin-isaacson",
      None,
      MUSK, "Farnam Street recoge que Musk recomienda la biografía de Benjamin Franklin escrita por Walter Isaacson."),
])

P("warren-buffett", "Warren Buffett", "Inversor",
  "Presidente de Berkshire Hathaway. En las juntas de accionistas ha repetido, con el libro en la mano metafórica, qué hay que leer antes de comprar una acción.",
  142, [
    R("intelligent-investor",
      "All of the important ideas in investing … are in that book.",
      CNBC, "Archivo de CNBC sobre las juntas de Berkshire: Buffett lo recomienda «first and foremost» (junta de 1996)."),
    R("essays-buffett",
      "We’ve said exactly what we do.",
      CNBC, "Junta de Berkshire de 2000, archivo de CNBC: Buffett llama a este libro el más representativo de su manera de invertir."),
    R("common-stocks",
      "Those two books were terrific books.",
      CNBC, "Junta de Berkshire de 2004, archivo de CNBC: Buffett recomienda los libros de Phil Fisher, entre ellos Common Stocks and Uncommon Profits."),
])

P("charlie-munger", "Charlie Munger", "Inversor",
  "Durante décadas fue vicepresidente de Berkshire Hathaway y el interlocutor de Buffett en las juntas. Recomendaba libros del mismo modo que repartía modelos mentales: en voz alta y sin suavizar.",
  168, [
    R("influence",
      "If you have half as much sense as I think you do, you will immediately order copies for all of your children and several of your friends. You will never make a better investment.",
      MUNGER_SPEECH, "Discurso de Charlie Munger en Harvard (1995), «The Psychology of Human Misjudgment», transcripción de James Clear."),
    R("guns-germs-steel",
      "It’s the best work of its kind I have ever read.",
      CNBC, "Junta de Berkshire de 1998, archivo de CNBC: Munger recomienda Armas, gérmenes y acero."),
])

P("jeff-bezos", "Jeff Bezos", "Fundador de Amazon",
  "Fundó Amazon en 1994. En entrevistas de los primeros años de la empresa contestó, sin lista preparada, cuáles eran sus novelas.",
  32, [
    R("remains-of-the-day",
      "My wife got me to read Remains of the Day and I liked that a lot.",
      BEZOS_1996, "Entrevista de Jeff Bezos con Erik Lundegaard, octubre de 1996 (publicada en The Seattle Times)."),
    R("dune",
      "It used to be Dune. I’m sort of a techno-geek, propeller-head, science-fiction type.",
      BEZOS_1996, "Entrevista de Jeff Bezos con Erik Lundegaard, octubre de 1996."),
])

P("steve-jobs", "Steve Jobs", "Cofundador de Apple",
  "Cofundador de Apple y de Pixar. Lo que leía de joven —espiritualidad, Shakespeare, dieta— quedó contado por él en la biografía de Walter Isaacson.",
  220, [
    R("be-here-now",
      "It was profound. It transformed me and many of my friends.",
      JOBS, "Steve Jobs a Walter Isaacson, citado por HuffPost a partir de la biografía (2011)."),
    R("autobiography-yogi",
      None,
      JOBS, "HuffPost, citando a Isaacson: era el único libro en su iPad 2 y lo releía una vez al año desde la adolescencia."),
    R("king-lear",
      "I loved King Lear.",
      JOBS, "Steve Jobs, recordando sus lecturas de instituto, citado por HuffPost vía Isaacson."),
    R("diet-small-planet",
      "That’s when I swore off meat pretty much for good.",
      JOBS, "Steve Jobs a Isaacson, citado por HuffPost, sobre Diet for a Small Planet."),
    R("moby-dick",
      None,
      JOBS, "HuffPost, citando a Isaacson: Moby-Dick estaba entre las lecturas favoritas de Jobs en el instituto."),
])

P("mark-zuckerberg", "Mark Zuckerberg", "Cofundador de Meta",
  "Cofundador y consejero delegado de Meta. En 2015 dedicó el año a leer un libro cada dos semanas y a explicar en Facebook por qué lo elegía.",
  214, [
    R("sapiens",
      "Following the Muqaddimah, which was a history from the perspective of an intellectual in the 1300s, Sapiens is a contemporary exploration of many similar questions.",
      ZUCK, "Publicación de Mark Zuckerberg en A Year of Books (2015), citada por Business Insider."),
    R("muqaddimah",
      "While much of what was believed then is now disproven after 700 more years of progress, it’s still very interesting to see what was understood at this time and the overall worldview when it’s all considered together.",
      ZUCK, "Publicación de Mark Zuckerberg en A Year of Books (2015), citada por Business Insider."),
    R("new-jim-crow",
      "I’ve been interested in learning about criminal justice reform for a while, and this book was highly recommended by several people I trust.",
      ZUCK, "Publicación de Mark Zuckerberg en A Year of Books (2015), citada por Business Insider."),
    R("end-of-power",
      "The trend towards giving people more power is one I believe in deeply.",
      ZUCK, "Publicación de Mark Zuckerberg en A Year of Books (2015), citada por Business Insider."),
    R("creativity-inc",
      "I love reading first-hand accounts about how people build great companies like Pixar and nurture innovation and creativity.",
      ZUCK, "Publicación de Mark Zuckerberg en A Year of Books (2015), citada por Business Insider."),
    R("on-immunity",
      "The science is completely clear: vaccinations work and are important for the health of everyone in our community.",
      ZUCK, "Publicación de Mark Zuckerberg en A Year of Books (2015), citada por Business Insider."),
    R("gang-leader",
      "The more we all have a voice to share our perspectives, the more empathy we have for each other and the more we respect each other’s rights.",
      ZUCK, "Publicación de Mark Zuckerberg en A Year of Books (2015), citada por Business Insider."),
    R("dealing-with-china",
      "Over the last 35 years, China has experienced one of the greatest economic and social transformations in human history.",
      ZUCK, "Publicación de Mark Zuckerberg en A Year of Books (2015), citada por Business Insider."),
])

P("tim-ferriss", "Tim Ferriss", "Autor y presentador",
  "Autor de La semana laboral de 4 horas y presentador de The Tim Ferriss Show. Lleva años publicando en su blog las novelas y los estoicos que regala.",
  18, [
    R("zorba",
      "I have recommended this outstanding book before. […] Zorba reminds us how to live fully.",
      FERRISS_FIC, "Tim Ferriss, «The Top 10 Fiction Books for Non-Fiction Addicts», tim.blog (2012)."),
    R("musashi",
      "I never expected to finish it, and I tore through it in less than two weeks.",
      FERRISS_FIC, "Tim Ferriss, «The Top 10 Fiction Books for Non-Fiction Addicts», tim.blog (2012)."),
    R("stranger-in-a-strange-land",
      "Ever feel like you don’t quite fit in? Don’t want to follow society’s silly rules? Then you can probably relate to human-born and Martian-raised Valentine Michael Smith.",
      FERRISS_FIC, "Tim Ferriss, «The Top 10 Fiction Books for Non-Fiction Addicts», tim.blog (2012)."),
    R("enders-game",
      "If people ask me, for instance, “Which books should I read on leadership?”, I might reply: “Dune and Ender’s Game.”",
      FERRISS_FIC, "Tim Ferriss, «The Top 10 Fiction Books for Non-Fiction Addicts», tim.blog (2012)."),
    R("dune",
      "Dune presents, despite my synopsis, perhaps the most incredibly detailed and oddly believable fictional landscape I’ve ever encountered.",
      FERRISS_FIC, "Tim Ferriss, «The Top 10 Fiction Books for Non-Fiction Addicts», tim.blog (2012)."),
    R("hitchhikers",
      "If you need humor to make the jump to fiction, this might be your gateway drug.",
      FERRISS_FIC, "Tim Ferriss, «The Top 10 Fiction Books for Non-Fiction Addicts», tim.blog (2012)."),
    R("fahrenheit-451",
      "This classic work on state censorship remains as relevant in today’s world of digital delights as it was when published in the black-and-white world of 1953.",
      FERRISS_FIC, "Tim Ferriss, «The Top 10 Fiction Books for Non-Fiction Addicts», tim.blog (2012)."),
    R("letters-seneca",
      "Zorba the Greek and Seneca: Letters from a Stoic. These are two of the most readable books of practical philosophies I’ve ever had the fortune to encounter.",
      FERRISS_2008, "Tim Ferriss, «Things I’ve Learned and Loved in 2008», tim.blog."),
])

P("barack-obama", "Barack Obama", "44.º presidente de Estados Unidos",
  "Publica cada verano, en la Fundación Obama y en Medium, los libros que ha leído y quiere pasar a otros. Las frases de 2025 son suyas.",
  210, [
    R("mark-twain", "A comprehensive biography of one of the most important writers and social commentators in American history.", OBAMA_2025, "Lista de verano de 2025, Fundación Obama."),
    R("abundance", "A must-read for progressives who want a blueprint for reforming government so it can deliver for working people.", OBAMA_2025, "Lista de verano de 2025, Fundación Obama."),
    R("king-of-ashes", "One of my favorite crime fiction writers delivers in this story of family, ambition and corruption in a racially charged and violent South.", OBAMA_2025, "Lista de verano de 2025, Fundación Obama."),
    R("marriage-at-sea", "Amazing true story of a couple surviving crisis in the open seas.", OBAMA_2025, "Lista de verano de 2025, Fundación Obama."),
    R("who-is-government", "A timely reminder of the quiet dedication and skill of the people who work every day to make this country work.", OBAMA_2025, "Lista de verano de 2025, Fundación Obama."),
    R("sirens-call", "A useful primer on how social media and the attention economy have warped our democracy and reshaped our lives.", OBAMA_2025, "Lista de verano de 2025, Fundación Obama."),
    R("book-of-records", "A beautiful fable about migration, memory, and the struggle to recognize our common humanity.", OBAMA_2025, "Lista de verano de 2025, Fundación Obama."),
    R("empire-of-pain", None, OBAMA_2021, "Lista de verano de 2021 publicada por Barack Obama en Medium: libros que había leído y esperaba que otros disfrutaran."),
    R("project-hail-mary", None, OBAMA_2021, "Lista de verano de 2021 publicada por Barack Obama en Medium."),
    R("klara-and-the-sun", None, OBAMA_2021, "Lista de verano de 2021 publicada por Barack Obama en Medium."),
])

P("ryan-holiday", "Ryan Holiday", "Escritor",
  "Autor de libros sobre estoicismo y librero en The Painted Porch. Mantiene en su web una lista de los libros sobre los que, dice, se puede apoyar una vida.",
  350, [
    R("meditations",
      "To me, this is not only one of greatest books ever written but perhaps the only book of its kind.",
      HOLIDAY, "Ryan Holiday, «Books To Base Your Life On», ryanholiday.net."),
    R("letters-seneca",
      "After Marcus Aurelius, this is one of my favorite books. […] Seneca’s letters are the best place to start.",
      HOLIDAY, "Ryan Holiday, «Books To Base Your Life On», ryanholiday.net."),
    R("shortness-of-life",
      "The essays in On the Shortness of Life are excellent as well.",
      HOLIDAY, "Ryan Holiday, «Books To Base Your Life On», ryanholiday.net."),
    R("mans-search",
      "Frankl is one of the most profound modern thinkers on meaning and purpose.",
      HOLIDAY, "Ryan Holiday, «Books To Base Your Life On», ryanholiday.net."),
    R("score-takes-care",
      "Even if you’ve never watched a down of football, you’ll get something out of this book.",
      HOLIDAY, "Ryan Holiday, «Books To Base Your Life On», ryanholiday.net."),
    R("endurance-lansing",
      "This book (and his life) were living proof of his family motto: “Fortitudine vincimus” (By endurance we conquer).",
      HOLIDAY, "Ryan Holiday, «Books To Base Your Life On», ryanholiday.net."),
    R("black-swan",
      "You can draw a pretty straight line from Seneca […] to the modern day writings of Nassim Nicholas Taleb (read: The Black Swan, Fooled By Randomness and The Bed of Procrustes).",
      HOLIDAY, "Ryan Holiday, «Books To Base Your Life On», ryanholiday.net."),
    R("fooled-by-randomness",
      "Read: The Black Swan, Fooled By Randomness and The Bed of Procrustes.",
      HOLIDAY, "Ryan Holiday, «Books To Base Your Life On», ryanholiday.net."),
    R("bed-of-procrustes",
      "Read: The Black Swan, Fooled By Randomness and The Bed of Procrustes.",
      HOLIDAY, "Ryan Holiday, «Books To Base Your Life On», ryanholiday.net."),
    R("antifragile", None, FERRISS_GIFTS, LBL_GIFT),
    R("vasari-lives",
      "What I like about this book is that the profiles are not about statesmen or generals but artists.",
      HOLIDAY, "Ryan Holiday, «Books To Base Your Life On», ryanholiday.net."),
    R("forty-eight-laws",
      "You MUST read his books. His work on power and strategy are critical for anyone trying to accomplish anything.",
      HOLIDAY, "Ryan Holiday, «Books To Base Your Life On», ryanholiday.net."),
    R("what-makes-sammy",
      "What Makes Sammy Run? is Ari Gold before Ari Gold existed.",
      HOLIDAY, "Ryan Holiday, «Books To Base Your Life On», ryanholiday.net."),
    R("franklin-isaacson", None, FERRISS_GIFTS, LBL_GIFT),
])

P("patrick-collison", "Patrick Collison", "Cofundador de Stripe",
  "Cofundador y consejero delegado de Stripe. En su web mantiene una estantería de los libros que posee y marca en negrita los que considera particularmente buenos.",
  262, [
    R("beginning-of-infinity", None, COLLISON, "Estantería de Patrick Collison: lo marcó entre los libros particularmente buenos."),
    R("poor-charlie", None, COLLISON, "Estantería de Patrick Collison: lo marcó entre los libros particularmente buenos."),
    R("rise-fall-growth", None, COLLISON, "Estantería de Patrick Collison: lo marcó entre los libros particularmente buenos."),
    R("dream-machine", None, COLLISON, "Estantería de Patrick Collison: lo marcó entre los libros particularmente buenos."),
    R("hamming", None, COLLISON, "Estantería de Patrick Collison: lo marcó entre los libros particularmente buenos."),
    R("democracy-in-america", None, COLLISON, "Estantería de Patrick Collison: lo marcó entre los libros particularmente buenos."),
])

P("marc-andreessen", "Marc Andreessen", "Inversor",
  "Cofundador de Netscape y de Andreessen Horowitz. En abril de 2020 acompañó su ensayo «It’s Time to Build» con un hilo de libros.",
  24, [
    R("whole-earth-discipline",
      "On why even environmentalists should be pro building, pro cities, pro nuclear, and pro genetic engineering.",
      ANDREESSEN, "Hilo de Marc Andreessen en Twitter, 18 de abril de 2020 (archivo legible en Thread Reader)."),
    R("more-from-less",
      "On how modern technological economies can build more outputs with less inputs, and why we need all economies to be modern and technological.",
      ANDREESSEN, "Hilo de Marc Andreessen en Twitter, 18 de abril de 2020."),
    R("triumph-of-the-city",
      "On the central role cities play in our world and why it’s so important for us to build them — more, bigger, better.",
      ANDREESSEN, "Hilo de Marc Andreessen en Twitter, 18 de abril de 2020."),
    R("edison-morris",
      "On perhaps the greatest American builder of all, the builder who brought electricity to us all, Thomas Edison.",
      ANDREESSEN, "Hilo de Marc Andreessen en Twitter, 18 de abril de 2020."),
    R("the-tycoons",
      "On how four great builders of the 19th century built the world we live in today.",
      ANDREESSEN, "Hilo de Marc Andreessen en Twitter, 18 de abril de 2020."),
    R("golden-gates",
      "On why we can’t build in great American cities like San Francisco today and what we need to do about it.",
      ANDREESSEN, "Hilo de Marc Andreessen en Twitter, 18 de abril de 2020."),
])

P("peter-thiel", "Peter Thiel", "Inversor",
  "Cofundador de PayPal y de Palantir, e inversor inicial en Facebook. Ha señalado en entrevistas el libro que más le ha influido y, en The Week, seis títulos sobre el futuro.",
  268, [
    R("things-hidden",
      "Girard gives a sweeping view of the whole human experience on this planet — something captured in the title of his masterwork, Things Hidden Since the Foundation of the World.",
      THIEL_FERRISS, "Entrevista de Peter Thiel con Tim Ferriss (2014): el libro que más ha regalado."),
    R("sovereign-individual", None, THIEL_WEEK, "Los seis libros favoritos de Peter Thiel sobre el futuro, publicados por The Week."),
    R("black-swan", None, THIEL_WEEK, "Los seis libros favoritos de Peter Thiel sobre el futuro, publicados por The Week."),
    R("diamond-age", None, THIEL_WEEK, "Los seis libros favoritos de Peter Thiel sobre el futuro, publicados por The Week."),
    R("right-stuff", None, THIEL_WEEK, "Los seis libros favoritos de Peter Thiel sobre el futuro, publicados por The Week."),
    R("new-atlantis", None, THIEL_WEEK, "Los seis libros favoritos de Peter Thiel sobre el futuro, publicados por The Week."),
])

P("sam-altman", "Sam Altman", "Consejero delegado de OpenAI",
  "Consejero delegado de OpenAI y expresidente de Y Combinator. En un AMA de 2015 enseñó a cámara los libros que daría a un fundador joven, y lo comentó al día siguiente en Hacker News.",
  199, [
    R("zero-to-one", None, ALTMAN_HN, "AMA de Twitter de Sam Altman (21 de octubre de 2015), transcrito ese día en Hacker News. Altman intervino en el hilo."),
    R("thinking-fast", None, ALTMAN_HN, "AMA de Twitter de Sam Altman (21 de octubre de 2015), transcrito ese día en Hacker News."),
    R("score-takes-care", None, ALTMAN_HN, "AMA de Twitter de Sam Altman (21 de octubre de 2015), transcrito ese día en Hacker News."),
    R("dealers-of-lightning", None, ALTMAN_HN, "AMA de Twitter de Sam Altman (21 de octubre de 2015), transcrito ese día en Hacker News."),
    R("the-supermen", "That one’s particularly good.", ALTMAN_HN, "AMA de Twitter de Sam Altman (21 de octubre de 2015). La nota es del transcriptor, que recogió el comentario de Altman al enseñar el libro."),
    R("beak-of-the-finch", None, ALTMAN_HN, "AMA de Twitter de Sam Altman (21 de octubre de 2015), transcrito ese día en Hacker News."),
    R("art-of-war-middle-ages", "This is correct—art of war in the Middle Ages.", ALTMAN_HN, "Comentario del propio Sam Altman en el hilo de Hacker News, corrigiendo el título."),
    R("pandaemonium",
      "This is an incredible read, and as we sit in the middle of the software revolution it’s worthwhile to see what people thought as the industrial revolution was happening.",
      ALTMAN_YC, "Lista de invierno de Y Combinator (2016), con la frase de Sam Altman."),
])

P("paul-graham", "Paul Graham", "Ensayista y cofundador de Y Combinator",
  "Ensayista y cofundador de Y Combinator. En sus preguntas frecuentes recomienda pocos libros, y los nombra.",
  16, [
    R("soul-new-machine",
      "The best source of information about startups is probably not business books, but histories of particular startups and industries. The most famous is Tracy Kidder’s Soul of a New Machine.",
      PG_FAQ, "Paul Graham, «Startup FAQ», paulgraham.com."),
    R("how-to-win-friends",
      "The one book we encourage startup founders to read is Dale Carnegie’s How to Win Friends and Influence People.",
      PG_FAQ, "Paul Graham, «Startup FAQ», paulgraham.com."),
    R("franklin-autobiography",
      "I’d also recommend Franklin’s Autobiography.",
      PG_FAQ, "Paul Graham, «Startup FAQ», paulgraham.com."),
    R("vasari-lives", None, PG_RAQ, "Paul Graham, «RAQs»: lo incluye entre los libros de historia que le parecen más estimulantes."),
    R("art-of-war-middle-ages", None, PG_RAQ, "Paul Graham, «RAQs»: lo incluye entre los libros de historia que le parecen más estimulantes."),
    R("medieval-technology", None, PG_RAQ, "Paul Graham, «RAQs»: lo incluye entre los libros de historia que le parecen más estimulantes."),
])

P("kevin-kelly", "Kevin Kelly", "Cofundador de Wired",
  "Cofundador y primer director ejecutivo de Wired, y autor de libros sobre tecnología y cultura. Estas son las obras que señaló como favoritas en The Tim Ferriss Show.",
  186, [
    R("cats-cradle", None, FERRISS_GIFTS, LBL_GIFT),
    R("psychedelic-explorers", None, FERRISS_GIFTS, LBL_GIFT),
    R("johnny-bunko", None, FERRISS_GIFTS, LBL_GIFT),
    R("so-good", None, FERRISS_GIFTS, LBL_GIFT),
    R("shantaram", None, FERRISS_GIFTS, LBL_GIFT),
])

P("tony-robbins", "Tony Robbins", "Formador y autor",
  "Formador y autor de libros de desarrollo personal. En The Tim Ferriss Show enumeró los libros que considera favoritos y que más ha regalado.",
  4, [
    R("as-a-man-thinketh", None, FERRISS_GIFTS, LBL_GIFT),
    R("mans-search", None, FERRISS_GIFTS, LBL_GIFT),
    R("fourth-turning", None, FERRISS_GIFTS, LBL_GIFT),
    R("mindset", None, FERRISS_GIFTS, LBL_GIFT),
])

P("peter-diamandis", "Peter Diamandis", "Fundador de XPRIZE",
  "Fundador de la Fundación XPRIZE y coautor de Abundancia. En The Tim Ferriss Show dejó los libros que señala como favoritos.",
  196, [
    R("spirit-st-louis", None, FERRISS_GIFTS, LBL_GIFT),
    R("atlas-shrugged", None, FERRISS_GIFTS, LBL_GIFT),
    R("man-who-sold-the-moon", None, FERRISS_GIFTS, LBL_GIFT),
    R("singularity-kurzweil", None, FERRISS_GIFTS, LBL_GIFT),
])

P("ed-catmull", "Ed Catmull", "Cofundador de Pixar",
  "Cofundador de Pixar y durante años su presidente. Entre los libros que señaló como favoritos hay mito, viaje del héroe y un álbum infantil.",
  230, [
    R("hero-thousand-faces", None, FERRISS_GIFTS, LBL_GIFT),
    R("heros-journey", None, FERRISS_GIFTS, LBL_GIFT),
    R("one-monster", None, FERRISS_GIFTS, LBL_GIFT),
])

P("james-altucher", "James Altucher", "Inversor y autor",
  "Inversor y autor. En The Tim Ferriss Show enumeró una lista larga de favoritos; aquí va una selección de esa lista, sin añadir títulos que no estuvieran.",
  48, [
    R("antifragile", None, FERRISS_GIFTS, LBL_GIFT),
    R("black-swan", None, FERRISS_GIFTS, LBL_GIFT),
    R("fooled-by-randomness", None, FERRISS_GIFTS, LBL_GIFT),
    R("fight-club", None, FERRISS_GIFTS, LBL_GIFT),
    R("outliers", None, FERRISS_GIFTS, LBL_GIFT),
    R("kite-runner", None, FERRISS_GIFTS, LBL_GIFT),
])

P("ramit-sethi", "Ramit Sethi", "Autor",
  "Autor de Te enseñaré a ser rico. En The Tim Ferriss Show señaló como favoritos varios libros de psicología social y de hábitos profesionales.",
  130, [
    R("checklist-manifesto", None, FERRISS_GIFTS, LBL_GIFT),
    R("never-eat-alone", None, FERRISS_GIFTS, LBL_GIFT),
    R("social-animal-aronson", None, FERRISS_GIFTS, LBL_GIFT),
])

P("joshua-waitzkin", "Joshua Waitzkin", "Ajedrecista y autor",
  "Ajedrecista de niño —inspiró la película En busca de Bobby Fischer— y autor de El arte de aprender. Esta es la selección de favoritos que dio en The Tim Ferriss Show.",
  88, [
    R("on-the-road", None, FERRISS_GIFTS, LBL_GIFT),
    R("tao-te-ching", None, FERRISS_GIFTS, LBL_GIFT),
    R("zen-motorcycle", None, FERRISS_GIFTS, LBL_GIFT),
    R("shantaram", None, FERRISS_GIFTS, LBL_GIFT),
    R("old-man-sea", None, FERRISS_GIFTS, LBL_GIFT),
])

P("brian-koppelman", "Brian Koppelman", "Guionista y director",
  "Coguionista de Rounders y cocreador de Billions. Entre los libros que señaló como favoritos está la novela de Hollywood que también recomienda Ryan Holiday.",
  310, [
    R("what-makes-sammy", None, FERRISS_GIFTS, LBL_GIFT),
    R("war-of-art", None, FERRISS_GIFTS, LBL_GIFT),
])

P("neil-strauss", "Neil Strauss", "Autor",
  "Autor de varios superventas. En The Tim Ferriss Show incluyó entre sus favoritos a Séneca y a García Márquez.",
  332, [
    R("shortness-of-life", None, FERRISS_GIFTS, LBL_GIFT),
    R("hundred-years", None, FERRISS_GIFTS, LBL_GIFT),
])

# Validar
ids = {b["id"] for b in books.values()}
for p in people:
    seen = set()
    for r in p["recommendations"]:
        if r["bookId"] not in ids:
            raise SystemExit(f"libro desconocido {r['bookId']} en {p['id']}")
        if r["bookId"] in seen:
            raise SystemExit(f"duplicado {r['bookId']} en {p['id']}")
        seen.add(r["bookId"])
        if r["quote"] is not None and not r["quote"].strip():
            raise SystemExit("cita vacía")

out_books = list(books.values())
(ROOT / "data" / "books.json").write_text(json.dumps(out_books, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(ROOT / "data" / "people.json").write_text(json.dumps(people, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
nrec = sum(len(p["recommendations"]) for p in people)
print(f"personas={len(people)} libros={len(out_books)} recomendaciones={nrec}")
