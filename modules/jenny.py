import random, json
from datetime import datetime
from . import wolf as wolfModule
from . import chrome as chromeModule
from . import files as filesModule

globalConfigs = json.load(open('configs.json'))

def getName():
  return globalConfigs['name']

def config(item):
  if item in globalConfigs:
    return globalConfigs[item]

def getPositives():
  return globalConfigs['messages']['positives']

def getNegatives():
  return globalConfigs['messages']['negatives']

def yesOrNo(answer):
  yes = getPositives()
  no = getNegatives()

  if answer in yes:
    return 'yes'

  return 'no'

def isYes(answer):
  return yesOrNo(answer) == 'yes'

def isNo(answer):
  return yesOrNo(answer) == 'no'

def getTitles():
  return globalConfigs['messages']['titles']

def getRandomTitle():
  return random.choice(getTitles())

def greet():
  now = datetime.now()
  hour = now.hour
  if hour < 12:
    message = 'Good morning'
  elif hour < 18:
    message = 'Good afternoon'
  else:
    message = 'Good evening'

  return message + ', ' + getRandomTitle()

def ask(question=False, inputDefault=False, greetings=False):
  name = getName()
  title = getRandomTitle()

  if not question:
    question = random.choice(globalConfigs['messages']['initiators'])

  if greetings:
    say(greet())

  message = '\n' + name + ': ' + question + ', ' + title + '? \nYou: '

  return input(message)

def apologise():
  message = random.choice(globalConfigs['messages']['confused'])
  message = message + ',' + getRandomTitle()
  return message

def output(message):
  print(message)

def say(message):
  say = getName() + ': ' + str(message)
  return output(say)

def process(userCommand):
  commands = getCommandsList()

  for index, command in commands.items():
    module = command['module']
    match = command['match']
    keywords = command['keywords']
    action = command['action']

    if match == 'one':
      isMatched = any(keyword in userCommand for keyword in keywords)
    else:
      isMatched = all(keyword in userCommand for keyword in keywords)

    if isMatched:
      if module == 'help':
        return help()
      else:
        function = getattr(module, action)
        return function()

  if isYes(config('always_search')):
    answer = 'yes'
    say('No commands matched. Let me pull it from the internet for you.')
  else:
    answer = ask('No commands matched. Would you like to search instead')

  if isYes(answer):
    output = wolfModule.search(userCommand)
    if not output or output == 'None':
      return say(apologise())

    return say(output)

def help():
  for command, contents in getCommandsList().items():
    print(f'    {command} : {contents["info"]}')
    print('    ' + str(contents['keywords']))
    print('\n')

# match options are one or all

def getCommandsList():
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
    'module': filesModule,
    'keywords': {'random', 'music'},
    'match': 'one',
    'action': 'playRandomMusic'
  }

  commands['chrome_cleannsfw'] = {
    'info': 'Removes all NSFW links from Chrome history',
    'module': chromeModule,
    'keywords': {'chrome', 'clean', 'nsfw'},
    'match': 'all',
    'action': 'removeNsfw'
  }

  commands['play_on_youtube'] = {
    'info': 'Play a video on YouTube in Chrome',
    'module': chromeModule,
    'keywords': {'play', 'youtube'},
    'match': 'all',
    'action': 'playOnYoutube'
  }

  commands['search_torrent'] = {
    'info': 'Search a torrent across multiple websites',
    'module': chromeModule,
    'keywords': {'search', 'torrent'},
    'match': 'all',
    'action': 'searchTorrent'
  }

  commands['sort_directory'] = {
    'info': 'Sorts a directory contents by file type into another dir',
    'module': filesModule,
    'keywords': {'sort', 'directory'},
    'match': 'all',
    'action': 'sortDirectory'
  }

  return commands