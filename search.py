from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/', methods=('GET', 'POST'))
def search_display(spots=None):
    # keyword, spot_address, max_travellers, ticket, discount_have, spot_level
    # 搜索展示页面，上面的是搜索的参数，分别是关键词，地址，最大人流量，票价免费与否，优惠政策有没有，几A级景区
    if request.method == 'POST':
        # 数据库筛选数据
        spots = []
        # 把所有符合的数据都传送给前端，所有的
        for i in range(1, 21):
            spots.append({
                'spot-id': i,
                'spot-name': '景区名字' + str(i),
                'spot-img': '景区图片' + str(i),
                'spot-profile': '景区简介' + str(i)
            })

        # 数据处理，不要删除
        spots = [spots[i:i + 5] for i in range(0, len(spots), 5)]

        return render_template('search/search-display.html', spots=spots)
    return render_template('search/search-display.html', spots=spots)
