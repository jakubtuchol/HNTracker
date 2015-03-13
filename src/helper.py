import sys
import os.path

def load_json(filepath, logger):
    # check if file exists
    if not os.path.isfile(filepath):
      logger.error('config file not found. exiting program...')
      sys.exit(1)
    
    with open(filepath, 'r') as conf_file:
      try:
        conf_json = json.loads(conf_file.read())
        logger.debug('successfully loaded json config')
        return conf_json
      except ValueError:
        logger.error('malformed json config. exiting program...')
        sys.exit(1)
