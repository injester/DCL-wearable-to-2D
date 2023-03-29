import bpy
import math
import os


# Add cameras if it doesn't exist already

if 'Camera_F' not in bpy.data.objects:
    bpy.ops.object.camera_add()
    bpy.context.object.name = 'Camera_F'
if 'Camera_B' not in bpy.data.objects:
    bpy.ops.object.camera_add()
    bpy.context.object.name = 'Camera_B'
if 'Camera_R' not in bpy.data.objects:
    bpy.ops.object.camera_add()
    bpy.context.object.name = 'Camera_R'
if 'Camera_L' not in bpy.data.objects:
    bpy.ops.object.camera_add()
    bpy.context.object.name = 'Camera_L'

# Set the location of the cameras
bpy.data.objects['Camera_F'].location = (0.0, -3.5, 1.0)
bpy.data.objects['Camera_B'].location = (0.0, 3.5, 1.0)
bpy.data.objects['Camera_R'].location = (-3.5, 0.0, 1.0)
bpy.data.objects['Camera_L'].location = (3.5, 0.0, 1.0)

# Set the rotation of the cameras
bpy.data.objects['Camera_F'].rotation_euler = (math.radians(90.0), 0.0, math.radians(0.0))
bpy.data.objects['Camera_B'].rotation_euler = (math.radians(90.0), 0.0, math.radians(180.0))
bpy.data.objects['Camera_R'].rotation_euler = (math.radians(90.0), 0.0, math.radians(270.0))
bpy.data.objects['Camera_L'].rotation_euler = (math.radians(90.0), 0.0, math.radians(90.0))

# Add area light settings
light_size = 30
light_data = bpy.data.lights.new(name="Light", type='AREA')
light_data.energy = 100.0

# Top light
if not any(obj.name == "Light_Top" for obj in bpy.context.scene.objects):
    light_object_t = bpy.data.objects.new(name="Light_Top", object_data=light_data)
    light_object_t.location = (0.0, 0.0, 5.0)
    light_object_t.rotation_euler = (math.radians(0.0), math.radians(0.0), math.radians(0.0))
    light_object_t.scale = (light_size, light_size, light_size)
    bpy.context.scene.collection.objects.link(light_object_t)

# Down light
if not any(obj.name == "Light_Down" for obj in bpy.context.scene.objects):
    light_object_d = bpy.data.objects.new(name="Light_Down", object_data=light_data)
    light_object_d.location = (0.0, 0.0, -3.0)
    light_object_d.rotation_euler = (math.radians(180.0), math.radians(0.0), math.radians(0.0))
    light_object_d.scale = (light_size, light_size, light_size)
    bpy.context.scene.collection.objects.link(light_object_d)

# Front light
if not any(obj.name == "Light_Front" for obj in bpy.context.scene.objects):
    light_object_f = bpy.data.objects.new(name="Light_Front", object_data=light_data)
    light_object_f.location = (0.0, -5.0, 1.0)
    light_object_f.rotation_euler = (math.radians(90.0), math.radians(0.0), math.radians(0.0))
    light_object_f.scale = (light_size, light_size, light_size)
    bpy.context.scene.collection.objects.link(light_object_f)

# Back light
if not any(obj.name == "Light_Back" for obj in bpy.context.scene.objects):
    light_object_d = bpy.data.objects.new(name="Light_Back", object_data=light_data)
    light_object_d.location = (0.0, 5.0, 1.0)
    light_object_d.rotation_euler = (math.radians(90.0), math.radians(0.0), math.radians(180.0))
    light_object_d.scale = (light_size, light_size, light_size)
    bpy.context.scene.collection.objects.link(light_object_d)


# Left light
if not any(obj.name == "Light_Left" for obj in bpy.context.scene.objects):
    light_object_d = bpy.data.objects.new(name="Light_Left", object_data=light_data)
    light_object_d.location = (-5.0, 0.0, 1.0)
    light_object_d.rotation_euler = (math.radians(90.0), math.radians(0.0), math.radians(-90.0))
    light_object_d.scale = (light_size, light_size, light_size)
    bpy.context.scene.collection.objects.link(light_object_d)


# Right light
if not any(obj.name == "Light_Right" for obj in bpy.context.scene.objects):
    light_object_d = bpy.data.objects.new(name="Light_Right", object_data=light_data)
    light_object_d.location = (5.0, 0.0, 1.0)
    light_object_d.rotation_euler = (math.radians(90.0), math.radians(0.0), math.radians(90.0))
    light_object_d.scale = (light_size, light_size, light_size)
    bpy.context.scene.collection.objects.link(light_object_d)


# Set up render settings
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.device = 'CPU'
bpy.context.scene.render.resolution_x = 512
bpy.context.scene.render.resolution_y = 512
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.film_transparent = True

# Create the render directory if it doesn't exist
render_path = "C:/2D Render"
if not os.path.exists(render_path):
    os.makedirs(render_path)

# Create the characters directory if it doesn't exist
characters_path = os.path.join(render_path, "characters")
if not os.path.exists(characters_path):
    os.makedirs(characters_path)

# Get the subdirectories in the characters directory
subdirs = next(os.walk(characters_path))[1]

# Determine the new subdirectory name
if '1' not in subdirs:
    subdir_name = '1'
else:
    i = 2
    while str(i) in subdirs:
        i += 1
    subdir_name = str(i)

# Create the new subdirectory
subdir_path = os.path.join(characters_path, subdir_name)
os.makedirs(subdir_path)

# Render the images from each camera
for camera_name in ['Camera_F', 'Camera_B', 'Camera_R', 'Camera_L']:
    # Set the active camera
    bpy.context.scene.camera = bpy.data.objects[camera_name]

    # Set the output file path
    file_path = os.path.join(subdir_path, '{}-image.png'.format(camera_name.lower()))
    bpy.context.scene.render.filepath = file_path

    # Render the image and write to disk
    bpy.ops.render.render(write_still=True)

    # Print the file path
    print("Output Path:", bpy.context.scene.render.filepath)

# Remove the cameras and lights
for obj in bpy.context.scene.objects:
    if obj.name.startswith('Camera_') or obj.name.startswith('Light_'):
        bpy.data.objects.remove(obj, do_unlink=True)
