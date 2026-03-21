import os
import pytest


from day3_CSV_practice import process_with_validation
from day4_CSV_practice import write_csv_report, write_html_report

@pytest.fixture(scope="module")
def setup_data():
    """Fixture: Procesa los datos y genera los reportes base."""
    file_path = os.path.join("data", "test_data.csv")
    
    valid, invalid, invalid_details = process_with_validation(file_path)
    
    write_csv_report(valid, invalid, invalid_details, "reporte.csv")
    write_html_report(valid, invalid, invalid_details, "reporte.html")
    
    return valid, invalid, invalid_details

def test_validation_has_data(setup_data):
    valid, invalid, _ = setup_data
    total = len(valid) + len(invalid)
    assert total > 0, "No se procesaron datos del CSV"

def test_invalid_users_detected(setup_data):
    _, invalid, invalid_details = setup_data
    assert len(invalid) > 0, "No se detectaron usernames inválidos"
    assert len(invalid_details) == len(invalid), "Detalles no coinciden"

def test_html_generated():
    assert os.path.exists("reporte.html"), "reporte.html no fue generado"

def test_csv_generated():
    assert os.path.exists("reporte.csv"), "reporte.csv no fue generado"

def test_screenshot_generated(page):
    folder = "evidencias"
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, "evidencia_validacion.png")

    page.goto("https://the-internet.herokuapp.com/")
    page.screenshot(path=filename)
    
    assert os.path.exists(filename), f"No se encontró el archivo {filename}"
     
    screenshots = [f for f in os.listdir(folder) if f.startswith("evidencia_")]
    assert len(screenshots) > 0, "No se detectó el archivo en la carpeta evidencias"
