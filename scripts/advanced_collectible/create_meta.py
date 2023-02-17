from scripts.utils import getAccount, getBreed
from scripts.advanced_collectible.dac import deployContract, mintCollectible
from metadata.sample import metadata_template
from brownie import AdvancedCollectible


def createMeta():
    adv = mintCollectible()
    adv = mintCollectible()
    adv = AdvancedCollectible[-1]
    NFTnumber = adv.tokenCounter()
    print(f"You have now {NFTnumber} of collectibles!")
    for tokenId in range(0, NFTnumber):
        breed = getBreed(tokenId)


def main():
    createMeta()
