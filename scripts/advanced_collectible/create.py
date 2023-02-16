from scripts.utils import getAccount
from scripts.advanced_collectible.dac import fundLink
from brownie import AdvancedCollectible


def main():
    account = getAccount()
    advanced_collectible = AdvancedCollectible[
        -1
    ]  # We do not wish to re-deploy the smart contract --> just to create a collectible.
    fundLink(advanced_collectible.address, amount=0.2 * 10**18)
    tx_create = advanced_collectible.createCollectible({"from": account})
    tx_create.wait(1)
    print("-->  NFT MINTED!")
