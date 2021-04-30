import jenny, chrome, os, subprocess
def wakeup():
	programs = [
	'C://Program Files (x86)//Google//Chrome//Application//chrome.exe',
	'C://Program Files (x86)//EliteWork LLC//TimeKeeper//EliteWork Desktop Tracker.exe',
	'C://Program Files//FileZilla FTP Client//filezilla.exe',
	'C://Program Files//Sublime Text 3//sublime_text.exe',
	'C://Users//saqic//AppData//Local//Programs//Evernote//Evernote.exe'
	]

	total = len(programs)
	#jenny.say(f'Openning up programs, total of {total}')
	for program in programs:
		command = 'Start-Process -FilePath "' + str(program) + '"'
		print(command)
		os.system(command)

def howmuch(daily):
	weekly = daily * 7
	monthly = daily * 30
	quarterly = monthly * 3
	halfYear = monthly * 6
	yearly = monthly * 12

	print(f'Weekly: {weekly}')
	print(f'Monthly: {monthly}')
	print(f'Quarterly: {quarterly}')
	print(f'Half Year: {halfYear}')
	print(f'1 Year: {yearly}')
	print(f'5 Years: {fiveYears}')
	print(f'10 Years: {tenYears}')