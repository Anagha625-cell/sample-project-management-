import pytest
from grade_calculator import calculate_grade

def test_zero_marks():
    assert calculate_grade(0)[1] == "F"

def test_full_marks():
    assert calculate_grade(100)[1] == "A"

def test_invalid():
    with pytest.raises(ValueError):
        calculate_grade(-5)
