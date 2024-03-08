from PIL import Image


# Create an empty image with the same dimensions
output_img = Image.new("L", (21,21))

# Loop over the bottom half of the image
for i in range(21):
    for j in range(21):
        # Calculate the pixel value based on (i+j) mod2
        if ((i/2) + (j/3)) % 2 == 0:
            pixel_value = 0
        else:
            pixel_value = 255

        # Set the pixel value in the output image
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
# Save the output image
output_img.save("mask4.jpg")