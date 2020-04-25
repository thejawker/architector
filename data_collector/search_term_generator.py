styles = [
	"cape cod",
	"mediterranean",
	"spanish",
	"tuscan",
	"victorian",
	"craftsman",
	"french",
	"traditional",
	"modern",
	"contemporary",
	"melrose",
]

location_modifiers = [
	"los angeles",
	"la",
	"venice",
	"santa monica",
	"santa barbara",
	"san diego",
	"san fransisco",
]

build_sizes = [
	"duplex",
	"small",
	"tiny",
	"large",
	"mansion",
	"single story",
	"double story",
	"3 story",
]

point_of_view_modifiers = [
	"street",
	"front",
	"back",
	"side"
]


class SearchTermGenerator(object):
	search_terms = []

	# very ugly, but don't care
	def generate(self):
		for style in styles:
			self.search_terms.append(style)

			for location in location_modifiers:
				self.search_terms.append(f"'{style}' '{location}'")

				for build_size in build_sizes:
					self.search_terms.append(f"'{style}' '{location}' '{build_size}'")

					for pov in point_of_view_modifiers:
						self.search_terms.append(f"'{style}' '{location}' '{build_size}' '{pov}'")

		return self.search_terms

