import argparse
import logging
import helper
import puller

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-v', '--verbose', 
                      help='increase logging verbosity',
                      action='store_true')
  parser.add_argument('-c', '--conf', type=str,
                      help='configuration file for HN api')
  parser.add_argument('-a', '--auth', type=str,
                      help='authorization credentials for pocket api')
  parser.add_argument('-l', '--log', type=str,
                      help='path for program log')

  args = parser.parse_args()

  # setting log level
  if args.verbose:
    log_level = logging.DEBUG
  else:
    log_level = logging.INFO

  # setting log location
  if args.log is not None:
    logfile = args.log
  else:
    logfile = './hntracker.log'
  
  # setting up log
  logging.basicConfig(filename=logfile, level=log_level, 
                      format='%(asctime)s %(message)s')

  logger = logging.getLogger(__name__)

  # checking if conf is present
  if args.conf is None:
    helper.fatal('no configuraton file set', logger)

  api_caller = puller.HNCaller(args.conf, logger)

  # cleaning up log
  logger.close()
