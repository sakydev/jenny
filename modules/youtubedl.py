from os import system, getlogin
from . import jenny

def getBasePath():
	return 'youtube-dl.exe'

def getUrl():
	return jenny.ask('URL of video to download')

def getOutputDir():
	downloadDefault = 'C:/Users/' + getlogin() + '/Downloads/'
	downloadDir = jenny.ask(f'Output directory or press enter to use default {downloadDefault}') or downloadDefault

def download():
	base = getBasePath()
	url = getUrl()
	outputDir = getOutputDir()

	command = f'{base} -o "{outputDir}/%(title)s-%(id)s.%(ext)s" "{url}"'
	system(command)

def downloadAudioOnly():
	base = getBasePath()
	url = getUrl()
	outputDir = getOutputDir()

	command = f'{base} -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 -o "{outputDir}/%(title)s-%(id)s.%(ext)s" "{url}"'
	system(command)

def downloadChannel():
	base = getBasePath()
	url = getUrl()
	outputDir = getOutputDir()

	command = f'{base} -f best -ciw -o "{outputDir}/%(title)s-%(id)s.%(ext)s" -v "{url}"'
	system(command)


