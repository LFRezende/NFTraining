from scripts.utils import getAccount
from brownie import SimpleCollectible


TOKEN_URI = "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deployContract():
    account = getAccount()
    tx_deploy = SimpleCollectible.deploy({"from": account})
    tx_deploy.wait(1)
    return tx_deploy


def mintNFT():
    account = getAccount()
    ctt = SimpleCollectible[-1]
    tx_minted = ctt.createCollectible(TOKEN_URI, {"from": account})
    tx_minted.wait(1)
    return tx_minted


def main():
    deployContract()
    mintNFT()
