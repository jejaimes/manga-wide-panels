import tkinter as tk

from PIL import Image, ImageTk


# TODO: Review this code
class ImageView(tk.Frame):
	def __init__(self, controller):
		self.root = tk.Tk()
		super().__init__(self.root)
		self.controller = controller
		self.create_widgets()
		self.pack(fill=tk.BOTH, expand=True)

	def create_widgets(self):
		self.canvas = tk.Canvas(self, bg="white")
		self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

		scrollbar_y = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
		scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

		scrollbar_x = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.canvas.xview)
		scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

		self.canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
		self.canvas.bind('<Configure>', self.on_canvas_configure)

		self.image_container = self.canvas.create_rectangle(0, 0, 0, 0, width=0, fill="white")

		folder_path_frame = tk.Frame(self)
		folder_path_frame.pack(pady=10)

		folder_path_label = tk.Label(folder_path_frame, text="Folder Path:")
		folder_path_label.grid(row=0, column=0, padx=5)

		self.folder_path_entry = tk.Entry(folder_path_frame, width=30)
		self.folder_path_entry.grid(row=0, column=1, padx=5)

		browse_button = tk.Button(folder_path_frame, text="Browse", command=self.browse_folder)
		browse_button.grid(row=0, column=2, padx=5)

		button_frame = tk.Frame(self)
		button_frame.pack(pady=10)

		combine_button = tk.Button(button_frame, text="Combine Images", command=self.combine_images)
		combine_button.grid(row=0, column=0, padx=5)

		keep_button = tk.Button(button_frame, text="Keep Combined Image", command=self.keep_combined_image)
		keep_button.grid(row=0, column=1, padx=5)

		save_button = tk.Button(button_frame, text="Save Combined Image", command=self.save_combined_image)
		save_button.grid(row=0, column=2, padx=5)

	def on_canvas_configure(self, event):
		self.canvas.itemconfigure(self.image_container, width=event.width)

	def browse_folder(self):
		folder_path = self.controller.browse_folder()
		if folder_path:
			self.folder_path_entry.delete(0, tk.END)
			self.folder_path_entry.insert(0, folder_path)

	def combine_images(self):
		self.controller.combine_images()
		self.display_images()

	def keep_combined_image(self):
		self.controller.keep_combined_image()
		self.display_images()

	def save_combined_image(self):
		self.controller.save_combined_image()

	def display_images(self):
		self.canvas.delete(self.image_container)

		if self.controller.model:
			images = [self.controller.model.combined_image] if self.controller.model.combined_image else []
			images.extend([Image.open(self.controller.model.folder_path + "/" + image_path) for image_path in
			               self.controller.model.image_files])

			max_width = self.canvas.winfo_width()
			x, y = 0, 0
			max_height = 0

			for image in images:
				image = ImageTk.PhotoImage(image)
				image_width = image.width()
				image_height = image.height()

				if x + image_width > max_width:
					x = 0
					y += max_height + 10
					max_height = 0

				self.canvas.create_image(x, y, anchor="nw", image=image)
				self.canvas.image = image
				x += image_width + 10
				max_height = max(max_height, image_height)

			self.canvas.configure(scrollregion=self.canvas.bbox("all"))
