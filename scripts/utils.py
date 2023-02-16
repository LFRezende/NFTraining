from brownie import accounts, network, config, VRFCoordinatorMock, LinkToken, Contract

LOCAL_CHAINS = ["development"]
FORKED_CHAINS = ["mainnet-fork"]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def getAccount(id=None, index=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_CHAINS or network.show_active() in FORKED_CHAINS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


name_to_type = {"vrfCoordinator": VRFCoordinatorMock, "linkToken": LinkToken}


def getContract(contract_name=None):
    contract_type = name_to_type[contract_name]  # This is a list of contracts still
    if network.show_active() in LOCAL_CHAINS:
        if len(contract_type) <= 0:
            deploy_mocks()
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract


def deploy_mocks():
    account = getAccount()
    print("-->  Deploying LinkToken Mock...")
    linktoken = LinkToken.deploy({"from": account})
    print("-->  LinkToken Deployed!")
    print("-->  Deploying VRFCoordinatorMock...")
    vrf = VRFCoordinatorMock.deploy(linktoken.address, {"from": account})
    print("-->  VRFCoordinatorMock deployed!")
    deployed_mocks = {"linkToken": linktoken, "vrfCoordinator": vrf}
    return deployed_mocks
