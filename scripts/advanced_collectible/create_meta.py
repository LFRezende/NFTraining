from scripts.utils import getAccount, getBreed
from scripts.advanced_collectible.dac import deployContract
from metadata.sample import metadata_template
from brownie import AdvancedCollectible, network
from pathlib import Path


def createMeta():
    deployContract()
    adv = AdvancedCollectible[-1]
    NFTnumber = adv.tokenCounter()
    print(f"You have now {NFTnumber} of collectibles!")
    for tokenId in range(0, NFTnumber):
        breed = getBreed(tokenId)
        # Checking if the metadata isn't repeated
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{tokenId}-{breed}.json"
        )
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists. Delete it to overwrite it.")
        else:
            print(f"Creating metadata file: {metadata_file_name}")


def main():
    createMeta()
