import pandas as pd
import random
import math
from typing import Set, Dict, List
from dataclasses import dataclass, field
from src.data_reference import DataReference
from src.generate_coord import generar_coordenada_en_localidad


@dataclass
class DataConfig:
    """Configuración de datos usando la referencia"""

    localidades: Dict[int, str] = field(default_factory=lambda: DataReference.LOCALIDADES)
    especies: Dict[str, Dict[str, float]] = field(default_factory=lambda: DataReference.ESPECIES)
    tratamientos: Dict[str, Dict[str, float]] = field(default_factory=lambda: DataReference.TRATAMIENTOS)
    espacios: List[str] = field(default_factory=lambda: DataReference.ESPACIO)
    riesgos: List[str] = field(default_factory=lambda: DataReference.RIESGOS)
    values_by_year: Dict[int, Dict[str, float]] = field(default_factory=lambda: DataReference.VALUES_BY_YEAR)
    tipos_ct: List[str] = field(default_factory=lambda: DataReference.TIPOS_CT)
    emplazamiento: List[str] = field(default_factory=lambda: DataReference.EMPLAZAMIENTO)
    estado_general: List[str] = field(default_factory=lambda: DataReference.ESTADO_GENERAL)
    autorizados: List[str] = field(default_factory=lambda: DataReference.AUTORIZADOS)


class SIGAUGenerator:
    def __init__(self):
        self.codigos_generados: Set[str] = set()

    def generate_sigau(self, codigo_localidad: int) -> str:
        """Genera código SIGAU único con prefijo de localidad"""

        prefijo = f"{codigo_localidad:02d}"

        while True:
            digitos = "".join(random.choices("0123456789", k=12))
            codigo = prefijo + "".join(digitos)

            if codigo not in self.codigos_generados:
                self.codigos_generados.add(codigo)
                return codigo


class TreeDataGenerator:
    def __init__(self, config: DataConfig = DataConfig()):
        self.config = config
        self.sigau_gen = SIGAUGenerator()

    def _generate_measurements(self) -> Dict[str, float]:
        """Genera medidas del árbol con relaciones realistas"""

        id_especie = random.randint(1, len(self.config.especies))
        # Generación de medidas
        pap = round(
            random.uniform(self.config.especies[id_especie]["min_pap"], self.config.especies[id_especie]["max_pap"]), 2
        )
        altura_total = round(
            random.uniform(
                self.config.especies[id_especie]["min_alturatotal"], self.config.especies[id_especie]["max_alturatotal"]
            ),
            2,
        )

        return {
            "especie": self.config.especies[id_especie]["nombre_comun"],
            "pap": pap,
            "dap": round(pap * 3.1416, 2),
            "altura_total": altura_total,
            "altura_comercial": round(random.uniform(0, altura_total), 2),
            "diam_copa_mayor": round(
                random.uniform(
                    self.config.especies[id_especie]["min_diamcopamayor"],
                    self.config.especies[id_especie]["max_diamcopamayor"],
                ),
                2,
            ),
            "diam_copa_menor": round(
                random.uniform(
                    self.config.especies[id_especie]["min_diamcopamenor"],
                    self.config.especies[id_especie]["max_diamcopamenor"],
                ),
                2,
            ),
            "perimetro_basal": round(pap * 3.1416 * 1.1, 2),
        }

    def _generate_status(self, tratamiento) -> Dict[str, float]:
        """Genera datos de estado del árbol"""

        # Generación de estado
        est_fuste = self.config.tratamientos[tratamiento]["est_fuste"]
        est_copa = self.config.tratamientos[tratamiento]["est_copa"]
        est_raiz = self.config.tratamientos[tratamiento]["est_raiz"]
        est_fito = self.config.tratamientos[tratamiento]["est_fito"]

        est_gen = math.floor((est_fuste + est_copa + est_raiz + est_fito) / 4)

        return {
            "Estado_fuste": est_fuste,
            "Estado_Copa": est_copa,
            "Estado_Raiz": est_raiz,
            "Estado_FitoSanitario": est_fito,
            "Estado_General": self.config.estado_general[est_gen],
            "riesgo": self.config.riesgos[est_gen],
        }

    def generate_tree(self, tree_id: int) -> Dict[str, any]:
        """Genera datos de un árbol individual"""
        anio = random.randint(2020, 2025)
        medidas = self._generate_measurements()
        tratamiento = random.choice(list(self.config.tratamientos.keys()))
        estado = self._generate_status(tratamiento)
        num_localidad = random.randint(1, len(self.config.localidades))
        consec = f"{random.randint(0, 99999):05d}"

        # Generar coordenadas
        coordenadas = generar_coordenada_en_localidad(
            "data/localidades_bogota.geojson", self.config.localidades[num_localidad].upper()
        )
        # print("coordenada ", coordenadas)

        return {
            "ID": tree_id,
            "Anio": anio,
            "IVP": self.config.values_by_year[anio]["ivp"],
            "Salario Minimo": self.config.values_by_year[anio]["salario_minimo"],
            "Concepto": f"{anio}EE{consec}",
            "TipoCT": random.choice(self.config.tipos_ct),
            "Consecutivo": f"SSFFS-{consec}",
            "SIGAU": self.sigau_gen.generate_sigau(num_localidad),
            "Especie": medidas["especie"],
            "Tratamiento": tratamiento,
            "Espacio": random.choice(self.config.espacios),
            "Emplazamiento": random.choice(self.config.emplazamiento),
            "Estrato": random.randint(1, 6),
            "Localidad": self.config.localidades[num_localidad],
            "Latitud": coordenadas[0],
            "Longitud": coordenadas[1],
            "PAP": medidas["pap"],
            "DAP": medidas["dap"],
            "Altura Total": medidas["altura_total"],
            "Altura Comercial": medidas["altura_comercial"],
            "Diam. Copa Polar": medidas["diam_copa_mayor"],
            "Diam. Copa Ecuatorial": medidas["diam_copa_menor"],
            "Perimetro basal": medidas["perimetro_basal"],
            "Estado fuste": estado["Estado_fuste"],
            "Estado Copa": estado["Estado_Copa"],
            "Estado Raiz": estado["Estado_Raiz"],
            "Estado FitoSanitario": estado["Estado_FitoSanitario"],
            "Estado General": estado["Estado_General"],
            "Riesgo": estado["riesgo"],
            "Interes patrimonial": random.choices(["Si", "No"], weights=[0.05, 0.95], k=1)[0],
            "Autorizado": random.choices(
                list(self.config.autorizados.keys()), weights=list(self.config.autorizados.values()), k=1
            )[0],
        }

    def generate_data(self, n: int = 100) -> pd.DataFrame:
        """Genera DataFrame con datos de árboles"""
        data = [self.generate_tree(i + 1) for i in range(n)]

        columns = [
            "ID",
            "Anio",
            "IVP",
            "Salario Minimo",
            "Concepto",
            "TipoCT",
            "Consecutivo",
            "SIGAU",
            "Especie",
            "Tratamiento",
            "Espacio",
            "Estrato",
            "Localidad",
            "Latitud",
            "Longitud",
            "PAP",
            "DAP",
            "Altura Total",
            "Altura Comercial",
            "Diam. Copa Polar",
            "Diam. Copa Ecuatorial",
            "Perimetro basal",
            "Estado fuste",
            "Estado Copa",
            "Estado Raiz",
            "Estado FitoSanitario",
            "Estado General",
            "Riesgo",
            "Interes patrimonial",
            "Autorizado",
        ]

        return pd.DataFrame(data, columns=columns)
