from app import db
from app.Models.Role import Role
from flask import Blueprint, request, jsonify

role = Blueprint('role', __name__)


@role.route('/list')
def role_list():
    filters = []
    if 'name' in request.args:
        filters.append(Role.name.like('%' + request.args['name'] + '%'))
    if 'status' in request.args and request.args['status'] != '2':
        filters.append(Role.status == request.args['status'])
    if 'sortField' in request.args and 'sortOrder' in request.args:
        if request.args['sortOrder'] == 'ascend':
            sort_by = getattr(getattr(Role, request.args['sortField']), 'asc')()
        else:
            sort_by = getattr(getattr(Role, request.args['sortField']), 'desc')()
    else:
        sort_by = Role.created_time.desc()

    pageNo = request.args.get('pageNo', 1, type=int)
    pageSize = request.args.get('pageSize', 10, type=int)
    pagination = Role.query.filter(*filters).order_by(sort_by).paginate(page=pageNo, per_page=pageSize, error_out=False)
    result = {
        'data': [item.to_json() for item in pagination.items],
        "pageSize": pageSize,
        "pageNo": pageNo,
        "totalPage": pagination.total,
        "totalCount": Role.query.filter(*filters).count()
    }
    return jsonify({'message': '操作成功', 'status': 200, 'timestamp': '', 'result': result})


@role.route('/changeStatus', methods=['POST'])
def change_status():
    data = request.get_json()
    roleById = Role.query.get(data['id'])
    roleById.status = data['status']
    db.session.add(roleById)
    return jsonify({'message': '操作成功', 'status': 200, 'timestamp': ''})


@role.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    roleById = Role.query.get(data['id'])
    db.session.delete(roleById)
    return jsonify({'message': '操作成功', 'status': 200, 'timestamp': ''})
