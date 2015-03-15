import argparse
import logging
import helper

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-v', '--verbose', 
                      help='increase logging verbosity',
                      action='store_true')
  parser.add_argument('-c', '--conf', type=str,
                      help='configuration file for HN api')
  parser.add_argument('-a', '--auth', type=str, default='',
                      help='authorization credentials for pocket api')
  parser.add_argument('-l', '--log', type=str, default='',
                      help='path for program log')

  args = parser.parse_args()

  # setting log level
  if args.verbose:
    log_level = logging.DEBUG
  else:
    log_level = logging.INFO

  # setting log location
  if args.log != '':
    logfile = args.log
  else:
    logfile = '/var/log/hntracker.log' 

  # setting up log
  logging.basicConfig(filename=logfile, level=log_level, 
                      format='%(asctime)s %(message)s')

  logger = logging.getLogger(__name__)
  api_caller = HNCaller(filepath, logger)
