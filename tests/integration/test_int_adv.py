from scripts.utils import LOCAL_CHAINS, FORKED_CHAINS, getAccount, getContract
from scripts.advanced_collectible.dac import deployContract
from brownie import AdvancedCollectible, network
import time
import pytest

RNG = 777


def test_create_adv_int():
    ## Arrange
    if (
        network.show_active() in LOCAL_CHAINS
        and network.show_active()  in FORKED_CHAINS
    ):
        pytest.skip("Only for TESTNET testing!")
    ## Act
    adv_collectible, created_tx = deployContract()
    # Giving time for the VRFCoordinator to respond.
    time.sleep(60)
    ## Assert
    assert adv_collectible.tokenCounter() == 1
