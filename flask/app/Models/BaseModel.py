from app.Vendor.Code import Code
from sqlalchemy import desc, asc
from app import dBSession
import math



class BaseModel():

    def getList(self, cls_, filters, order="id desc", field=(), offset=0, limit=15):
        res = {}
        res['page'] = {}
        res['page']['count'] = dBSession.query(cls_).filter(*filters).count()
        res['list'] = []
        res['page']['total_page'] = self.get_page_number(res['page']['count'], limit)
        res['page']['current_page'] = offset
        if offset != 0:
            offset = (offset-1) * limit
        if res['page']['count'] > 0:
            res['list'] = dBSession.query(cls_).filter(*filters)
            orderArr = order.split(',')
            if len(orderArr) <= 1:
                orderItem = order.split(' ')
                if orderItem[1].upper() == 'DESC':
                    res['list'] = res['list'].order_by(desc(orderItem[0])).offset(offset).limit(limit).all()
                else:
                    res['list'] = res['list'].order_by(asc(orderItem[0])).offset(offset).limit(limit).all()
            else:
                for item in orderArr:
                    orderItem = item.split(' ')
                    if orderItem[1].upper() == 'DESC':
                        res['list'] = res['list'].order_by(desc(orderItem[0]))
                    else:
                        res['list'] = res['list'].order_by(asc(orderItem[0]))
                res['list'] = res['list'].offset(offset).limit(limit).all()
        if not field:
            res['list'] = [c.to_dict() for c in res['list']]
        else:
            res['list'] = [c.to_dict(only=field) for c in res['list']]
        return res


    def getAll(self, cls_, filters, order='id desc', field=(), limit=0):
        if not filters:
            res = dBSession.query(cls_)
        else:   
            res = dBSession.query(cls_).filter(*filters)
        if limit != 0:
            res = res.limit(limit)
        orderArr = order.split(' ')
        if orderArr[1] == 'desc':
            res = res.order_by(desc(orderArr[0])).all()
        else:
            res = res.order_by(asc(orderArr[0])).all()
        if not field:
            res = [c.to_dict() for c in res]
        else:
            res = [c.to_dict(only=field) for c in res]
        return res


    def getOne(self, cls_, filters, order='id desc', field=()):
        res = dBSession.query(cls_).filter(*filters)
        orderArr = order.split(' ')
        if orderArr[1] == 'desc':
            res = res.order_by(desc(orderArr[0])).first()
        else:
            res = res.order_by(asc(orderArr[0])).first()
        if res == None:
            return None
        if not field:
            res = res.to_dict() 
        else:
           res = res.to_dict(only=field) 
        return res
  

    def add(self, cls_, data):
        users = cls_(**data)
        dBSession.add(users)
        dBSession.flush()
        return users.id


    def edit(self, cls_, data, filters):
        return dBSession.query(cls_).filter(*filters).update(data, synchronize_session=False)


    def delete(self, cls_, filters):
        return dBSession.query(cls_).filter(*filters).delete(synchronize_session=False)

    
    def getCount(self, cls_, filters, field=None): 
        if field == None:
            return dBSession.query(cls_).filter(*filters).count()
        else:
            return dBSession.query(cls_).filter(*filters).count(field)
        

    @staticmethod
    def get_page_number(count, page_size):
        page_size = abs(page_size)
        if page_size != 0:
            total_page = math.ceil(count / page_size)
        else:
            total_page = math.ceil(count / 5)
        return total_page


    @staticmethod
    def formatPaged(page, size, total):
        if int(total) > int(page) * int(size):
            more = 1
        else:
            more = 0
        return {
            'total': int(total),
            'page': int(page),
            'size': int(size),
            'more': more
        }


    @staticmethod
    def formatBody(data={}, msg='', show=True):
        dataformat = {}
        dataformat['error_code'] = Code.SUCCESS
        dataformat['data'] = data
        dataformat['msg'] = msg
        dataformat['show'] = show
        return dataformat


    @staticmethod
    def formatError(code, message='', show=True):
        if code == Code.BAD_REQUEST:
            message = 'Bad request.'
        elif code == Code.NOT_FOUND:
            message = 'No result matched.'
        body = {}
        body['error'] = True
        body['error_code'] = Code.BAD_REQUEST
        body['msg'] = message
        body['show'] = show
        return body