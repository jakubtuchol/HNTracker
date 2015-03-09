import requests

def get_hn_front_page(search_term):
  # using algolia hacker news api
  base_url = 'http://hn.algolia.com/api/v1/'
  search_params = 'search?query={term}&tags=front_page'.format(term=search_term)
  resp = requests.get(base_url + search_params)
  if resp.status_code == 200:
    json_resp = resp.json()
    if json_resp['nbHits'] == 0:
      print('No hits for term')
  else:
    print('Cannot connect to hacker news api')

if __name__ == '__main__':
  get_hn_front_page('haskell')
