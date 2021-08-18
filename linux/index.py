import modules.jenny as jenny

greetings = True
while True:
	command = jenny.ask(greetings=greetings)
	jenny.process(command)
	greetings = False