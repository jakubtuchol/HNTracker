import requests

def construct_call(search_terms=None, tags=None):
  '''
  Given search terms and tags, constructs url to
  be called
  '''
  # using algolia hacker news api
  base_url = 'http://hn.algolia.com/api/v1/'
  params = 'search?query={term}'.format(term=search_terms[0])

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
    if json_resp['nbHits'] == 0:
      return 0
    else:
      return json_resp['nbHits']
  else:
    return -1
