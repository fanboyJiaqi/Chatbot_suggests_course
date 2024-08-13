import pymupdf
import os
import fitz
import json
from io import BytesIO
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


def create_resume_prompt(text):
    prompt = f""" Here is the resume: {text}.\nPlease clearly identify and extract the Personal Information, Education, Work Experience, Skills, Certifications or Licenses, and Languages sections and return them as a JSON object with the following format:
      {{
        "PersonalInformation": {{
          "FullName": "string",
          "DateOfBirth": "string",
          "Gender": "string",
          "Address": "string",
          "PhoneNumber": "string",
          "Email": "string"
        }},
        "Education": [
          {{
            "School": "string",
            "Major": "string",
            "TimePeriod": "string",
            "Degree": "string"
          }}
        ],
        "WorkExperience": [
          {{
            "JobTitle": "string",
            "Company": "string",
            "TimePeriod": "string",
            "ResponsibilitiesAndAchievements": "string"
          }}
        ],
        "Skills": {{
          "TechnicalSkills": [
            "string"
          ],
          "SoftSkills": [
            "string"
          ]
        }},
        "CertificationsAndLicenses": [
          {{
            "CertificateOrLicense": "string",
            "AwardingOrganization": "string",
            "DateReceived": "string"
          }}
        ],
        "Languages": [
          {{
            "Language": "string",
            "ProficiencyLevel": "string"
          }}
        ]
      }}
      If any value for a key is not available, assign it an empty string (""). The returned result should be in JSON format without anything added."""
    return prompt


def extract_text_from_pdf(pdf_bytes):
    # Tạo đối tượng BytesIO từ dữ liệu byte của PDF
    pdf_stream = BytesIO(pdf_bytes)
    # Mở tài liệu PDF từ đối tượng BytesIO
    document = fitz.open(stream=pdf_stream, filetype="pdf")

    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text("text")
        if page_num > 0:
            text += "\n"

    document.close()
    return text


def save_file_pdf(output_directory: str, output_pdf_name: str, document: pymupdf.Document):
    output_pdf_path = os.path.join(output_directory, output_pdf_name)
    document.save(output_pdf_path)
    return output_pdf_path


def extract_resume_from_pdf(path_pdf):
    text = extract_text_from_pdf(path_pdf)
    prompt = create_resume_prompt(text=text)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    answer = llm.invoke(prompt)
    return answer


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# if __name__ == "__main__":
#     path_pdf = "ResumesPDF/cv (3).pdf"
#     answer = extract_resume_from_pdf(path_pdf)
#     data_json = json.loads(answer.content)
#     save_json("label_skill_cv/skills_cv3_1.json", data=data_json)
