
from bs4 import BeautifulSoup
import csv
import requests

CSV = 'cards.csv'
HOST = 'https://minfin.gov.ru/'
URL = 'https://minfin.gov.ru/ru/'
HEADERS = {

}

def get_html(url, params = ''):
	r = requests.get(url, headers = HEADERS, params = params)
	return r

def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('li', class_="new-list-item")
	news =  []

	for item in items:
		news.append(
			{
				'title':item.find('p', class_="new-list-text").get_text(strip = True),
				'link':HOST + item.find('a').get('href')
			}
		)
	return news

def save_doc(items, path):
	with open(path, 'w') as file:
		writer = csv.writer(file, delimiter = ';')
		writer.writerow(['project name', 'link'])
		for item in items:
			writer.writerow([item['title'], item['link']])



def parser():
	PAGENATION = input('page')
	PAGENATION = int(PAGENATION.strip())

	html = get_html(URL)
	if html.status_code == 200:
		pass
	else:
		print('Error')


html = get_html(URL)
save_doc(get_content(html), CSV)

