from flask import Response, request, make_response, render_template, jsonify
from flask_restful import Resource
from services.read_service import leer_votantes, obtener_mujeres_votantes, obtener_votantes_distrito
import json

# se crea la ruta que permite leer y reenviar todos los votantes
# en la respuesta renderiza y envia los datos


class Votantes(Resource):
    def get(self):
        try:
            votantes = leer_votantes()
            titulo = "Votantes Totales"
            return make_response(render_template('data.html', datos=votantes, titulo=titulo))
        except Exception as e:
            return make_response(jsonify(e, 500))

# se crea la ruta que permite leer y reenviar todos los votantes mujeres
# en la respuesta renderiza y envia los datos


class VotantesMujeres(Resource):
    def get(self):
        try:
            votantesMujeres = obtener_mujeres_votantes()
            titulo = "Votantes Mujeres"
            return make_response(render_template('data.html', datos=votantesMujeres, titulo=titulo))
        except Exception as e:
            return make_response(jsonify(e, 500))

# se crea la ruta que permite leer y reenviar todos los votantes de un distrito en especifico
# en la respuesta renderiza y envia los datos


class VotantesPorDistrito(Resource):
    def get(self, id):
        try:
            votantesPorDistrito = obtener_votantes_distrito(id)
            titulo = "Votantes por Distrito"
            return make_response(render_template('data.html', datos=votantesPorDistrito, titulo=titulo))
        except Exception as e:
            return make_response(jsonify(e, 500))
