from brownie import accounts, network, config

LOCAL_CHAINS = ["development"]
FORKED_CHAINS = ["mainnet-fork"]


def getAccount(id=None, index=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_CHAINS or network.show_active() in FORKED_CHAINS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
