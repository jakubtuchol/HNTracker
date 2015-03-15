import argparse
import logging

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-v', '--verbose', 
                      help='increase logging verbosity',
                      action='store_true')
  args = parser.parse_args()

  filepath = sys.argv[1] # figure out a less sloppy way of doing this
  # setting up log
  logging.basicConfig(filename='/var/log/hntracker.log',
                      level=logging.INFO
                      format='%(asctime)s %(message)s')
  logging.getLogger(__name__)
  api_caller = HNCaller(filepath, logger)
