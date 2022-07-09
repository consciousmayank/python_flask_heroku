from flask_restful import Resource
from sqlalchemy import delete
from models.store_model import StoreModel



class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404
    
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "An store with name '{}' already exists.".format(name)}
        store = StoreModel(name)
        store.save_to_db()
        return store.json()
    
    
    
    def delete(self, name):
        if StoreModel.find_by_name(name):
            store = StoreModel.find_by_name(name)
            store.delete_from_db()
            return {'message': 'Store deleted'}
        return {'message': 'Store not found'}, 404
    
    
    
    

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
    