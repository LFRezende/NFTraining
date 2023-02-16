from scripts.utils import LOCAL_CHAINS, FORKED_CHAINS, getAccount, getContract
from scripts.advanced_collectible.dac import deployContract
from brownie import AdvancedCollectible, network
import pytest

RNG = 777


def test_can_create_adv_collectible():
    ## Arrange
    if (
        network.show_active() not in LOCAL_CHAINS
        and network.show_active() not in FORKED_CHAINS
    ):
        pytest.skip()
    ## Act
    adv_collectible, created_tx = deployContract()
    # Grabbing an event
    requestId = created_tx.events["requestedCollectible"]["requestId"]
    getContract("vrfCoordinator").callBackWithRandomness(
        requestId, RNG, adv_collectible.address, {"from": getAccount()}
    )
    ## Assert
    assert adv_collectible.tokenCounter() == 1
    assert adv_collectible.tokenIdtoBreed(0) == RNG % 3
