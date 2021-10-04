from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from resources.data import (
    SimpleSearch,
    IVSearch,
    TPSearch,
    ProjectSearch,
    CDSearch,
    Related
)


app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = 'node.js'
api = Api(app)

jwt = JWTManager(app)  # /auth


# Course
api.add_resource(SimpleSearch, '/search/<string:term>')
api.add_resource(IVSearch, '/image-video-search/<string:term>')
api.add_resource(TPSearch, '/techport')
api.add_resource(ProjectSearch, '/project/<string:_id>')
api.add_resource(CDSearch, '/catalog/<string:term>')
api.add_resource(Related, '/article/<string:_id>')



if __name__ == '__main__':
    app.run(port=5000)
