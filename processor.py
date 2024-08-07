from PIL import Image
import sys


def normalise(min, max, value, char_len):
    range = max - min
    return round(((value - min)/range)*char_len)


def convert(image_path, x_scale, y_scale):
    try:
        im = Image.open(image_path)

    except FileNotFoundError:
        print("This file doesn't exist")
        sys.exit(1)

    greyscale = im.convert("L")

    width, height = greyscale.size
    height = round(height/y_scale)
    width = round(width/x_scale)
    greyscale = greyscale.resize((width, height))

    greyscale.save("result.jpg")

    chars = [" ", ".", ":", "-", "c", "=", "+", "*", "o", "", "#", "%", "@"]

    comp = []

    for line in range(height):
        for column in range(width):
            pixel = greyscale.getpixel((column, line))
            comp.append(pixel)

    minimum = min(comp)
    maximum = max(comp)

    output_file = open("result.txt", "w")
    for line in range(height):
        for column in range(width):
            value = greyscale.load()[column, line]
            pixel = chars[normalise(minimum, maximum, value, len(chars))-1]
            print(pixel)
            output_file.write(pixel)
        output_file.write("\n")

    output_file.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("you need to provide the image path [python3 processor.py /]")
        sys.exit(1)
    elif len(sys.argv) < 4:
        x_scale = 8
        y_scale = 12
    else:
        x_scale = int(sys.argv[2])
        y_scale = int(sys.argv[3])

    image_path = sys.argv[1]

    convert(image_path, x_scale, y_scale)
