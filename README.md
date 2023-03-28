# DCL-wearable-to-2D
Uploading a 3D wearable to blender and then use a script to get pictures of all 4 sides.

This Python script automates the process of setting up and rendering images from four different camera angles with six area lights. It also creates the render directory if it doesn't exist and saves the rendered images to disk.

The requirements for running this script are as follows:

Blender - The script is intended to be run within Blender, so you will need to have Blender installed on your system. The script was written and tested on Blender 2.92, but it should work on other versions as well.

OpenCV - The script does not require OpenCV or any other external libraries to run.

Sufficient system resources - Depending on the complexity of the scene you want to render, you may need a powerful CPU and/or GPU, as well as enough memory to handle the rendering process.

To use the script, follow these steps:

1. Open Blender and create or open a scene that you want to render.
2. Open the Scripting workspace in Blender.
3. Create a new text block and paste the code into it.
4. Edit the render_path variable to the desired path where the rendered images will be saved.
5. Import the wearable as GLB 
6. Run the script.

The pictures will be saved in the directory specified by the render_path variable in the script.

By default, the script sets render_path to "C:/2D Render". Therefore, the rendered images will be saved in the "2D Render" folder on the C drive (assuming you're using a Windows operating system).

If the specified directory doesn't exist, the script will create it automatically before saving the images.

The images will be named based on the name of the camera they were rendered from. For example, the image rendered from the 'Camera_F' will be named 'camera_f-image.png'.

The script will create four cameras and six area lights if they don't already exist in the scene. It will then set the locations and rotations of the cameras and the lights, and set up the render settings.

After that, the script will render the images from each camera, save the images to disk in the specified render directory, and print the file paths to the console.

Finally, the script will remove the cameras and lights from the scene.

Note: The script assumes that you are using CPU for rendering. If you want to use GPU instead, you need to edit the line 'bpy.context.scene.cycles.device = 'CPU'' to 'bpy.context.scene.cycles.device = 'GPU'' and set the device type to GPU in the Blender user preferences.

