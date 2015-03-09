import requests

def get_hn():
  resp = requests.get('http://news.ycombinator.com')
  if resp.status_code == 200:
    print(resp)
  else:
    print('Cannot connect to hacker news')

if __name__ == '__main__':
  get_hn()
