from flask import jsonify
from ..libs.Helper import getCurrentTime

class CommonService():

    def listFormat(list, pageNo, pageSize):
        data = []
        for item in list:
            data.append({
                "id": item.id,
                "key": item.key,
                "url": item.url,
                "status": item.status,
                "created_time": item.created_time,
                "updated_time": item.updated_time
            })
        
        return jsonify({
            "result": {
                "data": data,
                "pageNo": pageNo,
                "pageSize": pageSize,
                "totalPage": 1,
                "totalCount": 10
            },
            "status": 200,
            "message": '',
            "timestamp": ''
        })

    def code200(message, data=""):
        return jsonify({"status": 200, "message": message, "data": data, "timestamp": getCurrentTime()})
    
    def code201(message):
        return jsonify({"status": 201, "message": message, "timestamp": getCurrentTime()})

    def code400(message):
        return jsonify({"status": 400, "message": message, "timestamp": getCurrentTime()})
    
    def code401(message):
        return jsonify({"status": 401, "message": message, "timestamp": getCurrentTime()})

    def code403(message):
        return jsonify({"status": 403, "message": message, "timestamp": getCurrentTime()})
    
    def code500(message):
        return jsonify({"status": 500, "message": message, "timestamp": getCurrentTime()})
