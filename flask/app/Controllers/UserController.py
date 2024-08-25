from app.Controllers.BaseController import BaseController
from app.Models.User import User
from app.Vendor.UserAuthJWT import UserAuthJWT
from flask import Blueprint, request, jsonify

user = Blueprint('user', __name__)


@user.route('/list')
def user_list():
    filters = []
    if 'username' in request.args:
        filters.append(User.username.like('%' + request.args['username'] + '%'))
    if 'status' in request.args and request.args['status'] != '2':
        filters.append(User.status == request.args['status'])
    if 'sortField' in request.args and 'sortOrder' in request.args:
        if request.args['sortOrder'] == 'ascend':
            sort_by = getattr(getattr(User, request.args['sortField']), 'asc')()
        else:
            sort_by = getattr(getattr(User, request.args['sortField']), 'desc')()
    else:
        sort_by = User.created_time.desc()

    pageNo = request.args.get('pageNo', 1, type=int)
    pageSize = request.args.get('pageSize', 10, type=int)
    pagination = User.query.filter(*filters).order_by(sort_by).paginate(page=pageNo, per_page=pageSize, error_out=False)
    result = {
        'data': [item.to_json() for item in pagination.items],
        "pageSize": pageSize,
        "pageNo": pageNo,
        "totalPage": pagination.total,
        "totalCount": User.query.filter(*filters).count()
    }
    return jsonify({'message': '操作成功', 'status': 200, 'timestamp': '', 'result': result})


@user.route('/info')
def info():
    token = UserAuthJWT.decode_auth_token(request.headers.get('Access-Token'))
    userData = User.query.filter_by(id=token.get('data')['id']).first()
    return BaseController().success(data=userData.to_json(), msg='登录成功')