from scripts.utils import getAccount
from brownie import SimpleCollectible


TOKEN_URI = "ipfs://QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


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


def main():
    deployed = deployContract()
    minted = mintNFT()
    print(
        f"You can view your NFT at {OPENSEA_URL.format(deployed.address, deployed.tokenCounter()-1)}"
    )
    print("You may have to wait up to 20 minutes for the minting to be successful.")
