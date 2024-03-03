from PIL import Image

def xor_images(image_path1, image_path2):
    img1 = Image.open(image_path1).convert("L")
    img2 = Image.open(image_path2).convert("L")

   
    if img1.size != img2.size:
        raise ValueError("Images must have the same size.")

   
    xor_result = Image.eval(img1, lambda x: 0 if x != img2.getpixel((x % img2.width, x // img2.width)) else 255)

    return xor_result


path_to_image1 = "/Users/anshu/qr_code/masking/initial.jpg"  
path_to_image2 = "/Users/anshu/qr_code/masking/final.jpg"  

result_image = xor_images(path_to_image1, path_to_image2)


result_image.save("result_xor_black_white.png")
