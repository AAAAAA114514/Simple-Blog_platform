1. backend
cd backend
------------------------------
###创建虚拟###
python -m venv venv
venv\Scripts\activate
------------------------------
###安装依赖
pip install fastapi uvicorn sqlalchemy pymysql
pip install python-jose passlib python-multipart
------------------------------
###本地数据库
CREATE DATABASE blog_db DEFAULT
CHARACTER SET utf8mb4;
------------------------------
uvicorn main:app --reload