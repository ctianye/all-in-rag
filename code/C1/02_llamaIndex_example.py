import os
# os.environ['HF_ENDPOINT']='https://hf-mirror.com'
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings 
from llama_index.llms.openai_like import OpenAILike
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

#加载环境变量
load_dotenv()

#配置模型
# 使用 AIHubmix
Settings.llm = OpenAILike(
    model="GLM-5.3-Flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    api_base="https://llm.ujn.edu.cn/v1",
    is_chat_model=True
)

# Settings.llm = OpenAI(
#     model="deepseek-chat",
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     api_base="https://api.deepseek.com"
# )
Settings.embed_model = HuggingFaceEmbedding("BAAI/bge-small-zh-v1.5")

#1.数据准备，导入文档
docs = SimpleDirectoryReader(input_files=["../../data/C1/markdown/easy-rl-chapter1.md"]).load_data()

#2.构建索引，向量
index = VectorStoreIndex.from_documents(docs)

#创建查询引擎
query_engine = index.as_query_engine()

#查询引擎的提示词模板
print(query_engine.get_prompts())

#3.进行查询并回答
print(query_engine.query("文中举了哪些例子?"))