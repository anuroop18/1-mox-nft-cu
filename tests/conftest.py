import boa
import pytest
from eth_utils import to_wei
from moccasin.config import get_active_network

from script.deploy_basic_nft import deploy_basic_nft
from script.deploy_mood_nft import deploy_mood_nft


@pytest.fixture(scope="session")
def owner():
    owner = get_active_network().get_default_account()
    return owner.address

@pytest.fixture(scope="function")
def aryan():
    aryan = boa.env.generate_address("aryan")
    boa.env.set_balance(aryan, to_wei(100, "ether"))
    return aryan

@pytest.fixture(scope="function")
def raghav():
    raghav = boa.env.generate_address("raghav")
    boa.env.set_balance(raghav, to_wei(100, "ether"))
    return raghav

@pytest.fixture(scope="function")
def chikapa():
    chikapa = boa.env.generate_address("chikapa")
    boa.env.set_balance(chikapa, to_wei(100, "ether"))
    return chikapa

@pytest.fixture(scope="function")
def basic_nft(owner):
    with boa.env.prank(owner):
        return deploy_basic_nft()

@pytest.fixture(scope="function")
def mood_nft(owner):
    with boa.env.prank(owner):
        return deploy_mood_nft()
    
