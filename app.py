from src import data_generator
import os

if __name__ == "__main__":
    # Configuración
    NUM_REGISTROS = 2000
    OUTPUT_FILE = "data/arboles_bogota.csv"

    # Crear directorio si no existe
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Generar datos
    print("Generando datos...")
    generator = data_generator.TreeDataGenerator()
    df = generator.generar_dataset(NUM_REGISTROS)
    print(df.head())

    # Save to CSV
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
    print("Datos generados exitosamente!")
    print(f"Archivo generado: {OUTPUT_FILE}")
    print(f"Registros creados: {len(df):,}")
