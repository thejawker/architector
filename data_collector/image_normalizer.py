import os

from tqdm import tqdm
from PIL import Image

styles = {
	"contemporary": ["contemporary", "modern"],
	"tuscan": ["tuscan"],
	"victorian": ["victorian"],
	"traditional": ["traditional"],
	"mediterranean": ["mediterranean", "spanish"],
	"cape_cod": ["capecod"],
	"craftsman": ["craftsman"],
	"french": ["french"],
}


class ImageNormalizer(object):
	def __init__(self, from_dir=None, to_dir=None):
		self.dir_name = os.path.join(os.getcwd(), from_dir)
		self.to_dir = to_dir
		self.dirs = os.listdir(self.dir_name)
		self.total_counter = 0
		self.image_size = 600, 600

	def clean_images(self):
		for (style, sub_styles) in styles.items():
			for dirname in sub_styles:
				print(dirname)
				print('\n\n')
				self.organize_image(dirname, style)

	def organize_image(self, from_dir_starting_with, to_dir):
		dest_dir = os.path.join(self.to_dir, to_dir)
		related_dirs = []
		images = []

		for dir_name in self.dirs:
			if dir_name.startswith(from_dir_starting_with):
			# if dir_name == f"{from_dir_starting_with}house":
				related_dirs.append(dir_name)

		for dir_name in related_dirs:
			dir_images = os.listdir(os.path.join(self.dir_name, dir_name))
			dir_images = [os.path.join(self.dir_name, dir_name, img) for img in dir_images]
			images.extend(dir_images)

		try:
			os.makedirs(dest_dir)
		except OSError:
			print('something went wrong')
			pass

		self.convert_images(images, dest_dir)

	def convert_images(self, images, dest_dir):
		index = 0
		for image in tqdm(images):
			index = index + 1
			self.total_counter = self.total_counter + 1
			name = f"{image.split('/')[-2]}_{self.total_counter}_{index}.jpg"

			try:
				im = Image.open(image)
				im.thumbnail(self.image_size)
				im.save(os.path.join(dest_dir, name), 'JPEG')
			except Exception:
				pass
				# print('could not save')


normalizer = ImageNormalizer('../data/house_scraper/bing', to_dir='../data/house_scraper/bing_normalized')
normalizer.clean_images()
