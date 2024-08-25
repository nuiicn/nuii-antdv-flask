from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    CORS(app, supports_credentials=True)

    # blueprint
    from app.Controllers.AuthController import auth
    app.register_blueprint(auth, url_prefix='/api/auth')

    from app.Controllers.UserController import user
    app.register_blueprint(user, url_prefix='/api/user')

    from app.Controllers.RoleController import role
    app.register_blueprint(role, url_prefix='/api/role')

    from app.Controllers.PermissionController import permission
    app.register_blueprint(permission, url_prefix='/api/permission')

    from app.Controllers.DepartmentController import department
    app.register_blueprint(department, url_prefix='/api/department')

    return app

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import environment as e
# from app.env import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, UPLOAD_FOLDER, MAX_CONTENT_LENGTH
# import os, json
#
# #读取启动环境
# # environment = e.read()
#
# #普通json带error_code风格
# app = Flask(__name__)
#
# #配置sqlalchemy数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
#
# #配置上传文件
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #上传目录
# app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH #上传大小
#
# #创建数据库及连接
# engine = create_engine(SQLALCHEMY_DATABASE_URI)
#
# #创建DBSession类型:
# DBSession = sessionmaker(bind=engine)
# dBSession = DBSession()
#
# db = SQLAlchemy()
#
# #引入使用的控制器
# # if environment == 'run' or environment == 'restful':
#     # from app.Controllers import UsersController
#     # 蓝图，新增的后台部分代码
#
# from app.Controllers.AuthController import auth
# app.register_blueprint(auth, url_prefix='/api/auth')
#
# from app.Controllers.UserController import user
# app.register_blueprint(user, url_prefix='/api/user')
#
# from app.Controllers.RoleController import role
# app.register_blueprint(role, url_prefix='/api/role')
#
# from app.Controllers.PermissionController import permission
# app.register_blueprint(permission, url_prefix='/api/permission')
#
# #引入数据库事件
# # from app.Event import Log