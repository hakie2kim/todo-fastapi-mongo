from pymongo import MongoClient

import os
from dotenv import load_dotenv

import urllib.parse

# .env 파일에서 환경 변수 로드
load_dotenv()
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

client = MongoClient(f"mongodb+srv://{urllib.parse.quote_plus(db_user)}:{urllib.parse.quote_plus(db_password)}@cluster0.w1u8l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
db = client.todo_db # db connected to client
collection_name = db["todo_collection"]