from scripts.utils import LOCAL_CHAINS, FORKED_CHAINS, getAccount
from scripts.dac import deploy_and_mint
from brownie import SimpleCollectible, network
import pytest


def test_simple_collectible():
    if (
        network.show_active() not in LOCAL_CHAINS
        and network.show_active() not in FORKED_CHAINS
    ):
        pytest.skip()
    # Deploy and Mint. See if the owner of the first minted NFT is the actual account.
    simple_collectible = deploy_and_mint()
    # Owner of the tokenId!
    assert simple_collectible.ownerOf(0) == getAccount()
