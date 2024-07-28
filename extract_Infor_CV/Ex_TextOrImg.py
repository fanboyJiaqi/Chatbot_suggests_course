import fitz  # PyMuPDF
import os
import sys
import pytesseract
from PIL import Image
import json
from extract_info_from_cv_2 import extract_skill_from_pdf, extract_skill_from_image, save_json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from get_data_ocr.convert_image import one_pdf_to_jpg
# from get_data_ocr.data_cv_ocr import ocr_image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def check_text_and_images_in_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    has_text = False
    has_images = False
    num_page = len(doc)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        # Kiểm tra text
        text = page.get_text()
        if text.strip():
            has_text = True
        
        # Kiểm tra images
        image_list = page.get_images(full=True)
        if image_list:
            has_images = True
        
        # Nếu đã tìm thấy cả text và images thì không cần kiểm tra thêm
        if has_text and has_images:
            return True, True, num_page

    return has_text, has_images, num_page

def process_pdf_to_images(pdf_path, output_folder_path):
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=300)
        img_path = os.path.join(output_folder_path, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_{page_num + 1}.jpg")
        pix.save(img_path)

pdf_path = r'C:\Users\Admin\Documents\GPT_LLM\Bai_So_6\dataset\ResumesPDF\ResumesPDF\cv (136).pdf'

contains_text, contains_images, n_page_pdf = check_text_and_images_in_pdf(pdf_path)
text_of_pdf = ""
list_text_pdf = []

if contains_text and contains_images:
    print("PDF contains both text and images.")
    # Chuyển qua Img
    output_folder_path = r"C:\Users\Admin\Documents\F_GPT_Demo\image_data_cv"  # Thay bằng đường dẫn đến thư mục để lưu các file JPG
    process_pdf_to_images(pdf_path, output_folder_path)
    # Dung OCR
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]
    for i in range(1, n_page_pdf + 1):  # Sử dụng n_page_pdf để xác định số lượng ảnh
        image_path = os.path.join(output_folder_path, f"{file_name}_{i}.jpg")
        # print(image_path)
        if os.path.exists(image_path):  # Kiểm tra xem ảnh có tồn tại không
            text = pytesseract.image_to_string(image_path, lang='eng')
            text_of_pdf += text
            # list_text_pdf.append(text)
        else:
            print(f"Ảnh không tồn tại: {image_path}")
    
    answer = extract_skill_from_image(text_of_pdf)
    data_json = json.loads(answer.content)
    save_json(f"label_skill_cv/{file_name}_1.json", data= data_json)
elif contains_text:
    print("PDF contains only text.")
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]
    # Vao prompt
    answer = extract_skill_from_pdf(pdf_path)
    data_json = json.loads(answer.content)
    save_json(f"label_skill_cv/{file_name}_1.json", data= data_json)
elif contains_images:
    print("PDF contains only images.")
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]
    # Dung OCR
    output_folder_path = r"C:\Users\Admin\Documents\F_GPT_Demo\image_data_cv"  # Thay bằng đường dẫn đến thư mục để lưu các file JPG
    process_pdf_to_images(pdf_path, output_folder_path)
    # Dung OCR
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]
    for i in range(1, n_page_pdf + 1):  # Sử dụng n_page_pdf để xác định số lượng ảnh
        image_path = os.path.join(output_folder_path, f"{file_name}_{i}.jpg")
        if os.path.exists(image_path):  # Kiểm tra xem ảnh có tồn tại không
            text = pytesseract.image_to_string(image_path, lang='eng')
            text_of_pdf += text
            # list_text_pdf.append(text)
        else:
            print(f"Ảnh không tồn tại: {image_path}")
    
    answer = extract_skill_from_image(text_of_pdf)
    data_json = json.loads(answer.content)
    save_json(f"label_skill_cv/{file_name}_1.json", data= data_json)
else:
    print("PDF contains neither text nor images.")
    # Dang rong
