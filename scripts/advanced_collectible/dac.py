from scripts.utils import getAccount, getContract, config, network, OPENSEA_URL
from brownie import AdvancedCollectible


TOKEN_URI = "ipfs://QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png"


def deployContract():
    account = getAccount()
    # REMEMBER: DEPLOYMENT DOES NOT REQUIRE WAITING!
    adv = AdvancedCollectible.deploy(
        getContract("vrfCoordinator"),
        getContract("linkToken"),
        config["networks"][network.show_active()]["keyHash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    return adv


def main():
    deployContract()
