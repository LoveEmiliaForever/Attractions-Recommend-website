import os
from flask import Flask
from . import home, authentic, detail, account, search


def create_app(test_config=None):
    # 创建Flask的实例app
    # __name__是当前Python包的名字，app需要知道路径而__name__可以告诉他
    # instance_relative_config告诉app配置文件和实例文件夹是相对关系
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping设置一些默认设置
    app.config.from_mapping(
        # 密钥
        SECRET_KEY='dd9755eaa1ae9b97c11619e2ad7cb6dc1b408769de5d68fd0083cafc4a3ed27c',
        # 设置数据库文件存放位置
        # app.instance_path是Flask选择的实例文件夹，不一定创建了，下面会检查
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # 如果实例文件夹存在，app会从config.py拿设置值来覆盖默认值
        app.config.from_pyfile('config.py', silent=True)
    else:
        # from_mapping使用test_config来设置app的config,这有利于独立出不同设置文件
        app.config.from_mapping(test_config)

    try:
        # 检查app.instance_path这个实例文件夹存在与否
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(home.bp)
    app.register_blueprint(authentic.bp)
    app.register_blueprint(account.bp)
    app.register_blueprint(detail.bp)
    app.register_blueprint(search.bp)
    app.add_url_rule('/', endpoint='home')

    return app
