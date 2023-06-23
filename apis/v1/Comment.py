# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: Comment 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/12 
"""

from fastapi import APIRouter

commentRouter = APIRouter(tags=['详情页评论区相关'])

@commentRouter.get("/comments", summary="删除评论")
async def get_point():
	"""
	获取评论区内容
	"""
	pass

@commentRouter.post("/add_comment", summary="添加评论")
async def get_point():
	"""
	获取详情页内容
	"""
	pass
