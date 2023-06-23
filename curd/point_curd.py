# -*- coding: utf-8 -*-
"""
PROJECT_NAME: backend 
FILE_NAME: point_curd 
AUTHOR: welt 
E_MAIL: tjlwelt@foxmail.com
DATE: 2023/5/11 
"""
from sqlalchemy import or_
from sqlalchemy.orm import Session

from models import model
from schemas import point_schema


def get_points(db: Session, skip: int = 0, limit: int = 100):
	"""
	查询所有地图点
	"""
	points = db.query(model.Point).offset(skip).limit(limit).all()
	pointlist = {"Points": points}
	return pointlist


def search_keyword(db: Session, keywords):
	"""
	查询所有地图点
	"""
	rule = or_(*[model.Point.name.like('%' + w + '%') for w in keywords])
	rule1 = or_(*[model.Point.flower_class.like('%' + w + '%') for w in keywords])
	q_1 = db.query(model.Point).filter(rule)
	q_2 = db.query(model.Point).filter(rule1)
	points = q_1.union(q_2).all()
	pointlist = {"Points": points}
	return pointlist


def get_mappoints(db: Session, skip: int = 0, limit: int = 100):
	"""
	查询所有地图点
	"""
	points = db.query(model.Point).offset(skip).limit(limit).all()
	print(points)
	map_points = []
	for point in points:
		mappoint = {
			'name': '',
			'position': [],
			'description': '',
			'imgURL': '',
			'traffic': '',
			'open_time': '',
			'ticket': '',
			'flower_class': ''
		}
		position = []
		position.clear()
		position.append(point.longitude)
		position.append(point.latitude)
		mappoint['name'] = point.name
		mappoint['position'] = position
		mappoint['description'] = point.description
		mappoint['imgURL'] = point.imgURL
		mappoint['traffic'] = point.traffic
		mappoint['open_time'] = point.open_time
		mappoint['ticket'] = point.ticket
		mappoint['flower_class'] = point.flower_class
		map_points.append(mappoint)
	mappointlist = {"Points": map_points}
	return mappointlist


def create_point(db: Session, point: point_schema.PointCreate):
	"""
	添加新的地图点
	"""
	name = point.name
	description = point.description
	longitude = point.longitude
	latitude = point.latitude
	imgURL = point.imgURL
	traffic = point.traffic  # 此处为对于地点的描述
	open_time = point.open_time
	ticket = point.ticket
	flower_class = point.flower_class
	db_point = model.Point(name=name, description=description, longitude=longitude, latitude=latitude, imgURL=imgURL,
	                       traffic=traffic, open_time=open_time, ticket=ticket, flower_class=flower_class)
	db.add(db_point)
	db.commit()
	db.refresh(db_point)
	return db_point


def delete_point(db: Session, point_id: int):
	"""
	根据编号删除地图点
	"""
	db_point = db.query(model.Point).filter(model.Point.id == point_id).delete()
	db.commit()
	return db_point


def update_point(pointinfo: point_schema.Point, db: Session, point_id: int):
	"""
		更新地图点信息
	"""
	try:
		u_point = db.query(model.Point).filter(model.Point.id == point_id).first()
		if u_point:
			u_point.name = pointinfo.name
			u_point.description = pointinfo.description
			u_point.longitude = pointinfo.longitude
			u_point.latitude = pointinfo.latitude
			u_point.imgURL = pointinfo.imgURL
			u_point.traffic = pointinfo.traffic
			u_point.open_time = pointinfo.open_time
			u_point.ticket = pointinfo.ticket
			u_point.flower_class = pointinfo.flower_class
			db.commit()
			db.close()
			return {"code": "0000", "message": "修改成功"}
		else:
			return {"code": "0001", "message": "参数错误"}
	except ArithmeticError:
		return {"code": "0002", "message": "数据库错误"}


def get_point(db: Session, point_id: int):
	return db.query(model.Point).filter(model.Point.id == point_id).first()
