import pandas as pd
import random
import math
from typing import Set, Dict, List, Any
from dataclasses import dataclass, field
from src.data_reference import DataReference
from src.generate_coord import generar_coordenada_en_localidad


@dataclass
class DataConfig:
    """Contenedor de configuración y datos base para la generación de árboles"""

    localidades: Dict[int, str] = field(default_factory=lambda: DataReference.LOCALIDADES)
    especies: Dict[str, Dict[str, float]] = field(default_factory=lambda: DataReference.ESPECIES)
    tratamientos: Dict[str, Dict[str, float]] = field(default_factory=lambda: DataReference.TRATAMIENTOS)
    espacios: List[str] = field(default_factory=lambda: DataReference.ESPACIO)
    riesgos: List[str] = field(default_factory=lambda: DataReference.RIESGOS)
    valores_anuales: Dict[int, Dict[str, float]] = field(default_factory=lambda: DataReference.VALUES_BY_YEAR)
    tipos_ct: List[str] = field(default_factory=lambda: DataReference.TIPOS_CT)
    emplazamientos: List[str] = field(default_factory=lambda: DataReference.EMPLAZAMIENTO)
    estados_generales: List[str] = field(default_factory=lambda: DataReference.ESTADO_GENERAL)
    autorizados: Dict[str, float] = field(default_factory=lambda: DataReference.AUTORIZADOS)


class SIGAUGenerator:
    def __init__(self):
        self.codigos_generados: Set[str] = set()

    def generar(self, codigo_localidad: int) -> str:
        """Genera un código SIGAU único basado en la localidad"""

        prefijo = f"{codigo_localidad:02d}"

        while True:
            digitos = "".join(random.choices("0123456789", k=12))
            codigo = prefijo + digitos
            if codigo not in self.codigos_generados:
                self.codigos_generados.add(codigo)
                return codigo


class TreeDataGenerator:
    def __init__(self, config: DataConfig = DataConfig()):
        self.config = config
        self.sigau_gen = SIGAUGenerator()

    def _seleccionar_especie(self) -> Dict[str, Any]:
        """Selecciona una especie y genera sus medidas"""

        especie_id = random.choice(list(self.config.especies.keys()))
        especie = self.config.especies[especie_id]

        pap = round(random.uniform(especie["min_pap"], especie["max_pap"]), 2)
        altura_total = round(random.uniform(especie["min_alturatotal"], especie["max_alturatotal"]), 2)

        return {
            "nombre": especie["nombre_comun"],
            "pap": pap,
            "dap": round(pap * math.pi, 2),
            "altura_total": altura_total,
            "altura_comercial": round(random.uniform(0, altura_total), 2),
            "diam_copa_mayor": round(random.uniform(especie["min_diamcopamayor"], especie["max_diamcopamayor"]), 2),
            "diam_copa_menor": round(random.uniform(especie["min_diamcopamenor"], especie["max_diamcopamenor"]), 2),
            "perimetro_basal": round(pap * math.pi * 1.1, 2),
        }

    def _generar_estado(self, tratamiento: str) -> Dict[str, Any]:
        """Genera los estados del árbol a partir del tratamiento"""

        t = self.config.tratamientos[tratamiento]
        promedio = math.floor((t["est_fuste"] + t["est_copa"] + t["est_raiz"] + t["est_fito"]) / 4)

        return {
            "estado_fuste": t["est_fuste"],
            "estado_copa": t["est_copa"],
            "estado_raiz": t["est_raiz"],
            "estado_fito": t["est_fito"],
            "estado_general": self.config.estados_generales[promedio],
            "riesgo": self.config.riesgos[promedio],
        }

    def generar_arbol(self, tree_id: int) -> Dict[str, Any]:
        """Genera los datos simulados de un árbol individual"""

        anio = random.randint(2020, 2025)
        especie_data = self._seleccionar_especie()
        tratamiento = random.choice(list(self.config.tratamientos.keys()))
        estado = self._generar_estado(tratamiento)
        num_localidad = random.randint(1, len(self.config.localidades))
        localidad = self.config.localidades[num_localidad]
        consecutivo = f"{random.randint(0, 99999):05d}"

        lat, lon = generar_coordenada_en_localidad("data/localidades_bogota.geojson", localidad.upper())

        return {
            "ID": tree_id,
            "Anio": anio,
            "IVP": self.config.valores_anuales[anio]["ivp"],
            "Salario Minimo": self.config.valores_anuales[anio]["salario_minimo"],
            "Concepto": f"{anio}EE{consecutivo}",
            "TipoCT": random.choice(self.config.tipos_ct),
            "Consecutivo": f"SSFFS-{consecutivo}",
            "SIGAU": self.sigau_gen.generar(num_localidad),
            "Especie": especie_data["nombre"],
            "Tratamiento": tratamiento,
            "Espacio": random.choice(self.config.espacios),
            "Emplazamiento": random.choice(self.config.emplazamientos),
            "Estrato": random.randint(1, 6),
            "Localidad": localidad,
            "Latitud": lat,
            "Longitud": lon,
            "PAP": especie_data["pap"],
            "DAP": especie_data["dap"],
            "Altura Total": especie_data["altura_total"],
            "Altura Comercial": especie_data["altura_comercial"],
            "Diam. Copa Polar": especie_data["diam_copa_mayor"],
            "Diam. Copa Ecuatorial": especie_data["diam_copa_menor"],
            "Perimetro basal": especie_data["perimetro_basal"],
            "Estado fuste": estado["estado_fuste"],
            "Estado Copa": estado["estado_copa"],
            "Estado Raiz": estado["estado_raiz"],
            "Estado FitoSanitario": estado["estado_fito"],
            "Estado General": estado["estado_general"],
            "Riesgo": estado["riesgo"],
            "Interes patrimonial": random.choices(["Si", "No"], weights=[0.05, 0.95])[0],
            "Autorizado": random.choices(
                list(self.config.autorizados.keys()), weights=list(self.config.autorizados.values())
            )[0],
        }

    def generar_dataset(self, cantidad: int = 100) -> pd.DataFrame:
        """Genera un DataFrame con múltiples árboles simulados"""

        registros = [self.generar_arbol(i + 1) for i in range(cantidad)]
        return pd.DataFrame(registros)
