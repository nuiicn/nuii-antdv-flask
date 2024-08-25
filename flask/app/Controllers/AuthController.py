from app import db
from app.Controllers.BaseController import BaseController
from app.Models.User import User
from app.Vendor.UserAuthJWT import UserAuthJWT
from app.Vendor.Utils import Utils
from flask import Blueprint, jsonify, request

# 设置日志记录级别
# logging.basicConfig(level=logging.INFO)

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User()
        user.nickname = username
        user.username = username
        user.email = username
        user.password = User.set_password(password)
        user.parent_id = 0
        user.department_id = 0
        user.status = 1
        user.created_by = 0
        user.updated_by = 0
        user.created_time = Utils.getCurrentTime()
        user.updated_time = Utils.getCurrentTime()

        db.session.add(user)

        return jsonify({'message': '注册成功', 'status': 200, 'timestamp': ''})
    else:
        return jsonify({'msg': '账号已注册'}), 401


@auth.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return BaseController().error('用户名或密码不能为空')
    else:
        return UserAuthJWT.authenticate(username, password)


# logging.info(f'Login attempt with username: {login_name}')

# @auth.route('/refresh_token', method=['POST'])
# @AuthService.token_required
# def refresh_token():
#     token = request.args.get('token')
#     try:
#         data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'], options={'verify_exp': False})
#         new_token = jwt.encode(data, app.config['SECRET_KEY'])
#         CommonService.code200('Refresh token successfully!', {'token': new_token.decode('UTF-8')})
#     except:
#         CommonService.code403('Token is invalid!')
