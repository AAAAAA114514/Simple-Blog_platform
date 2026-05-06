# Simple\-Blog\_platform 后端 README\.md

\# Simple\-Blog\_platform 后端项目

本项目是 Simple\-Blog\_platform 博客平台的后端服务，基于 FastAPI 开发，提供博客相关的接口服务，支持用户管理、文章发布、数据存储等核心功能，搭配 MySQL 数据库实现数据持久化。

## \#\# 项目简介

用于支撑博客平台的后端接口，负责处理前端请求、业务逻辑处理、数据库交互等，采用 FastAPI 框架实现高效、快速的接口开发，配合 SQLAlchemy 进行ORM映射，保证代码的可维护性和扩展性。

## \#\# 技术栈

- 后端框架：FastAPI

- 服务器：Uvicorn

- ORM框架：SQLAlchemy

- 数据库：MySQL

- 其他依赖：python\-jose（加密）、passlib（密码加密）、python\-multipart（文件上传）

## \#\# 环境依赖

- Python 3\.8\+

- MySQL 5\.7\+ / 8\.0\+

- Git（项目克隆）

## \#\# 安装与运行步骤

### \#\#\# 1\. 克隆项目

```bash
git clone https://github.com/AAAAAA114514/Simple-Blog_platform.git
cd Simple-Blog_platform/backend  # 进入后端目录
```

### \#\#\# 2\. 创建并激活虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# Windows 激活虚拟环境
venv\Scripts\activate

# Mac/Linux 激活虚拟环境
source venv/bin/activate
```

### \#\#\# 3\. 安装依赖包

```bash
pip install fastapi uvicorn sqlalchemy pymysql
pip install python-jose passlib python-multipart
```

### \#\#\# 4\. 配置本地数据库

打开MySQL客户端，执行以下命令创建数据库（编码为utf8mb4，支持所有字符）：

```sql
CREATE DATABASE blog_db DEFAULT CHARACTER SET utf8mb4;
```

根据实际情况，修改项目中数据库配置（如数据库地址、用户名、密码），确保能正常连接数据库。

### \#\#\# 5\. 启动项目

```bash
uvicorn main:app --reload
```

启动成功后，访问 [http://127\.0\.0\.1:8000/docs](http://127.0.0.1:8000/docs) 可查看接口文档（FastAPI自动生成）。

## \#\# 项目结构（简要）

```plain text
backend/
├── venv/          # 虚拟环境目录
├── main.py        # 项目入口文件（接口路由、服务启动）
├── models/        # 数据库模型（SQLAlchemy ORM）
├── routes/        # 接口路由模块
├── crud/          # 数据库增删改查操作
├── schemas/       # 接口请求/响应模型（Pydantic）
└── README.md      # 后端项目说明（本文档）
```

## \#\# 常见问题

- 启动失败提示“数据库连接失败”：检查MySQL是否启动、数据库配置是否正确、blog\_db数据库是否已创建。

- 依赖安装失败：确保Python版本符合要求，可尝试升级pip后重新安装。

- 接口访问404：检查接口路径是否正确，可通过接口文档（/docs）确认接口地址。

## \#\# 开源协议

MIT License

> （注：文档部分内容可能由 AI 生成）
