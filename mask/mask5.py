from PIL import Image

output_img = Image.new("L", (21,21))


for i in range(21):
    for j in range(21):
        if ((i*j) % 2 + (i*j)) % 3 == 0:
            pixel_value = 0
        else:
            pixel_value = 255
        output_img.putpixel((j, i), pixel_value)
for i in range(9):
    for j in range(9):
        output_img.putpixel((i, j), 255)
for i in range(13, 21):
    for j in range(9):
        output_img.putpixel((i, j), 255)
for i in range(9):
    for j in range(13, 21):
        output_img.putpixel((i, j), 255)
pixels_to_set_white = [(6,9), (6,10), (6,11), (6,12)]
for pixel in pixels_to_set_white:
    output_img.putpixel(pixel, 255)
output_img.save("mask5.jpg")