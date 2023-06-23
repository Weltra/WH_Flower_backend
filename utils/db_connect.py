# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: db_connect 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/16 
"""

# Dependency
from database.database import SessionLocal


def get_db():
	"""
	连接数据库
	"""
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
