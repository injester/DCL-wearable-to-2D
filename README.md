# 2D Converter for Decentraland Wearables

This script is designed to convert a 3D model into a 2D image from multiple angles, which can be used as a texture for a Decentraland wearable. It automatically sets up cameras and lighting for the scene, and saves the rendered images to disk.

## Installation

To use this script, you will need to have Blender installed on your computer. You can download Blender for free from the [Blender website](https://www.blender.org/download/).

## Tutorial Video

Watch our tutorial video on YouTube to see how to use the 2D Converter for Decentraland Wearables: [Converting 3D Models to 2D Textures for Decentraland Wearables with Blender](https://youtu.be/mofqXaKx818).

## Usage

1. Open Blender and load the 3D model you want to convert into a 2D image.
2. Open the Scripting workspace in Blender by selecting it from the top menu.
3. Open a new text editor window by selecting it from the bottom menu.
4. Add your GLB file in the middle to blender.
5. Copy and paste the code from `2D Converter.py` or `Building 2D.py` into the text editor window.
6. If you are using the builder script, you will have to run the script to see indicators (PLANE MODELS), center your building within this indicator.
7. Press the "Run Script" button or press `Alt + P` on your keyboard to run the script.
8. The script will automatically set up cameras and lighting for the scene, render the images, and save them to disk in a folder called "2D Render" on your `C:` drive. The rendered images will be saved in a folder for each render with the file names being `camera_f-image.png`, `camera_b-image.png`, `camera_r-image.png`, and `camera_l-image.png`.
9. Once the images have been rendered, you can use them as a texture for your Decentraland wearable.

## Customization

You can customize the script to suit your needs by modifying the following variables:

- `light_size`: The size of the area lights. Increase this value to make the lighting more diffuse, or decrease it to make the lighting more focused.
- `render_path`: The directory where the rendered images will be saved. By default, the images will be saved in a folder called "2D Render" on your `C:` drive.
- `camera_name`: The names of the cameras used to render the scene. By default, the script sets up four cameras: `Camera_F`, `Camera_B`, `Camera_R`, and `Camera_L`. You can change these names to whatever you like, but make sure to update them in the script as well.
- `device_type`: The type of device used to render the images. By default, the script uses the CPU (`'CPU'`), but you can switch to the GPU (`'CUDA'`) by changing this variable.

## License

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use and modify it for personal or commercial purposes.
