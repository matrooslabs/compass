"""Chatgpt API client.

Set OPENAI_API_KEY environment variable to your API key.
"""
from absl import logging

import string

from openai import OpenAI


def generate_contract_description(contract_abi, contract_sourcecode, model="gpt-3.5-turbo"):

    template = """
    This is an ethereum solidity contract. Please explain step by step what this contract does.
    You should list out all the methods and storages used in this contract.
    Explain every methods and storage variables in detail as if you are explaining it to a golden retriever or a five year old child.
    It wasn't brain that got me here, I assure you that.

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
            {"role": "system", "content": "You are a solidity auditor to assist explaining solidity smart contract."},
            {"role": "user", "content": msg},
        ]
    )

    # return response
    return response.choices[0].message.content


def generate_search_tags(contract_abi, contract_sourcecode, model="gpt-3.5-turbo"):
    template = """
    Extract all the valid search tags from the contract abi and source code. Search tags are words with great importance when
    indexing the document into search engine. For example, if the contract has a method called "transfer", then "transfer" is a valid search tag.
    It should consider that the search tags should be the most probable words that a user would search for when they are looking for this contract.
    Please remove all the duplicates and return a list of search tags.

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
            {"role": "system", "content": "You are a solidity auditor to assist extract search tags from given solidity smart contract."},
            {"role": "user", "content": msg},
        ]
    )

    # return response
    return response.choices[0].message.content
