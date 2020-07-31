import pytest
import app
def test_answer():
    assert 1 == 1

def test_lambda():
    assert app.get_visits({"Items":[{"ID":1,"Visit":5}]}) == 5