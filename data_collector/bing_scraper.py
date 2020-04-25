import os

from .search_term_generator import SearchTermGenerator


class BingScraper(object):
	def __init__(self, search_terms = [], limit = 100, output = "../data/house_scraper/bing"):
		self.search_terms = search_terms
		self.limit = limit

	def scrape(self):
		print('starting scraping')
		index = 0;

		for search_term in self.search_terms:
			print(f"{index + 1}/{len(self.search_terms)}: Scraping {search_term}")
			command = f"python {os.getcwd()}/bbid.py -s \"{search_term}\" --limit {self.limit} -o {self.create_output_dir(search_term)} "
			print(os.system('pwd'))

	def create_output_dir(self, search_term):
		return search_term.replace("' '", '_').replace(" ", '')


generator = SearchTermGenerator()
search_terms = generator.generate()

scraper = BingScraper(search_terms=search_terms, limit=2)
scraper.scrape()
