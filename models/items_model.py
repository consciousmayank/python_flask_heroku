from database import sql_database

class ItemModel(sql_database.Model):
    
    __tablename__ = 'items'
    
    id = sql_database.Column(sql_database.Integer, primary_key=True, autoincrement=True)
    name = sql_database.Column(sql_database.String(50), nullable=False)
    price = sql_database.Column(sql_database.Float(precision = 2), nullable=False)
    
    store_id = sql_database.Column(sql_database.Integer, sql_database.ForeignKey('stores.id'))
    store = sql_database.relationship('StoreModel')
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
        
    def json(self):
        return {'name': self.name, 'price': self.price}    
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        
    def save_to_database(self):
        sql_database.session.add(self)
        sql_database.session.commit()
    
    
    def delete_from_database(self):
        sql_database.session.delete(self)
        sql_database.session.commit()
    