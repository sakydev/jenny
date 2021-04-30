from os import system, getlogin
from . import jenny

def getBasePath():
	return 'ffmpeg.exe'

def getInputFile():
	return jenny.ask('Input file')

def getOutputDir():
	outputDefault = 'C:/Users/' + getlogin() + '/Downloads/test.mp4'
	outputDir = jenny.ask(f'Output directory with filename and extension or press enter to use default {outputDefault}') or outputDefault

	return outputDir

def convert():
	base = getBasePath()
	inputFile = getInputFile()
	outputFile = getOutputDir()

	command = f'{base} -i {inputFile} {outputFile}'
	return system(command)

def mute():
	print('')

def rotate():
	base = getBasePath()
	inputFile = getInputFile()
	outputFile = getOutputDir()
	degreeDefault = '360'
	degrees = jenny.ask(f'Rotate degrees or press enter to use default {degreeDefault}') or degreeDefault

	command = f'{base} -i {inputFile} -c copy -metadata:s:v:0 rotate={degrees} {outputFile}'
	return system(command)

def merge():
	print('')

def split():
	print('')
