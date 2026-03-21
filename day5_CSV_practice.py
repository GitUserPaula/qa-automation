import os
import asyncio
from datetime import datetime
from playwright.sync_api import sync_playwright

HTML_FILE = "reporte.html"
SCREENSHOT_DIR = "evidencias"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def get_screenshot_name():
    now = datetime.now()
    return f"evidencia_{now.strftime('%Y-%m-%d_%H-%M-%S')}.png"

def generate_screenshot():
    if not os.path.exists(HTML_FILE):
        print(f"ERROR: No se encuentra {HTML_FILE}")
        print("Ejecuta day4.py primero")
        return

    screenshot_path = os.path.join(SCREENSHOT_DIR, get_screenshot_name())
    
    print(f"Abrir {HTML_FILE}...")
    print(f"Guardando screenshot en: {screenshot_path}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        page = browser.new_page()
        
        file_url = f"file://{os.path.abspath(HTML_FILE)}"
        page.goto(file_url)
        
        page.wait_for_selector("table", timeout=5000)
        
        page.screenshot(path=screenshot_path, full_page=True)
        
        browser.close()
    
    print(f"Screenshot guardado: {screenshot_path}")
    print("¡Evidencia generada con éxito!")

# === MAIN ===
if __name__ == "__main__":
    print("=== DÍA 5: EVIDENCIA AUTOMÁTICA CON PLAYWRIGHT ===\n")
    generate_screenshot()