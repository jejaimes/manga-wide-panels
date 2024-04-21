import os

from PIL import Image

from CombinedImage import CombinedImage


class ImageModel:
	"""
	A class for the Model that controls the logic of the program

	...

	Attributes
	----------
	folder_path : str
		The path of the folder with the images to combine
	image_files : List
		The list of images paths
	combined_images : List
		The list of combined images

	Methods
	-------
	load_images(folder_path)
		Loads the images paths to image_files

	combine_images()
		Combines the all images in their default order

	save_combined_image(file_path='result', file_type='JPEG')
		Saves the combined images to a certain file numbered with the name and file type specified

	reverse_order_combined(i)
		Reverses the order of images in a certain combined image

	replace_image(i, img, second)
		Replaces one of the images in a certain combined image
	"""

	def __init__(self, folder_path: str):
		"""
		Create a Model
		:param folder_path: The folder where the images to combine are located
		"""
		self.folder_path = folder_path
		self.image_files: list[str] = []
		self.combined_images: list[CombinedImage] = []

	def load_images(self) -> None:
		"""
		Load the images paths to image_files list
		:return: None
		"""
		self.image_files = [f for f in os.listdir(self.folder_path) if f.endswith((".jpg", ".png", ".bmp"))]
		self.image_files.sort()

	def combine_images(self) -> None:
		"""
		Combines all the images in the image_files list and creates a CombinedImage for each one
		:return: None
		"""
		for i in range(0, len(self.image_files), 2):
			image1_path = os.path.join(self.folder_path, self.image_files[i])

			if i + 1 < len(self.image_files):
				image2_path = os.path.join(self.folder_path, self.image_files[i + 1])
				self.combined_images.append(CombinedImage(image1_path, image2_path))

	def save_combined_image(self, file_path='result', file_type='JPEG') -> None:
		"""
		Saves all the combined images to files
		:param file_path: A string with the file path for the combined images
		:param file_type: File type to save the images with
		:return: None
		"""
		if self.combined_images:
			for i in range(len(self.combined_images)):
				self.combined_images[i].save_combine(file_path + str(i), file_type)

	def reverse_order_combined(self, i: int) -> None:
		"""
		Reverse the order of the images on a certain combined image
		:param i: Place of the combined image in the list
		:return: None
		"""
		self.combined_images[i].reverse_order()

	def replace_image(self, i: int, img: Image, second: bool) -> None:
		"""
		Replaces one of the two images in the combined image
		:param i: Place of the combined image in the list
		:param img: New image
		:param second: If changes the second image or the first image
		:return: None
		"""
		if second:
			self.combined_images[i].image2 = img
		else:
			self.combined_images[i].image1 = img
