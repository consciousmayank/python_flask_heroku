from datetime import timedelta
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from resources.item import Item, ItemList
from security import authenticate, identity
from resources.user import UserRegister
from resources.store import Store, StoreList
from database import sql_database
    

app = Flask(__name__)
app.secret_key = 'mayank' # should not be pushed to git or shown to anyone
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_app_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=60 * 60 * 24)


jwt = JWT(app, authenticate, identity) #/auth

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify({
                        'access_token': access_token.decode('utf-8'),
                        'expires_after_seconds': 60 * 60 * 24
                   })

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

# if __name__ == '__main__':
sql_database.init_app(app)
app.run(debug=True)
    # app.run(host='192.168.29.107', port=5000, debug=True, threaded=False)
