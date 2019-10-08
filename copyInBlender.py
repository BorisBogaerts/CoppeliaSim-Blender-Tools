import csv
import os
import bpy
import math

file_Folder = 'C:\\Program Files\\V-REP3\\V-REP_PRO_EDU\\cadFiles\\'
fullpath = os.path.join(file_Folder, 'content.txt')
fps = bpy.context.scene.render.fps

counter = 0
animName = {}
obj_object = {}
    
with open(fullpath, 'r', newline='') as csvfile:
    ofile = csv.reader(csvfile, delimiter=',')
    # This loads all the meshes
    for line in ofile:
         f, *pts = line
         
         # Load the mesh
         imported_object = bpy.ops.import_scene.obj(filepath=f+'.obj')
         obj_object[counter] = bpy.context.selected_objects[0] ####<--Fix

         animName[counter] = f
         counter = counter + 1

# Now load animation for each mesh
for i in range(len(obj_object)):
    fullpath = os.path.join(fullpath, animName[i]+'.txt')
    with open(fullpath, 'r', newline='') as csvfile:
        ofile = csv.reader(csvfile, delimiter=',')
        next(ofile) # <-- skip the header
        for line in ofile:
            f, *pts = line
            # these things are still strings (that's how they get stored in the file)
            # here we recast them to integer and floats
            fpts = [float(p) for p in line]
            
            fpts[0] = fpts[0]*fps
            bpy.context.scene.frame_set(math.floor(fpts[0]), subframe=fpts[0]%1)
            obj_object[i].location = fpts[1:4]
            obj_object[i].rotation_mode = 'QUATERNION'
            obj_object[i].rotation_quaternion = fpts[4:8]
            obj_object[i].keyframe_insert(data_path="location", index=-1)
            obj_object[i].keyframe_insert(data_path="rotation_quaternion", index=-1)
