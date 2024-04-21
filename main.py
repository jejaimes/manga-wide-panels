"""
This script takes two images, combines them and saves the result in a file.
"""

from CombinedImage import CombinedImage


def main():
	print('Enter the path to the first (leftmost) image: ')
	path1 = input()
	print('Enter the path to the second (rightmost) image: ')
	path2 = input()
	print('Enter the file type of the output (leave empty for default="JPEG"): ')
	file_type = input()
	print('Enter the output filename (leave empty for default="result"): ')
	out = input()
	combination = CombinedImage(path1, path2)
	combination.combine_images()
	combination.save_combine(out, file_type)
	print('Saved the image successfully!')


if __name__ == "__main__":
	main()
