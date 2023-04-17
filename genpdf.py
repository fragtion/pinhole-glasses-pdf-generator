#!/usr/bin/python

from PIL import Image, ImageDraw

def generate_pinhole_image(pinhole_diameter_mm, spacing_mm, paper_size_mm):
    # Convert millimeters to pixels
    pinhole_diameter_pixels = round(pinhole_diameter_mm * 300 / 25.4)
    spacing_pixels = round((pinhole_diameter_mm + spacing_mm) * 300 / 25.4)

    # Calculate the size of the image in pixels
    paper_size_pixels = (round(paper_size_mm[0] * 300 / 25.4), round(paper_size_mm[1] * 300 / 25.4))

    # Create a new image with a white background
    image = Image.new('RGB', paper_size_pixels, 'white')

    # Draw pinholes on the image
    draw = ImageDraw.Draw(image)
    for j in range(0, paper_size_pixels[1], spacing_pixels):
        shift = spacing_pixels / 2 if j % (2 * spacing_pixels) == spacing_pixels else 0
        for i in range(round(0 + shift), paper_size_pixels[0], spacing_pixels):
            draw.ellipse((i - pinhole_diameter_pixels / 2, j - pinhole_diameter_pixels / 2, i + pinhole_diameter_pixels / 2, j + pinhole_diameter_pixels / 2), fill='black')

    # Save the image as PDF
    image.save('pinhole_image.pdf', 'PDF', resolution=300.0)

# Example usage
generate_pinhole_image(1.1, 3.5, (210, 297))
