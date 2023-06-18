from flask import (
    Blueprint, render_template, request, redirect, url_for, g, session
)
from travelRecommend.authentic import login_required
import random
import pymysql
import pandas as pd


bp = Blueprint('home', __name__)


@bp.route('/')
@login_required
def home():
    def recommend_1(man_image):
        count = {}
        result_1 = []
        conn = pymysql.connect(host='localhost', user='root', password='root', db='recommend')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM travelRecommend')
        data0 = cursor.fetchall()
        data = pd.DataFrame(data0)
        for i in range(len(data)):
            data1 = []
            lst = []
            data1 = data.iloc[i, 9].split(",")
            lst = list(filter(None, data1))
            count[data.iloc[i, 0]] = len(set(lst) & set(man_image)) * 100  # 计算用户喜好标签和景区标签的相似性
            count[data.iloc[i, 0]] += int(data.iloc[i, 15]) * 10  # 增加景区承载量作为权重，提高旅游体验，尽量匹配承载量大的景区
            count[data.iloc[i, 0]] += int(data.iloc[i, 13])  # 对评级高的景区适当增加权重，提高被匹配的几率
        sorted_dict = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))  # 排序
        sorted_dict_min = list(sorted_dict.keys())
        result_1 += sorted_dict_min[:5]
        vlt = 0
        while True:  # 将产生的超出预计推荐数部分添加入推荐列表
            if list(sorted_dict.values())[4 + vlt] == list(sorted_dict.values())[5 + vlt]:
                result_1.append(sorted_dict_min[5 + vlt])
                vlt += 1
            elif list(sorted_dict.values())[4 + vlt] != list(sorted_dict.values())[5 + vlt]:
                break
            pass
        result = random.sample(result_1, 5)
        return result

    user_id = session['user-id']
    # 获取推荐的景点的数据，一共5条
    recommend_spot = []
    conn = pymysql.connect(host='localhost', user='root', password='root', db='recommend')
    cursor = conn.cursor()
    cursor.execute('SELECT userprefer FROM registerinfo WHERE username=' + user_id)
    man_image = cursor.fetchall()
    man_image = [i for j in man_image for i in j[0].split(',')]
    x = recommend_1(man_image)
    # recommand_1(list_man_image[一些偏好])
    for i in range(0, 5):
        # 景点图片，景点名字，景点描述，景点id
        cursor.execute('SELECT NameOfTheScenicSpot FROM travelrecommend WHERE ScenicID=' +x[i])
        spot_name = cursor.fetchall()
        spot_name = [i for j in spot_name for i in j[0].split(',')]
        cursor.execute('SELECT TypeOfScenicSpot FROM travelrecommend WHERE ScenicID='+x[i])
        spot_class = cursor.fetchall()
        spot_class = [i for j in spot_class for i in j[0].split(',')]
        spot_class = list(filter(None, spot_class))
        spot_class = ' '.join(spot_class)
        recommend_spot.append({
            'spot-id': x[i],
            'spot-name':str(spot_name[0]),
            'spot-img': '景点图片' + str(i),
            'spot-profile': '景点类型' + spot_class
        })
    conn.close()
    # 获取最近的景点的数据，一共3条
    near_by_spot = []
    for i in range(1, 4):
        # 景点图片，景点名字，景点描述，景点id
        near_by_spot.append({
            'spot-id': i,
            'spot-name': '景点名字' + str(i),
            'spot-img': '景点图片' + str(i),
            'spot-profile': '景点简介' + str(i)
        })

    # 获取主页弹幕数据，一共10条，主页弹幕的所属id为0，作者id为0
    comments = []
    for i in range(1, 11):
        comments.append({
            'comment-id': 1,  # 评论id
            'affiliation-id': 2,  # 所属位置id
            'author-id': 3,  # 发布者id
            'comment-body': '评论内容'
        })

    # 对主页弹幕数据进行处理的函数，不要删除
    temp_time = 1
    temp_num = 0
    for i in comments:
        i.update({'delay-time': temp_time})
        temp_time += (random.randint(5, 10) / 10.0)
        i.update({'top': str(random.randint(0, 7)*4) + 'vh'})
        i.update({'right': str(temp_num*30) + 'vw'})
        temp_num += 1

    # 获取三篇游记，放在主页
    notes = []
    for i in range(1, 4):
        # 游记id，用户id，游记标题，游记内容
        notes.append({
            'note-id': 1,  # 评论id
            'affiliation-id': 2,  # 所属位置id
            'author-id': 3,  # 发布者id
            'note-title': '游记标题',
            'note-body': '游记内容'
        })

    # 对游记数据进行处理的函数，不要删除
    notes = flag_add(notes)

    # 传送数据给前端模板，前面的时形参，后面是实参
    return render_template(
        'home/home-page.html',
        recommend_spot=recommend_spot,
        near_by_spot=near_by_spot,
        comments=comments,
        notes=notes
    )


@bp.route('/post-comment', methods=('POST',))
def post_comment(affiliation_id=0, author_id=0):
    # 用户在主页发送的弹幕数据，affiliation_id 和 author_id代表着弹幕是主页的
    comment_body = request.form['comment-body']
    # 数据库处理 保存数据
    return redirect(url_for('home'))


# 游记数据处理函数， 不要删除
def flag_add(notes):
    flag = True
    for dic in notes:
        if flag:
            dic.update({'flag': flag})
            flag = not flag
        else:
            dic.update({'flag': flag})
            flag = not flag
    return notes
