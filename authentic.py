from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, session, g
)
import functools
import pymysql
import numpy as np

bp = Blueprint('authentic', __name__, url_prefix='/authentic')


@bp.route('/register', methods=('POST', 'GET'))
def register():
    # 用户注册界面
    if request.method == 'POST':
        error = None
        user_name = request.form['user-name']
        password = request.form['password']
        # 检查用户注册的账号有没有冲突等等问题
        conn = pymysql.connect(host='localhost', user='root', password='root', db='recommend',autocommit=True)
        cursor = conn.cursor()
        cursor.execute('SELECT username FROM registerinfo')
        user =  cursor.fetchall()
        user = [i for j in user for i in j[0].split(',')]
        user = list(filter(None, user))
        if not user_name:
            error = '请输入用户名'
        elif not password:
            error = '请输入密码'
        elif error is None:
            for check in range(len(user)):
                if user[check] == user_name:
                    error = '用户名冲突'
        if error is None:
            # 没有错误就保存注册信息
            sql_in="insert into registerinfo (username, password) VALUES ('"+user_name+"','"+password+"')"
            print(sql_in)
            cursor.execute(sql_in)
            return redirect(url_for('authentic.log_in'))
        flash(error)
    return render_template('authentic/log-in.html')


@bp.route('/log-in', methods=('POST', 'GET'))
def log_in():
    # 用户登录界面
    if request.method == 'POST':
        error = None
        user_name = request.form['user-name']
        password = request.form['password']
        conn = pymysql.connect(host='localhost', user='root', password='root', db='recommend')
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM registerinfo WHERE username='+user_name)
        user = cursor.fetchall()
        password_user = [i for j in user for i in j[0].split(',')]
        if str(password_user[0]) == str(password):
            pass
        else:
            error = '密码或账户错误'
        # 检查登录是否合法
        if not user_name:
            error = '请输入用户名'
        elif not password:
            error = '请输入密码'
        if error is None:
            # 返回用户信息
            # 浏览器保存登录状态
            cursor.execute('SELECT username FROM registerinfo WHERE username='+user_name)
            user_temp=cursor.fetchall()
            session.clear()
            session['user-id'] = str(user_temp[0][0])
            cursor.execute('SELECT userprefer FROM registerinfo WHERE username=' + user_name)
            user_per=cursor.fetchall()
            print(user_temp[0][0],user_per[0][0])
            # 检查信息是否完整
            if not user_temp[0][0] or not user_per[0][0]:
                return redirect(url_for('account.user_edit'))
            return redirect(url_for('home'))
        flash(error)
    return render_template('authentic/log-in.html')


@bp.before_app_request
# 运行在所有东西的前面，检查浏览器是否包含登录信息
def load_logged_in_user():
    user_id = session.get('user-id')

    # 使用g来存储数据
    if user_id is None:
        g.user = None
    else:
        # 从数据库里面返回用户信息
        g.user = {
            'user-id': 1,
            'user-name': '用户名'
        }


@bp.route('/log-out')
def log_out():
    session.clear()
    return redirect(url_for('home'))


@bp.route('/')
def authentic():
    redirect('authentic.log_in')


def login_required(view):
    # 检查是否登录
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('authentic.log_in'))

        return view(**kwargs)

    return wrapped_view
