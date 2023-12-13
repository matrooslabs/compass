from absl import logging
import chatgpt
import etherscan


def get_description(address, client=None):
    """
    Gets the contract code analysis from the address using chatgpt
    """
    if not client:
        client = etherscan.EtherscanClient()

    abi = client.get_contract_abi(address)
    code = client.get_contract_source_code(address)

    return chatgpt.generate_contract_description(abi, code)


def get_search_tags(address, client=None):
    """
    Gets the contract search tags from the address using chatgpt
    """

    if not client:
        client = etherscan.EtherscanClient()

    abi = client.get_contract_abi(address)
    code = client.get_contract_source_code(address)

    return chatgpt.generate_search_tags(abi, code)
