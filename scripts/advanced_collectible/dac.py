from scripts.utils import getAccount, OPENSEA_URL
from brownie import SimpleCollectible


TOKEN_URI = "ipfs://QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png"



def deployContract():
    account = getAccount()
    # REMEMBER: DEPLOYMENT DOES NOT REQUIRE WAITING!
    tx_deploy = SimpleCollectible.deploy({"from": account})
    # tx_deploy.wait(1)
    return tx_deploy


def mintNFT():
    account = getAccount()
    ctt = SimpleCollectible[-1]
    tx_minted = ctt.createCollectible(TOKEN_URI, {"from": account})
    tx_minted.wait(1)
    return tx_minted


def deploy_and_mint():
    deployed = deployContract()
    minted = mintNFT()
    print(
        f"You can view your NFT at {OPENSEA_URL.format(deployed.address, deployed.tokenCounter()-1)}"
    )
    print("You may have to wait up to 20 minutes for the minting to be successful.")
    return deployed

def main():
    deploy_and_mint()