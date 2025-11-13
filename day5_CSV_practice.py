# day5.py - Abrir reporte HTML + Screenshot automático

import os
import asyncio
from datetime import datetime
from playwright.sync_api import sync_playwright

# === CONFIGURACIÓN ===
HTML_FILE = "reporte.html"
SCREENSHOT_DIR = "evidencias"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# === FUNCIÓN: Generar nombre con fecha/hora ===
def get_screenshot_name():
    now = datetime.now()
    return f"evidencia_{now.strftime('%Y-%m-%d_%H-%M-%S')}.png"

# === FUNCIÓN: Abrir HTML y tomar screenshot ===
def generate_screenshot():
    if not os.path.exists(HTML_FILE):
        print(f"ERROR: No se encuentra {HTML_FILE}")
        print("Ejecuta day4.py primero")
        return

    screenshot_path = os.path.join(SCREENSHOT_DIR, get_screenshot_name())
    
    print(f"Abrir {HTML_FILE}...")
    print(f"Guardando screenshot en: {screenshot_path}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # ← headless=False = ves el navegador
        page = browser.new_page()
        
        # Abre el HTML local
        file_url = f"file://{os.path.abspath(HTML_FILE)}"
        page.goto(file_url)
        
        # Espera que cargue la tabla
        page.wait_for_selector("table", timeout=5000)
        
        # Toma screenshot de toda la página
        page.screenshot(path=screenshot_path, full_page=True)
        
        browser.close()
    
    print(f"Screenshot guardado: {screenshot_path}")
    print("¡Evidencia generada con éxito!")

# === MAIN ===
if __name__ == "__main__":
    print("=== DÍA 5: EVIDENCIA AUTOMÁTICA CON PLAYWRIGHT ===\n")
    generate_screenshot()