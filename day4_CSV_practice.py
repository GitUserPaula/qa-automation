# day4.py - Generar reportes CSV + HTML

import os
import csv
from datetime import datetime

from day3_CSV_practice import process_with_validation  # ← Reutilizamos Día 3!

# === FUNCIÓN: Escribir CSV de resultados ===
def write_csv_report(valid, invalid, invalid_details, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["username", "status", "detalle"])
        
        # Válidos
        for user in valid:
            writer.writerow([user, "VÁLIDO", ""])
        
        # Inválidos
        for i, username in enumerate(invalid):
            detalle = invalid_details[i]  # ← errors ahora es invalid_details
            writer.writerow([username, "INVÁLIDO", detalle])
    
    print(f"CSV generado: {output_path}")



# === FUNCIÓN: Generar HTML con colores ===
def write_html_report(valid, invalid, invalid_details, output_path):
    total = len(valid) + len(invalid)
    success_rate = (len(valid) / total * 100) if total > 0 else 0
    date_str = datetime.now().strftime("%d/%m/%Y %H:%M")

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>QA Report - Usernames</title>
    <style>
        body {{ font-family: Arial; margin: 40px; }}
        h1 {{ color: #2c3e50; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f2f2f2; }}
        .valid {{ color: darkgreen; }}
        .invalid {{ color: purple; font-weight: bold; }}
        .summary {{ background: #f8f9fa; padding: 15px; border-radius: 8px; }}
    </style>
</head>
<body>

    <h1>QA Report - Usernames</h1>
    <p><em>Generado el {date_str}</em></p>

    <div class="summary">
        <p><strong>Total:</strong> {total}</p>
        <p><strong>Válidos:</strong> {len(valid)} (<span class="valid">{success_rate:.1f}%</span>)</p>
        <p><strong>Inválidos:</strong> {len(invalid)}</p>
    </div>

    <table>
        <tr>
            <th>Username</th>
            <th>Estado</th>
            <th>Detalle</th>
        </tr>"""

    # Filas válidas
    for user in valid:
        html_content += f"""
        <tr>
            <td>{user}</td>
            <td class="valid">VÁLIDO</td>
            <td></td>
        </tr>"""

    # Filas inválidas
    for i, username in enumerate(invalid):
        detalle = invalid_details[i]
        html_content += f"""
        <tr>
            <td>{username}</td>
            <td class="invalid">INVÁLIDO</td>
            <td>{detalle}</td>
        </tr>"""

        html_content += """
    </table>
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)
    
    print(f"HTML generado: {output_path}")


# === MAIN ===
print("=== DÍA 4: GENERACIÓN DE REPORTES ===")

file_path = os.path.join("data", "test_data.csv")
valid, invalid, invalid_details = process_with_validation(file_path)

# Generar reportes
csv_output = "reporte.csv"
html_output = "reporte.html"

write_csv_report(valid, invalid, invalid_details, csv_output)
write_html_report(valid, invalid, invalid_details, html_output)

print("\n¡Reportes generados con éxito! Abre 'reporte.html' en tu navegador")