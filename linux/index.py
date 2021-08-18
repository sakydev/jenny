import modules.jenny as jenny
import sys


greetings = True
singleRan = False

while True:
	if len(sys.argv) > 1 and not singleRan:
		command = ' '.join(sys.argv)
		singleRan = True
	else:
		command = jenny.ask(greetings=greetings)

	jenny.process(command)
	greetings = False