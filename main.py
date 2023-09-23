#!/usr/bin/env python3

from PIL import Image
import glob


# Original and final directory
ORIGINAL_DIRECTORY = "/images/"
FINAL_DIRECTORY = "/opt/icons/"

def change_image(image_path: str) -> Image:
    """Change image to 128x128 and rotate 90 degrees clockwise"""
    with Image.open(image_path) as image:
        image = image.convert("RGB").rotate(90).resize((128, 128))
        return image


# get image files from the directory
search_string = ORIGINAL_DIRECTORY + "*"
file_names = glob.glob(search_string)
for file_path in file_names:
    file_name = file_path.split("/")[-1]
    file_name = FINAL_DIRECTORY + file_name + ".jpeg"
    new_image = change_image(file_path)
    new_image.save(file_name, "JPEG")
