import argparse
import logging
import helper

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-v', '--verbose', 
                      help='increase logging verbosity',
                      action='store_true')
  parser.add_argument('-c', '--conf',
                      help='configuration file for HN api')
  parser.add_argument('-a', '--auth',
                      help-'authorization credentials for pocket api')

  args = parser.parse_args()

  print(args.verbose)
  # setting up log
  logging.basicConfig(filename='/var/log/hntracker.log',
                      level=logging.INFO
                      format='%(asctime)s %(message)s')
  logging.getLogger(__name__)
  api_caller = HNCaller(filepath, logger)
