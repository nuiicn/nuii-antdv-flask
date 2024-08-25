from app import app
from flask import request
from functools import wraps
from . import CommonService
import random, string, hashlib, base64
import jwt
import logging

class AuthService():

    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.args.get("token")
            if not token:
                CommonService.code403("Token is missing")
            try:
                data = jwt.decode(token, app.config["SECRET_KEY"])
            except:
                CommonService.code403("Token is invalid!")

            return f(*args, **kwargs)
        return decorated
                

    @staticmethod
    def geneAuthCode(info=None):
        m = hashlib.md5()
        str = "%s-%s-%s-%s-%s"%(info.id, info.username, info.password, info.salt, info.status)
        m.update(str.encode("utf-8"))
        return m.hexdigest()
    

    @staticmethod
    def genePwd(pwd, salt):
        m = hashlib.md5()
        str = "%s-%s"%(base64.encodebytes(pwd.encode("utf-8")), salt)
        m.update( str.encode("utf-8"))
        return m.hexdigest()
    

    @staticmethod
    def geneSalt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits )) for i in range(length)]
        return ("".join(keylist))
    
    