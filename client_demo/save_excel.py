import pandas as pd
import json


def create_personal_info_df(personal_info):
    # Tạo DataFrame với một cột "Personal Information"
    personal_info_df = pd.DataFrame({
        "FullName": [personal_info.get('FullName', '')],
        "DateOfBirth": [personal_info.get('DateOfBirth', '')],
        "Gender": [personal_info.get('Gender', '')],
        "Address": [personal_info.get('Address', '')],
        "PhoneNumber": [personal_info.get('PhoneNumber', '')],
        "Email": [personal_info.get('Email', '')]
    })
    return personal_info_df


def create_education_df(education_list):
    education_rows = []
    for education in education_list:
        education_info = (f"School: {education.get('School', '')}\n"
                          f"Major: {education.get('Major', '')}\n"
                          f"TimePeriod: {education.get('TimePeriod', '')}\n"
                          f"Degree: {education.get('Degree', '')}")
        education_rows.append(education_info)

    education_df = pd.DataFrame({
        "Education": education_rows
    })
    return education_df


def create_workexp_df(workexp_list):
    # Tạo DataFrame với cột "Education"
    workexp_rows = []
    for workexp in workexp_list:
        workexp_rows.append(f"JobTitle: {workexp.get('JobTitle', '')}")
        workexp_rows.append(f"Company: {workexp.get('Company', '')}")
        workexp_rows.append(f"TimePeriod: {workexp.get('TimePeriod', '')}")
        workexp_rows.append(
            f"ResponsibilitiesAndAchievements: {workexp.get('ResponsibilitiesAndAchievements', '')}")
        # Thêm dòng trống để ngăn cách giữa các education entry
        workexp_rows.append("")

    workexp_rows = pd.DataFrame({
        "Work Experience": workexp_rows
    })
    return workexp_rows


def create_skills_df(skills_dict):
    technical_skills = ", ".join(skills_dict.get("TechnicalSkills", []))
    soft_skills = ", ".join(skills_dict.get("SoftSkills", []))

    skills_df = pd.DataFrame({
        "Technical Skills": [technical_skills],
        "Soft Skills": [soft_skills]
    })
    return skills_df


def create_cerandlice_df(cerandlice_list):
    # Tạo DataFrame với cột "Education"
    cerandlice_rows = []
    for cerandlice in cerandlice_list:
        cerandlice_rows.append(
            f"CertificateOrLicense: {cerandlice.get('CertificateOrLicense', '')}")
        cerandlice_rows.append(
            f"AwardingOrganization: {cerandlice.get('AwardingOrganization', '')}")
        cerandlice_rows.append(
            f"DateReceived: {cerandlice.get('DateReceived', '')}")
        # Thêm dòng trống để ngăn cách giữa các education entry
        cerandlice_rows.append("")

    cerandlice_rows = pd.DataFrame({
        "Certifications And Licenses": cerandlice_rows
    })
    return cerandlice_rows


def create_language_df(language_list):
    language_rows = []
    for language in language_list:
        language_rows.append(f"Language: {language.get('Language', '')}")
        language_rows.append(
            f"ProficiencyLevel: {language.get('ProficiencyLevel', '')}")
        # Thêm dòng trống để ngăn cách giữa các education entry
        language_rows.append("")

    language_rows = pd.DataFrame({
        "Languages": language_rows
    })
    return language_rows


def to_excel(data):
    # Tạo DataFrame từ dữ liệu PersonalInformation
    personal_info_df = create_personal_info_df(data['PersonalInformation'])
    education_df = create_education_df(data['Education'])
    workexp_df = create_workexp_df(data['WorkExperience'])
    skills_df = create_skills_df(data['Skills'])
    cerandlice_df = create_cerandlice_df(data['CertificationsAndLicenses'])
    language_df = create_language_df(data['Languages'])

    combined_df = pd.concat([personal_info_df, education_df,
                            workexp_df, skills_df, cerandlice_df, language_df], axis=1)
    return combined_df
