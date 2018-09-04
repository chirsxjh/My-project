# flask_sqlalchemy学习
---
```
# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 创建flask对象
app = Flask(__name__)
# 创建数据库模型
basedir = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite') #配置flask的地址
db = SQLAlchemy(app) # 初始化数据库


class User(db.Model): # 创建User表
    id = db.Column(db.Integer, primary_key=True) # 创建id列，并设置为主键
    username = db.Column(db.String(80), unique=True) # 创建username列，设置为不可重复
    email = db.Column(db.String(120), unique=True) # 创建email列，设置为不可重复

    def __init__(self, username, email): # 插入新值的方法
        self.username = username
        self.email = email

    def __repr__(self): # 输出的格式
        return '<User %r>' % self.username
```
### 创建表
1. 引入SQLAlchemy并绑定到app上  
2. class name 是创建表，必须继承db.Model类 
3. db.Column用来创建列 
4. __init__用来创建插入的方法 
5. __repr__用来控制输出的格式
### 数据库数据类型
类型	            描述  
Integer 	    整形  
String (size)	字符串
Text	        文本  
DateTime	    python datetime对应的时间  
Float	        浮点  
Boolean	        布尔  
PickleType	    python 内存对象  
LargeBinary	    二进制数据  