import geopandas as gpd
from shapely.geometry import Polygon, Point
import random
import os


def generar_coordenada_en_localidad(ruta_geojson, nombre_localidad):
    if not os.path.exists(ruta_geojson):
        raise FileNotFoundError(f"El archivo '{ruta_geojson}' no existe.")

    # Cargar el GeoJSON
    try:
        localidades = gpd.read_file(ruta_geojson)
    except Exception as e:
        raise RuntimeError(f"No se pudo leer el archivo GeoJSON: {e}")

    # Filtrar la localidad deseada
    localidad = localidades[localidades["LocNombre"] == nombre_localidad]

    if localidad.empty:
        print(f"Localidad '{nombre_localidad}' no encontrada.")
        return None

    # Obtener el polígono de la localidad
    poligono = localidad.geometry.iloc[0]

    # Generar coordenadas aleatorias dentro del polígono
    minx, miny, maxx, maxy = poligono.bounds
    while True:
        # Generar un punto aleatorio dentro del bounding box
        punto = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if punto.within(poligono):
            return (punto.y, punto.x)  # Latitud, Longitud


"""
# Ejemplo de uso
ruta_geojson = "data/localidades_bogota.geojson"  # Ajusta la ruta
localidad = "BOSA"  # Cambia por la localidad deseada

coordenada = generar_coordenada_en_localidad(ruta_geojson, localidad)
if coordenada:
    print(f"Coordenada en {localidad}: Lat {coordenada[0]:.6f}, Lon {coordenada[1]:.6f}")
"""
