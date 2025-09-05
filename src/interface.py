import customtkinter as interface
from PIL import Image
from dir import list_dirs, change_wallpaper, get_monitors

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

        self.set_grid()
        self.image_showcase()
        self.grid_layout()
        self.combo_def()

    def image_showcase(self) -> None:
        default_width = 400
        default_height = 240

        self.images = []

        for image in list_dirs():
            self.my_image = interface.CTkImage(
                dark_image=Image.open(image), size=(default_width, default_height))

            self.my_label = interface.CTkLabel(
                self.container, image=self.my_image, text="",
                corner_radius=10)

            self.my_label.bind("<Button-1>", lambda event, path=image:
                               self.path_provider(path))
            self.images.append([self.my_label, image])

    def path_provider(self, path) -> None:
        monitor = self.combobox.get()

        if monitor == "Default!!!":
            change_wallpaper(path)
        else:
            change_wallpaper(path, monitor)

    def set_grid(self):
        self.container = interface.CTkScrollableFrame(self)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.container.grid_columnconfigure((0, 1), weight=1)
        self.container.grid_rowconfigure(0, weight=1)

    def grid_layout(self) -> None:
        current_row = 0
        current_column = 0

        # setting images on layout
        for arr in self.images:
            if current_column > 1:
                current_row += 1
                current_column = 0

            arr[0].grid(row=current_row, column=current_column,
                        padx=20, pady=20)
            current_column += 1

    def combo_def(self) -> None:
        res = list(get_monitors())
        self.combobox = interface.CTkComboBox(self, values=res,)
        self.combobox.grid(row=1, column=0, sticky="nsew")
        self.combobox.set("Default!!!")
