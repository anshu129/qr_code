from PIL import Image

def get_masking_pattern(qr_code):
    try:
        format_info = qr_code.getpixel((8, 0))  
        masking_pattern = (format_info >> 3) & 0b111

        return masking_pattern
    except Exception as e:
        print(f"Error extracting masking pattern: {e}")
        return None

qr_code_path = "/Users/anshu/qr_code/xor/img1.png"  
qr_code = Image.open(qr_code_path)

masking_pattern_used = get_masking_pattern(qr_code)

if masking_pattern_used is not None:
    print(f"The masking pattern used is: {masking_pattern_used}")
else:
    print("Masking pattern could not be determined.")
