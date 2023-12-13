from web3 import Web3


def get_storage(address, slot):
    """
    Gets the storage from the address
    """
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/5c92864a308b45b6a8c3559b63cb5b38'))
    contract = w3.eth.get_storage_at(address, slot)
    return contract.functions.getStorage().call()
