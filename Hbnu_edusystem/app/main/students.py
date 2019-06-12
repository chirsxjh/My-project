# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect

user = Blueprint('user',__name__)

@user.route('/index')
def index():
    return render_template('user/index.html')

@user.route('/add')
def add():
    return 'user_add'

@user.route('/show')
def show():
    return 'user_show'