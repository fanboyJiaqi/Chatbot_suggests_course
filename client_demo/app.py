import streamlit as st
import json
from bs4 import BeautifulSoup
import io
import pandas as pd
from extract_info_from_cv_2 import *
from save_excel import to_excel


def dict_to_html(data_dict):
    html = ""
    for key, value in data_dict.items():
        if isinstance(value, list):  # Kiểm tra nếu giá trị là danh sách (dành cho Skills)
            html += f"<b>{key}:</b><br>"
            html += "<ul>"
            for item in value:
                html += f"<li>{item}</li>"
            html += "</ul>"
        # Kiểm tra nếu giá trị là dictionary (đối với các mục lồng nhau)
        elif isinstance(value, dict):
            html += f"<b>{key}:</b><br>"
            # Đệ quy để xử lý các dictionary lồng nhau
            html += dict_to_html(value)
        else:
            html += f"<b>{key}:</b> {value}<br>"
    return html


def export_to_excel(df):
    output = BytesIO()

    # Sử dụng 'xlsxwriter' engine để tạo file Excel
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
        writer.close()

    return output.getvalue()


def main():
    st.sidebar.header("Upload CV")
    upload_file = st.sidebar.file_uploader("Upload CV", type="pdf")

    if upload_file is not None:
        st.sidebar.success("Uploaded successfully")
        pdf_bytes = upload_file.read()
        answer = extract_resume_from_pdf(pdf_bytes)
        # Assuming answer.content is a JSON string
        data = json.loads(answer.content)

        # Generate HTML for each section
        personal_info_html = dict_to_html(data['PersonalInformation'])

        education_html = ""
        for edu in data['Education']:
            education_html += dict_to_html(edu) + "<br>"

        work_experience_html = ""
        for work in data['WorkExperience']:
            work_experience_html += dict_to_html(work) + "<br>"

        skills_html = ""
        for skill_type, skill_list in data['Skills'].items():
            skills_html += f"<b>{skill_type}:</b><br>"
            skills_html += "<ul>"
            for skill in skill_list:
                skills_html += f"<li>{skill}</li>"
            skills_html += "</ul><br>"

        cer_and_lice_html = ""
        for cal in data['CertificationsAndLicenses']:
            cer_and_lice_html += dict_to_html(cal) + "<br>"

        langs_html = ""
        for lang in data['Languages']:
            langs_html += dict_to_html(lang) + "<br>"

        # HTML code to create a table with borders
        # # html_table = f"""
        # # <style>
        # #     table, th, td {{
        # #         border: 1px solid black;
        # #         border-collapse: collapse;
        # #     }}
        # #     th, td {{
        # #         padding: 10px;
        # #     }}
        # #     th {{
        # #         background-color: #f2f2f2;
        # #     }}
        # # </style>

        # # <table>
        # #     <tr>
        # #         <th>Personal Information</th>
        # #         <th>Education</th>
        # #         <th>Work Experience</th>
        # #         <th>Skills</th>
        # #         <th>Certifications and Licenses</th>
        # #         <th>Languages</th>
        # #     </tr>
        # #     <tr>
        # #         <td>
        # #             {personal_info_html}
        # #         </td>
        # #         <td>
        # #             {education_html}
        # #         </td>
        # #         <td>
        # #             {work_experience_html}
        # #         </td>
        # #         <td>
        # #             {skills_html}
        # #         </td>
        # #         <td>
        # #             {cer_and_lice_html}
        # #         </td>
        # #         <td>
        # #             {langs_html}
        # #         </td>
        # #     </tr>
        # # </table>
        # # """

        # # Display the HTML table in Streamlit
        # st.markdown(html_table, unsafe_allow_html=True)

        combine_df = to_excel(data)

        st.dataframe(combine_df)

        excel_data = export_to_excel(combine_df)

        st.download_button(
            label="Download Excel",
            data=excel_data,
            file_name="resume_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.write("Please upload a CV file to see the details.")


if __name__ == "__main__":
    main()
