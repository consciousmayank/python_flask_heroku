from database import sql_database

class StoreModel(sql_database.Model):
    __tablename__ = 'stores'

    id = sql_database.Column(sql_database.Integer, primary_key=True)
    name = sql_database.Column(sql_database.String(80))

    items = sql_database.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        sql_database.session.add(self)
        sql_database.session.commit()

    def delete_from_db(self):
        sql_database.session.delete(self)
        sql_database.session.commit()