from PIL import Image

def resize_image(filename, new_width, new_height):
    # Open the image file
    with Image.open(filename) as img:
        # Resize the image
        resized_img = img.resize((new_width, new_height))
        # Split the filename into name and extension
        name, extension = filename.split('.')
        # Save the resized image with a new filename
        new_filename = f"{name}_{new_width}x{new_height}.{extension}"
        resized_img.save(new_filename)
        print(f"Resized image saved as {new_filename}")

# Example usage
filename = "example.jpg"
new_width = 800
new_height = 600
resize_image(filename, new_width, new_height)
