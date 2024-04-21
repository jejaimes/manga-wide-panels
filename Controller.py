from tkinter import filedialog

from Model import ImageModel
from View import ImageView


class ImageController:
    def __init__(self):
        self.model = None
        self.view = ImageView(self)

    def browse_folder(self):
        folder_path = filedialog.askdirectory(title="Select Folder")
        if folder_path:
            self.model = ImageModel(folder_path)
            self.model.load_images()
        return folder_path

    def combine_images(self):
        if self.model:
            self.model.combine_images()
            self.view.display_images()

    def keep_combined_image(self):
        if self.model and self.model.combined_image:
            self.model.combined_image = self.model.combined_image.copy()
            self.view.display_images()

    def save_combined_image(self):
        if self.model and self.model.combined_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg", title="Save Combined Image")
            if file_path:
                self.model.save_combined_image(file_path)


if __name__ == "__main__":
    app = ImageController()
    app.view.root.mainloop()
