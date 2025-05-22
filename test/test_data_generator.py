import unittest
from src.data_generator import TreeDataGenerator
import pandas as pd


class TestTreeDataGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = TreeDataGenerator()

    def test_generate_single_tree_structure(self):
        tree = self.generator.generar_arbol(1)
        self.assertIsInstance(tree, dict)
        expected_keys = {
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
            "Emplazamiento",
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
        }
        self.assertEqual(set(tree.keys()), expected_keys)

    def test_generate_data_frame_shape(self):
        df = self.generator.generar_dataset(10)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 10)
        self.assertEqual(len(df.columns), 31)  # Cambia este valor si agregaste más columnas
        self.assertIn("ID", df.columns)
        self.assertTrue((df["PAP"] > 0).all())


if __name__ == "__main__":
    unittest.main()
