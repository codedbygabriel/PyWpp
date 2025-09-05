import customtkinter as interface
from dir import list_dirs, change_wallpaper
from PIL import Image

interface.set_appearance_mode('dark')


class Interface(interface.CTk):
    def __init__(self):
        super().__init__()
        self.title = "PyWpp"
        self.minsize(800, 600)
        self.maxsize(1280, 768)

        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.container = interface.CTkScrollableFrame(self)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.container.grid_columnconfigure((0, 1), weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        self.image_showcase()
        self.grid_layout()

    def image_showcase(self):
        default_width = 320
        default_height = 240

        self.images = []

        for image in list_dirs():
            self.my_image = interface.CTkImage(
                dark_image=Image.open(image), size=(default_width, default_height))

            self.my_label = interface.CTkLabel(
                self.container, image=self.my_image, text="")

            self.my_label.bind("<Button-1>", lambda event, img=image:
                               change_wallpaper(img))

            self.images.append([self.my_label, image])

    def path_provider(self, event, path):
        change_wallpaper(path)

    def grid_layout(self):
        current_row = 0
        current_column = 0

        for arr in self.images:
            if current_column > 1:
                current_row += 1
                current_column = 0

            arr[0].grid(row=current_row, column=current_column,
                        padx=20, pady=20)
            current_column += 1
