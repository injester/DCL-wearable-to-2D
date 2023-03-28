# DCL-wearable-to-2D
Uploading a 3D wearable to blender and then use a script to get pictures of all 4 sides.

This Python script automates the process of setting up and rendering images from four different camera angles with six area lights. It also creates the render directory if it doesn't exist and saves the rendered images to disk.

To use the script, follow these steps:

Open Blender and create or open a scene that you want to render.
Open the Scripting workspace in Blender.
Create a new text block and paste the code into it.
Edit the render_path variable to the desired path where the rendered images will be saved.
Run the script.
The script will create four cameras and six area lights if they don't already exist in the scene. It will then set the locations and rotations of the cameras and the lights, and set up the render settings.

After that, the script will render the images from each camera, save the images to disk in the specified render directory, and print the file paths to the console.

Finally, the script will remove the cameras and lights from the scene.

Note: The script assumes that you are using CPU for rendering. If you want to use GPU instead, you need to edit the line 'bpy.context.scene.cycles.device = 'CPU'' to 'bpy.context.scene.cycles.device = 'GPU'' and set the device type to GPU in the Blender user preferences.
