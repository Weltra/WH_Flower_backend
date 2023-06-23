# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: article_schema 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/13 
"""

from pydantic import BaseModel
class Article(BaseModel):
	"""
	详情页内容架构
	"""
	id: int
	name: str
	article_content: str
	panel_imgURL_top: str
	panel_imgURL_bottom: str
	background_image: str
	like_times: int  # 此处为点击喜欢的次数

	class Config:
		orm_mode = True

class UpdateArticle(BaseModel):
	"""
	更新详情页内容架构
	"""
	article_content: str

	class Config:
		orm_mode = True
