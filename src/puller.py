import src.helper as helper

class HNCaller(object):
  def __init__(self, conf_path, logger):
    self.logger = logger
    self.logger.debug('initializing api caller class...')
    
    conf_json = helper.load_json(conf_path, self.logger)

    # check if terms key in json configuration
    if 'terms' in conf_json:
      self.terms = conf_json['terms']
    else:
      self.terms = None
      self.logger.warning('no search terms provided in configuration')

    if 'tags' in conf_json:
      self.tags = conf_json['tags']
    else:
      self.tags = None
      self.logger.warning('no tags provided in configuration')

  def construct_call(self):
    # checking that at least one argument is provided
    if self.terms is None and self.tags is None:
      raise Exception('No arguments supplied')

    # using algolia hacker news api
    base_url = 'http://hn.algolia.com/api/v1/'
    params = ''

    if self.terms is not None and len(self.terms) > 0:
      if len(self.terms) == 1:
        params += 'search?query={}'.format(self.terms[0])
      else:
        search_str = ','.join(self.terms)
        params += 'search?query=({})'.format(search_str)

    # handling tags present
    if self.tags is not None and len(self.tags) > 0:
      if len(self.tags) == 1:
        params += '&tags={}'.format(self.tags[0])
      else:
        tag_str = ','.join(self.tags)
        params += '&tags=({})'.format(tag_str)
    
    return base_url + params

  def process_call(self, url):
    resp = helper.call_api(url, self.logger)
    if resp['nbHits'] == 0:
      self.logger.info('no hits found')
      return
    stories = []
    for elem in resp['hits']:
      story = {
        'id':    elem['objectID'],
        'date':  elem['created_at'],
        'title': elem['title'],
        'url':   elem['url']
      }
      stories.append(story)
    return stories
