import pymongo
from api_key import DB_CONNECTION
class DB:
    def __init__(self):
        # self.cluster = pymongo.MongoClient('mongodb://localhost:27017')
        # self.db = self.cluster['nasa']
        
        self.client = pymongo.MongoClient("mongodb+srv://octopus:eJfdHSjx9ZZlvEj8@cluster0.ckcoz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client['nasa']

    def save(self, data_Set):
        try:
            if self.if_exists(data_Set['id']):
                return True
            self.db['study'].insert_one(data_Set)
        except Exception as e:
            print('='*30)
            print(e)
            print('='*30)
            return False
        else:
            return True

    def if_exists(self, _id):
        try:
            # print(_id)
            res = self.db['study'].find({'id': _id}).count()
        except Exception as e:
            print(e)
        else:
            return res


    def get_article(self, _id):
        try:
            res = [x for x in self.db['study'].find({'id': _id})]
        except Exception as e:
            raise e
        else:
            res[0].pop('_id')
            return res