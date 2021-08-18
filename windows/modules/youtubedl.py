from os import system, getlogin
from . import jenny

def get_base_path():
	return 'youtube-dl.exe'

def get_url():
	return jenny.ask('URL of video to download')

def get_output_dir():
	download_default = 'C:/Users/' + getlogin() + '/Downloads/'
	download_directory = jenny.ask(f'Output directory or press enter to use default {download_default}') or download_default

	return download_directory

def download():
	base = get_base_path()
	url = get_url()
	output_dir = get_output_dir()

	command = f'{base} -o "{output_dir}/%(title)s-%(id)s.%(ext)s" "{url}"'
	system(command)

def download_audio_only():
	base = get_base_path()
	url = get_url()
	output_dir = get_output_dir()

	command = f'{base} -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 -o "{output_dir}/%(title)s-%(id)s.%(ext)s" "{url}"'
	system(command)

def download_channel():
	base = get_base_path()
	url = get_url()
	output_dir = get_output_dir()

	command = f'{base} -f best -ciw -o "{output_dir}/%(title)s-%(id)s.%(ext)s" -v "{url}"'
	system(command)


