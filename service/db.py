from pymongo import MongoClient

class Data_Base:
    
    # OPEN CLOUSE
    @staticmethod
    def add_document(host, data_base, collection, document):
        cliente = MongoClient(host)
        db = cliente[data_base]
        try:
            db[collection].insert_one(document)
            return True
        except KeyError:
            print("The document hasn't any key")
            
        return False

    @staticmethod
    def get_data(host, data_base, collection, data={}):
        cliente = MongoClient(host)
        db = cliente[data_base]
        res = {"data" : []}
        docs = db[collection].find(data)
        for doc in docs:
            res["data"].append(doc)
            
        return res
    
    '''@staticmethod
    def update_error(data_base, host, collection, document):
        cliente = MongoClient(host)
        db = cliente[data_base]

        query = {
            "error-id" : document["error-id"]
        }

        docs = db[collection].find(query)
        if docs.count() > 0:
            for doc in docs:
                db[collection].update_one(doc, {"$set" : document})
            return True
        else:
            return False
    
    @staticmethod
    def delete_error(data_base, host, collection, document):
        cliente = MongoClient(host)
        db = cliente[data_base]

        query = {
            "error-id" : document["error-id"]
        }

        docs = db[collection].find(query)
        if docs.count() > 0:
            for doc in docs:
                db[collection].delete_one(doc)
            return True
        else:
            return False'''