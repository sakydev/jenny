from os import system, getlogin
from . import jenny

def get_base():
	return 'ffmpeg.exe'

def get_input_file():
	return jenny.ask('Input file')

def get_output_dir():
	output_default = 'C:/Users/' + getlogin() + '/Downloads/test.mp4'
	output_directory = jenny.ask(f'Output directory with filename and extension or press enter to use default {output_default}') or output_default

	return output_directory

def convert():
	command = f'{get_base()} -i {get_input_file()} {get_output_dir()}'
	return system(command)

def rotate():
	degree_default = '360'
	degrees = jenny.ask(f'Rotate degrees or press enter to use default {degree_default}') or degree_default

	command = f'{get_base()} -i {get_input_file()} -c copy -metadata:s:v:0 rotate={degrees} {get_output_dir()}'
	return system(command)

def mute():
	command = f'{get_base()} -i {get_input_file()} -c copy -an {get_output_dir()}'
	return system(command)

def add_subtitles():
	subs_file = jenny.ask('Subtitles file')

	if not os.path.exists(subs_file):
		return jenny.say('Subtitles file does not exist')

	command = f'{get_base()} -i {get_input_file()} -vf subtitles={subs_file} {get_output_dir()}'
	return system(command)

def add_watermark():
	default_position = 'top_left'

	position = jenny.ask('Positon: top_left, top_right, bottom_right, bottom_left, center') or default_position
	if position == 'top_left':
		position = 'overlay=10:10'
	elif position == 'top_right':
		position = 'overlay=main_w-overlay_w-10:10'
	elif position == 'bottom_left':
		position = 'overlay=10:main_h-overlay_h-10'
	elif position == 'bottom_right':
		position = 'overlay=main_w-overlay_w-10:main_h-overlay_h-10'
	elif position == 'center':
		position = 'overlay=x=(main_w-overlay_w)/2:y=(main_h-overlay_h)/2'
	else:
		return jenny.say('Invalid watermark position')

	command = f'{get_base()} -i {get_input_file()} -i {watermark_file} -filter_complex "{position}" {get_output_dir()}'
	return system(command)

def extract_audio():
	command = f'{get_base()} -i {get_input_file()} -vn -acodec copy {get_output_dir()}'
	return system(command)

def extract_video_waveform():
	default_size = '640x120'

	size = jenny.ask('Output image size') or default_size
	command = f'{get_base()} -i {get_input_file()} -filter_complex "compand,showwavespic=s={size}" -frames:v 1 {get_output_dir()}'
	return system(command)

def flip():
	default_flip = 'vflip'
	flip_direction = jenny.ask('Flip direction') or default_flip

	command = f'{get_base()} -i {get_input_file()} -vf "{flip_direction}" {get_output_dir()}'
	return system(command)

def thumbnails():
	default_position = '00:00:03'
	thumbnail_position = jenny.ask('Thumbnail position in 00:00:00 format') or default_position

	command = f'{get_base()} -i {get_input_file()} -ss {thumbnail_position} -vframes 12 {get_output_dir()}'
	return system(command)

def speed():
	default_speed = '0.5'
	speed = jenny.ask('Video speed e.g 0.5') or default_speed
	command = f'{get_base()} -i {get_input_file()} -filter:v "setpts={speed}*PTS" {get_output_dir()}'
	return system(command)

def volume():
	default_volume = '0.5'
	volume = jenny.ask('Video volume') or default_volume
	command = f'{get_base()} -i {get_input_file()} -filter:a "volume={volume}" {get_output_dir()}'
	return system(command)

def greyscale():
	command = f'{get_base()} -i {get_input_file()} -vf "hue=s=0" {get_output_dir()}'
	return system(command)

def reverse():
	command = f'{get_base()} -i {get_input_file()} -vf "reverse" -af "areverse" {get_output_dir()}'
	return system(command)

def stack():
	left_video = jenny.ask('Left video')
	right_video = jenny.ask('Right video')

	command = f'{get_base()} -i {left_video} -i {right_video} -filter_complex hstack {get_output_dir()}'
	return system(command)

def split():
	start = jenny.ask('Split start time') or 0
	end = jenny.ask('Split end time') or 10

	command = f'{get_base()} -i {get_input_file()} -ss {start} -t {end} -c copy {get_output_dir()}'

	return system(command)