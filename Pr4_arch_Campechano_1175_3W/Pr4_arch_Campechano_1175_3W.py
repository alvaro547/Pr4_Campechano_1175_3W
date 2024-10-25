print(" ")
print("Alvaro Campchano 3W")
print(" ")
# programa_lectura_parcial_archivo.py

def leer_parcial_archivo(nombre_archivo, num_caracteres):
    """
    Esta función abre un archivo y lee solo una parte de él, 
    especificando la cantidad de caracteres a devolver.
    
    Args:
        nombre_archivo (str): El nombre del archivo a leer.
        num_caracteres (int): Número de caracteres a leer.
        
    Returns:
        None
    """
    try:
        # Abrir el archivo en modo lectura
        with open(nombre_archivo, "r") as f:
            # Leer los primeros num_caracteres caracteres del archivo
            contenido_parcial = f.read(num_caracteres)
            print(contenido_parcial)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

if __name__ == "__main__":
    # Nombre del archivo y número de caracteres a leer
    archivo = 'demofile.txt'  # Asegúrate de que este archivo exista
    caracteres_a_leer = 5      # Cambia este valor según lo que necesites
    leer_parcial_archivo(archivo, caracteres_a_leer)
