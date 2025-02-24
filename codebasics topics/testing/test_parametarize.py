import parametrize_mathlib as pm 
import pytest 

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (2,4),
                             (3,9),
                             (9,81)
                         ])

def test_calc_square_1(test_input,expected_output):
    result=pm.calc_square(test_input)
    assert result==expected_output
