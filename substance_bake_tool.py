import os
import json

class Bakemap:

    def __init__(self, meshes, resolution, sbsbaker, output):
        self.meshes = meshes
        self.resolution = resolution
        self.sbsbaker = sbsbaker
        self.output = output

class AmbientOcclusion(Bakemap):

    def __init__(self, meshes, resolution, sbsbaker, output, use_unselected, quality, precision, distance_fade):
        super().__init__(meshes, resolution, sbsbaker, output)
        self.use_unselected = use_unselected
        self.quality = quality
        self.precision = precision
        self.distance_fade = distance_fade

class GlobalSettings:

    def __init__(self, sbsbaker, mesh_input, bake_output):
        self.sbsbaker = sbsbaker
        self.mesh_input = mesh_input
        self.bake_output = bake_output

def load_prefs():
    prefs = json.load(open('prefs.json'))
    globalSettings = GlobalSettings(*prefs)

def init_prefs():
    prefs = {
        'sbsbaker':'',
        'mesh-input':'',
        'bake-output':''
    }
    json.dump(prefs, open("prefs.json", 'w'))

def write_prefs():
    

def main():
    for file_name in os.listdir(str(os.curdir)):
        if file_name == 'prefs.json':
            load_prefs()
            break
    init_prefs()


if __name__ == '__main__':
    main()