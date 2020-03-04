from datetime import datetime

filename = "PADRON_COMPLETO.txt"
# tupla con los valores por defecto de cada votante
values = ("Cedula", "Codelec", "Sexo", "FechaCaduc",
          "Junta", "Nombre", "Apellido1", "Apellido2")

# metodo que permite leer el archivo de padron completo
# se leen los archivos y se almacenan en el array votantes
# a cada votante se le agrega el key value con los valores por defecto


def leer_votantes():
    with open(filename, 'r') as filehandle:
        votantes = []
        for i in range(0, 50):
            votante = {}
            line = filehandle.readline()
            s = line.strip().split(",")  # parte la linea leida en un array al separarla por coma
            for i in range(len(s)):
                # se agrega el key value a cada campo del votante
                votante[values[i]] = s[i]
            votante["FechaCaduc"] = datetime.strptime(
                votante["FechaCaduc"], '%Y-%m-%d').date()
            votantes.append(votante)
        return votantes

# metodo que permite leer el archivo de padron completo
# se leen los archivos y se almacenan en el array votantesMujeres
# a cada votante se le agrega el key value con los valores por defecto


def obtener_mujeres_votantes():
    with open(filename, 'r') as filehandle:
        votantesMujeres = []
        for i in range(0, 50):
            votante = {}
            line = filehandle.readline()
            s = line.strip().split(",")  # parte la linea leida en un array al separarla por coma
            for i in range(len(s)):
                # se agrega el key value a cada campo del votante
                votante[values[i]] = s[i]
            if(votante["Sexo"] == '2'):
                # si el votante es de sexo femenino se agrega al array
                votante["FechaCaduc"] = datetime.strptime(
                    votante["FechaCaduc"], "%Y-%m-%d").date()
                votantesMujeres.append(votante)
        return votantesMujeres

# metodo que permite leer el archivo de padron completo
# se leen los archivos y se almacenan en el array votantesPorDistrito
# a cada votante se le agrega el key value con los valores por defecto


# se recibe el id del distrito por parametros de la url
def obtener_votantes_distrito(id):
    with open(filename, 'r') as filehandle:
        votantesPorDistrito = []
        for i in range(0, 50):
            votante = {}
            line = filehandle.readline()
            s = line.strip().split(",")  # parte la linea leida en un array al separarla por coma
            for i in range(len(s)):
                # se agrega el key value a cada campo del votante
                votante[values[i]] = s[i]
            if(votante["Codelec"] == id):
                # si el votante es de distrito recibido por el id se agrega al array
                votante["FechaCaduc"] = datetime.strptime(
                    votante["FechaCaduc"], "%Y-%m-%d").date()
                votantesPorDistrito.append(votante)
        return votantesPorDistrito
