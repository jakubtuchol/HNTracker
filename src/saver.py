import os.path

class HNSaver(object):
  def __init__(self, conf_path, logger):
    self.logger = logger
    self.logger.debug('initializing saver class...')

    conf_json = helper.load_json(conf_path, self.logger)

    if 'location' not in conf_json.keys():
      helper.fatal('no location for save file specified')

    savefile = conf_json['location']

    # setting file mode to write/append depending
    # on whether or not it exists
    if os.path.isfile(savefile):
      filemode = 'a'
    else:
      filemode = 'w'

  def save_story(url):
    pass
