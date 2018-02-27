import tkinter as tk

class BakeGUI:

    def __init__(self, bg_app, bg_btn, bg_entry, fg_text, font):
        self.bg_app = bg_app
        self.bg_btn = bg_btn
        self.bg_entry = bg_entry
        self.fg_text = fg_text
        self.tk = tk.Tk()
        self.variables = {}
        self.font = font
        self.prop_choice = None

    def make_label(self, frame, text):
            return tk.Label(frame, text=text, bg=self.bg_app, foreground=self.fg_text, font=self.font)

    def make_entry(self, frame, reference):
        entry = tk.Entry(frame, bg=self.bg_entry, foreground=self.fg_text, font=self.font)
        self.variables['reference'] = entry
        return entry

    def make_button(self, frame, cmd, text, width=5, height=1):
        return tk.Button(frame, command=cmd, text=text, font=self.font, bg=self.bg_btn, foreground=self.fg_text, width=width, height=height, activebackground=self.bg_app, activeforeground=self.fg_text)

    def make_checkbutton(self, frame, text):
        return tk.Checkbutton(frame, text=text, bg=self.bg_app, fg=self.fg_text, selectcolor=self.bg_app, activebackground=self.bg_app, activeforeground=self.fg_text, bd=0)

    def make_radiobutton(self, frame, text, position, choice, types):
        return tk.Radiobutton(frame, command=self.draw_properties_frame(self.properties_frame, types), text=text, value=position, variable=choice, indicatoron=0, bg=self.bg_app, fg=self.fg_text, font=self.font, width=25, selectcolor=self.bg_entry, activebackground=self.bg_app, activeforeground=self.fg_text, offrelief=tk.FLAT, relief=tk.SOLID)

    def make_label_frame(self, frame, height, width, text, padding):
        return tk.LabelFrame(frame, height=height, width=width, bg=self.bg_app, text=text, fg=self.fg_text, font=self.font, padx=padding, pady=padding)

    def draw_paths_frame(self, frame):
        self.make_label(frame, 'Baker:').grid(row=0, column=0)
        self.make_label(frame, 'Meshes:').grid(row=1, column=0)
        self.make_label(frame, 'Output:').grid(row=2, column=0)
        self.make_entry(frame, 'sbsbaker').grid(row=0, column=1)
        self.make_entry(frame, 'meshes').grid(row=1, column=1)
        self.make_entry(frame, 'output').grid(row=2, column=1)

    def draw_types_frame(self, frame, types):
        for idx, t in enumerate(types):
            btn = self.make_radiobutton(frame, text=t, position=idx, choice=self.prop_choice, types=types)
            ch_btn = self.make_checkbutton(frame, '')
            btn.grid(row=idx, column=0)
            ch_btn.grid(row=idx, column=1)

    def draw_actions_frame(self, frame):
        self.make_button(frame, cmd=bake, text='BAKE', width=15, height=3).grid(row=0, column=0, padx=10, sticky='W')
        self.make_button(frame, cmd=save, text='Save').grid(row=0, column=1)
        self.make_button(frame, cmd=load, text='Load').grid(row=0, column=2)

    def draw_properties_frame(self, frame, types):
        self.make_label(frame, types[self.prop_choice.get()]).grid(row=0, column=0)
        print(self.prop_choice.get())

    def draw(self, title):
        main = self.tk
        main.title(title)
        main.iconbitmap(bitmap='./resources/sbs_icon.ico')

        padding = "4"
        bake_types = 'Ambient Occlusion', 'Normal', 'Bent Normals', 'Curvature', 'Position', 'Thickness', 'Height', 'World Space Dir', 'World Space Normals', 'Transfer Texture', 'Convert UV to SVG'

        main.configure(background=self.bg_app, padx=padding, pady=padding)

        ##Frame creation##
        ##              ##
        paths_frame = self.make_label_frame(main, 300, 300, 'Paths', padding)
        types_frame = self.make_label_frame(main, 300, 300, 'Types', padding)
        actions_frame = self.make_label_frame(main, 100, 300, 'Actions', padding)
        sep_frame = tk.Frame(main, height=550, width=10, bg=self.bg_app).grid(row=0, column=1, rowspan=3)
        self.properties_frame = self.make_label_frame(main, 550, 350, 'Properties', padding)

        ##Frame Positioning##
        ##                 ##
        paths_frame.grid(row=0, column=0)
        types_frame.grid(row=1, column=0)
        actions_frame.grid(row=2, column=0)
        self.properties_frame.grid(row=0, column=2, rowspan=3)

        self.prop_choice = tk.IntVar()
        self.draw_paths_frame(paths_frame)
        self.draw_types_frame(types_frame, bake_types)
        self.draw_actions_frame(actions_frame)

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

action_buttons = {
    'Bake' : bake,
    'Save' : save,
    'Load' : load
}

app = BakeGUI(bg_app="#323232", bg_btn="#323232", bg_entry="#252525", fg_text="#C8C8C8", font='Helvetica')

app.draw('Substance Batch Baker')

#root.mainloop()