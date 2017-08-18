#! /usr/bin/env python
"""
This module is a test webscraper written for learning purposes. 
Foundation for this project: https://datasciencedojo.com/web-scraping-30-minutes 
v2: Refactored loop attributes; prices now appear in final dataset
v3: Incorporated the ability to scrape multiple pages 
"""
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

# URL to webscrape from. In this example we scrape graphics cards from Newegg
my_urls = ['https://www.newegg.com/Product/ProductList.aspx?Submit=Property&N=100007709%2050001419%2050001315%2050001402%2050001312%2050001669%2050012150%2050001561%2050001314%2050001471%20600566292%20600566291%20600565504%20601201888%20601204369%20601210955%20601203793%204814%20601296707&IsNodeId=1&bop=And&PageSize=96&order=BESTMATCH', \
'https://www.newegg.com/Product/ProductList.aspx?Submit=Property&N=100007709%2050001419%2050001315%2050001402%2050001312%2050001669%2050012150%2050001561%2050001314%2050001471%20600566292%20600566291%20600565504%20601201888%20601204369%20601210955%20601203793%204814%20601296707&IsNodeId=1&bop=And&Page=2&PageSize=96&order=BESTMATCH', \
'https://www.newegg.com/Product/ProductList.aspx?Submit=Property&N=100007709%2050001419%2050001315%2050001402%2050001312%2050001669%2050012150%2050001561%2050001314%2050001471%20600566292%20600566291%20600565504%20601201888%20601204369%20601210955%20601203793%204814%20601296707&IsNodeId=1&page=3&bop=And&PageSize=96&order=BESTMATCH', \
'https://www.newegg.com/Product/ProductList.aspx?Submit=Property&N=100007709%2050001419%2050001315%2050001402%2050001312%2050001669%2050012150%2050001561%2050001314%2050001471%20600566292%20600566291%20600565504%20601201888%20601204369%20601210955%20601203793%204814%20601296707&IsNodeId=1&page=4&bop=And&PageSize=96&order=BESTMATCH']

#name the output file to write to local disk
filename = "grafx_cards.csv"
# header of csv file to be written
headers = "brand, product_name, price, shipping\n"

# opens file and writes headers
f = open(filename, "w") 
f.write(headers)

for url in my_urls:
	uClient = uReq(url)   # open up connection, fetch html page

	# parse html into a soup data structure to traverse html as if it were a json data type
	page_html = uClient.read()

	# html parsing
	page_soup = soup(page_html, "html.parser")
	uClient.close()

	# grabs each product
	containers = page_soup.findAll("div",{"class": "item-container"})
	container = containers[0]

	for container in containers:   # loops over each product & grabs attributes
		try:
			brand = container.div.div.a.img["title"]
		except AttributeError:
			brand = 'N/A'

	    # grabs text within the second "a" tag within list of queries
		title_container = container.findAll("a", {"class": "item-title"})
		product_name = title_container[0].text

		# grabs price info
		price_container = container.findAll("li", {"class": "price-current"})
		meta_container = price_container[0].text.strip()
		price = meta_container[2:9]

		# grabs shipping info by searching all lists within the "price-ship" class
		shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

		# print dataset to console
		print("brand: " + brand + "\n")
		print("product_name: " + product_name + "\n")
		print("price: " + price + "\n")
		print("shipping: " + shipping + "\n")

		# write dataset to file
		eggscraps = (brand.replace(",", "|") + ", " + product_name.replace(",", "|") + ", " + price + ", " + shipping + "\n")
		f.write(eggscraps.encode('utf-8', 'replace'))

f.close()  # close the file