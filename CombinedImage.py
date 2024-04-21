from PIL import Image


class CombinedImage:
	"""
	A class to represent 2 combined images

	...

	Attributes
	----------
	combined : Image
		The result of the combined images
	_image1 : Image
		The 1st image
	_image2 : Image
		The 2nd image
	_reverse : bool
		The current order of the images

	Methods
	-------
	reverse_order()
		Reverses the order of the 2 images

	combine_images()
		Combines the 2 images in the current order

	save_combine(outfile='result', file_type='JPEG')
		Saves the combined image to a certain file with the name and file type
	"""

	def __init__(self, image1_path: str, image2_path: str):
		"""
		Create a new combined image
		:param image1_path: A string with the filename of image 1
		:param image2_path: A string with the filename of image 2
		"""
		self.combined = Image.new('RGB', (128, 128))
		self._image1 = Image.open(image1_path)
		self._image2 = Image.open(image2_path)
		self._reverse = False

	@property
	def reverse(self) -> bool:
		"""
		Get the current order of the images.
		:return: False if the order is 12, True otherwise
		"""
		return self._reverse

	def reverse_order(self) -> None:
		"""
		Reverse the order of the images
		:return: None
		"""
		self._reverse = not self._reverse
		self.combine_images()

	@property
	def image1(self) -> Image:
		"""
		Get the image 1
		:return: Image 1
		"""
		return self._image1

	@image1.setter
	def image1(self, img: Image) -> None:
		"""
		Change the image 1
		:param img: New image 1
		:return: None
		"""
		self._image1 = img
		self.combine_images()

	@property
	def image2(self) -> Image:
		"""
		Get the image 2
		:return: Image 2
		"""
		return self._image2

	@image2.setter
	def image2(self, img: Image) -> None:
		"""
		Change the image 2
		:param img: New image 2
		:return: None
		"""
		self._image2 = img
		self.combine_images()

	def combine_images(self) -> None:
		"""
		Combines images 1 and 2 according to the current order
		:return: None
		"""
		width2, height2 = self.image2.size
		width1, height1 = self.image1.size

		# Define the size of the combined image
		combined_width = width1 + width2
		combined_height = max(height1, height2)

		# Create a new image and paste the 2 images side by side
		self.combined = Image.new('RGB', (combined_width, combined_height))
		self.combined.paste(self.image1, (0 + width2 * self.reverse, 0))
		self.combined.paste(self.image2, (0 + width1 * (not self.reverse), 0))

	def save_combine(self, outfile='result.jpg', file_type='JPEG') -> None:
		"""
		Save the combined image to a file
		:param outfile: A string for the name of the file to be saved
		:param file_type: A string with the file type to save the image
		:return: None
		"""
		if not outfile:
			outfile = 'result.jpg'
		if not file_type:
			file_type = 'JPEG'
		self.combined.save(outfile, file_type)
