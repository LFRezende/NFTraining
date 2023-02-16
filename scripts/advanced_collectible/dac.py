from scripts.utils import getAccount, getContract, config, network, OPENSEA_URL
from brownie import AdvancedCollectible
from web3 import Web3


TOKEN_URI = "ipfs://QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png"


def deployContract():
    account = getAccount()
    # REMEMBER: DEPLOYMENT DOES NOT REQUIRE WAITING!
    tx_deploy = AdvancedCollectible.deploy(
        getContract("vrfCoordinator"),
        getContract("linkToken"),
        config["networks"][network.show_active()]["keyHash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    print("-->  Advanced Collectible Deployed!")

    return tx_deploy


def mintCollectible():
    account = getAccount()
    adv = AdvancedCollectible[-1]
    fundLink(adv.address)
    creating_tx = adv.createCollectible({"from": account})
    creating_tx.wait(1)
    print("NFT minted!")
    print(
        f"You can view your NFT at {OPENSEA_URL.format(adv.address, adv.tokenCounter()-1)}"
    )
    return adv


def fundLink(
    contract_address, account=None, linktoken=None, amount=Web3.toWei(1, "ether")
):
    print(f"-->  Funding with LINK...")
    account = account if account else getAccount()
    linktoken = linktoken if linktoken else getContract("linkToken")
    tx_fund = linktoken.transfer(contract_address, amount, {"from": account})
    tx_fund.wait(1)
    print(f"Contract has been funded with LINK!")
    return tx_fund


def main():
    deployContract()
    mintCollectible()
