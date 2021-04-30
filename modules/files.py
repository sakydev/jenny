# iterates over each file in input directory
# and moves to outputdir under folders by file type
from os import system, listdir, path, mkdir, rename, getlogin
import shutil
from . import jenny

def sortDirectory():
  inputDefault = 'C:/Users/' + getlogin() + '/Downloads'
  outputDefault = 'G:/Downloads'

  inputDir = jenny.ask(f'Input directory or press enter to use default {inputDefault}') or inputDefault
  outputDir = jenny.ask(f'Output directory (enter to use default {outputDefault}') or outputDefault

  if not path.exists(inputDir):
    jenny.say(f'Input directory not found @ {inputDir}')
    return

  if not path.exists(outputDir):
    jenny.say(f'Output directory not found @ {outputDir}')
    return

  mapping = {
    'video': ['mp4', 'mpeg', 'wmv', 'mov', 'flv'],
    'audio': ['wav', 'mp3'],
    'images': ['jpg', 'jpeg', 'png', 'ico'],
    'torrents': ['torrent'],
    'subtitles': ['srt'],
    'zips': ['zip'],
    'software': ['exe', 'msi'],
    'files': ['html', 'php', 'css', 'js', 'py', 'csv', 'json', 'pdf', 'docx', 'txt'],
    'sql': ['sql']
  }

  for file in listdir(inputDir):
    fullFilePath = inputDir + '/' + file
    extension = path.splitext(file)[1].replace('.', '')
    for folder, extensions in mapping.items():
      if extension in extensions:
        destination = outputDir + '/' + folder
        if not path.exists(destination):
          mkdir(destination)

        try:
          status = shutil.move(fullFilePath, destination)
          if status:
            jenny.say(f'Moved {fullFilePath} to {destination}')
        except Exception as e:
          print(f'____ FAILED TO MOVE {fullFilePath} to {destination}')
          print(e)

  return jenny.say('Finished sorting..')

def playRandomMusic():
  inputDefault = 'C:/Users/' + getlogin() + '/Music/favs'
  inputDir = jenny.ask(f'Input directory or press enter to use default {inputDefault}') or inputDefault
  system("vlc.exe.lnk " + inputDir + " --qt-start-minimized")