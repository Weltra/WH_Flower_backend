# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: user 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/11 
"""
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from curd import user_curd
from schemas import user_schema
from utils.db_connect import get_db

userRouter = APIRouter(tags=['用户相关'])


@userRouter.post("/register/", response_model=user_schema.User, summary="用户注册")
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
	"""
	创建用户
	"""
	db_user = user_curd.get_user_by_email(db, email=user.email)
	if db_user:
		raise HTTPException(status_code=400, detail="Email already registered")
	return user_curd.create_user(db=db, user=user)


@userRouter.get("/users/", response_model=List[user_schema.User], summary="获取全部的用户列表")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
	"""
	获取全部用户
	"""
	users = user_curd.get_users(db, skip=skip, limit=limit)
	return users


@userRouter.get("/users/{user_id}", response_model=user_schema.User, summary="根据用户ID来获取用户")
def read_user(user_id: int, db: Session = Depends(get_db)):
	"""
	详情页用到
	"""
	db_user = user_curd.get_user(db, user_id=user_id)
	if db_user is None:
		raise HTTPException(status_code=404, detail="User not found!")
	return db_user


@userRouter.post("/users/{user_id}", summary="根据用户ID删除用户")
def delete_user(user_id: int, db: Session = Depends(get_db)):
	"""
	根据用户ID删除用户（表格中管理用户时使用）
	"""
	return user_curd.delete_user(db=db, user_id=user_id)


@userRouter.post("/update_user_info/{user_id}", summary="更新用户信息")
async def update_user(user_id: int, user: user_schema.UserCreate, db: Session = Depends(get_db)):
	"""
	更新用户信息页面API
	"""
	db_user = user_curd.get_user_by_email(db, email=user.email)
	if db_user:
		if db_user.id == user_id:
			return user_curd.update_user(db=db, user_id=user_id, user=user)
		else:
			raise HTTPException(status_code=400, detail="Email already registered!")
	return user_curd.update_user(db=db, user_id=user_id, user=user)


@userRouter.post("/update_user_avatar/", summary="更新用户头像")
async def update_user(user: user_schema.UserChangeAvatar, db: Session = Depends(get_db)):
	"""
	更新用户信息页面API
	"""
	return user_curd.update_user_avatar(db=db, user=user)


@userRouter.get("/login/", summary="用户登录")
async def user_login(email: str, password: str, db: Session = Depends(get_db)):
	"""
	用户登录API
	"""
	db_user = user_curd.get_user_by_email(db, email)
	hash_password = password + 'notreallyhashed'
	if db_user is None:
		raise HTTPException(status_code=404, detail="User not found!")
	if hash_password == db_user.hashed_password:
		return db_user
	else:
		return {"code": 501, "message": "密码错误！"}


@userRouter.post("/delete_user/{user_id}", summary="删除用户")
async def delete_point(user_id: int, db: Session = Depends(get_db)):
	"""
	删除用户
	"""
	return user_curd.delete_user(db=db, user_id=user_id)
