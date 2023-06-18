from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, session
)
from travelRecommend.authentic import login_required
import string
import pymysql
bp = Blueprint('account', __name__, url_prefix='/account')


@bp.route('/')
@login_required
def user_space():
    # local_page是前端需要的数据，不要删除
    local_page = int(request.args.get('local_page', 1))
    # 返回用户信息
    user = {
        'user-id': session.get('user-id'),
        'user-name': '用户姓名',
        'user-birth': '用户生日',
        'user-gender': '用户性别',
        'user-address': '用户地址',
        'user-prefer': '用户偏好',
        'user-sign': '用户个性签名'
    }
    # 返回游记信息  要返回该用户的所有游记， 所有
    notes = []
    for i in range(1, 16):
        notes.append({
            'note-id': 1,
            'affiliation-id': 2,  # 所属id
            'note-title': '游记标题' + str(i),
            'note-body': '游记内容' + str(i)
        })
    # 游记信息的逻辑处理，不要删除
    total_notes = len(notes)
    notes = [notes[i:i + 5] for i in range(0, len(notes), 5)]
    if local_page > len(notes):
        local_page = len(notes)
    elif local_page < 1:
        local_page = 1

    return render_template('account/user-space.html', notes=notes[local_page - 1],
                           user=user, local_page=local_page, total_page=len(notes), total_notes=total_notes)


@bp.route('/user-edit', methods=('GET', 'POST'))
@login_required
# 用户信息编辑页面
def user_edit():
    user_id = session.get('user-id')
    if request.method == 'POST':
        user_birth = request.form['user-birth']
        user_gender = request.form['user-gender']
        user_address = request.form['user-address']
        user_sign = request.form['user-sign']
        user_prefer = [item for item in request.form.getlist('user-prefer')]
        # 字符串列表
        user_prefer=str(",".join(user_prefer))
        conn = pymysql.connect(host='localhost', user='root', password='root', db='recommend',autocommit=True)
        cursor = conn.cursor()
        input_temp="UPDATE registerinfo SET userbirth='"+user_birth+"',usergender='"+user_gender+"',useraddress='"+user_address+"',usersign='"+user_sign+"',userprefer='"+user_prefer+"' WHERE username="+str(user_id)
        cursor.execute(input_temp)
        cursor.close()
        # 检查输入信息是否合法
        error = None
        if not user_birth:
            error = '请选择生日'
        if not user_gender:
            error = '请选择性别'
        if not user_address:
            error = '请选择地址'
        if not user_sign:
            user_sign = '留下点什么吧~'
        if not user_prefer:
            error = '请选择偏好'
        if error is not None:
            flash(error)
        else:
            #存数据时用户偏好要进行的操作：
            user_prefer = ','.join(user_prefer)
            #修改数据库的USER，把东西保存进去
            #取数据时用户偏好要进行的操作：
            user_prefer = user_prefer.split(',')
            # 数据库操作
            # 保存信息
            # return redirect(url_for('account.user_space'))
            return redirect(url_for('home'))

    return render_template('account/user-edit.html')


def get_note(note_id):
    # 根据note_id返回相应的游记
    note = {
        'note-id': 1,
        'author-id': 2,
        'note-title': '游记标题' + str(note_id),
        'note-body': '游记内容' + str(note_id)
    }
    return note


@bp.route('/note-edit', methods=('GET', 'POST'))
@login_required
# 修改已有游记
def note_edit():
    # 接受数据
    local_page = int(request.args.get('local_page'))
    note_id = int(request.args.get('note_id'))
    note = get_note(note_id)

    if request.method == 'POST':
        note_title = request.form['note-title']
        note_body = request.form['note-body']
        error = None

        if not note_title:
            error = '请输入标题'

        if not note_body:
            error = '请输入内容'

        if error is not None:
            flash(error)
        else:
            # 数据库保存修改后的游记
            return redirect(url_for('account.user_space', local_page=local_page))

    return render_template('account/note-edit.html', note=note, local_page=local_page)


@bp.route('/note-delete')
@login_required
# 游记删除
def note_delete():
    note_id = int(request.args.get('note_id'))
    get_note(note_id)
    # 删除数据库数据
    return redirect(url_for('account.user_space'))


@bp.route('/jump-to', methods=('POST',))
@login_required
# 前端需要的函数
def jump_to():
    jump_page = request.form['jump-page']
    return redirect(url_for('account.user_space', local_page=jump_page))


@bp.route('/flip')
@login_required
# 前端需要的函数
def flip():
    local_page = int(request.args.get('local_page', 1))
    next_page = bool(request.args.get('next_page', False))
    if next_page:
        return redirect(url_for('account.user_space', local_page=local_page+1))
    return redirect(url_for('account.user_space', local_page=local_page-1))
