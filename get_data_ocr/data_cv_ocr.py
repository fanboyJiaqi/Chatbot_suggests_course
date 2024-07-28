import pytesseract
from PIL import Image
 
# Nếu bạn sử dụng Windows, hãy chỉ định đường dẫn tới tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
 
def ocr_image(image_path):
    # Mở hình ảnh bằng PIL
    img = Image.open(image_path)
   
    # Sử dụng Tesseract để nhận dạng văn bản
    text = pytesseract.image_to_string(img, lang='eng')  # Thay 'eng' bằng ngôn ngữ bạn muốn nhận dạng
   
    # In ra kết quả
    print(text)
 
# Đường dẫn tới file hình ảnh
image_path = r'C:\Users\Admin\Documents\F_GPT_Demo\image_data_cv\cv (136)_2.jpg'
ocr_image(image_path)