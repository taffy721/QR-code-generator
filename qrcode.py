import pyqrcode
import png
import tkinter as tk

def generate_qr_code(input_url, file_name):
    url = pyqrcode.create(input_url)
    url.png(file_name, scale=6, module_color=[0, 0, 128], background=[0xFF, 0xFF, 0xCC])
    url.show()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Enter URL:")
        label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()

        next_button = tk.Button(self, text="Next", command=self.generate_qr)
        next_button.pack()

    def generate_qr(self):
        input_url = self.entry.get()
        self.controller.show_frame(PageTwo, input_url)

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Enter file name (e.g., qrcode.png):")
        label.pack()

        self.file_entry = tk.Entry(self)
        self.file_entry.pack()

        button = tk.Button(self, text="Generate", command=self.generate_qr)
        button.pack()

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(PageOne))
        back_button.pack()

    def generate_qr(self):
        input_url = self.controller.page_data[PageTwo][0]
        file_name = self.file_entry.get()
        if ".png" not in file_name:
            label = tk.Label(self, text="Please make sure the file name has a '.png' in it, for example qrcode.png", fg="red")
            label.pack()
        generate_qr_code(input_url, file_name)


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        container = tk.Frame(self)
        container.pack()

        self.frames = {}
        self.page_data = {}
        self.create_frames(container)

    def create_frames(self, container):
        for FrameClass in (PageTwo, PageOne):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, frame_class, *args):
        frame = self.frames[frame_class]
        self.page_data[frame_class] = args
        frame.tkraise()

app = Application()
app.mainloop()
