# day3.py - Validación avanzada de usernames

import os

# === IMPORT SEGURO ===
try:
    from day2_CSV_practice import read_test_data, count_results
except ImportError:
    print("ERROR: No se encuentra 'day2.py'")
    print("Asegúrate de que esté en la misma carpeta que day3.py")
    exit()

# === FUNCIÓN: Validar username ===
def validate_username(username):
    if not username:
        return False, "username vacío"
    
    errors = []
    if len(username) < 5:
        errors.append("muy corto (mínimo 5 caracteres)")
    if not username.isalnum():
        errors.append("solo letras y números")
    
    if errors:
        return False, "; ".join(errors)
    return True, "válido"


# === FUNCIÓN: Procesar CSV con validación ===
def process_with_validation(file_path):
    data = read_test_data(file_path)
    if not data:
        print("No hay datos para procesar.")
        return [], [], []

    valid_cases = []
    invalid_cases = []      # ← Usernames inválidos
    invalid_details = []    # ← Detalles del error

    print(f"Validando {len(data)} usernames...\n")
    
    for username, password, expected_result in data:
        is_valid, message = validate_username(username)
        
        if is_valid:
            valid_cases.append(username)
        else:
            invalid_cases.append(username)
            invalid_details.append(message)  # ← Solo el mensaje

    return valid_cases, invalid_cases, invalid_details


# === MAIN ===
print("=== DÍA 3: VALIDACIÓN DE USERNAMES EN CSV ===\n")

file_path = os.path.join("data", "test_data.csv")
valid, invalid, invalid_details = process_with_validation(file_path)

# === REPORTE ===
print(f"RESUMEN:")
print(f"   Válidos: {len(valid)}")
print(f"   Inválidos: {len(invalid)}\n")

if valid:
    print("Usernames VÁLIDOS:")
    for user in valid:
        print(f"   {user}")
    print()

if invalid:
    print("Usernames INVÁLIDOS:")
    for i, username in enumerate(invalid):
        detalle = invalid_details[i]
        print(f"   {username}: {detalle}")
    print()
else:
    print("¡Todos los usernames son válidos!\n")

# === CONTEO DE RESULTADOS (opcional) ===
success, fail = count_results(read_test_data(file_path))
print(f"Resultados de prueba: {success} Success, {fail} Fail")