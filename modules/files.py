# iterates over each file in input directory
# and moves to output_directory under folders by file type
from os import system, listdir, path, mkdir, rename, getlogin, startfile
import ctypes, random, shutil
from . import jenny

def sort_directory():
  input_default = 'C:/Users/' + getlogin() + '/Downloads'
  output_default = 'G:/Downloads'

  input_directory = jenny.ask(f'Input directory or press enter to use default {input_default}') or input_default
  output_directory = jenny.ask(f'Output directory (enter to use default {output_default}') or output_default

  if not path.exists(input_directory):
    jenny.say(f'Input directory not found @ {input_directory}')
    return

  if not path.exists(output_directory):
    jenny.say(f'Output directory not found @ {output_directory}')
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

  for file in listdir(input_directory):
    full_file_path = input_directory + '/' + file
    extension = path.splitext(file)[1].replace('.', '')
    for folder, extensions in mapping.items():
      if extension in extensions:
        destination = output_directory + '/' + folder
        if not path.exists(destination):
          mkdir(destination)

        try:
          status = shutil.move(full_file_path, destination)
          if status:
            jenny.say(f'Moved {full_file_path} to {destination}')
        except Exception as e:
          print(f'____ FAILED TO MOVE {full_file_path} to {destination}')
          print(e)

  return jenny.say('Finished sorting..')

def play_random_music():
  input_default = 'C:/Users/' + getlogin() + '/Music/favs'
  input_directory = jenny.ask(f'Input directory or press enter to use default {input_default}') or input_default
  system("vlc.exe.lnk " + input_directory + " --qt-start-minimized")

def set_random_wallpaper():
  default_path = 'C:/Users/' + getlogin() + '/Pictures/Wallpapers'
  path = jenny.ask(f'Input directory or press enter to use default {default_path}') or default_path
  image = default_path + '/' + random.choice(listdir(default_path))

  ctypes.windll.user32.SystemParametersInfoW(20, 0, image , 0)

def start_work_place():
  startfile('powershell')
  startfile('chrome')
  startfile('evernote')
  startfile('filezilla')
  startfile('D:\Clients')

def goto(query=False):
  destination = query or jenny.ask('Where do you want to go')
  mapped_directories = jenny.config('directories')
  if destination in mapped_directories:
    fpath = mapped_directories[destination]
    fullPath = path.abspath(fpath)
    if path.exists(fullPath):
      startfile(fullPath)
      return

  jenny.output('Directory not found')