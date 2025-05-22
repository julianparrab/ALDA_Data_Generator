
import pandas as pd
import random
from typing import Set
from src import data_reference as dr

# Function to generate random data
def generate_data(n):
    datos = []
    # Generate random data for n rows
    for i in range(n):
        id = i + 1
        # Random year between 2020 and 2025 for IVP and SMMLV
        anio = random.randint(2020, 2025)
        ivp = dr.values_by_year[anio]["ivp"]
        salario_minimo = dr.values_by_year[anio]["salario_minimo"]

        # Consecutive number for the concept
        consec = f"{random.randint(0, 99999):05d}"
        concepto = f"{anio}EE{consec}"
        consecutivo = f"SSFFS-{consec}"

        # Random SIGAU number
        num_localidad = random.randint(1, len(dr.localidades))
        sigau = f"{num_localidad:02d}{random.randint(0, 999999999999):12d}"
        # Random values for the rest of the fields
        especie = random.choice(dr.especies)
        tratamiento = random.choice(dr.tratamientos)
        espacio = random.choice(dr.espacios)
        estrato = random.randint(1, 6)
        localidad = dr.localidades[num_localidad]
        latitud = round(random.uniform(4.5, 4.8), 6)
        longitud = round(random.uniform(-74.2, -74.0), 6)
        pap = round(random.uniform(10, 100), 2)
        dap = round(random.uniform(5, 50), 2)
        altura_total = round(random.uniform(3, 30), 2)
        altura_comercial = round(random.uniform(1, altura_total), 2)
        diam_copa_polar = round(random.uniform(1, 10), 2)
        diam_copa_ecuat = round(random.uniform(1, 10), 2)
        perimetro_basal = round(dap * 3.14, 2)
        estado_fuste = random.choice(dr.estados_fuste)
        estado_copa = random.choice(dr.estados_copa)
        estado_raiz = random.choice(dr.estados_raiz)
        estado_fitosanitario = random.choice(dr.estados_fitosanitarios)
        riesgo = random.choice(dr.riesgos)
        interes_patrimonial = random.choice([True, False])
        autorizado = random.choice([True, False])
        compensacion = round(random.uniform(100000, 500000), 2)
        descuento = round(random.uniform(0, compensacion), 2)
        total = round(compensacion - descuento, 2)

        fila = [
            id, anio, ivp, salario_minimo, concepto, consecutivo, sigau,
            especie, tratamiento, espacio, estrato, localidad, latitud, longitud,
            pap, dap, altura_total, altura_comercial, diam_copa_polar, diam_copa_ecuat,
            perimetro_basal, estado_fuste, estado_copa, estado_raiz,
            estado_fitosanitario, riesgo, interes_patrimonial, autorizado,
            compensacion, descuento, total
        ]
        datos.append(fila)

    columnas = [
        "ID", "Anio", "IVP", "Salario Minimo", "Concepto", "Consecutivo", "SIGAU", "Especie",
        "Tratamiento", "Espacio", "Estrato", "Localidad", "Latitud", "Longitud", "PAP", "DAP",
        "Altura Total", "Altura Comercial", "Diam. Copa Polar", "Diam. Copa Ecuatorial",
        "Perimetro basal", "Estado fuste", "Estado Copa", "Estado Raiz", "Estado FitoSanitario",
        "Riesgo", "Interes patrimonial", "Autorizado", "Compensacion", "Compensacion Descuento", "Total"
    ]

    return pd.DataFrame(datos, columns=columnas)




