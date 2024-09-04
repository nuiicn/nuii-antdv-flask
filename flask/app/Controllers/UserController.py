from app import db
from app.Controllers.BaseController import BaseController
from app.Models.User import User
from app.Vendor.UserAuthJWT import UserAuthJWT
from flask import Blueprint, request, jsonify

user = Blueprint('user', __name__)


@user.route('/upsert', methods=['POST'])
def upsert():
    data = request.get_json()
    userById = User.query.get(data['id'])
    userById.nickname = data['nickname']
    userById.username = data['username']
    userById.email = data['email']
    db.session.add(userById)
    return jsonify({'message': '操作成功', 'status': 200, 'timestamp': ''})


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

    current = request.args.get('current', 1, type=int)
    pageSize = request.args.get('pageSize', 10, type=int)
    pagination = User.query.filter(*filters).order_by(sort_by).paginate(page=current, per_page=pageSize, error_out=False)
    data = {
        'list': [item.to_json() for item in pagination.items],
        "pageSize": pageSize,
        "current": current,
        "totalPage": pagination.total,
        "totalCount": User.query.filter(*filters).count()
    }
    return jsonify({'msg': '操作成功', 'status': 200, 'timestamp': '', 'data': data})


@user.route('/update-table-column')
def updateTableColumn():
    userById = User.query.get(request.args['id'])
    setattr(userById, request.args['column'], request.args['value'])
    db.session.commit()

    return jsonify({'msg': '操作成功', 'status': 200, 'timestamp': ''})


@user.route('/excluding-current')
def excludingCurrent():
    users = User.query.with_entities(User.id, User.username).filter(User.id != request.args['id']).all()
    data = [{'id': item[0], 'username': item[1]} for item in users]
    return jsonify({'msg': '操作成功', 'status': 200, 'timestamp': '', 'data': data})


@user.route('/info')
def info():
    token = UserAuthJWT.decode_auth_token(request.headers.get('authorization'))
    userData = User.query.filter_by(id=token.get('data')['id']).first()
    return BaseController().success(data=userData.to_json(), msg='登录成功')
