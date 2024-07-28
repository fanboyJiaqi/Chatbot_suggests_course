import fitz  # PyMuPDF
from PIL import Image
import os

def pdf_to_jpg(pdf_folder_path, output_folder_path):
    # Kiểm tra thư mục đầu vào và đầu ra
    if not os.path.exists(pdf_folder_path):
        print(f"Thư mục {pdf_folder_path} không tồn tại.")
        return
    
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    # Duyệt qua tất cả các tệp PDF trong thư mục
    for pdf_file in os.listdir(pdf_folder_path):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder_path, pdf_file)
            pdf_document = fitz.open(pdf_path)
            
            # Duyệt qua từng trang của tệp PDF
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                pix = page.get_pixmap(dpi=300)
                
                # Tạo tên file đầu ra
                output_filename = f"{os.path.splitext(pdf_file)[0]}_{page_num + 1}.jpg"
                output_path = os.path.join(output_folder_path, output_filename)
                
                # Lưu ảnh thành file JPG
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                img.save(output_path, "JPEG")
                
            pdf_document.close()
    print("Chuyển đổi hoàn tất.")
    
def one_pdf_to_jpg(pdf_file_path, output_folder_path):
    # Kiểm tra tệp PDF đầu vào
    if not os.path.exists(pdf_file_path):
        print(f"Tệp PDF {pdf_file_path} không tồn tại.")
        return
    
    # Kiểm tra và tạo thư mục đầu ra nếu chưa tồn tại
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    # Mở tệp PDF
    pdf_document = fitz.open(pdf_file_path)
    
    # Duyệt qua từng trang của tệp PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap(dpi=300)
        
        # Tạo tên file đầu ra
        output_filename = f"{os.path.splitext(os.path.basename(pdf_file_path))[0]}_{page_num + 1}.jpg"
        output_path = os.path.join(output_folder_path, output_filename)
        
        # Lưu ảnh thành file JPG
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(output_path, "JPEG")
                
    pdf_document.close()
    print("Chuyển đổi hoàn tất.")

# Sử dụng hàm
# pdf_folder_path = r"C:\Users\Admin\Documents\F_GPT_Demo\data_CV"  # Thay bằng đường dẫn đến thư mục chứa các file PDF
# output_folder_path = r"C:\Users\Admin\Documents\F_GPT_Demo\image_data_cv"  # Thay bằng đường dẫn đến thư mục để lưu các file JPG
# pdf_to_jpg(pdf_folder_path, output_folder_path)
