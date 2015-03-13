import os.path

class HNSaver(object):
  def __init__(self, conf_path, logger):
    self.logger = logger
    self.logger.debug('initializing saver class...')

    conf_json = helper.load_json(conf_path, self.logger)
    if 'consumer_key' not in conf_json:
      self.logger.error('consumer_key tag not in auth file, cannot access pocket api')
      self.logger.error('exiting program')
      sys.exit(1)
      
    self.cons_key = conf_json['consumer_key']

  def save_story(url):
    pass
