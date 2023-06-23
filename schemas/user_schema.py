# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: user_schema 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/11 
"""

from pydantic import BaseModel


class BaseUser(BaseModel):
	email: str


class UserCreate(BaseUser):
	name: str
	password: str

class UserChangeAvatar(BaseUser):
	avatar:str


class User(BaseUser):
	"""
	用户架构
	"""
	id: int
	name: str
	hashed_password: str
	avatar: str

	class Config:
		orm_mode = True
