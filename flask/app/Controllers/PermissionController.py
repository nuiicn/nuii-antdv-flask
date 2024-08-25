from app.Controllers.BaseController import BaseController
from app.Models.Permission import Permission
from flask import Blueprint, request, jsonify

permission = Blueprint('permission', __name__)


@permission.route('/list')
def permission_list():
    filters = []
    if 'name' in request.args:
        filters.append(Permission.name.like('%' + request.args['name'] + '%'))
    if 'status' in request.args and request.args['status'] != '2':
        filters.append(Permission.status == request.args['status'])
    if 'sortField' in request.args and 'sortOrder' in request.args:
        if request.args['sortOrder'] == 'ascend':
            sort_by = getattr(getattr(Permission, request.args['sortField']), 'asc')()
        else:
            sort_by = getattr(getattr(Permission, request.args['sortField']), 'desc')()
    else:
        sort_by = Permission.created_time.desc()

    pageNo = request.args.get('pageNo', 1, type=int)
    pageSize = request.args.get('pageSize', 10, type=int)
    pagination = Permission.query.filter(*filters).order_by(sort_by).paginate(page=pageNo, per_page=pageSize, error_out=False)
    result = {
        'data': [item.to_json() for item in pagination.items],
        "pageSize": pageSize,
        "pageNo": pageNo,
        "totalPage": pagination.total,
        "totalCount": Permission.query.filter(*filters).count()
    }
    return jsonify({'message': '操作成功', 'status': 200, 'timestamp': '', 'result': result})


@permission.route('/no-pager')
def no_pager():
    code = request.args.get('code')
    permissions = Permission.query.filter(Permission.code == code).all()
    data = [item.to_json() for item in permissions]

    return BaseController().success(data=data, msg='获取成功')
