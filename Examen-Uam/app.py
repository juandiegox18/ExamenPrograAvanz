from flask_restful import Api
from flask import Flask
from resources.routes import initialize_routes

# se inicializa el app flask y flaskrestful
app = Flask(__name__)
api = Api(app)

# se le pasa a la funcion el api de flaskrestful
initialize_routes(api)

app.run()
