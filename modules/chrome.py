import sqlite3, webbrowser
from os import getlogin
from . import jenny

def remove_nsfw():
	print('asd')
	con = sqlite3.connect('C:\\Users\\' + getlogin() + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')

	cursor = con.cursor()
	cursor.execute("select id, url, title from urls")
	urls = cursor.fetchall()

	total = len(urls)
	done = 0
	deleted = 0
	pending_ids = []
	keywords = jenny.config('bad_words')

	for url in urls:
		jenny.output(f'Processing {done} / {total} urls [deleted: {deleted}]')

		uid = url[0]
		link = url[1].lower()
		title = url[2].lower()

		for keyword in keywords:
			if keyword in link or keyword in title:
				jenny.output(f'{keyword} matched, deleting..')
				pending_ids.append((uid,))
				deleted += 1

		done += 1

	query = 'DELETE FROM urls WHERE id=?'
	cursor.executemany(query, pending_ids)
	con.commit()

def open_url(url):
	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
	webbrowser.get('chrome').open(url)

def search_on_youtube(query=False):
	query = query or jenny.ask('What would you like to play')
	open_url('https://youtube.com/search?q=' + query.replace(' ', ''))
	jenny.say(f'YouTube with results for "{query}" has been opened in your browser')

def search_images(query=False):
	query = query or jenny.ask('What images are you looking for')
	print('search images for ' + query)
	url = f'https://www.google.com/search?q={query}&tbm=isch'
	open_url(url)

def search_torrent(query=False):
	query = query or jenny.ask('What are you looking for')
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
		open_url(url)

	jenny.say('You torrent query has been opened in Chrome')

def motivate(query=False):
	open_url('https://youtube.com/search?q=motivation')