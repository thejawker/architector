import os
import sys
import time

sys.path.append('../')
from data_collector.search_term_generator import SearchTermGenerator
# print(sys.path)


class BingScraper(object):
	def __init__(self, search_terms = [], limit = 500):
		self.search_terms = search_terms
		self.limit = limit
		print(os.getcwd())
		self.output = f"{os.getcwd()}/../data/house_scraper/bing"

	def scrape(self):
		print('starting scraping...\n')
		print(f"{self.limit} images per search term\n")
		print(f"{len(self.search_terms)} search terms\n")
		print(f"Roughly resulting in {len(self.search_terms) * self.limit} images")
		index = 0

		print('Starting in 2 seconds')
		time.sleep(2)

		for search_term in self.search_terms:
			print("\n\n= = = = = = = = = = = = = =")
			print(f"{index + 1}/{len(self.search_terms)}: Scraping {search_term}")
			print("\n")
			index = index + 1
			command = f"python {os.getcwd()}/bbid.py -s \"{search_term}\" --limit {self.limit} -o {self.create_output_dir(search_term)} "
			print(os.system(command))

	def create_output_dir(self, search_term):
		dirname = search_term.replace("' '", '_').replace(" ", '')
		return os.path.join(self.output, dirname)


generator = SearchTermGenerator()
search_terms = generator.generate()

scraper = BingScraper(search_terms=search_terms)
scraper.scrape()
