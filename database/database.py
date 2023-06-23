# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: connection 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/11 
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库访问地址
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# 启动引擎
engine = create_engine(
	SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# 启动会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 数据模型的基类
Base = declarative_base()
