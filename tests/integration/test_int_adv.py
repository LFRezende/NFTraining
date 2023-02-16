from scripts.utils import LOCAL_CHAINS, FORKED_CHAINS, getAccount, getContract
from scripts.advanced_collectible.dac import deployContract, mintCollectible
from brownie import AdvancedCollectible, network
import time
import pytest


def test_create_adv_int():
    ## Arrange
    if (
        network.show_active() in LOCAL_CHAINS
        and network.show_active()  in FORKED_CHAINS
    ):
        pytest.skip("Only for TESTNET testing!")
    ## Act
    rx_deployed = deployContract()
    adv_collectible = mintCollectible()
    # Giving time for the VRFCoordinator to respond.
    time.sleep(60)
    ## Assert
    assert adv_collectible.tokenCounter() == 1
