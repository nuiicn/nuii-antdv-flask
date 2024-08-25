from app.Controllers.BaseController import BaseController
from flask import jsonify, Response, abort
from app.Models.User import User
from app.Vendor.Utils import Utils
from app.env import SECRET_KEY, JWT_LEEWAY
import jwt
import datetime


class UserAuthJWT:

    @staticmethod
    def encode_auth_token(user_id, updated_time):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_LEEWAY),
                'iat': datetime.datetime.utcnow(),
                'iss': 'nuii',
                'data': {
                    'id': user_id,
                    'updated_time': updated_time
                }
            }
            return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            # payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'), leeway=datetime.timedelta(seconds=10))
            # 取消过期时间验证
            payload = jwt.decode(auth_token, SECRET_KEY, algorithms=['HS256'])
            if 'data' in payload and 'id' in payload['data']:
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'

    @staticmethod
    def authenticate(username, password):
        userData = User.query.filter_by(username=username).first()
        if userData is None:
            return jsonify({'msg': '找不到用户'}), 401
        else:
            if User.check_password(userData.password, password):
                updated_time = Utils.getCurrentTime()
                User.update(username, updated_time)
                token = UserAuthJWT.encode_auth_token(userData.id, updated_time)
                return BaseController().success({'token': token, 'user': userData.to_json()}, '登陆成功')
                # return self.json({'error_code': Code.SUCCESS, 'data': data, 'msg': msg, 'show': show})
            else:
                return jsonify({'message': '密码不正确', 'status': 200, 'timestamp': ''})

    def identify(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_tokenArr = auth_header.split(" ")
            if (not auth_tokenArr or auth_tokenArr[0] != 'JWT'
                    or len(auth_tokenArr) != 2):
                return '请传递正确的验证头信息'
            else:
                auth_token = auth_tokenArr[1]
                payload = self.decode_auth_token(auth_token)
                # if not isinstance(payload, str):
                #     user = User.get(payload['data']['id'])
                #     if (user is None):
                #         return '找不到该用户信息'
                #     else:
                #         if (user.updated_time == payload['data']['updated_time']):
                #             result = payload
                #         else:
                #             return 'Token已更改，请重新登录获取'
                # else:
                #     result = payload
                result = ''
        else:
            return '没有提供认证token'
        return result
