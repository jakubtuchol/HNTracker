import requests
import helper

class HNCaller(object):
  def __init__(self, conf_path, logger):
    self.logger = logger
    self.logger.debug('initializing api caller class...')
    
    conf_json = helper.load_json(conf_path, self.logger)

    # check if terms key in json configuration
    if terms in conf_json:
      self.terms = conf_json['terms']
    else:
      self.logger.info('no search terms provided')

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
        params += 'search?query={}'.format(search_terms[0])
      else:
        search_str = ','.join(search_terms)
        params += 'search?query=({})'.format(search_str)

    # handling tags present
    if tags is not None and len(tags) > 0:
      if len(tags) == 1:
        params += '&tags={}'.format(tags[0])
      else:
        tag_str = ','.join(tags)
        params += '&tags=({})'.format(tag_str)
    
    return base_url + params

  def call_api(url):
    
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
