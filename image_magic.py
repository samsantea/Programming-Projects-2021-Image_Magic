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

# def brighter(pixel: tuple, brightness: int) -> tuple:
#     """Increases the brightness of a pixel
#
#     Args:
#         pixel: a 3-tuple of (red, green, blue)
#             subpixels
#         brightness: the amount to increase pixel brightness by.
#
#
#     Returns:
#           a 3-tuple representing a brighter pixel
#     """
#
#     red, green, blue = pixel
#
#     # Calculate the brighter pixel
#
#     brighten_colours = True
#
#     if red and green and blue >= 255:
#         brighter_red = red
#         brighter_green = green
#         brighter_blue = blue
#         brighten_colours = False
#
#     while brighten_colours == True:
#         if red >= 255:
#             brighter_red = red
#             brighter_green = int(green + brightness)
#             brighter_blue = int(blue + brightness)
#         elif green>= 255:
#             brighter_red = int(red + brightness)
#             brighter_green = green
#             brighter_blue = int(blue + brightness)
#         elif blue >= 255:
#             brighter_red = int(red + brightness)
#             brighter_green = int(green + brightness)
#             brighter_blue = blue
#         else:
#             if red + magnitude >= 255:
#                 red = 255
#             else:
#                 red += 25
#             if green + magnitude >= 255:
#                 green = 255
#             else:
#                 green += 25
#             if blue + 25 >= 255:
#                 blue = 255
#             else:
#                 blue += 25
#     return brighter_red, brighter_green, brighter_blue

def brightness(pixel: tuple, magnitude) -> tuple:
    """Increases the brightness of a pixel

    Args:
        pixel: a 3-tuple of (red, green, blue)
            subpixels
        magnitude: an int from -255 to 255 that indicates how much to increase brightness


    Returns:
          a 3-tuple representing a brighter pixel
    """

    red, green, blue = pixel

    # max value for a subpixel
    MAX = 255
    MIN = 0

    #  Increase the value by some number
    if red + magnitude >= MAX:
        red = 255
    elif red + magnitude < MIN:
        red = MIN
    else:
        red += magnitude
    if green + magnitude >= MAX:
        green = MAX
    elif green + magnitude < MIN:
        green = MIN
    else:
        green += magnitude
    if blue + magnitude >= MAX:
        blue = MAX
    elif blue + magnitude < MIN:
        blue = MIN
    else:
        blue += magnitude

    return red, green, blue


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

        brighter_pixel = brightness(pixel, 100)

        # put that in the new image
        output_image.putpixel((x, y), brighter_pixel)

output_image.save('brighterer.jpg')

print("Done!")