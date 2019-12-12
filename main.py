from flask import Flask
from flask_restful import Api

import handler

app = Flask(__name__)
api = Api(app)

api.add_resource(handler.DiagramBuilder, "/diagramBuilder")

if __name__ == '__main__':
    app.run(debug=True)
