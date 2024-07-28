from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate 
import json
import fitz

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text("text")
        if page_num > 0 :
            text += "\n"
    return text

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


def extract_skill_from_pdf(path_pdf):
    text = extract_text_from_pdf(path_pdf)
    prompt = create_resume_prompt(text=text)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    answer = llm.invoke(prompt)
    return answer
  
def extract_skill_from_image(text):
    prompt = create_resume_prompt(text=text)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    answer = llm.invoke(prompt)
    return answer


def save_json(path, data):
  with open(path, 'w', encoding='utf-8') as file:
      json.dump(data, file, ensure_ascii=False, indent=4)

# if __name__ == "__main__" :
    
#     answer = extract_skill_from_pdf(r"C:\Users\Admin\Documents\F_GPT_Demo\data_CV\cv (2005).pdf")
#     print(answer.content)
#     data_json = json.loads(answer.content)
#     save_json("label_skill_cv/skills_cv2005_1.json", data= data_json)
    #     # Duyệt và in thông tin
    # for key, value in data_json.items():
    #     if isinstance(value, list):
    #         print(f"{key}:")
    #         for item in value:
    #             for inner_key, inner_value in item.items():
    #                 print(f"  {inner_key}: {inner_value}")
    #     elif isinstance(value, dict):
    #         print(f"{key}:")
    #         for inner_key, inner_value in value.items():
    #             print(f"  {inner_key}: {inner_value}")
    #     else:
    #         print(f"{key}: {value}")