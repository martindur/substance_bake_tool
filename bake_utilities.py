import os
import sys
import subprocess
import shutil

def get_sbsbaker(path):
    if 'darwin' or 'linux' in sys.platform:
        return os.path.join(path, os.sep, 'sbsbaker')
    elif 'win' in sys.platform:
        return os.path.join(path, os.sep, 'sbsbaker.exe')

def run_command_popen(cmd):
    sp = subprocess.Popen(cmd, stderr=subprocess.PIPE)
    out, err = sp.communicate()
    if err:
        print("__________________________")
        print("Subprocess standard error:")
        print(err.decode('ascii'))
    sp.wait()

def get_meshes_in_path(meshes_path, extension):
    if os.path.exists(meshes_path):
        meshes = []
        dir_path = os.listdir(str(meshes_path))
        for file_name in dir_path:
            if os.path.splitext(file_name)[1] == extension:
                complete_path = os.path.join(meshes_path, file_name)
                meshes.append(complete_path)
        if meshes:
            return meshes
        else:
            print("No meshes found of type: " + extension)
            return None
    else:
        print("Provided path is not valid: " + meshes_path)

def bake_from_meshes(map_type, sbsbaker, meshes_path, width_resolution, height_resolution, output_path):
    meshes = get_meshes_in_path(meshes_path, '.fbx')
    #sbsbaker = get_sbsbaker(sbsbaker_path)
    #print(sbsbaker)
    if not meshes:
        return None
    for mesh in meshes:
        if map_type == 'curvature':
            bake_cmd = [sbsbaker, map_type,
                    '--inputs', mesh, 
                    '--output-size', width_resolution + ',' + height_resolution,
                    '--output-path', output_path,
                    '--enable-seams', 'false']
        else:    
            bake_cmd = [sbsbaker, map_type,
                    '--inputs', mesh, 
                    '--output-size', width_resolution + ',' + height_resolution,
                    '--output-path', output_path]
        run_command_popen(bake_cmd)

def bake_curvature_from_meshes(map_type, sbsbaker, meshes_path, width_resolution, height_resolution, output_path):
    meshes = get_meshes_in_path(meshes_path, '.fbx')
    if not meshes:
        return None
    for mesh in meshes:
        bake_cmd = [sbsbaker, map_type,
                    '--inputs', mesh, 
                    '--output-size', width_resolution + ',' + height_resolution,
                    '--output-path', output_path]
        run_command_popen(bake_cmd)

def move_baked_meshes(meshes_path, output_path, extension, copy=False):
    dir_path = os.listdir(str(meshes_path))
    for file_name in dir_path:
        if os.path.splitext(file_name)[1] == extension:
            old_path = os.path.join(meshes_path, file_name)
            new_path = os.path.join(output_path, file_name)
            if copy:
                shutil.copyfile(old_path, new_path)
            else:
                os.rename(old_path, new_path)