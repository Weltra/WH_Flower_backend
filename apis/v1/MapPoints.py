# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: mappoints 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/11 
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from curd import point_curd
from schemas import point_schema
from utils.db_connect import get_db

pointRouter = APIRouter(tags=['地图点相关'])


@pointRouter.get("/points/", response_model=point_schema.PointList, summary="在表格中获取所有地图点")
def read_points(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
	pointlist = point_curd.get_points(db, skip=skip, limit=limit)
	return pointlist


@pointRouter.get("/map_points/", response_model=point_schema.MapPointList, summary="获取所有地图点")
def read_map_points(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
	"""
	获取所有展示在地图上的地图点
	"""
	mappoint_list = point_curd.get_mappoints(db, skip=skip, limit=limit)
	return mappoint_list


@pointRouter.post("/search_points/", response_model=point_schema.PointList, summary="关键词搜索")
def search_points(keywords: list, db: Session = Depends(get_db)):
	"""
	获取所有展示在地图上的地图点
	"""
	mappoint_list = point_curd.search_keyword(db, keywords=keywords)
	return mappoint_list


@pointRouter.post("/add_map_point", summary="添加地图点")
async def add_point(point: point_schema.PointCreate, db: Session = Depends(get_db)):
	"""
	在列表中添加新的地图点
	"""
	return point_curd.create_point(db=db, point=point)


@pointRouter.post("/delete_map_point/{point_id}", summary="删除地图点")
async def delete_point(point_id: int, db: Session = Depends(get_db)):
	"""
	删除地图点（单个）
	"""
	return point_curd.delete_point(db=db, point_id=point_id)


@pointRouter.post("/update_map_point/{point_id}", summary="更新地图点")
async def update_point(point: point_schema.Point, point_id: int, db: Session = Depends(get_db)):
	"""
	更新地图点
	"""
	return point_curd.update_point(db=db, point_id=point_id, pointinfo=point)


@pointRouter.get("/points/{point_id}", summary="根据ID获取地图点")
async def get_point(point_id: int, db: Session = Depends(get_db)):
	"""
	更新地图点
	"""
	db_point = point_curd.get_point(db, point_id=point_id)
	if db_point is None:
		raise HTTPException(status_code=404, detail="User not found!")
	return db_point
