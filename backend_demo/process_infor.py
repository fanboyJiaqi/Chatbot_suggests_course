
import sys
import os
import json
# Thêm đường dẫn của thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from azure_demo_v1 import *
from backend_demo.read_data import extract_text_from_pdf


def extract_skill_from_pdf(page_text):
    text = page_text
    prompt = f"""Here is the resume: {text}. Please explicitly identify and extract the SKILLS section and return as a JSON object with the following format:
    {{"skills": ["skill1", "skill2", "skill3", ...]}}
    The returned result should be in JSON format without anything added.
    """
    llm = model
    answer = llm.invoke(prompt)
    return answer

def extract_skill_from_pdf_1(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    prompt = f"""You are a system serving the purpose of recruiting human resources. Please read the following CV: {text} and evaluate the candidate based on the information provided in the CV, focusing on the following aspects:
                    Skills
                    Work Experience
                    Education
                    Certifications and Licenses
                    Professional Certificates Achieved
                    Online or Extracurricular Courses Completed
                    Languages Known and Proficiency Level
                For each skill mentioned, determine the candidate's proficiency level based on the following criteria:
                    Beginner:
                        Less than 6 months of experience.
                        No relevant work experience.
                        Skills mentioned without supporting work experience or projects.
                    Intermediate:

                        Over 6 months but under 2 years of experience.
                        Relevant work experience or projects that indicate active usage of the skill for the specified duration.
                    Expert:
                        Over 2 years of experience.
                        Significant and relevant work experience or projects that demonstrate deep knowledge and proficiency in the skill.
                Your task is to classify each skill according to the candidate's experience and the relevance of their work to the skill described in the CV.
    """
    llm = model
    answer = llm.invoke(prompt)
    return answer

pdf_path = r"C:\Users\Admin\Documents\GPT_LLM\Bai_So_6\dataset\ResumesPDF\ResumesPDF\cv (20).pdf"
skills = extract_skill_from_pdf_1(pdf_path)
print(skills)