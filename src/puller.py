import requests

def construct_call(search_term=None, tags=None):
  pass

def call_api(search_term, tags=None):
  '''
  Given search term and tags, constructs
  and executes search query
  '''
  # using algolia hacker news api
  base_url = 'http://hn.algolia.com/api/v1/'
  search_params = 'search?query={term}'
  # handling tags present
  if tags is not None and len(tags) > 0:
    if len(tags) == 1:
      search_params += '&tags={tag}'.format(tag=tags[0])
    else:
      tag_str = ','.join(tags)
      search_params += '&tags=({tag})'.format(tag=tag_str)
  
  resp = requests.get(base_url + search_params)
  if resp.status_code == 200:
    json_resp = resp.json()
    if json_resp['nbHits'] == 0:
      print('No hits for term')
  else:
    print('Cannot connect to hacker news api')

if __name__ == '__main__':
  get_hn_front_page('haskell')
