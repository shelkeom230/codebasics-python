import mathlib 

'''
the testing function doesn't takes any input

some rules 

1. file name must have test_ prefix
2. function name must have test_ prefix


methods to run the test files 
1. python -m pytest (run all files with test_ prefix)
2. py.test -v (does the same but with detailed info about all the functions)

3. to stip running a test
do @pytest.mark.skip and pass the reason 

to see the reason for skipping

do pytest -v -rxs 

@pytest.mark.skipif(sys.version_info<(3,5),reason="not required at that moment.") (use this reason to check for if condition)
'''
import pytest,sys 

def test_calc_total():
    total=mathlib.calc_total(4,5)
    assert total==9

def test_calc_product():
    product=mathlib.calc_product(4,5)
    assert product==20

def test_dummy():
    assert True 
    