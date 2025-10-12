import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I setup module instance")
    return "pass"


@pytest.fixture(scope="function")
def secondWork():
    print("I setup secondwork instance")
    yield 
    print("teardown validation")
    

def test_initialCheck(preWork,secondWork):
    print("This is the first test")
    assert preWork == "pass"
    
    
def test_SecondCheck(preSetupWork, secondWork):
    print("This is the Second test")