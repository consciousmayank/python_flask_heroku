from app import app
from database import sql_database

sql_database.init_app(app)

@app.before_first_request
def create_tables():
    sql_database.create_all()