#Creando una excepcion propia:
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Impresionante, cometiste este error: {err}")
        
#Mostrando la excepcion        
raise MiExcepcion("Peñarol")

#Manejando nuestra excepcion
try:      
    raise MiExcepcion("Peñarol")
except:
    print("Persona poco culta")