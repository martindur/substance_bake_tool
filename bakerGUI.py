import bake_utilities as bu
import os
import tkinter as tk
from tkinter import ttk
#from ttkthemes import themed_tk as tk
import tkinter.messagebox as msg

bakes = [
    'ambient-occlusion',
    'curvature',
]

def bake_meshes():
    output_path = dir_entries['Texture Output'].get()
    mesh_input_path = dir_entries['Mesh Input'].get()
    mesh_output_path = dir_entries['Mesh Output(Optional)'].get()

    if mesh_input_path == '':
        msg.showwarning('Missing Info', "No Mesh input path defined.")
        return None
    elif output_path == '':
        msg.showwarning('Missing Info', "No Bake output path defined.")
        return None

    for bake in bakes:
        bu.bake_from_meshes(bake, mesh_input_path, '10', '10', output_path)

    if mesh_output_path is not '':
        bu.move_baked_meshes(mesh_input_path, mesh_output_path, '.fbx', copy=True)

###GUI###
master = tk.Tk()
#master = tk.ThemedTk()
#ttk.Style().theme_use('classic')

def create_entries(entries):
    for idx, entry in enumerate(entries):
        ttk.Label(master, text=entry).grid(row=idx)
        e = ttk.Entry(master)
        e.grid(row=idx, column=1)
        dir_entries[entry] = e

#Variables#
entry_fields = 'Mesh Input', 'Texture Output', 'Mesh Output(Optional)'
dir_entries = {}
#Content#
bake_button = ttk.Button(master, text="Bake maps", command=bake_meshes)
#Draw#
resolution_slider = tk.Scale(master, from_=16, to=4096, tickinterval=8)
resolution_slider.grid(row=3)
create_entries(entry_fields)
bake_button.grid(row=0, column=2)
master.mainloop()