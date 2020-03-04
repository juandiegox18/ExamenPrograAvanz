from .landing import LandingApi
from .votantes import Votantes, VotantesMujeres, VotantesPorDistrito

# se inicializan y se crean las rutas de la aplicacion


def initialize_routes(api):
    api.add_resource(LandingApi, '/')
    api.add_resource(Votantes, '/api/cargarVotantes')
    api.add_resource(VotantesMujeres, '/api/votantes/mujeres')
    api.add_resource(VotantesPorDistrito, '/api/votantes/distrito/<id>')
