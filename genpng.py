#!/usr/bin/python3

from PIL import Image, ImageDraw

def generate_pinhole_image(pinhole_diameter_mm, spacing_mm, image_size_mm):
    # Calculate the size of the image in pixels
    dpi = 300  # print resolution in DPI
    image_size_pixels = tuple(round(dpi * mm / 25.4) for mm in image_size_mm)

    # Calculate the size of the pinhole dots and spacing in pixels
    pinhole_diameter_pixels = round(dpi * pinhole_diameter_mm / 25.4)
    spacing_pixels = round(dpi * (spacing_mm + pinhole_diameter_mm) / 25.4)

    # Create a new image with a white background
    image = Image.new('RGB', image_size_pixels, 'white')

    # Draw pinholes on the image
    draw = ImageDraw.Draw(image)
    for j in range(0, image_size_pixels[1], spacing_pixels):
        shift = spacing_pixels / 2 if j % (2 * spacing_pixels) == spacing_pixels else 0
        for i in range(round(0 + shift), image_size_pixels[0], spacing_pixels):
            draw.ellipse((i-pinhole_diameter_pixels/2, j-pinhole_diameter_pixels/2, i+pinhole_diameter_pixels/2, j+pinhole_diameter_pixels/2), fill='black')

    # Save the image to a file
    image.save('pinhole_image.png')

# Example usage
generate_pinhole_image(1.1, 2.5, (210, 297))
