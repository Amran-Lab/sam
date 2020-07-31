import pytest
import visits
def test_answer():
    assert 1 == 1

def test_lambda():
    assert visits.get_visits({"Items":[{"ID":1,"Visit":5}]}) == 6