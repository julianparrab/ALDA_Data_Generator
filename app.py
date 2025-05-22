from src import data_generator

if __name__ == '__main__':
    number_rows = 10  # Cambia este número para generar más o menos filas
    df = data_generator.generate_data(number_rows)  
    print(df.head())  # Muestra las primeras filas del DataFrame generado
    #df.to_csv("datos_arboles.csv", index=False)
    print("Archivo 'datos_arboles.csv' generado con éxito.")
