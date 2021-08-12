import pytest
from brownie import Greeter, accounts

@pytest.fixture
def greeter():
    return accounts[0].deploy(Greeter, "Hello, World!")

# Check if the contract was deployed with the correct greeting 
def test_greeter(greeter):
    assert greeter.greet() == "Hello, World!"

# Check if the greeting changes
def test_set_greeting(greeter):
    greeter.setGreeting("Hola, mundo!")
    assert greeter.greet() == "Hola, mundo!"