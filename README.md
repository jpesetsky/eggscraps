# eggscraps
A scraper for Newegg, written in Python.

This is a test module written for learning purposes. The foundation for this project comes from http://datasciencedojo.com/web-scraping-30-minutes. 


# Features
The script pulls html data for graphics cards and lists their brand, product name, price, and shipping cost. It has the ability to scrape multiple pages by inserting the each URL into the list at the beginning of the script. At the end of the script, the data is written to CSV.


# Steps
* Insert your URLs into the list at the start of the file
* Enter your preferred filename into the filename variable
* Run the script; your output file will appear in the directory where your eggscraps.py file is located


# Note
This script may be updated in the future to accomodate for more flexibility in which products are being scraped, a higher number of fields listed in the output, and general refactoring. It also may need updates contingent on changes to newegg's HTML tags.
