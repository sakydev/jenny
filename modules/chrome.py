import sqlite3, webbrowser
from os import getlogin
from . import jenny

def removeNsfw():
	con = sqlite3.connect('C:\\Users\\' + getlogin() + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')

	cursor = con.cursor()
	cursor.execute("select id, url, title from urls")
	urls = cursor.fetchall()

	total = len(urls)
	done = 0
	deleted = 0
	pendingIds = []
	keywords = jenny.config('bad_words')

	for url in urls:
		jenny.output(f'Processing {done} / {total} urls [deleted: {deleted}]')

		uid = url[0]
		link = url[1].lower()
		title = url[2].lower()

		for keyword in keywords:
			if keyword in link or keyword in title:
				jenny.output(f'{keyword} matched, deleting..')
				pendingIds.append((uid,))
				deleted += 1

		done += 1

	query = 'DELETE FROM urls WHERE id=?'
	cursor.executemany(query, pendingIds)
	con.commit()

def openUrl(url):
	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
	webbrowser.get('chrome').open(url)

def playOnYoutube():
	query = jenny.ask('What would you like to play')
	openUrl('https://youtube.com/search?q=' + query.replace(' ', ''))
	jenny.say(f'YouTube with results for "{query}" has been opened in your browser')

def motivate():
	openUrl('https://youtube.com/search?q=motivation')