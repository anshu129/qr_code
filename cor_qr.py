import qrcode
from PIL import Image

def create_binary_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def combine_qrs(qr1, qr2):
    img1 = qr1.get_image()
    img1.save("img1.png")
    img2 = qr2.get_image()
    img2.save("img2.png")

    pixels1 = img1.getdata()
    pixels2 = img2.getdata()

    # Combine pixels based on XOR logic
    new_pixels = [pixel1 ^ pixel2 for pixel1, pixel2 in zip(pixels1, pixels2)]

    # Create a new image with the combined pixel data
    combined_img = Image.new("L", img1.size)
    combined_img.putdata(new_pixels)

    return combined_img

data1 = "QR Code 1 Data"
data2 = "QR Code 2 Data"

qr1 = create_binary_qr(data1)
qr2 = create_binary_qr(data2)

combined_qr = combine_qrs(qr1, qr2)
combined_qr.save("combined_qr_xor.png")
