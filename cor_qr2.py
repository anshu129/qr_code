import qrcode
from PIL import Image
import numpy as np
from scipy.ndimage import correlate

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

def calculate_correlation(qr1, qr2):
    img1 = qr1.get_image()
    img2 = qr2.get_image()

    
    pixels1 = np.array(img1)
    pixels2 = np.array(img2)

    
    correlation_result = correlate(pixels1, pixels2)

    return correlation_result

def combine_qrs(qr1, qr2, correlation_threshold=0.95):
    correlation_result = calculate_correlation(qr1, qr2)

    
    combined_img = Image.new("L", qr1.size)
    pixels_combined = []

    
    for row in correlation_result:
        for value in row:
            if value >= correlation_threshold:
                pixels_combined.append(0)  # Set to black
            else:
                pixels_combined.append(255)  # Set to white

    combined_img.putdata(pixels_combined)

    return combined_img


data1 = "QR Code 1 Data"
data2 = "QR Code 2 Data"

qr1 = create_binary_qr(data1)
qr2 = create_binary_qr(data2)

combined_qr = combine_qrs(qr1, qr2)
combined_qr.save("combined_qr2.png")
