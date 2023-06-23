# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: model
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/11 
"""

# models.py
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy import Table
from sqlalchemy.orm import relationship

from database.database import Base


class User(Base):
	"""
	用户表
	"""
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	hashed_password = Column(String)
	email = Column(String, unique=True, index=True)
	name = Column(String, index=True)
	avatar = Column(String, index=True)
	points = relationship('Point', secondary='user_points', back_populates='users')


class Point(Base):
	"""
	地图点表
	"""
	__tablename__ = "points"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	description = Column(String, index=True)
	longitude = Column(Float, index=True)
	latitude = Column(Float, index=True)
	imgURL = Column(String, index=True)
	traffic = Column(String, index=True)
	open_time = Column(String, index=True)
	ticket = Column(String, index=True)
	flower_class = Column(String, index=True)
	users = relationship('User', secondary='user_points', back_populates='points')


user_points = Table('user_points', Base.metadata,
                    Column('point_id', ForeignKey('points.id'), primary_key=True),
                    Column('user_id', ForeignKey('users.id'), primary_key=True))
