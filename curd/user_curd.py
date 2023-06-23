# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: user_curd 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/11 
"""

from sqlalchemy.orm import Session

from models import model
from schemas import user_schema


def get_user(db: Session, user_id: int):
	"""
	根据用户ID来获取用户
	"""
	return db.query(model.User).filter(model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
	"""
	根据邮箱在数据库中查询是否有相关的用户
	"""
	return db.query(model.User).filter(model.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
	"""
	查询所有用户
	"""
	return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):
	"""
	创建用户
	"""
	fake_hashed_password = user.password + "notreallyhashed"
	default_avatar = 'https://picture-tjl.oss-cn-hangzhou.aliyuncs.com/WuHan_Flower/avatars/20230514144252.png'
	db_user = model.User(email=user.email, hashed_password=fake_hashed_password, name=user.name, avatar=default_avatar)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user


def delete_user(db: Session, user_id: int):
	"""
	删除用户
	"""
	try:
		d_user = db.query(model.User).filter(model.User.id == user_id).first()
		if d_user:
			db.delete(d_user)
			db.commit()
			db.close()
			return {"code": "0000", "message": "删除成功"}
		else:
			return {"code": "0001", "message": "参数错误"}
	except ArithmeticError:
		return {"code": "0002", "message": "数据库错误"}


def update_user(db: Session, user: user_schema.UserCreate, user_id: int):
	"""
	更新用户信息
	"""
	try:
		u_user = db.query(model.User).filter(model.User.id == user_id).first()
		if u_user:
			fake_hashed_password = user.password + "notreallyhashed"
			u_user.name = user.name
			u_user.email = user.email
			u_user.hashed_password = fake_hashed_password
			db.commit()
			db.close()
			return {"code": "0000", "message": "修改成功"}
		else:
			return {"code": "0001", "message": "参数错误"}
	except ArithmeticError:
		return {"code": "0002", "message": "数据库错误"}


def update_user_avatar(db: Session, user: user_schema.UserChangeAvatar):
	"""
	更新用户信息
	"""
	try:
		u_user = db.query(model.User).filter(model.User.email == user.email).first()
		print(u_user)
		if u_user:
			u_user.avatar = user.avatar
			db.commit()
			db.close()
			return {"code": "0000", "message": "修改成功"}
		else:
			return {"code": "0001", "message": "参数错误"}
	except ArithmeticError:
		return {"code": "0002", "message": "数据库错误"}
