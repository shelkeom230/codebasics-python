import pytest ,mathlib

@pytest.mark.windows
def windows_1():
    assert True 

@pytest.mark.windows
def windows_2():
    assert True 

@pytest.mark.mac 
def mac_1():
    assert True 

@pytest.mark.mac 
def mac_2():
    assert True 