import playwright
import pytest


@pytest.fixture(scope="session")
def preSetupWork():
    print("I setup browser instance")
    
    
 