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

def searchImages():
	query = jenny.ask('What are you looking for')
	url = f'https://www.google.com/search?q={query}&tbm=isch'
	openUrl(url)

def searchTorrent():
	query = jenny.ask('What are you looking for')
	sites = [
		'https://proxyrarbg.org/torrents.php?search=[query]',
		'https://thepiratebay10.org/search/[query]/1/99/0',
		'https://yts.mx/browse-movies/[query]/all/all/0/latest/0/all',
		'https://torrentz2eu.org/index.html?q=[query]',
		'https://eztv.re/search/[query]',
		'https://zooqle.com/search?q=[query]',
		'https://www.limetorrents.info/search/all/[query]/',
		'https://www.torlock.com/?qq=1&q=[query]',
		'https://1337x.to/search/[query]/1/'
		]

	for site in sites:
		url = site.replace('[query]', query)
		openUrl(url)

	jenny.say('You torrent query has been opened in Chrome')

def motivate():
	openUrl('https://youtube.com/search?q=motivation')