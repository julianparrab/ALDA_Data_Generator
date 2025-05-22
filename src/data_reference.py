# Dictionary with SMMLV and IVP values by year
values_by_year= {
    2020: {"salario_minimo": 877803, "ivp": 0.4379},
    2021: {"salario_minimo": 908526, "ivp": 0.432},
    2022: {"salario_minimo": 1000000, "ivp": 0.4581},
    2023: {"salario_minimo": 1160000, "ivp": 0.4476},
    2024: {"salario_minimo": 1300000, "ivp": 0.4745}
}

# Locality in Bogotá where the tree is located
localidades = {
    1: "USAQUÉN",
    2: "CHAPINERO",
    3: "SANTA FÉ",
    4: "SAN CRISTÓBAL",
    5: "USME",
    6: "TUNJUELITO",
    7: "BOSA",
    8: "KENNEDY",
    9: "FONTIBÓN",
    10: "ENGATIVÁ",
    11: "SUBA",
    12: "BARRIOS UNIDOS",
    13: "TEUSAQUILLO",
    14: "LAS MÁRTIRES",
    15: "ANTONIO NARIÑO",
    16: "PUENTE ARANDA",
    17: "LA CANDELARIA",
    18: "RAFAEL URIBE",
    19: "CIUDAD BOLÍVAR"
}

# Botanical species of the tree
especies = especies = ['Araucaria','Araucaria crespa','Cipres, Pino cipres, Pino','Pino candelabro','Pino patula','Cipres italiano','Pino hayuelo',
                       'Cipres enano','Pino azul','Pino australiano','Pino colombiano, pino de pacho, pino romeron','Pino colombiano, chaquiro',
                       'Eucalipto común','Eucalipto pomarroso','Eucalipto plateado','Eucalipto de flor, eucalipto lavabotella','Eucalipto',
                       'Palma de cera, Palma blanca','Palma coquito','Palma yuca, palmiche','Palma fenix','Palma washingtoniana','Helecho palma',
                       'Urapán, Fresno','Acacia japonesa','Acacia negra, gris','Acacia de jardin','Acacia baracatinga, acacia sabanera, acacia nigra',
                       'Acacia blanca, leucaena','Carbonero rojo','Carbonero rosado','Aliso, fresno, chaquiro','Cedro, cedro andino, cedro clavel',
                       'Nogal, cedro nogal, cedro negro','Roble','Caucho de la india, caucho','Caucho sabanero','Caucho tequendama','Cerezo, capuli',
                       'Durazno comun','Duraznillo, velitas','Eugenia','Roble australiano','Guayacan de Manizales','Hojarasco','Liquidambar, estoraque',
                       'Magnolio','Sangregao, drago, croto','Sauce lloron','Alcaparro doble','Alcaparro enano','Amarrabollo','Arboloco',
                       'Cajeto, garagay, urapo','Cedrillo, Yuco','Corono','Cucharo','Falso pimiento','Gaque','Jazmin de la china',
                       'Jazmin del cabo, laurel huesito','Laurel de cera (hoja pequeña)','Laurel de cera','Mangle de tierra fria','Mano de oso',
                       'Mortillo','Raque, San juanito','Sietecueros nazareno','Sietecueros real','Tibar, pagoda o rodamonte','Yarumo','Abutilon blanco',
                       'Abutilon rojo y amarillo (Farolito)','Arrayan blanco','Brevo','Papayuelo','Calistemo lloron','Cayeno',
                       'Chicala, chirlobirlo, flor amarillo','Chilco','Chocho','Ciro','Ciruelo','Dividivi de tierra fria','Espino, Garbancillo',
                       'Feijoa','Gurrubo','Hayuelo','Higuerillo','Higueron','Holly espinoso','Holly liso','Platano de tierra fria','Sauco','Trompeto',
                       'Tuno roso','Aguacate','Sombrilla japonesa','Guamo santafereño','Encenillo','Alamo de lombardia','Tomate de arbol','Mandarina',
                       'Garrocho','Cafe','NN','Otro','Pino libro','Cipres Japones, criptomeria','Eucalipto','Eucalipto blanco',
                       'Palma de cera, Palma de ramo','Palma de yuca, Palma de bayoneta','Palma de datiles','Palma roebeleni','Palma payanesa',
                       'Palma sancona','Acacia morada','Acacia','Carbonero','Caucho','Caucho benjamin','Caucho lira','Guayabo brasilero','Cordoncillo',
                       'Salvio negro','Laurel europeo','Sangregado','Tibar, Rodamonte, Pagoda','Gaquillo','Pitosporo','Arrayan negro','Callistemo',
                       'Corazon de pollo','Schefflera, Pategallina hojigrande','Schefflera, Pategallina hojipequeña','Gualanday','Amarguero amarillo',
                       'Tabaquillo','Algodoncillo','Guayabo','Pimiento','Olivo','Naranjo','Borrachero blanco','Borrachero rojo',
                       'Caballero de la noche, Jazmin, Dama de noche','Granado','Tominejero','Cariseco, Tres hojas','Tomatillo','Cucubo',
                       'Algodon extranjero','Pino','Cipres','Eucalipto plateado','Tibar extranjero','Guayabillo','Uva camarona','Uva de Anis',
                       'Salvio morado','Nispero','Pomarroso','Curapin, Campanilla','Quina','Metrosideros','Arbol de corcho','Pero','Manzano',
                       'Pino Montezuma','Limon','Acacia','Palo blanco','Arbol pipermint','Algodoncillo','Chirimoyo','Pate vaca','Ayer, hoy y mañana',
                       'Salton o Charne','Carbonero','Calistemo','Caballero de la noche','Arupo','Palma areca','Citrus spp.','Manzano de monte',
                       'Sangregado','Cipres','Palma funeral','Chiripique','Chocho, balu, cambulo','Tibar, tobo, rodamonte','Eucalipto manchado',
                       'Eucalipto','Bonetero del Japon','Liberal o lechero','Caucho','Fucsia boliviana','Motilon, chuguaca','Guamo','Jazmin amarillo',
                       'Lavatera, Malvavisco morado','Leptospermun','Aligustre del Japon','Magnolia rosada','Malvavisco','Tuno esmeraldo','Tuno','Tuno',
                       'Tinto','Angelito','Arrayan','Cucharo','Susque','Yolombo','Fenix','Pino','Cerezo, ciruelo','Romero','Jomi, upacon','Tinto',
                       'Tecomaria','Trompo','Yuca, palma yuca','Olmo de agua','Schefflera, Yuco blanco','Schefflera, Tortolito','Schefflera',
                       'Schefflera pategallina peludo','Abutilonpequeño','Arce','Té de Bogotá','Almanegra, quedo','Lembo, pategallo','Diosme',
                       'Ocobo, Guayacan','Gardenia','Granizo','Balso blanco','Romero de paramo','Chirriador','Siete Cueros peludo','Canelo','Pegamosco',
                       'Punta de lanza','Tulipan africano','Acacia blanca, Cultriformes','Buganbil, veranera','Boj','Camelia','Pajarito','Mangostino',
                       'Acebo','Venturosa','Cidron','Azuceno, enebro','Ombu, Arbol de la bella sombra','Árbol de platano','Cafetillo, crucito','Azalea',
                       'Mimbre','Moquillo','Ceiba de tierra fria','Guayabo de pava','Lulo de perro','Aloe arboreo','Balazo','Camaron','Cigarrillo',
                       'Dalia','Rosa','Manto de Maria','Hebe','Marihuana','Mermelada','Mirto','Retamo','Palma cinta','Aralia japonesa','Abelia',
                       'Azara','Guayabo anselmo, Champo','Moradilla','Hiperico, Corazoncillo','Platano','Secuoya','Algarrobo','Anona','Arbol de neem',
                       'Arbol de Te','Arupo','Guacimo','Mamey','Oreja de Burro','Punga','Totumillo','Espino blanco','Guarana, guacharo','Guayabo de mico',
                       'Tachuelo','Mango','Morera','Nacedero','Tabaquillo','Flor morado','Escolin, Espadero','Pimiento negro','Fotinia','Ojo de perdiz',
                       'Motilón','Cipres','Tinto','Agracejo','Arrayan','Mulato','Cucharo','Fucsia arbustiva','Tagua','Crucito','Cerezo','Tuno roso',
                       'Palma Alejandra','Abutilon quesito','Acacia azul','Alcaparro enano','Arbol de hierro','Ardicia','Aromo','Cajeto','Cajeto',
                       'Cajeto de Bogota','Cerezo','Chicala rosado','Guayabo del peru','Holly liso','Jazmin australiano','Mano de oso']


# Type of silvicultural treatment applied
tratamientos = ['Poda', 'Tala', 'Control Fitosanitario']

# Type of space where the tree is located
espacios = ['Publico', 'Privado']

# Condition of the trunk (tree stem)
estados_fuste = ['Bueno', 'Regular', 'Malo']

# Condition of the crown (upper part of the tree)
estados_copa = ['Denso', 'Claro', 'Ralo']

# Condition of the tree roots
estados_raiz = ['Estable', 'Inestable', 'Expuesta']

# General phytosanitary condition of the tree (health)
estados_fitosanitarios = ['Sano', 'Enfermo', 'Plagas']

# Risk level represented by the tree
riesgos = ['Bajo', 'Medio', 'Alto']

# Autorizado
autorizado = ['OTRO', 'ENEL', 'IDU', 'JBB','UAESP', 'EEAB']

#
