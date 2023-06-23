# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: Abstract 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/12 
"""

from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import article_schema
from utils.db_connect import get_db
from curd import abstract_curd

abstractRouter = APIRouter(tags=['详情页相关'])


@abstractRouter.get("/abstract_content/{abstract_id}", summary="根据详情页的ID获取详情页内容", response_model=article_schema.Article)
async def get_content(abstract_id: int, db: Session = Depends(get_db)):
	"""
	根据ID获取详情页内容
	"""
	return abstract_curd.get_content(db=db, Abstract_id=abstract_id)


@abstractRouter.post("/update_abstract_content/{abstract_id}", summary="更改详情页内容")
async def update_content(abstract_id: int, contend: article_schema.UpdateArticle, db: Session = Depends(get_db)):
	"""
	更改详情页内容(详情页文章部分)
	"""
	return abstract_curd.update_content(db=db, Abstract_id=abstract_id, content=contend)


@abstractRouter.get("/get_abstract_contents/", response_model=List[article_schema.Article], summary="获取全部详情页内容")
async def get_content(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
	"""
	获取全部详情页内容
	"""
	abstracts = abstract_curd.get_contents(db, skip=skip, limit=limit)
	print(abstracts)
	return abstracts
