import random, json, os
from datetime import datetime
from . import wolf as wolf_module
from . import chrome as chrome_module
from . import files as files_module
from . import youtubedl as youtubedl_module
from . import ffmpeg as ffmpeg_module

current_directory = os.path.dirname(os.path.abspath(__file__))
base_directory = os.path.dirname(current_directory)
global_cofigs = json.load(open(base_directory + '/configs.json'))

def get_name():
  return global_cofigs['name']

def config(item):
  if item in global_cofigs:
    return global_cofigs[item]

def get_positives():
  return global_cofigs['messages']['positives']

def get_negatives():
  return global_cofigs['messages']['negatives']

def yes_or_no(answer):
  yes = get_positives()
  no = get_negatives()

  if answer in yes:
    return 'yes'

  return 'no'

def is_yes(answer):
  return yes_or_no(answer) == 'yes'

def is_no(answer):
  return yes_or_no(answer) == 'no'

def get_titles():
  return global_cofigs['messages']['titles']

def get_random_title():
  return random.choice(get_titles())

def greet():
  now = datetime.now()
  hour = now.hour
  if hour < 12:
    message = 'Good morning'
  elif hour < 18:
    message = 'Good afternoon'
  else:
    message = 'Good evening'

  return message + ', ' + get_random_title()

def get_query_from_user_command(user_cmd):
  if '[' in user_cmd and ']' in user_cmd:
    return user_cmd[user_cmd.find('[')+1 : user_cmd.find(']')]

def ask(question=False, input_default=False, greetings=False):
  name = get_name()
  title = get_random_title()

  if not question:
    question = random.choice(global_cofigs['messages']['initiators'])

  if greetings:
    say(greet())

  message = '\n' + name + ': ' + question + ', ' + title + '? \nYou: '

  return input(message)

def apologise():
  message = random.choice(global_cofigs['messages']['confused'])
  message = message + ',' + get_random_title()
  return message

def output(message):
  print(message)

def say(message):
  say = get_name() + ': ' + str(message)
  return output(say)

def process(user_command):
  commands = get_commands_list()

  for index, command in commands.items():
    module = command['module']
    match = command['match']
    keywords = command['keywords']
    action = command['action']

    if match == 'one':
      is_matched = any(keyword in user_command for keyword in keywords)
    else:
      is_matched = all(keyword in user_command for keyword in keywords)

    if is_matched:
      if module == 'help':
        return help()
      else:
        query = get_query_from_user_command(user_command)
        if query:
          function = getattr(module, action)(query=query)
        else:
          function = getattr(module, action)
          function()

        return function

  if is_yes(config('always_search')):
    answer = 'yes'
    say('No commands matched. Let me pull it from the internet for you.')
  else:
    answer = ask('No commands matched. Would you like to search instead')

  if is_yes(answer):
    output = wolf_module.search(user_command)
    if not output or output == 'None':
      return say(apologise())

    return say(output)

def help():
  for command, contents in get_commands_list().items():
    keywords = str(contents['keywords'])
    print(f'    {command} : {contents["info"]} {keywords}')
    print('')

# match options are one or all

def get_commands_list():
  commands = {}

  commands['help'] = {
    'info': 'Prints out available actions',
    'module': 'help',
    'keywords': {'help', '--help', 'show commands'},
    'match': 'one',
    'action': ''
  }

  commands['rand_music'] = {
    'info': 'Plays random music from music dir',
    'module': files_module,
    'keywords': {'random', 'music'},
    'match': 'all',
    'action': 'play_random_music'
  }

  commands['chrome_cleannsfw'] = {
    'info': 'Removes all NSFW links from Chrome history',
    'module': chrome_module,
    'keywords': {'chrome', 'clean', 'nsfw'},
    'match': 'all',
    'action': 'remove_nsfw'
  }

  commands['search_on_youtube'] = {
    'info': 'Search a video on YouTube in Chrome',
    'module': chrome_module,
    'keywords': {'play', 'youtube'},
    'match': 'all',
    'action': 'search_on_youtube'
  }

  commands['download_video'] = {
    'info': 'Download a video from 30+ sources',
    'module': youtubedl_module,
    'keywords': {'download', 'video'},
    'match': 'all',
    'action': 'download'
  }

  commands['download_audio_youtube'] = {
    'info': 'Download MP3 of YouTube video',
    'module': youtubedl_module,
    'keywords': {'download', 'audio'},
    'match': 'all',
    'action': 'download_audio_only'
  }

  commands['download_channel_youtube'] = {
    'info': 'Download entire YouTube channel',
    'module': youtubedl_module,
    'keywords': {'download', 'channel'},
    'match': 'all',
    'action': 'download_channel'
  }

  # ffmpeg starts
  commands['convert_video'] = {
    'info': 'Convert video to other format or audio',
    'module': ffmpeg_module,
    'keywords': {'convert', 'video'},
    'match': 'all',
    'action': 'convert'
  }

  commands['rotate_video'] = {
    'info': 'Rotate video by any degrees',
    'module': ffmpeg_module,
    'keywords': {'rotate', 'video'},
    'match': 'all',
    'action': 'rotate'
  }
  # ffmpeg ends

  commands['search_torrent'] = {
    'info': 'Search a torrent across multiple websites',
    'module': chrome_module,
    'keywords': {'search', 'torrent'},
    'match': 'all',
    'action': 'search_torrent'
  }

  commands['search_images'] = {
    'info': 'Search images in browser',
    'module': chrome_module,
    'keywords': {'search', 'images'},
    'match': 'all',
    'action': 'search_images'
  }

  commands['sort_directory'] = {
    'info': 'Sorts a directory contents by file type into another dir',
    'module': files_module,
    'keywords': {'sort', 'directory'},
    'match': 'all',
    'action': 'sort_directory'
  }

  commands['set_wallpaper'] = {
    'info': 'Set random wallpaper from directoruy',
    'module': files_module,
    'keywords': {'set', 'wallpaper'},
    'match': 'all',
    'action': 'set_random_wallpaper'
  }

  commands['start_workplace'] = {
    'info': 'Opens up tools needed for development',
    'module': files_module,
    'keywords': {'startwork', 'wakeup'},
    'match': 'one',
    'action': 'start_work_place'
  }

  commands['goto'] = {
    'info': 'Quickly jump to a folder [reads from configs.json]',
    'module': files_module,
    'keywords': {'goto', 'openup'},
    'match': 'one',
    'action': 'goto'
  }

  return commands