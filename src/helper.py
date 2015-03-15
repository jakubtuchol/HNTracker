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

def call_api(url, logger):
  '''
  Given url, executes get request and returns json response
  '''
  resp = requests.get(url)
  if resp.status_code == 200:
    logger.debug('successful api call: 200 response')
    return resp.json()
  else:
    logger.error('api returning non-200 response')
    logger.error('returning %{resp}d reponse for call to %{url}s'.format(resp=response.status_code, call_url=url))
    return None

def err_exit(message, logger):
  logger.error(message)
  sys.exit(1)
