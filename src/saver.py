import os.path

class HNSaver(object):
  def __init__(self, conf_path, logger):
    self.logger = logger
    self.logger.debug('initializing saver class...')

    conf_json = helper.load_json(conf_path, self.logger)

    if 'location' not in conf_json.keys():
      helper.fatal('no location for save file specified')

    self.savefile = conf_json['location']

    if not os.path.isfile(self.savefile):
      with open(self.savefile, 'w') as save:
        save.write('date,title,url\n')

  def save_csv(stories):
    with open(self.savefile, 'a') as save:
      for story in stories:
        save.write('{},{},{},{}\n'.format(story['id'],
                                       story['date'],
                                       story['title'],
                                       story['url']))
