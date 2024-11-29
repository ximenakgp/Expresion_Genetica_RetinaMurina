'''
NAME: 
        
    
VERSION: 
        1
    
AUTHORS: 
        Edna Karen Rivera Zagal 
        Karla Ximena González Platas

DESCRIPTION:
BUSCAR UNA FUNCION EN BASE A LOS IDS QUE MAS SE REGULAN Y ENCONTRAR LA SSCARCATERISTICAS MAS IMPORTANTES DE ESTOS 
GENE SPAR AEVALUAR LAS FUNCIONES A LAS QUE ESTAN ASOCIADOS 
            
    
CATEGORY:
        Proyecto de Biopython: Expresion_Genetica_RetinaMurina

USAGE:
        % python analisis_regulacion.py -i <ruta al archivo> -o <ruta a donde se guardaran los resultados> 
          -c <nombre de la columna> -r <tipo de regulación>

        % gen_ontology_ora.py [-h] -i INPUT -o OUTPUT [-g ORGANISMO]
        EXAMPLES:       

PARAMETERS:

'''


#=======================================================================#
#===                           Imports                               ===#
#=======================================================================#

from Bio import Entrez

#=======================================================================#
#===                             Main                                ===#
#=======================================================================#

# Correo
Entrez.email = "ximenagp@lcg.unam.mx"  
# Proporciona información sobre la base de datos "pubmed"
handle = Entrez.einfo(db = "pubmed")
# Lee la respuesta de la consulta a la base de datos
record = Entrez.read(handle)
# Cierra la conexión
handle.close() 

# Primera parte: Imprimir el nombre y la descripción de todos los "FieldList"

# Se emplea un iterador para acceder a los campos
for field in record["DbInfo"]["FieldList"]:
  print("%(Name)s, %(FullName)s, %(Description)s" % field)

# Segunda parte: Imprimir la descripción del primer elemento de la lista de los "FieldList" 

field = record["DbInfo"]["FieldList"][0]  # Accede al primer campo
print("\nPrimera descripción de FieldList:")
print("%(Description)s" % field)

