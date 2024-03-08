from PIL import Image
import qrcode

# retrieving mask pattern
def get_masking_pattern(qr_code):
    try:
        format_info = qr_code.getpixel((8, 0))  
        masking_pattern = (format_info >> 3) & 0b111

        return masking_pattern
    except Exception as e:
        print(f"Error extracting masking pattern: {e}")
        return None

#genrating qr
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
    img.save("qr.jpg");


#resizing the images 
def resize_images(image1, image2):
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    # Ensure both images have the same size
    if img1.size != img2.size:
        # Resize the larger image to match the size of the smaller one
        if img1.size[0] > img2.size[0] or img1.size[1] > img2.size[1]:
            img1 = img1.resize(img2.size, Image.LANCZOS)
        else:
            img2 = img2.resize(img1.size, Image.LANCZOS)

    return img1, img2

#XOR operatrion 
def xor_images(image1, image2):
    img1, img2 = resize_images(image1, image2)

    xor_result = Image.new("L", img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            pixel1 = img1.getpixel((x, y))
            pixel2 = img2.getpixel((x, y))
            xor_result.putpixel((x, y), pixel1 ^ pixel2)
    xor_result.show()
    xor_result.save("org_image.jpg")



#main code
data = input("type the input you want to genrate the qr of");
create_binary_qr(data);
qr = "/Users/anshu/qr_code/qr.jpg"
qr_code = Image.open(qr)
mask = get_masking_pattern(qr_code);

mask0 = "/Users/anshu/qr_code/mask/mask0.jpg"
mask1 = "/Users/anshu/qr_code/mask/mask1.jpg"
mask2 = "/Users/anshu/qr_code/mask/mask2.jpg"
mask3 = "/Users/anshu/qr_code/mask/mask3.jpg"
mask4 = "/Users/anshu/qr_code/mask/mask4.jpg"
mask5 = "/Users/anshu/qr_code/mask/mask5.jpg"
mask6 = "/Users/anshu/qr_code/mask/mask6.jpg"
mask7 = "/Users/anshu/qr_code/mask/mask7.jpg"

if(mask == 0):
    org_image = xor_images(qr,mask0);
if(mask == 1):
    org_image = xor_images(qr,mask1);
if(mask == 2):
    org_image = xor_images(qr,mask2);
if(mask == 3):
    org_image = xor_images(qr,mask3);
if(mask == 4):
    org_image = xor_images(qr,mask4);
if(mask == 5):
    org_image = xor_images(qr,mask5);
if(mask == 6):
    org_image = xor_images(qr,mask6);
if(mask == 7):
    org_image = xor_images(qr,mask7);
desired_mask = int(input("type your desired mask"));

org_image = "/Users/anshu/qr_code/org_image.jpg"

if(desired_mask == 0):
    xor_images(org_image,mask0);
if(desired_mask == 1):
    xor_images(org_image,mask1);
if(desired_mask == 2):
    xor_images(org_image,mask2);

if(desired_mask == 3):
    xor_images(org_image,mask3);
if(desired_mask == 4):
    xor_images(org_image,mask4);
if(desired_mask == 5):
    xor_images(org_image,mask5);
if(desired_mask == 6):
    xor_images(org_image,mask6);
if(desired_mask == 7):
    xor_images(org_image,mask7);
    