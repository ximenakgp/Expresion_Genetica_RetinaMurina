'''
NAME: Busqueda en Entrez de los genes significativos 
        
    
VERSION: 
        1
    
AUTHORS: 
        Edna Karen Rivera Zagal 
        Karla Ximena González Platas

DESCRIPTION:
        Script para buscar en la base de datos NCBI los valores de so
        breexpresión de los genes regulados ya sea negativa o positiv
        a mente, 
            
    
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
import argparse
import pandas as pd
# ===========================================================================
# =                            Functions
# ===========================================================================

def obtener_argumentos():
    """
    Obtiene argumentos desde la línea de comandos
    """
    parser = argparse.ArgumentParser(description="Análisis de expresión diferencial de genes")
    parser.add_argument("-i", "--input", required=True, help="Ruta del archivo de entrada")
    parser.add_argument("-o", "--output", required=True, help="Ruta del archivo de salida")
    parser.add_argument("-c", "--cantidad",type=int, default = 10, help="Valor entero de la cantidade de genes a buscar")
    parser.add_argument("-s", "--significancia", choices=["mayor", "menor"], required=True,
                        help="Tipo de regulación ('mayor' o 'menor')")
    parser.add_argument("-e", "--email", required=True, help="correo electronico para realizar la busqueda en Entrez")
    parser.add_argument("-d", "--basedatos", default ="gene", help="Base de datos en la que quieres realizar la busqueda")
    return parser.parse_args()

def leer_archivo(ruta, sep="\t"):
    """
    Lee un archivo en formato tabular y retorna un DataFrame
    """
    try:
        # Leer el archivo en un DataFrame considerando que esta separado por tabulaciones
        df = pd.read_csv(ruta, sep=sep)
        print("Archivo leído correctamente")
        return df
    
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def filtrar_genes(df,cantidad, regulacion="mayor"):

    """
    Filtra genes regulados según el criterio especificado.

    Args:
        df (DataFrame): DataFrame con los datos de expresión.
        columna (str): Columna para aplicar el filtro (por defecto, "pvalue").
        regulacion (str): Tipo de regulación ("mayor" o "menor").

    Returns:
        DataFrame: Genes filtrados según el criterio.

    """
    columna = "pvalue"
    if columna not in df.columns:
        print(f"La columna '{columna}' no existe en el DataFrame.")
        return None
    
    if regulacion == "mayor":
        
        # Obtener los valores más pequeños de la columna 'pvalue'
        valores_mas_pequenos = df.nsmallest(cantidad, columna)
        genes_filtrados = valores_mas_pequenos["RefSeq Symbol"]

    
    elif regulacion == "menor":
       # Obtener los valores más altos de la columna 'pvalue'
        valores_mas_altos = df.nlargest(cantidad, columna)
        genes_filtrados = valores_mas_altos["RefSeq Symbol"]

    else:
        print(f"Regulación desconocida: {regulacion}. Use 'positiva' o 'negativa'.")
        return None
    
    return genes_filtrados

def busqueda_entrez (email, genes_filtrados, database): 
   
    # Correo
    Entrez.email = email
    # Lista para almacenar los resultados
    resultados = [] 
    for gene_filtrado in genes_filtrados:
         try: 
                 # Realiza la búsqueda en la base de datos Nucleotide
                 handle = Entrez.efetch(db=database, id=gene_filtrado, rettype="gb", retmode="text")
                 data = handle.read()
                 handle.close()
                 
                 # Agregar los datos obtenidos para cada ID a la lista de resultados
                 resultados.append(f"Datos para {gene_filtrado}:\n{data}\n")
                        
         except Exception as e:
                 print(f"Error al buscar {gene_filtrado}: {e}")
    return resultados 


def guardar_genes(lista_busqueda, output_file):
    """
    Guarda los genes filtrados en un archivo
    
    """
    try:
        # Guardar la lista de resultados en un archivo de texto
        with open(output_file, "w") as archivo:
                for resultado in lista_busqueda:
                        archivo.write(resultado)
        print("Resultados de la busqueda guardados en {output_file}")
    except Exception as e:
        print(f"Error al guardar los genes buscados: {e}")

#=======================================================================#
#===                             Main                                ===#
#=======================================================================#


def main():
    args = obtener_argumentos()
    df = leer_archivo(args.input)
    if df is not None:
        genes_filtrados = filtrar_genes(df,args.cantidad, args.significancia)
        if genes_filtrados is not None:
            busqueda = busqueda_entrez(args.email, genes_filtrados, args.basedatos)
        
            # Generar el nombre del archivo de salida dinámicamente
            regulacion = args.significancia
            output_file = args.output.replace(".txt", f"_{regulacion}.txt")
            guardar_genes(busqueda, output_file)

if __name__ == "__main__":
    main()

