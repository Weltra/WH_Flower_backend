# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: main 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/11 
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW

from apis.v1 import Abstract
from apis.v1 import MapPoints
from apis.v1 import User
from database.database import engine
from models import abstract_content, model

app = FastAPI()

# 设置一个首页
@app.get('/')
async def welcome() -> dict:
	return {"message": "Welcome to my Page"}


# 跨域处理
app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:8080", "http://localhost:8081"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# 在数据库中生成表结构
model.Base.metadata.create_all(bind=engine)
abstract_content.Base.metadata.create_all(bind=engine)

# 添加FastAPI的API路由
app.include_router(User.userRouter)
app.include_router(MapPoints.pointRouter)
app.include_router(Abstract.abstractRouter)

if __name__ == '__main__':
	uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True)
