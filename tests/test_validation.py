# tests/test_validation.py

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from day3_CSV_practice import process_with_validation
from day4_CSV_practice import write_csv_report, write_html_report
from day5_CSV_practice import generate_screenshot

@pytest.fixture
def setup_data():
    """Fixture: Genera reporte.html y screenshot"""
    file_path = os.path.join("data", "test_data.csv")
    
    # Paso 1: Validar
    valid, invalid, invalid_details = process_with_validation(file_path)
    
    # Paso 2: Generar reportes
    csv_output = "reporte.csv"
    html_output = "reporte.html"
    write_csv_report(valid, invalid, invalid_details, csv_output)
    write_html_report(valid, invalid, invalid_details, html_output)
    
    # Paso 3: Screenshot
    import asyncio
    generate_screenshot()
    
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

def test_screenshot_generated():
    screenshots = [f for f in os.listdir("evidencias") if f.startswith("evidencia_")]
    assert len(screenshots) > 0, "No se generó screenshot"