import qrcode
from PIL import Image

def generate_qr_code(data, masking_pattern=4):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    
    qr_code = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    qr_code = set_masking_pattern(qr_code, masking_pattern)

    return qr_code

def set_masking_pattern(qr_code, masking_pattern):
    if 0 <= masking_pattern <= 7:
        img = qr_code.convert("RGB")

        
        new_img = Image.new("RGB", img.size)

        
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                pixel = img.getpixel((x, y))
                new_x, new_y = x, y

                if masking_pattern == 0:
                    new_x, new_y = x + y, y
                elif masking_pattern == 1:
                    new_x, new_y = x, y % 2
                elif masking_pattern == 2:
                    new_x, new_y = x % 2, y % 2
                elif masking_pattern == 3:
                    new_x, new_y = (x + y) % 2, y % 2
                elif masking_pattern == 4:
                    new_x, new_y = ((x // 2) + (y // 3)) % 2, (y % 3) % 2
                elif masking_pattern == 5:
                    new_x, new_y = (x * y) % 2 + (x * y) % 3, (x * y) % 2 + (x * y) % 3
                elif masking_pattern == 6:
                    new_x, new_y = ((x * y) % 2 + (x * y) % 3) % 2, ((x * y) % 2 + (x * y) % 3) % 2
                elif masking_pattern == 7:
                    new_x, new_y = ((x + y) % 2 + (x * y) % 3) % 2, ((x + y) % 2 + (x * y) % 3) % 2

                new_img.putpixel((x, y), pixel)

        return new_img
    else:
        raise ValueError("Masking pattern should be between 0 and 7.")


data_value = "Hi"
initial_masking_pattern = 4
new_masking_pattern = int(input("Enter the new masking pattern (0-7): "))

initial_qr_code = generate_qr_code(data_value, initial_masking_pattern)
initial_qr_code.show()
initial_qr_code.save("initial.jpg")

new_qr_code = set_masking_pattern(initial_qr_code, new_masking_pattern)
new_qr_code.show()
new_qr_code.save("final.jpg")