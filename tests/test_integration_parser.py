
import pytest
from backend.contact_parser import ContactParser
from backend.title_manager import TitleManager

@pytest.fixture
def parser():
    title_manager = TitleManager()
    return ContactParser(title_manager=title_manager)

def test_parse_complete_contact(parser):
    input_str = "Herr Dr. Karl von Württemberg"
    result = parser.parse(input_str)
    assert result["salutation"] == "Herr"
    assert "Dr." in result["titles"]
    assert result["first_name"] == "Karl"
    assert "Württemberg" in result["last_name"]
    assert "von" in result["last_name"]
    assert result["gender"] == "männlich"

def test_parse_complex_title_chain(parser):
    input_str = "Herr Dr.-Ing. Dr. rer. nat. Paul Steffens"
    result = parser.parse(input_str)
    assert "Dr.-Ing." in result["titles"]
    assert "Dr. rer. nat." in result["titles"]
    assert result["first_name"] == "Paul"
    assert result["last_name"] == "Steffens"

def test_female_french_title(parser):
    input_str = "Mme. Charlotte Noir"
    result = parser.parse(input_str)
    assert result["salutation"] == "Mme."
    assert result["gender"] == "weiblich"
    assert result["language"] == "FR"
    assert result["first_name"] == "Charlotte"
    assert result["last_name"] == "Noir"

def test_unknown_input(parser):
    input_str = "Estobar y Gonzales"
    result = parser.parse(input_str)
    assert result["last_name"] == "Estobar y Gonzales" or "Gonzales" in result["last_name"]
