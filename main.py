import os

from absl import app
from absl import flags
from absl import logging
import dotenv

import features


FLAGS = flags.FLAGS

flags.DEFINE_string('contract_address', None, 'Address of the contract.')
flags.DEFINE_string('model_name', 'gpt-3.5-turbo', 'Name of the model in openai.')
flags.DEFINE_string('etherscan_api_key', None, 'Etherscan API key.')

# Loads env vars.
dotenv.load_dotenv(verbose=True)


def main(_):
    logging.info('Extracting features for %s', FLAGS.contract_address)
    desc = features.get_description(FLAGS.contract_address)
    logging.info('Contract %s Description: %s', FLAGS.contract_address, desc)

    tags = features.get_search_tags(FLAGS.contract_address)
    logging.info('Contract %s Search Tags: %s', FLAGS.contract_address, tags)


if __name__ == '__main__':
    app.run(main)
