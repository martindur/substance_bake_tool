import tkinter as tk

class BakeGUI:

    def __init__(self, bg_app, bg_btn, bg_entry, fg_text):
        self.bg_app = bg_app
        self.bg_btn = bg_btn
        self.bg_entry = bg_entry
        self.fg_text = fg_text
        self.tk = tk.Tk()
        self.variables = {}

    def make_label(self, frame, text):
            return tk.Label(frame, text=text, bg=self.bg_app, foreground=self.fg_text)

    def make_entry(self, frame, reference):
        entry = tk.Entry(frame, bg=self.bg_entry, foreground=self.fg_text)
        self.variables['reference'] = entry
        return entry

    def make_button(self, frame, cmd, text):
        return tk.Button(frame, command=cmd, text=text, bg=self.bg_btn, foreground=self.fg_text)

    def make_checkbutton(self, frame, text):
        print('.')

    def draw_paths_frame(self, frame):
        self.make_label(frame, 'Baker:').grid(row=0, column=0)
        self.make_label(frame, 'Meshes:').grid(row=1, column=0)
        self.make_label(frame, 'Output:').grid(row=2, column=0)
        self.make_entry(frame, 'sbsbaker').grid(row=0, column=1)
        self.make_entry(frame, 'meshes').grid(row=1, column=1)
        self.make_entry(frame, 'output').grid(row=2, column=1)

    def draw_types_frame(self, frame, types):
        bake_property_selection = tk.Listbox(frame, bg=self.bg_app, foreground=self.fg_text, highlightcolor=self.bg_entry, height=len(types))
        for idx, t in enumerate(types):
            bake_property_selection.insert(idx+1, t)
        bake_property_selection.grid(row=0)
        bake_property_selection.bind('<<ListBoxSelect>>', get_bake_property_selection)

    def draw(self, title):
        main = self.tk
        main.title(title)
        main.iconbitmap(bitmap='./resources/sbs_icon.ico')

        padding = "4"
        bake_types = 'Ambient Occlusion', 'Curvature', 'Position', 'World Space Dir', 'World Space Normals', 'Convert UV to SVG'

        main.configure(background=self.bg_app, padx=padding, pady=padding)


        paths_frame = tk.LabelFrame(main, height=150, width=300, bg=self.bg_app, text="Paths", foreground=self.fg_text, padx=padding, pady=padding)
        types_frame = tk.LabelFrame(main, height=300, width=300, bg=self.bg_app, text="Types", foreground=self.fg_text, padx=padding, pady=padding)
        actions_frame = tk.LabelFrame(main, height=100, width=300, bg=self.bg_app, text="Actions", foreground=self.fg_text, padx=padding, pady=padding)
        sep_frame = tk.Frame(main, height=550, width=10, bg=self.bg_app).grid(row=0, column=1, rowspan=3)
        properties_frame = tk.LabelFrame(main, height=550, width=350, bg=self.bg_app, text="Properties", foreground=self.fg_text, padx=padding, pady=padding)

        paths_frame.grid(row=0, column=0)
        types_frame.grid(row=1, column=0)
        actions_frame.grid(row=2, column=0)
        properties_frame.grid(row=0, column=2, rowspan=3)

        self.draw_paths_frame(paths_frame)
        self.draw_types_frame(types_frame, bake_types)

        main.mainloop()

def get_bake_property_selection(e):
    w = e.widget
    idx = int(w.curselection()[0])
    val = w.get(idx)
    print(val)

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