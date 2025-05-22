from typing import Dict, List
import os
import csv


class DataReference:
    """Clase que contiene todos los datos de referencia para la generación"""

    @staticmethod
    def csv_a_diccionario(ruta_archivo: str) -> Dict[str, Dict[str, float]]:
        """
        Convierte un archivo CSV con datos de árboles en un diccionario de Python.
        Estructura esperada del CSV:
        nombre_comun,min_pap,max_pap,min_alturatotal,max_alturatotal,min_diamcopamayor,max_diamcopamayor,min_diamcopamenor,max_diamcopamenor,total
        """
        especies = {}

        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            i = 1
            for fila in lector:
                especie_id = i
                i += 1
                nombre = fila["nombre_comun"].strip()

                especies[especie_id] = {
                    "nombre_comun": nombre,
                    "min_pap": float(fila["min_pap"]),
                    "max_pap": float(fila["max_pap"]),
                    "min_alturatotal": float(fila["min_alturatotal"]),
                    "max_alturatotal": float(fila["max_alturatotal"]),
                    "min_diamcopamayor": float(fila["min_diamcopamayor"]),
                    "max_diamcopamayor": float(fila["max_diamcopamayor"]),
                    "min_diamcopamenor": float(fila["min_diamcopamenor"]),
                    "max_diamcopamenor": float(fila["max_diamcopamenor"]),
                    "total": int(fila["total"]),
                }

        return especies

    ESPECIES = csv_a_diccionario("data/info_especies.csv")

    # Lista de especies
    # ESPECIES = ['Araucaria','Araucaria crespa','Cipres, Pino cipres, Pino','Pino candelabro','Pino patula','Cipres italiano','Pino hayuelo','Cipres enano','Pino azul','Pino australiano','Pino colombiano, pino de pacho, pino romeron','Pino colombiano, chaquiro','Eucalipto común','Eucalipto pomarroso','Eucalipto plateado','Eucalipto de flor, eucalipto lavabotella','Eucalipto','Palma de cera, Palma blanca','Palma coquito','Palma yuca, palmiche','Palma fenix','Palma washingtoniana','Helecho palma','Urapán, Fresno','Acacia japonesa','Acacia negra, gris','Acacia de jardin','Acacia baracatinga, acacia sabanera, acacia nigra','Acacia blanca, leucaena','Carbonero rojo','Carbonero rosado','Aliso, fresno, chaquiro','Cedro, cedro andino, cedro clavel','Nogal, cedro nogal, cedro negro','Roble','Caucho de la india, caucho','Caucho sabanero','Caucho tequendama','Cerezo, capuli','Durazno comun','Duraznillo, velitas','Eugenia','Roble australiano','Guayacan de Manizales','Hojarasco','Liquidambar, estoraque','Magnolio','Sangregao, drago, croto','Sauce lloron','Alcaparro doble','Alcaparro enano','Amarrabollo','Arboloco','Cajeto, garagay, urapo','Cedrillo, Yuco','Corono','Cucharo','Falso pimiento','Gaque','Jazmin de la china','Jazmin del cabo, laurel huesito','Laurel de cera (hoja pequeña)','Laurel de cera','Mangle de tierra fria','Mano de oso','Mortillo','Raque, San juanito','Sietecueros nazareno','Sietecueros real','Tibar, pagoda o rodamonte','Yarumo','Abutilon blanco','Abutilon rojo y amarillo (Farolito)','Arrayan blanco','Brevo','Papayuelo','Calistemo lloron','Cayeno','Chicala, chirlobirlo, flor amarillo','Chilco','Chocho','Ciro','Ciruelo','Dividivi de tierra fria','Espino, Garbancillo','Feijoa','Gurrubo','Hayuelo','Higuerillo','Higueron','Holly espinoso','Holly liso','Platano de tierra fria','Sauco','Trompeto','Tuno roso','Aguacate','Sombrilla japonesa','Guamo santafereño','Encenillo','Alamo de lombardia','Tomate de arbol','Mandarina','Garrocho','Cafe','NN','Otro','Pino libro','Cipres Japones, criptomeria','Eucalipto','Eucalipto blanco','Palma de cera, Palma de ramo','Palma de yuca, Palma de bayoneta','Palma de datiles','Palma roebeleni','Palma payanesa','Palma sancona','Acacia morada','Acacia','Carbonero','Caucho','Caucho benjamin','Caucho lira','Guayabo brasilero','Cordoncillo','Salvio negro','Laurel europeo','Sangregado','Tibar, Rodamonte, Pagoda','Gaquillo','Pitosporo','Arrayan negro','Callistemo','Corazon de pollo','Schefflera, Pategallina hojigrande','Schefflera, Pategallina hojipequeña','Gualanday','Amarguero amarillo','Tabaquillo','Algodoncillo','Guayabo','Pimiento','Olivo','Naranjo','Borrachero blanco','Borrachero rojo','Caballero de la noche, Jazmin, Dama de noche','Granado','Tominejero','Cariseco, Tres hojas','Tomatillo','Cucubo','Algodon extranjero','Pino','Cipres','Eucalipto plateado','Tibar extranjero','Guayabillo','Uva camarona','Uva de Anis','Salvio morado','Nispero','Pomarroso','Curapin, Campanilla','Quina','Metrosideros','Arbol de corcho','Pero','Manzano','Pino Montezuma','Limon','Acacia','Palo blanco','Arbol pipermint','Algodoncillo','Chirimoyo','Pate vaca','Ayer, hoy y mañana','Salton o Charne','Carbonero','Calistemo','Caballero de la noche','Arupo','Palma areca','Citrus spp.','Manzano de monte','Sangregado','Cipres','Palma funeral','Chiripique','Chocho, balu, cambulo','Tibar, tobo, rodamonte','Eucalipto manchado','Eucalipto','Bonetero del Japon','Liberal o lechero','Caucho','Fucsia boliviana','Motilon, chuguaca','Guamo','Jazmin amarillo','Lavatera, Malvavisco morado','Leptospermun','Aligustre del Japon','Magnolia rosada','Malvavisco','Tuno esmeraldo','Tuno','Tuno','Tinto','Angelito','Arrayan','Cucharo','Susque','Yolombo','Fenix','Pino','Cerezo, ciruelo','Romero','Jomi, upacon','Tinto','Tecomaria','Trompo','Yuca, palma yuca','Olmo de agua','Schefflera, Yuco blanco','Schefflera, Tortolito','Schefflera','Schefflera pategallina peludo','Abutilonpequeño','Arce','Té de Bogotá','Almanegra, quedo','Lembo, pategallo','Diosme','Ocobo, Guayacan','Gardenia','Granizo','Balso blanco','Romero de paramo','Chirriador','Siete Cueros peludo','Canelo','Pegamosco','Punta de lanza','Tulipan africano','Acacia blanca, Cultriformes','Buganbil, veranera','Boj','Camelia','Pajarito','Mangostino','Acebo','Venturosa','Cidron','Azuceno, enebro','Ombu, Arbol de la bella sombra','Árbol de platano','Cafetillo, crucito','Azalea','Mimbre','Moquillo','Ceiba de tierra fria','Guayabo de pava','Lulo de perro','Aloe arboreo','Balazo','Camaron','Cigarrillo','Dalia','Rosa','Manto de Maria','Hebe','Marihuana','Mermelada','Mirto','Retamo','Palma cinta','Aralia japonesa','Abelia','Azara','Guayabo anselmo, Champo','Moradilla','Hiperico, Corazoncillo','Platano','Secuoya','Algarrobo','Anona','Arbol de neem','Arbol de Te','Arupo','Guacimo','Mamey','Oreja de Burro','Punga','Totumillo','Espino blanco','Guarana, guacharo','Guayabo de mico','Tachuelo','Mango','Morera','Nacedero','Tabaquillo','Flor morado','Escolin, Espadero','Pimiento negro','Fotinia','Ojo de perdiz','Motilón','Cipres','Tinto','Agracejo','Arrayan','Mulato','Cucharo','Fucsia arbustiva','Tagua','Crucito','Cerezo','Tuno roso','Palma Alejandra','Abutilon quesito','Acacia azul','Alcaparro enano','Arbol de hierro','Ardicia','Aromo','Cajeto','Cajeto','Cajeto de Bogota','Cerezo','Chicala rosado','Guayabo del peru','Holly liso','Jazmin australiano','Mano de oso']

    # Localidades de Bogotá con sus códigos
    LOCALIDADES = {
        1: "USAQUEN",
        2: "CHAPINERO",
        3: "SANTA FE",
        4: "SAN CRISTOBAL",
        5: "USME",
        6: "TUNJUELITO",
        7: "BOSA",
        8: "KENNEDY",
        9: "FONTIBON",
        10: "ENGATIVA",
        11: "SUBA",
        12: "BARRIOS UNIDOS",
        13: "TEUSAQUILLO",
        14: "LOS MARTIRES",
        15: "ANTONIO NARIÑO",
        16: "PUENTE ARANDA",
        17: "CANDELARIA",
        18: "RAFAEL URIBE URIBE",
        19: "CIUDAD BOLIVAR",
    }

    # Tipos de tratamientos
    TRATAMIENTOS = {
        # Felling: When the tree is in a very poor overall condition and is not recoverable.
        "Tala": {"est_fuste": 1, "est_copa": 1, "est_raiz": 1, "est_fito": 1},
        # Comprehensive Treatment: When the tree has problems in several parts, but is recoverable.
        "Tratamiento integral": {"est_fuste": 2, "est_copa": 2, "est_raiz": 2, "est_fito": 2},
        # Structural Pruning: When the tree is healthy but needs shaping or guidance for its future growth.
        "Poda estructural": {"est_fuste": 4, "est_copa": 3, "est_raiz": 4, "est_fito": 4},
        # Stability Pruning: For trees that may be at risk of falling or breaking, but are not diseased.
        "Poda estabilidad": {"est_fuste": 3, "est_copa": 2, "est_raiz": 3, "est_fito": 4},
        # Preserve: For trees in good overall condition that do not require drastic intervention
        "Conservar": {"est_fuste": 5, "est_copa": 4, "est_raiz": 5, "est_fito": 4},
        # Relocation: For trees that are in good condition but need to be moved to a new location.
        "Traslado": {"est_fuste": 4, "est_copa": 4, "est_raiz": 5, "est_fito": 4},
        # Root Pruning: Applied when roots cause problems
        "Poda radicular": {"est_fuste": 4, "est_copa": 4, "est_raiz": 2, "est_fito": 4},
        # Thinning Pruning (Aclareo): To improve light and air penetration into the crown, reducing density.
        "Poda aclareo": {"est_fuste": 4, "est_copa": 3, "est_raiz": 4, "est_fito": 5},
        # Crown Raising/Realce Pruning: To lift the crown or improve its aesthetics by removing lower or damaged branches.
        "Poda realce": {"est_fuste": 4, "est_copa": 4, "est_raiz": 4, "est_fito": 4},
        # Height Control Pruning: To reduce the height of trees growing near infrastructure or cables.
        "Poda control altura": {"est_fuste": 3, "est_copa": 2, "est_raiz": 3, "est_fito": 5},
        # Special Treatment: For very specific or rare conditions, or high-value trees
        "Tratamiento especial": {"est_fuste": 3, "est_copa": 3, "est_raiz": 3, "est_fito": 2},
    }

    # Espacios públicos
    ESPACIO = ["Publico", "Privado"]

    # Emplazamiento
    EMPLAZAMIENTO = [
        "Parques Metropolitanos",
        "Parques Zonales",
        "Plaza Vecinal",
        "Parques de Barrio",
        "Parque Ecologico Distrital",
        "Plazas",
        "Plazoletas",
        "Zona ajardinada",
    ]

    # Estados General
    ESTADO_GENERAL = {1: "Muy Malo", 2: "Malo", 3: "Regular", 4: "Bueno", 5: "Muy Bueno"}

    # Niveles de riesgo
    RIESGOS = {5: "Sin Riesgo", 4: "Bajo", 3: "Medio", 2: "Alto", 1: "Muy Alto"}

    # Valores históricos por año
    VALUES_BY_YEAR = {
        2020: {"salario_minimo": 877803, "ivp": 0.4379},
        2021: {"salario_minimo": 908526, "ivp": 0.4379},
        2022: {"salario_minimo": 1000000, "ivp": 0.432},
        2023: {"salario_minimo": 1160000, "ivp": 0.4581},
        2024: {"salario_minimo": 1300000, "ivp": 0.4476},
        2025: {"salario_minimo": 1423500, "ivp": 0.4745},
    }

    # Tipos de CT
    TIPOS_CT = ["Emergencia", "Infraestructura", "Manejo"]

    def csv_a_diccionario(ruta_archivo):
        arboles = {}

        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                nombre = fila["nomcomun"].strip()

                arboles[nombre] = {
                    "min_pap": float(fila["min_pap"]),
                    "max_pap": float(fila["max_pap"]),
                    "min_alturatotal": float(fila["min_alturatotal"]),
                    "max_alturatotal": float(fila["max_alturatotal"]),
                    "min_diamcopamayor": float(fila["min_diamcopamayor"]),
                    "max_diamcopamayor": float(fila["max_diamcopamayor"]),
                    "min_diamcopamenor": float(fila["min_diamcopamenor"]),
                    "max_diamcopamenor": float(fila["max_diamcopamenor"]),
                    "total": int(fila["total"]),
                }

        return arboles

    AUTORIZADOS = {"OTRO": 0.1, "ENEL": 0.15, "IDU": 0.05, "JBB": 0.4, "UAESP": 0.2, "EEAB": 0.1}
