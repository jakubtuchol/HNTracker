import requests
import os.path
import logging
import sys

class HNCaller(object):
  def __init__(self, filepath, logger):
    self.logger = logger
    self.logger.debug('initializing api caller class...')
    
    # check if file exists
    if not os.path.isfile(filepath):
      self.logger.error('config file not found. exiting program...')
      sys.exit(1)
    
    with open(filepath, 'r') as conf_file:
      try:
        conf_json = json.loads(conf_file.read())
        self.logger.debug('successfully loaded json config')
      except ValueError:
        self.logger.error('malformed json config. exiting program...')
        sys.exit(1)

      # check if terms key in json configuration
      if terms in conf_json:
        self.terms = conf_json['terms']
      else:
        log.info('no search terms provided')
      #self.tags = conf_json['tags']

  def construct_call(self, search_terms=None, tags=None):
    '''
    Given search terms and tags, constructs url to
    be called
    '''
    # checking that at least one argument is provided
    if search_terms is None and tags is None:
      raise Exception('No arguments supplied')

    # using algolia hacker news api
    base_url = 'http://hn.algolia.com/api/v1/'
    params = ''

    if search_terms is not None and len(search_terms) > 0:
      if len(search_terms) == 1:
        params += 'search?query={term}'.format(term=search_terms[0])
      else:
        search_str = ','.join(search_terms)
        params += 'search?query=({term})'.format(term=search_str)

    # handling tags present
    if tags is not None and len(tags) > 0:
      if len(tags) == 1:
        params += '&tags={tag}'.format(tag=tags[0])
      else:
        tag_str = ','.join(tags)
        params += '&tags=({tag})'.format(tag=tag_str)
    
    return base_url + params

  def call_api(url):
    '''
    Given url, executes api call and evaluates return
    '''
    resp = requests.get(url)
    if resp.status_code == 200:
      json_resp = resp.json()
      resp.connection.close()
      if json_resp['nbHits'] == 0:
        self.logger.info('no hits found')
        return None
      else:
        return json_resp['nbHits']
    else:
      self.logger.error('hacker news api returning non-200 response')
      return None

def main():
  filepath = sys.argv[1] # figure out a less sloppy way of doing this
  # setting up log
  logging.basicConfig(filename='/var/log/hntracker.log',
                      level=logging.INFO
                      format='%(asctime)s %(message)s')
  logging.getLogger(__name__)
  api_caller = HNCaller(filepath, logger)
  
  
if __name__ == '__main__':
  main()
