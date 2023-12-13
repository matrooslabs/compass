from absl import logging
import chatgpt
import etherscan


def get_contract_code(address, client=None):
    """
    Gets the contract code from the address
    """
    if not client:
        client = etherscan.EtherscanClient()

    return client.get_contract(address)


def get_contract_code_description(address, client=None):
    """
    Gets the contract code analysis from the address using chatgpt
    """
    if not client:
        client = etherscan.EtherscanClient()

    abi = client.get_contract_abi(address)
    logging.info("Contract abi: %s", abi)

    code = client.get_contract_source_code(address)
    logging.info("Contract code: %s", code)

    return chatgpt.explain_solidity(abi, code)
