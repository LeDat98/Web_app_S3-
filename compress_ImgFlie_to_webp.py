import os
from PIL import Image

# Set the directory path where the images are located
directory = "/Users/leducdat/Desktop/Flask_Web/static/images"
directory_to_save = 'images'
# Iterate through all the files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        # Open the image file
        image = Image.open(f"{directory}/{filename}")
        # Compress the image and save it in .png format
        image.save(f"{directory_to_save}/{filename}.webp", "webp", optimize=True, quality=95)

