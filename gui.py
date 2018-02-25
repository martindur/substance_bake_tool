import tkinter as tk


class BakeGUI:

    def __init__(self, bg_app, bg_btn, bg_entry, fg_text):
        self.bg_app = bg_app
        self.bg_btn = bg_btn
        self.bg_entry = bg_entry
        self.fg_text = fg_text
        self.tk = tk.Tk()

    def draw(self, title):
        main = self.tk
        main.title(title)
        main.iconbitmap(bitmap='./resources/sbs_icon.ico')

        padding = "4"

        main.configure(background=self.bg_app, padx=padding, pady=padding)


        paths_frame = tk.LabelFrame(main, height=150, width=300, bg=self.bg_app, text="Paths", foreground=self.fg_text, padx=padding, pady=padding).grid(row=0, column=0)
        types_frame = tk.LabelFrame(main, height=300, width=300, bg=self.bg_app, text="Types", foreground=self.fg_text, padx=padding, pady=padding).grid(row=1, column=0)
        actions_frame = tk.LabelFrame(main, height=100, width=300, bg=self.bg_app, text="Actions", foreground=self.fg_text, padx=padding, pady=padding).grid(row=2, column=0)
        sep_frame = tk.Frame(main, height=550, width=10, bg=self.bg_app).grid(row=0, column=1, rowspan=3)
        properties_frame = tk.LabelFrame(main, height=550, width=350, bg=self.bg_app, text="Properties", foreground=self.fg_text, padx=padding, pady=padding).grid(row=0, column=2, rowspan=3)

        path1 = tk.Label(paths_frame, text="Hello")
        path2 = tk.Label(paths_frame, text="Hi")
        path3 = tk.Label(paths_frame, text="hey")

        path1.grid(row=0)
        path2.grid(row=1)
        path3.grid(row=2)

        main.mainloop()

    def draw_label(self, frame, text):
        print("none")

def create_window():
    return tk.Tk()

def init(window):
    print(window)

def draw(window):
    print(window)

def bake():
    print("none")

def save():
    print("none")

def load():
    print("none")


''' root = tk.Tk()
root.title('Substance Bake Tool')
root.iconbitmap(bitmap='./resources/sbs_icon.ico')
root.configure(background="#323232", padx=padding, pady=padding)

left_main_frame = tk.LabelFrame(root, bg="#323232", height=150, width=250, text="Paths", foreground="#C8C8C8").grid(row=0, column=0, rowspan=3, columnspan=2)
action_frame = tk.LabelFrame(root, bg="#323232", height=150, width=250, text="Actions", foreground="#C8C8C8").grid(row=1, column=0, columnspan=3) '''


def create_entries(entries, frame):
    '''Creates entries with labels in a grid, based on a list of entries and a frame. Returns entry variable with label in a dict'''
    labeled_entries = {}
    for idx, entry in enumerate(entries):
        tk.Label(frame, text=entry, bg="#323232", foreground="#C8C8C8").grid(row=idx)
        e = tk.Entry(frame, bg="#252525", foreground="#C8C8C8")
        e.grid(row=idx, column=1)
        labeled_entries[entry] = e
    return labeled_entries

def create_buttons(buttons, frame):
    labeled_buttons = {}
    for idx, entry in enumerate(buttons):
        tk.Button()

entries = 'sbsbaker', 'mesh-input', 'texture-output'
#labeled_entries = create_entries(entries, left_main_frame)
action_buttons = {
    'Bake' : bake,
    'Save' : save,
    'Load' : load
}

app = BakeGUI(bg_app="#323232", bg_btn="#323232", bg_entry="#252525", fg_text="#C8C8C8")

app.draw('Substance Bake Tool')

#root.mainloop()