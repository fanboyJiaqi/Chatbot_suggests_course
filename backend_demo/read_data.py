import fitz
import sys
import os

def extract_text_from_pdf(pdf_path):
    document = document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text("text")
        if page_num > 0 :
            text += "\n"
    return text

def save_text_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        
# save_text_to_file(learnpath, "learn_path_demo.txt")

# pdf_path = r"C:\Users\Admin\Documents\GPT_LLM\Bai_So_6\dataset\ResumesPDF\ResumesPDF\cv (283).pdf"
# text_of_pdf = extract_text_from_pdf(pdf_path)
# print(text_of_pdf)