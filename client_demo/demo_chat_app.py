import streamlit as st
import os
import sys
import fitz  # PyMuPDF
import json
import time
sys.path.append(os.path.abspath('..'))

from backend_demo.process_infor import extract_skill_from_pdf
from backend_demo.build_learn_path import build_path


def typing_effect(placeholder, message, delay=0.01):
    displayed_message = ""
    for char in message:
        displayed_message += char
        placeholder.markdown(displayed_message + "▌")
        time.sleep(delay)
    placeholder.markdown(displayed_message)

def main():
    upload_file = st.file_uploader("Up load CV", type="pdf")
    text = ""
    if upload_file is not None:
        st.success("Uploaded successfully")
        document = fitz.open(stream=upload_file.read(), filetype="pdf")
        
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text("text")
            if page_num > 0 :
                text += "\n"
        # save_text_to_file(text, "save_text.txt")
        # skills = extract_skill_from_pdf(page_text)
        # st.write(skills)
        ex_skill = extract_skill_from_pdf(text)
        json_data = json.loads(ex_skill.content)
        
        st.write(json_data["skills"])
    # courses = []
    # for item in courses:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])
    if prompt := st.chat_input("Nhập tin nhắn ở đây"):
        st.session_state.messages.append(
            {
                'role': 'user',
                'content' : prompt
            }
        )

        with st.chat_message('user'):
            st.markdown(prompt)
        with st.chat_message('assistant'):
            with st.spinner('Đang soạn thảo...'):
                time.sleep(0.05)
                answers = build_path(prompt)
                placeholder = st.empty()
                typing_effect(placeholder, answers.content)
        st.session_state.messages.append(
            {
                'role': 'assistant',
                'content' : answers.content
            }
        )
        
if __name__ == "__main__":
    main()