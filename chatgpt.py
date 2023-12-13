"""Chatgpt API client.

Set OPENAI_API_KEY environment variable to your API key.
"""
from absl import logging

import string

from openai import OpenAI


def explain_solidity(contract_abi, contract_sourcecode, model="gpt-3.5-turbo"):

    template = """
    This is a solidity contract. Please explain step by step what this contract does.
    You should list out all the methods and storages used in this contract.
    Explain every methods and storages in detail as if you are explaining it to a golden retriever or a five year old child
    who has no idea what solidity or what blockchain is.

    Here is the contract abi:

    $abi

    And here is the contract source code:

    $code

    """

    code = ''

    for filename, content in contract_sourcecode.items():
        code += filename
        code += '\n'
        code += content

    msg = string.Template(template).substitute(abi=contract_abi, code=code)
    logging.debug('Chatgpt message: %s', msg)
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a solidity expert to assist explaining solidity contract from its abi."},
            {"role": "user", "content": msg},
        ]
    )

    # return response
    return response.choices[0].message.content