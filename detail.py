import pymysql
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, session
)
from travelRecommend.authentic import login_required
from travelRecommend.home import flag_add
import random

bp = Blueprint('detail', __name__, url_prefix='/detail')


@bp.route('/<int:spot_id>')
def spot_detail(spot_id):
    # 景区详情页面，根据spot_id找到相应的景区信息
    conn = pymysql.connect(host='localhost', user='root', password='root', db='recommend')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM travelrecommend WHERE ScenicID=' + str(spot_id))
    temp=cursor.fetchall()
    spot = {
        'spot-name': temp[0][12],
        'spot-img': '景区图片',
        'spot-address': temp[0][1],
        'open-time': temp[0][10],
        'spot-level': temp[0][13]+"A",
        'spot-classify': temp[0][8],
        'serve-phone-num': temp[0][3],
        'complaint-phone-num': temp[0][4],
        'spot-profile': temp[0][7]
    }

    # 根据弹幕的affiliation_id 等于 spot_id返回该景区的弹幕10条
    comments = []
    for i in range(1, 11):
        comments.append({
            'comment-id': 1,  # 评论id
            'affiliation-id': 2,  # 所属位置id
            'author-id': 3,  # 发布者id
            'comment-body': '评论内容'
        })

    # 数据处理，不要删除
    temp_time = 1
    temp_num = 0
    for i in comments:
        i.update({'delay-time': temp_time})
        temp_time += (random.randint(5, 10) / 10.0)
        i.update({'top': str(random.randint(0, 6) * 4) + 'vh'})
        i.update({'right': str(temp_num * 30) + 'vw'})
        temp_num += 1

    # 根据游记的affiliation_id 等于 spot_id返回该景区的游记3条
    notes = []
    for i in range(1, 4):
        notes.append({
            'note-id': 1,  # 评论id
            'affiliation-id': 2,  # 所属位置id
            'author-id': 3,  # 发布者id
            'note-title': '游记标题',
            'note-body': '游记内容'
        })

    # 数据处理，不要删除
    notes = flag_add(notes)

    return render_template(
        'detail/spot-detail.html',
        spot=spot,
        comments=comments,
        notes=notes,
        spot_id=spot_id
    )


@bp.route('/<int:spot_id>/note-create', methods=('GET', 'POST'))
@login_required
# 用户添加的游记数据
def note_create(spot_id):
    if request.method == 'POST':
        # 获取用户输入的游记数据
        note_title = request.form['note-title']
        note_body = request.form['note-body']
        error = None

        # 逻辑处理，检查输入数据是否合法
        if not note_title:
            error = '请输入标题'

        if not note_body:
            error = '请输入内容'

        if error is not None:
            # 不合法则报错，并把报错信息传送到前端flash(error)
            flash(error)

        else:
            return redirect(url_for('detail.spot_detail', spot_id=spot_id))

    return render_template('detail/note-create.html', spot_id=spot_id)


@bp.route('/post-comment', methods=('POST',))
@login_required
def post_comment():
    # 新添加的该景区的弹幕数据，保存到数据库
    comment_body = request.form['comment-body']
    author_id = request.form['author-id']
    affiliation_id = request.form['affiliation-id']
    # 数据库处理 保存数据
    return redirect(url_for('detail.spot_detail', spot_id=affiliation_id))
