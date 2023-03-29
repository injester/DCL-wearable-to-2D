import bpy
import math
import os

# Check if scale indicator and ground indicator already exist
if 'Scale Indicator' not in bpy.data.objects or 'Ground Indicator' not in bpy.data.objects:

    # Add the scale indicator plane
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, location=(0, 1, 1))
    scale_indicator = bpy.context.object
    scale_indicator.name = 'Scale Indicator'
    scale_indicator.scale = (2.226, 1, 1)
    scale_indicator.rotation_euler = (1.5708, 0, 0)
    scale_indicator.scale = (4.45, 2, 0)

    # Add the ground indicator plane
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, location=(0, 0, 0))
    ground_indicator = bpy.context.object
    ground_indicator.name = 'Ground Indicator'
    ground_indicator.scale = (2.226, 1, 1)
    ground_indicator.scale = (4.45, 2, 0)

    # Hide the planes from camera view
    for plane in [scale_indicator, ground_indicator]:
        plane.hide_render = True

    # Stop the script
    raise Exception("ADD YOUR BUILDING CENTERED IN THE PLANES. MAKE SURE IT STAYS INSIDE IT!")

else:
    # Continue with the script
    pass


# Add cameras if it doesn't exist already

if 'Camera_F' not in bpy.data.objects:
    bpy.ops.object.camera_add()
    bpy.context.object.name = 'Camera_F'

# Set the location and rotation of the front camera
bpy.data.objects['Camera_F'].location = (0.0, -4.5, 5.5)
bpy.data.objects['Camera_F'].rotation_euler = (math.radians(45.0), 0.0, math.radians(0.0))

# Add area light settings
light_size = 30
light_data = bpy.data.lights.new(name="Light", type='AREA')
light_data.energy = 1000.0

# Top light

if not any(obj.name == "Light_Top" for obj in bpy.context.scene.objects):
    light_object_t = bpy.data.objects.new(name="Light_Top", object_data=light_data)
    light_object_t.location = (0.0, -2.2, 4.3)
    light_object_t.rotation_euler = (math.radians(45.0), math.radians(0.0), math.radians(0.0))
    light_object_t.scale = (light_size, light_size, light_size)
    bpy.context.scene.collection.objects.link(light_object_t)


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

# Create the buildings directory if it doesn't exist
buildings_path = os.path.join(render_path, "buildings")
if not os.path.exists(buildings_path):
    os.makedirs(buildings_path)

# Get the subdirectories in the characters directory
subdirs = next(os.walk(buildings_path))[1]

# Determine the new subdirectory name
if '1' not in subdirs:
    subdir_name = '1'
else:
    i = 2
    while str(i) in subdirs:
        i += 1
    subdir_name = str(i)

# Create the new subdirectory
subdir_path = os.path.join(buildings_path, subdir_name)
os.makedirs(subdir_path)

# Render the images from the front camera
camera_name = 'Camera_F'
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
