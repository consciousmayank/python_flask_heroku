from database import sql_database


class UserModel(sql_database.Model):
    
    __tablename__ = 'users'
    
    id = sql_database.Column(sql_database.Integer, primary_key=True, autoincrement=True)
    username = sql_database.Column(sql_database.String(50), unique=True, nullable=False)
    password= sql_database.Column(sql_database.String(50), nullable=False)
    
    def __init__(self, username, password) -> None:
        self.username=username
        self.password=password
        
    def __repr__(self) -> str:
        return f"User('{self.id}', '{self.username}', '{self.password}')"                    
        
    @classmethod    
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    def save_to_database(self):
        sql_database.session.add(self)
        sql_database.session.commit()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()