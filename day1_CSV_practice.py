# day1.py - Validaciones básicas para QA

def validate_username(username):
    if len(username) >= 5:
        return True, "Válido"
    else:
        return False, "Inválido: debe tener al menos 5 caracteres"

def generate_email(name):
    return f"{name}@qa.com"

def validate_test_id(test_id_input):
    try:
        test_id = int(test_id_input)
        if 1 <= test_id <= 100:
            return True, f"ID {test_id} válido"
        else:
            return False, f"ID {test_id} fuera de rango (1-100)"
    except ValueError:
        return False, "Error: debe ser un número"
    

# === PRUEBAS INTERACTIVAS ===
print("=== VALIDACIÓN DE USUARIO ===")
user = input("Ingresa un username: ")
valid, msg = validate_username(user)
print(msg)

print("\n=== GENERAR EMAIL ===")
#print(f"Email generado: {generate_email('testuser')}")
nombre = input("Ingresa un nombre: ")
print(f"Email generado: {generate_email(nombre)}")
print("\n=== VALIDAR ID DE TEST ===")
test_id = input("Ingresa un ID de test: ")
valid, msg = validate_test_id(test_id)
print(f"Resultado técnico: valid={valid}, msg='{msg}'")
print(f"Mensaje amigable: {msg}")
print(msg)