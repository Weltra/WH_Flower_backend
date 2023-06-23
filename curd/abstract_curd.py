# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: abstract_curd 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/11 
"""

from sqlalchemy.orm import Session

from models import abstract_content
from schemas import article_schema


def get_content(db: Session, Abstract_id: int):
	"""
	根据对应的ID来获取详情页的内容
	"""
	return db.query(abstract_content.Article).filter(abstract_content.Article.id == Abstract_id).first()


def update_content(db: Session, Abstract_id: int, content: article_schema.UpdateArticle):
	"""
	根据对应的ID来获取详情页的内容
	"""
	try:
		u_abstract = db.query(abstract_content.Article).filter(abstract_content.Article.id == Abstract_id).first()
		if u_abstract:
			u_abstract.article_content = content.article_content
			db.commit()
			db.close()
			return {"code": "0000", "message": "修改成功"}
		else:
			return {"code": "0001", "message": "参数错误"}
	except ArithmeticError:
		return {"code": "0002", "message": "数据库错误"}


def get_contents(db: Session, skip: int = 0, limit: int = 100):
	"""
	查询所有用户
	"""
	return db.query(abstract_content.Article).offset(skip).limit(limit).all()
