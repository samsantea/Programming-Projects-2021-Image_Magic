# Image Magic
# Load an image and manipulate the pixels

from PIL import Image

def to_greyscale(pixel: tuple, algo="average") -> tuple:
    """ Convert a pixel to greyscale.
    Can also specify the greyscale algorithm.
    Defaults to average.

    Args:
        pixel: a 3-tuple of ints
            from 0-255, e.g. (140, 120, 255)
            represents (red, green, blue)
        algo: The greyscale conversion algorithm
            specified by the user
            valid values are "average", "luma"
            Defaults to "average"

    Returns:
        a 3-tuple pixel (r, g, b) in greyscale
    """

    # GRAB R, G, B
    # red = pixel[0]
    # green = pixel[1]
    # blue = pixel[2]

    red, green, blue = pixel  # can only be done with lists or tuples

    # calculate the grey pixel
    if algo.lower() == "luma":
        grey = int(red * 0.3 + green * 0.59 + blue * 0.11)
    else:
        grey = int((red + green + blue) / 3)

    return grey, grey, grey

# Load the image (pumpkin)

# Use single quotes when referring to something
image = Image.open('./halloween-unsplash.jpg')
output_image = Image.open('./halloween-unsplash.jpg')

# Grab pixel information
# inside parentheses must be x, y value of pixel in tuple/list
a_pixel = image.getpixel((0, 0)) # Grab pixel (0, 0) top-left

print(a_pixel)

# Iterate over EVERY PIXEL
# Get dimensions (size) of the image
image_width = image.width
image_height = image.height
# Top bottom

# Modify the image to convert it from colour to grayscale
# (r, g, b) --> (?, ?, ?)
# take the r g b, add them up and divide by 3
# replace r, g, b with that AVERAGE value

for y in range(image_height):
    # Left to right
    for x in range(image_width):
        # Grab pixel information for THIS pixel
        pixel = image.getpixel((x, y))

        grey_pixel = to_greyscale(pixel)

        # put that in the new image
        output_image.putpixel((x, y), grey_pixel)

output_image.save('greyscale_2.jpg')

print("Done!")