import os
import json
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg
import bake_utilities as bu
#from ttkthemes import themed_tk as tk

#Outputs are based on a 2^value. E.g. 2^7 is 128.
outputs = {
    '128':'7',
    '256':'8',
    '512':'9',
    '1024':'10',
    '2048':'11',
    '4096':'12'
}

def initialization():
    for file_name in os.listdir(str(os.curdir)):
        if file_name == 'prefs.json':
            load_prefs()
            return
    init_prefs()

def init_prefs():
    prefs = {
        'sbsbaker':'',
        'mesh-input':'',
        'texture-output':''
        #'mesh-output':''
    }
    json.dump(prefs, open("prefs.json", 'w'))

def load_prefs():
    prefs = json.load(open('prefs.json'))
    for key, entry in dir_entries.items():
        entry.insert(0, prefs[key])

def save_prefs():
    try:
        prefs = json.load(open('prefs.json'))
    except:
        init_prefs()
    for key in prefs:
        prefs[key] = dir_entries[key].get()
    json.dump(prefs, open("prefs.json", 'w'))

def bake_meshes():
    sbsbaker_path = dir_entries['sbsbaker'].get()
    output_path = dir_entries['texture-output'].get()
    mesh_input_path = dir_entries['mesh-input'].get()
    #mesh_output_path = dir_entries['mesh-output'].get()

    output_resolution = outputs[resolution.get()]

    bake_selection = []
    for map_type, value in map_entries.items():
        if value.get() == 1:
            bake_selection.append(map_type)

    if mesh_input_path == '':
        msg.showwarning('Missing Info', "No Mesh input path defined.")
        return None
    elif output_path == '':
        msg.showwarning('Missing Info', "No Bake output path defined.")
        return None

    for bake in bake_selection:
        bu.bake_from_meshes(bake, sbsbaker_path, mesh_input_path, output_resolution, output_resolution, output_path)

    #if mesh_output_path is not '':
        #bu.move_baked_meshes(mesh_input_path, mesh_output_path, '.fbx', copy=True)

###GUI###
master = tk.Tk()
master.title('Substance Bake Tool 0.1')
master.iconbitmap(bitmap='./resources/sbs_icon.ico')
#master = tk.ThemedTk()
#ttk.Style().theme_use('classic')

def create_entries(entries):
    for idx, entry in enumerate(entries):
        tk.Label(master, text=entry).grid(row=idx)
        e = tk.Entry(master)
        e.grid(row=idx, column=1)
        dir_entries[entry] = e

def create_bake_options(maps):
    for idx, map in enumerate(maps):
        var = tk.IntVar()
        c = tk.Checkbutton(master, text=map, variable=var, indicatoron=0).grid(row=3, column=idx)
        map_entries[map] = var

#Variables#
entry_fields = 'sbsbaker', 'mesh-input', 'texture-output'#, 'mesh-output'
dir_entries = {}
map_types = 'ambient-occlusion', 'curvature', 'position'
map_entries = {}
resolution_options = ['128', '256', '512', '1024', '2048', '4096']
resolution = tk.StringVar()
resolution.set('512')
resolution_label = tk.Label(master, text='Resolution:').grid(row=1, column=2)
#Content#
create_entries(entry_fields)
create_bake_options(map_types)
bake_btn = tk.Button(master, text="Bake", command=bake_meshes)
save_prefs_btn = tk.Button(master, text="Save prefs", command=save_prefs)
resolution_dropdown = tk.OptionMenu(master, resolution, *resolution_options)
#Draw#
resolution_dropdown.grid(row=1, column=3)
bake_btn.grid(row=0, column=2)
save_prefs_btn.grid(row=0, column=3)

initialization()
master.mainloop()