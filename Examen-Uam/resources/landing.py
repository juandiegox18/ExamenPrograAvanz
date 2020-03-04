from flask import Response, request, make_response, render_template, jsonify
from flask_restful import Resource


# se crea la ruta del landing page principal
# se renderiza el template de index.html
class LandingApi(Resource):
    def get(self):
        return make_response(render_template('index.html'))
