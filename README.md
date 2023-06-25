# Image-Resizer-in-Python
This is a Python program that uses the Pillow library to resize images. The program allows you to specify the filename of the image and the new dimensions (width and height) that you want to resize the image to. It then uses the Pillow library to open the image file, resize it to the new dimensions, and save the resized image with a new filename.

# Usage
To use the program, simply call the resize_image function in the image_resizer.py file with the filename of the image and the new dimensions as arguments. For example:
```
from image_resizer import resize_image

filename = "example.jpg"
new_width = 800
new_height = 600
resize_image(filename, new_width, new_height)
```
This will resize the example.jpg image to a width of 800 pixels and a height of 600 pixels, and save the resized image with a new filename that includes the original filename and the new dimensions.

# Requirements
The program requires the Pillow library to be installed. You can install Pillow using pip by running the command pip install Pillow in your terminal or command prompt.

# Contributing
If you find any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request. Contributions are welcome and appreciated!


