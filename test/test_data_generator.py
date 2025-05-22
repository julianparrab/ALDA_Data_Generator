import unittest
from unittest.mock import patch, MagicMock
import random
import math
import pandas as pd
from dataclasses import dataclass, field
from typing import Dict, List, Set
from src import SIGAUGenerator, TreeDataGenerator
from src.data_reference import DataReference


# Mock para DataReference (ya que no se proporcionó)
class MockDataReference:
    LOCALIDADES = {1: "USME", 2: "CHAPINERO"}
    ESPECIES = {
        1: {
            "nombre_comun": "Roble",
            "min_pap": 0.5,
            "max_pap": 1.5,
            "min_alturatotal": 5.0,
            "max_alturatotal": 15.0,
            "min_diamcopamayor": 3.0,
            "max_diamcopamayor": 10.0,
            "min_diamcopamenor": 2.0,
            "max_diamcopamenor": 8.0,
        }
    }
    TRATAMIENTOS = {"Poda": {"est_fuste": 3, "est_copa": 2, "est_raiz": 4, "est_fito": 3}}
    ESPACIO = ["Publico", "Privado"]
    RIESGOS = ["Bajo", "Medio", "Alto", "Muy alto"]
    VALUES_BY_YEAR = {2020: {"ivp": 100, "salario_minimo": 800000}, 2021: {"ivp": 105, "salario_minimo": 850000}}
    TIPOS_CT = ["Ornamental", "Forestal"]
    EMPLAZAMIENTO = ["Aceras", "Parques"]
    ESTADO_GENERAL = ["Bueno", "Regular", "Malo"]
    AUTORIZADOS = {"Si": 0.8, "No": 0.2}


@dataclass
class DataConfig:
    """Configuración mockeada para pruebas"""

    localidades: Dict[int, str] = field(default_factory=lambda: MockDataReference.LOCALIDADES)
    especies: Dict[str, Dict[str, float]] = field(default_factory=lambda: MockDataReference.ESPECIES)
    tratamientos: Dict[str, Dict[str, float]] = field(default_factory=lambda: MockDataReference.TRATAMIENTOS)
    espacios: List[str] = field(default_factory=lambda: MockDataReference.ESPACIO)
    riesgos: List[str] = field(default_factory=lambda: MockDataReference.RIESGOS)
    values_by_year: Dict[int, Dict[str, float]] = field(default_factory=lambda: MockDataReference.VALUES_BY_YEAR)
    tipos_ct: List[str] = field(default_factory=lambda: MockDataReference.TIPOS_CT)
    emplazamiento: List[str] = field(default_factory=lambda: MockDataReference.EMPLAZAMIENTO)
    estado_general: List[str] = field(default_factory=lambda: MockDataReference.ESTADO_GENERAL)
    autorizados: Dict[str, float] = field(default_factory=lambda: MockDataReference.AUTORIZADOS)


class TestSIGAUGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = SIGAUGenerator()

    def test_generate_sigau_unique(self):
        """Test que verifica que los códigos generados son únicos"""
        codigos = set()
        for _ in range(100):
            codigo = self.generator.generate_sigau(1)
            self.assertNotIn(codigo, codigos)
            codigos.add(codigo)

    def test_generate_sigau_format(self):
        """Test que verifica el formato del código SIGAU"""
        codigo = self.generator.generate_sigau(5)
        self.assertTrue(codigo.startswith("05"))
        self.assertEqual(len(codigo), 14)  # 2 dígitos localidad + 12 dígitos

    def test_generate_sigau_different_localidades(self):
        """Test que verifica que se generan códigos diferentes para diferentes localidades"""
        codigo1 = self.generator.generate_sigau(1)
        codigo2 = self.generator.generate_sigau(2)
        self.assertNotEqual(codigo1, codigo2)
        self.assertTrue(codigo1.startswith("01"))
        self.assertTrue(codigo2.startswith("02"))


class TestTreeDataGenerator(unittest.TestCase):
    def setUp(self):
        self.config = DataConfig()
        self.generator = TreeDataGenerator(self.config)

    @patch("src.generate_coord.generar_coordenada_en_localidad")
    def test_generate_tree_basic(self, mock_coord):
        """Test básico de generación de árbol"""
        # Configurar mock para coordenadas
        mock_coord.return_value = (4.123456, -74.123456)

        # Fijar semilla aleatoria para resultados predecibles
        random.seed(42)

        tree = self.generator.generate_tree(1)

        # Verificar estructura básica
        self.assertIsInstance(tree, dict)
        self.assertEqual(tree["ID"], 1)
        self.assertIn(tree["Anio"], [2020, 2021, 2022, 2023, 2024, 2025])
        self.assertIn(tree["Localidad"], ["USME", "CHAPINERO"])
        self.assertEqual(tree["Latitud"], 4.123456)
        self.assertEqual(tree["Longitud"], -74.123456)

        # Verificar que se llamó a la función de coordenadas
        mock_coord.assert_called_once()

    def test_generate_measurements(self):
        """Test de generación de medidas del árbol"""
        medidas = self.generator._generate_measurements()

        self.assertIsInstance(medidas, dict)
        self.assertEqual(medidas["especie"], "Roble")
        self.assertGreaterEqual(medidas["pap"], 0.5)
        self.assertLessEqual(medidas["pap"], 1.5)
        self.assertEqual(medidas["dap"], round(medidas["pap"] * 3.1416, 2))
        self.assertGreaterEqual(medidas["altura_total"], 5.0)
        self.assertLessEqual(medidas["altura_total"], 15.0)

    def test_generate_status(self):
        """Test de generación de estado del árbol"""
        estado = self.generator._generate_status("Poda")

        self.assertIsInstance(estado, dict)
        self.assertEqual(estado["Estado_fuste"], 3)
        self.assertEqual(estado["Estado_Copa"], 2)
        self.assertEqual(estado["Estado_Raiz"], 4)
        self.assertEqual(estado["Estado_FitoSanitario"], 3)
        self.assertIn(estado["Estado_General"], ["Bueno", "Regular", "Malo"])
        self.assertIn(estado["riesgo"], ["Bajo", "Medio", "Alto", "Muy alto"])

    @patch("src.generate_coord.generar_coordenada_en_localidad")
    def test_generate_data(self, mock_coord):
        """Test de generación de DataFrame completo"""
        # Configurar mock para coordenadas
        mock_coord.return_value = (4.123456, -74.123456)

        # Generar 10 árboles
        df = self.generator.generate_data(10)

        # Verificar estructura básica
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 10)
        self.assertEqual(df["ID"].tolist(), list(range(1, 11)))

        # Verificar que todos los SIGAU son únicos
        self.assertEqual(len(df["SIGAU"].unique()), 10)

        # Verificar rangos de valores
        self.assertTrue((df["PAP"] >= 0.5).all())
        self.assertTrue((df["PAP"] <= 1.5).all())

        # Verificar que se llamó a la función de coordenadas 10 veces
        self.assertEqual(mock_coord.call_count, 10)

    def test_relationships_between_measurements(self):
        """Test que verifica relaciones entre medidas del árbol"""
        medidas = self.generator._generate_measurements()

        # Altura comercial no puede ser mayor que altura total
        self.assertLessEqual(medidas["altura_comercial"], medidas["altura_total"])

        # Diámetro copa menor no puede ser mayor que diámetro copa mayor
        self.assertLessEqual(medidas["diam_copa_menor"], medidas["diam_copa_mayor"])

        # Perímetro basal debe ser mayor que DAP (circunferencia > diámetro)
        self.assertGreater(medidas["perimetro_basal"], medidas["dap"])


if __name__ == "__main__":
    unittest.main()
