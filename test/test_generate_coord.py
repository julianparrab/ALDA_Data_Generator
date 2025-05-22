import unittest
import os
import tempfile
from shapely.geometry import Polygon, Point
import geopandas as gpd
import pandas as pd


class TestGenerarCoordenadaEnLocalidad(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Crear un GeoJSON de prueba para las localidades"""
        # Crear un GeoDataFrame de prueba con dos localidades simples (cuadrados)
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.test_geojson_path = os.path.join(cls.temp_dir.name, "test_localidades.geojson")

        data = {
            "LocNombre": ["Localidad1", "Localidad2"],
            "geometry": [Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]), Polygon([(2, 2), (3, 2), (3, 3), (2, 3)])],
        }

        gdf = gpd.GeoDataFrame(data, crs="EPSG:4326")
        gdf.to_file(cls.test_geojson_path, driver="GeoJSON")

    @classmethod
    def tearDownClass(cls):
        """Limpiar el directorio temporal"""
        cls.temp_dir.cleanup()

    def test_localidad_existente(self):
        """Test que verifica que se genera una coordenada dentro de una localidad existente"""
        from src.generate_coord import generar_coordenada_en_localidad

        # Probar con Localidad1
        coordenada = generar_coordenada_en_localidad(self.test_geojson_path, "Localidad1")

        self.assertIsNotNone(coordenada)
        self.assertEqual(len(coordenada), 2)

        # Verificar que el punto está dentro del polígono de Localidad1
        punto = Point(coordenada[1], coordenada[0])  # Longitud, Latitud
        poligono = gpd.read_file(self.test_geojson_path).geometry.iloc[0]
        self.assertTrue(punto.within(poligono))

    def test_localidad_inexistente(self):
        """Test que verifica el comportamiento cuando la localidad no existe"""
        from src.generate_coord import generar_coordenada_en_localidad

        # Capturar el output de print
        import io
        import sys

        captured_output = io.StringIO()
        sys.stdout = captured_output

        coordenada = generar_coordenada_en_localidad(self.test_geojson_path, "LocalidadInexistente")

        sys.stdout = sys.__stdout__

        self.assertIsNone(coordenada)
        self.assertIn("Localidad 'LocalidadInexistente' no encontrada.", captured_output.getvalue())

    def test_coordenadas_dentro_rango(self):
        """Test que verifica que las coordenadas generadas están dentro del rango de la localidad"""
        from src.generate_coord import generar_coordenada_en_localidad

        # Probar múltiples veces para asegurar que siempre está dentro
        for _ in range(100):
            coordenada = generar_coordenada_en_localidad(self.test_geojson_path, "Localidad2")

            self.assertIsNotNone(coordenada)
            lat, lon = coordenada

            # Localidad2 está entre 2 y 3 en ambos ejes
            self.assertGreaterEqual(lon, 2)
            self.assertLessEqual(lon, 3)
            self.assertGreaterEqual(lat, 2)
            self.assertLessEqual(lat, 3)

            # Verificar que el punto está dentro del polígono
            punto = Point(lon, lat)
            poligono = gpd.read_file(self.test_geojson_path).geometry.iloc[1]
            self.assertTrue(punto.within(poligono))

    def test_archivo_inexistente(self):
        """Test que verifica el comportamiento cuando el archivo GeoJSON no existe"""
        from src.generate_coord import generar_coordenada_en_localidad

        with self.assertRaises(FileNotFoundError):
            generar_coordenada_en_localidad("ruta/inexistente.geojson", "Localidad1")


if __name__ == "__main__":
    unittest.main()
