import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from azure_demo_v1 import *
from backend_demo.get_data import *

def build_path(skill):
    courses = get_Query(skill)
    prompt = f"Bạn là một chuyên gia tư vấn học tập. Nhiệm vụ của bạn là xây dựng lộ trình học tập tối ưu cho một người đi làm để phát triển các kỹ năng hiện có của họ.\
            Dưới đây là danh sách các kỹ năng hiện có của người này và danh sách các khóa học cùng với nội dung của chúng.\
            Kỹ năng hiện có: {skill}\
            Danh sách khóa học và nội dung:\
            {courses}\
            Không sử dụng bất kỳ thông tin nào khác ngoài những khóa học được cung cấp.\
            Hãy xây dựng một lộ trình học tập chi tiết chỉ dựa vào danh sách khóa học được cung cấp ở trên, bao gồm:\
            1. Thứ tự các khóa học nên học có cấp độ khó từ thấp đến cao\
            2. Thời gian dự kiến để hoàn thành mỗi khóa học\
            3. Những kỹ năng và thành tựu mà người học nhận được mỗi khi họ hoàn thành các khóa học trong lộ trình\
            4. Đánh giá của những người học trước đối với khóa học\
            5. Đường dẫn đến khóa học\
            Lưu ý:\
            - Chỉ ưu tiên các khóa học có mức đánh giá của người học trước cao.\
            - Hãy sắp xếp các khóa học theo thứ tự sao cho tối ưu nhất để phát triển các kỹ năng hiện có.\
            - Cung cấp giải thích ngắn gọn cho mỗi lựa chọn của bạn.\
            Lộ trình học tập:"
    llm = model
    learn_path = llm.invoke(prompt)
    return learn_path

def save_text_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

path_learn = build_path("C++") 
save_text_to_file(str(path_learn), "learn_path_demo.txt")