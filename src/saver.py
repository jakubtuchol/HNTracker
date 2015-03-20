import os.path
import json
import src.helper as helper

class HNSaver(object):
  def __init__(self, conf_path, logger):
    self.logger = logger
    self.logger.debug('initializing saver class...')

    conf_json = helper.load_json(conf_path, self.logger)

    if 'location' not in conf_json.keys():
      helper.fatal('no location for save file specified')

    self.savefile = conf_json['location']
    self.idfile = conf_json['idfile']

    if not os.path.isfile(self.savefile):
      with open(self.savefile, 'w') as save:
        save.write('id,date,title,url\n')

    if not os.path.isfile(self.idfile):
      with open(self.idfile, 'w') as idfile:
        id_json = { 'ids': [] }
        json.dump(id_json, idfile)

  def save_csv(self, stories):
    with open(self.savefile, 'a') as save, open(self.idfile, 'r+') as idfile:
      id_json = json.load(idfile)
      id_list = id_json['ids']
      for story in stories:
        if story['id'] not in id_list:
          id_list.append(story['id'])
          save.write('{},{},"{}",{}\n'.format(story['id'],
                                              story['date'],
                                              story['title'],
                                              story['url']))
      idfile.seek(0)
      id_json['ids'] = id_list
      json.dump(id_json, idfile)
      idfile.truncate()
