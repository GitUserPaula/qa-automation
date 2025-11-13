# day2.py - Leer CSV y contar resultados de pruebas

import csv 
import os 

file_path = os.path.join("data", "test_data.csv")

def read_test_data(file_path):
    data = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            
            reader = csv.reader(file, delimiter=",", quotechar='"')

            next(reader)  # ← Salta la primera fila (encabezados)
            for row in reader:
                if row:  # Evita filas vacías
                    data.append(row)
        return data
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []
if not os.path.exists(file_path):
    print(f"ERROR: No se encuentra {file_path}")
    print(f"Carpeta actual: {os.getcwd()}")
    exit()

print(f"Archivo encontrado: {file_path}")

# === FUNCIÓN: Contar Success y Fail (usa desempaquetado!) ===
def count_results(data):
    success = 0
    fail = 0
    for row in data:  # ← ¡Desempaquetado de tupla!
        try:    
            username, password, result = row
            if result.strip() == "Success":
                success += 1
            elif result.strip() == "Fail":
                fail += 1

        except ValueError:
            print(f"Advertencia: Se omitió una fila mal formateada: {row}")
        continue

    return success, fail  # ← Devuelve tupla (success, fail)


# === MAIN: Ejecutar todo ===
print("=== DÍA 2: ANÁLISIS DE RESULTADOS DE PRUEBA ===")

# 1. Leer el CSV
file_path = "data/test_data.csv"
test_data = read_test_data(file_path)

if not test_data:
    print("No hay datos para procesar.")
else:
    print(f"Se leyeron {len(test_data)} casos de prueba.\n")

    # 2. Contar resultados
    success_count, fail_count = count_results(test_data)  # ← ¡Desempaquetado!

    # 3. Mostrar resultados bonitos
    print(f"RESULTADOS:")
    print(f"   Success: {success_count}")
    print(f"   Fail: {fail_count}")
    print(f"   Total: {success_count + fail_count}")

    # Extra: Porcentaje
    total = success_count + fail_count
    if total > 0:
        success_rate = (success_count / total) * 100
        print(f"   Tasa de éxito: {success_rate:.1f}%")