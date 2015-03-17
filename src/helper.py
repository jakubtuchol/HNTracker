import sys
import os.path
import json


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

def call_api(url, logger):
  '''
  Given url, executes get request and returns json response
  '''
  resp = requests.get(url)
  if resp.status_code == 200:
    logger.debug('successful api call: 200 response')
    resp.connection.close() # necessary?
    return resp.json()
  else:
    logger.error('api returning non-200 response')
    logger.error('returning {} reponse for call to {}'.format(str(resp.status_code), url))
    resp.connection.close() # necessary?
    return None

def fatal(message, logger):
  logger.error(message)
  sys.exit(1)
