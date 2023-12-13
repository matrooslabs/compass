"""Etherscan.io API client.

Set ETHERSCAN_API_KEY environment variable to your API key."""
import json
import os

import requests


ETHERSCAN_ENDPOINT = "https://api.etherscan.io/api"


class EtherscanClient:

    def __init__(self, api_key=None):
        if api_key:
            self.api_key = api_key
        else:
            self.api_key = os.getenv("ETHERSCAN_API_KEY")


    def get_contract_abi(self, contract_address):
        """Get contract source code from Etherscan.io API."""
        params = {
            "module": "contract",
            "action": "getabi",
            "address": contract_address,
            "apikey": self.api_key
        }
        response = requests.get(ETHERSCAN_ENDPOINT, params=params)
        return response.json()

    def get_contract_source_code(self, contract_address, target_contract_name='Uniswap', max_count=3):
        """Get contract source code from Etherscan.io API."""
        params = {
            "module": "contract",
            "action": "getsourcecode",
            "address": contract_address,
            "apikey": self.api_key
        }
        response = requests.get(ETHERSCAN_ENDPOINT, params=params)
        result = response.json()['result'][0]['SourceCode']
        result = json.loads(result[1:-1])

        sources = {}
        count = 0
        for filename, value in result['sources'].items():
            if filename.find(target_contract_name) != -1:
                sourcecode = value['content'].encode('raw_unicode_escape').decode('unicode_escape')
                sources[filename] = sourcecode
                count += 1

            if count >= max_count:
                break

        return sources
