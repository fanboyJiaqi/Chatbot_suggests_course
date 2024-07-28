def create_personal_information_prompt(text):
    prompt = f"""Here is the resume: {text}.\nPlease identify and extract the Personal Information section and return it as a JSON object with the following format:
      {{
        "PersonalInformation": {{
          "FullName": "string",
          "DateOfBirth": "string",
          "Gender": "string",
          "Address": "string",
          "PhoneNumber": "string",
          "Email": "string"
        }}
      }}
      If any value for a key is not available, assign it an empty string (""). The returned result should be in JSON format without anything added.
      """
    return prompt

def create_education_prompt(text):
    prompt = f"""Here is the resume: {text}.\nPlease identify and extract the Education section and return it as a JSON object with the following format:
      {{
        "Education": [
          {{
            "School": "string",
            "Major": "string",
            "TimePeriod": "string",
            "Degree": "string"
          }}
        ]
      }}
      If any value for a key is not available, assign it an empty string (""). The returned result should be in JSON format without anything added.
      """
    return prompt

def create_work_experience_prompt(text):
    prompt = f"""Here is the resume: {text}.\nPlease identify and extract the Work Experience section and return it as a JSON object with the following format:
      {{
        "WorkExperience": [
          {{
            "JobTitle": "string",
            "Company": "string",
            "TimePeriod": "string",
            "ResponsibilitiesAndAchievements": "string"
          }}
        ]
      }}
      If any value for a key is not available, assign it an empty string (""). The returned result should be in JSON format without anything added.
      """
    return prompt

def create_skills_prompt(text):
    prompt = f"""Here is the resume: {text}.\nPlease identify and extract the Skills section and return it as a JSON object with the following format:
      {{
        "Skills": {{
          "TechnicalSkills": [
            {{
              "Skill": "string",
              "Level": "string"
            }}
          ],
          "SoftSkills": [
            "string"
          ]
        }}
      }}
      If any value for a key is not available, assign it an empty string (""). The returned result should be in JSON format without anything added.
      
      For determining the 'Level' for 'TechnicalSkills', follow these guidelines:
      1. If the skill is related to the major studied in 'Education', the level should be 'Intermediate'.
      2. Based on 'WorkExperience':
         - 'Beginner' if less than 2 years of related work experience.
         - 'Intermediate' if 2 to 5 years of related work experience.
         - 'Expert' if more than 5 years of related work experience.
      3. If there is no information related to the skill in 'Education' or 'WorkExperience', assign the level as 'Beginner'.
      """
    return prompt

def create_certifications_and_licenses_prompt(text):
    prompt = f"""Here is the resume: {text}.\nPlease identify and extract the Certifications or Licenses section and return it as a JSON object with the following format:
      {{
        "CertificationsAndLicenses": [
          {{
            "CertificateOrLicense": "string",
            "AwardingOrganization": "string",
            "DateReceived": "string"
          }}
        ]
      }}
      If any value for a key is not available, assign it an empty string (""). The returned result should be in JSON format without anything added.
      """
    return prompt

def create_languages_prompt(text):
    prompt = f"""Here is the resume: {text}.\nPlease identify and extract the Languages section and return it as a JSON object with the following format:
      {{
        "Languages": [
          {{
            "Language": "string",
            "ProficiencyLevel": "string"
          }}
        ]
      }}
      If any value for a key is not available, assign it an empty string (""). The returned result should be in JSON format without anything added.
      """
    return prompt



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
            {{
              "Skill": "string",
              "Level": "string"
            }}
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
      If any value for a key is not available, assign it an empty string (""). The returned result should be in JSON format without anything added.

      For determining the 'Level' for 'TechnicalSkills', follow these guidelines:
      1. If the skill is related to the major studied in 'Education', the level should be 'Intermediate'.
      2. Based on 'WorkExperience':
         - 'Beginner' if less than 2 years of related work experience.
         - 'Intermediate' if 2 to 5 years of related work experience.
         - 'Expert' if more than 5 years of related work experience.
      3. If there is no information related to the skill in 'Education' or 'WorkExperience', assign the level as 'Beginner'.
      """
    return prompt

