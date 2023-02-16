from scripts.utils import getAccount, getContract, config, network, Web3, OPENSEA_URL
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
    print("-->  Advanced Collectible Deployed!")
    fundLink(adv.address)
    return adv


def fundLink(contract_address, account=None, linktoken=None, amount=0.1 * 10**18):
    account = account if account else getAccount()
    linktoken = linktoken if linktoken else getContract("linkToken")
    tx_fund = linktoken.transfer(contract_address, amount, {"from": account})
    tx_fund.wait(1)
    print(f"Contract has been funded with {Web3.fromWei(amount)} LINK!")
    return tx_fund


def main():
    deployContract()
