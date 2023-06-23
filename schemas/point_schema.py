# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: point_schema 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/13 
"""

from typing import List

from pydantic import BaseModel


class Point(BaseModel):
	"""
	地图点架构
	"""
	id: int
	name: str
	description: str
	longitude: float
	latitude: float
	imgURL: str
	traffic: str  # 此处为对于地点的描述
	open_time: str
	ticket: str
	flower_class: str

	class Config:
		orm_mode = True


class PointCreate(BaseModel):
	"""
	创建地图点
	"""
	name: str
	description: str
	longitude: float
	latitude: float
	imgURL: str
	traffic: str  # 交通方式
	open_time: str
	ticket: str
	flower_class: str


class MapPoint(BaseModel):
	"""
	地图点架构
	"""
	name: str
	position: List[float]
	description: str
	imgURL: str
	traffic: str  # 交通方式
	open_time: str
	ticket: str
	flower_class: str

	class Config:
		orm_mode = True


class PointList(BaseModel):
	"""
	点集合架构
	"""
	Points: List[Point]

	class Config:
		orm_mode = True


class MapPointList(BaseModel):
	"""
	点集合架构
	"""
	Points: List[MapPoint]

	class Config:
		orm_mode = True
