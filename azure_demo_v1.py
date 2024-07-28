# from langchain.chat_models import AzureChatOpenAI
from langchain_openai import AzureChatOpenAI
# from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = "https://f-gpt-llm.openai.azure.com/"
API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
DEPLOYMENT_NAME = "F-GPT-LLM"

model = AzureChatOpenAI(
    azure_endpoint=BASE_URL,
    openai_api_version="2023-03-15-preview",
    deployment_name=DEPLOYMENT_NAME,
    openai_api_key=API_KEY,
    openai_api_type="azure",
    temperature= 1
)

from langchain_openai import AzureOpenAIEmbeddings

embeddings = AzureOpenAIEmbeddings(
    azure_deployment="F-GPT-Embedding",
    openai_api_version="2023-05-15",
)

# doc_result = embeddings.embed_documents(["this is a test document"])
# print(doc_result[0][:5])