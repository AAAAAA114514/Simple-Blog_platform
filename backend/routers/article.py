from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Article
from schemas import ArticleCreate

router = APIRouter(prefix="/article", tags=["文章"])

# 发布文章
@router.post("/add")
def add_article(art: ArticleCreate, db: Session = Depends(get_db)):
    new_art = Article(title=art.title, content=art.content, user_id=1)
    db.add(new_art)
    db.commit()
    return {"msg":"发布成功"}

# 获取所有文章
@router.get("/list")
def get_articles(db: Session = Depends(get_db)):
    return db.query(Article).all()