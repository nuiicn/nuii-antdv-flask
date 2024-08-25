from flask import request, jsonify
from app.Vendor.Code import Code


class BaseController(object):
    def error(self, msg='', show=True):
        try:
            requests = request.values
        except TypeError:
            requests = request.get_json()

        return self.json({'error_code': Code.BAD_REQUEST, 'error': True, 'msg': msg, 'show': show})

    def success(self, data='', msg='', show=True):
        try:
            requests = request.values
        except TypeError:
            requests = request.get_json()

        return self.json({'error_code': Code.SUCCESS, 'data': data, 'msg': msg, 'show': show})

    @staticmethod
    def json(body=None):
        # if DEBUG_LOG:
        #     debug_id = Utils.unique_id()
        #     data = {
        #         'LOG_ID': debug_id,
        #         'IP_ADDRESS': request.remote_addr,
        #         'REQUEST_URL': request.url,
        #         'REQUEST_METHOD': request.method,
        #         'PARAMETERS': request.args,
        #         'RESPONSES': body
        #     }
        #     if SAVE_LOG == 1:
        #         log().debug(data)
        #     elif SAVE_LOG == 2:
        #         LogService().add(json.dumps(data), 1, 2)
        #     body['debug_id'] = debug_id
        return jsonify(body)
