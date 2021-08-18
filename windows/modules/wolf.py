import json, requests

def search(keyword):
	keyword = keyword.replace(' ', '+')
	data = requests.get('https://api.wolframalpha.com/v2/query?input=' + keyword + '&format=plaintext&output=json&appid=V9X64Y-H3J9Q5XL2A')

	readable = data.json()
	results = readable['queryresult']
	if results['success'] == True:
	  for pod in results['pods']:
	    if pod['title'] == 'Result':
	      try:
	        value = pod['subpods'][0]['plaintext']
	        return value
	      except Exception as e:
	        value = ''
	        raise e
	else:
		print('Something went wrong. Below is full data')
		print(readable)