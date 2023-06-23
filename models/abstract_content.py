# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: abstract_content 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/11 
"""

from sqlalchemy import Column, Integer, String, Text

from database.database import Base

class Article(Base):
	"""
	详情页内容存储表
	"""
	__tablename__ = "article"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	article_content = Column(Text, index=True)
	panel_imgURL_top = Column(String, index=True)
	panel_imgURL_bottom = Column(String, index=True)
	background_image = Column(String, index=True)
	like_times = Column(Integer, index=True)