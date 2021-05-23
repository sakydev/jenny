from os import system, getlogin
from . import jenny

def get_base_path():
	return 'ffmpeg.exe'

def get_input_file():
	return jenny.ask('Input file')

def get_output_directory():
	output_default = 'C:/Users/' + getlogin() + '/Downloads/test.mp4'
	output_directory = jenny.ask(f'Output directory with filename and extension or press enter to use default {output_default}') or output_default

	return output_directory

def convert():
	base = get_base_path()
	input_file = get_input_file()
	output_file = get_output_directory()

	command = f'{base} -i {input_file} {output_file}'
	return system(command)

def rotate():
	base = get_base_path()
	input_file = get_input_file()
	output_file = get_output_directory()
	degree_default = '360'
	degrees = jenny.ask(f'Rotate degrees or press enter to use default {degree_default}') or degree_default

	command = f'{base} -i {input_file} -c copy -metadata:s:v:0 rotate={degrees} {output_file}'
	return system(command)

def mute():
	print('')

def mute():
	print('')

def mute():
	print('')

def mute():
	print('')

def mute():
	print('')
def split():
	print('')

def mute():
	print('')