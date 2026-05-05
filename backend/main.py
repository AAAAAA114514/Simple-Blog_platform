from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from routers import user, article

# 创建数据表
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="个人博客后端")

# 跨域允许前端访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(user.router)
app.include_router(article.router)

@app.get("/")
def root():
    return {"msg":"博客后端服务启动成功"}