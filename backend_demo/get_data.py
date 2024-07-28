import chromadb
from chromadb.utils import embedding_functions
import sys
import os
import chromadb.utils.embedding_functions as embedding_functions

# google_ef  = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key="AIzaSyDn5u_0oaOfJCOfEWYvf0ANJOkezPqqsQk")

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from azure_demo_v1 import embeddings

client = chromadb.PersistentClient(path="d_b")
embeddings = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

db_udemy = client.get_collection(name="B6_collection", embedding_function=embeddings)
db_cosera = client.get_collection(
    name="B6_collection_cosera", embedding_function=embeddings
)
db_skillshare = client.get_collection(
    name="B6_collection_skillshare", embedding_function=embeddings
)
db_edx = client.get_collection(name="B6_collection_edx", embedding_function=embeddings)


def get_Query(skill):
    query = f"Provide courses in increasing levels of {skill}"
    results_udemy = db_udemy.query(query_texts=[query], n_results=5)
    results_cosera = db_cosera.query(query_texts=[query], n_results=5)
    result_skillshare = db_skillshare.query(query_texts=[query], n_results=5)
    result_edx = db_edx.query(query_texts=[query], n_results=5)
    list_courses = []
    for i in range(5):
        tam_udemy = f"{results_udemy['documents'][0][i]} have {results_udemy['metadatas'][0][i]}"
        tam_cosera = f"{results_cosera['documents'][0][i]} have {results_cosera['metadatas'][0][i]}"
        tam_skillshare = f"{result_skillshare['documents'][0][i]} have {result_skillshare['metadatas'][0][i]}"
        tam_edx = f"{result_edx['documents'][0][i]} have {result_edx['metadatas'][0][i]}"
        list_courses.append(tam_udemy)
        list_courses.append(tam_cosera)
        list_courses.append(tam_skillshare)
        list_courses.append(tam_edx)
    return list_courses

# print(get_Query("Java"))
class GeminiEmbeddingFunction(EmbeddingFunction):
 
    """
    Sử dụng API Gemini AI để truy xuất tài liệu.

    Lớp này mở rộng lớp EmbeddingFunction và triển khai phương thức __call__
    để tạo phần embedding cho một bộ tài liệu nhất định bằng API Gemini AI.

    Tham số:
    - input (Documents): Tập hợp các tài liệu được embedding.

    Trả về:
    - Embeddings: Các phần embedding được tạo cho các tài liệu đầu vào.
    """
    def __call__(self, input: Documents) -> Embeddings:
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            raise ValueError("Gemini API Key not provided. Please provide GEMINI_API_KEY as an environment variable")
        genai.configure(api_key=gemini_api_key)
        model = "models/embedding-001"
        title = "Custom query"
        return genai.embed_content(model=model,
                                    content=input,
                                    task_type="retrieval_document",
                                    title=title)["embedding"]