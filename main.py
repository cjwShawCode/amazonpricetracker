import requests
from bs4 import BeautifulSoup
from datetime import date

import gui

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
url =  "https://www.amazon.co.uk/Samsung-Galaxy-Mobile-Phone-Smartphone/dp/B08FT71HH5/ref=sr_1_3?dchild=1&keywords=s20&qid=1629806406&sr=8-3"

def get_title_price(url):
	page = requests.get(url, headers=headers)
	bs = BeautifulSoup(page.content, 'html.parser')
	title = bs.find(id='productTitle').get_text().strip()
	price = bs.find(id='priceblock_ourprice').get_text()
	# format price
	price = price[1:]
	price = float(price.replace(",",""))

	return title, price

title, price = get_title_price(url)
dateprice = f'{date.today()},{price},\n'

with open(f'{title}.csv', 'r+') as f:
	content = f.readlines()
	if str(content[-1].split(",")[0]) != str(date.today()):
		f.write(dateprice)
	else:
		print("Already added today")
	
gui.show(title)