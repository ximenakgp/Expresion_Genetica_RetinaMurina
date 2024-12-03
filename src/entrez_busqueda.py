'''
NAME: 
        BÚSQUEDA EN ENTREZ DE LOS GENES SIGNIFICATIVOS     
    
VERSION: 
        1
    
AUTHORS: 
        Edna Karen Rivera Zagal 
        Karla Ximena González Platas

DESCRIPTION:
        Script para buscar en la base de datos NCBI los valores de sobreexpresión de los genes regulados ya sea negativa o positivamente
            
    
CATEGORY:
        Proyecto de Biopython: Expresion_Genetica_RetinaMurina

USAGE:
        % python entrez_busqueda.py -i <ruta al archivo> -o <ruta a d
        onde se guardaran los resultados> -c <cantidad de genes a bus
        car> -s <tipo de regulación (maxima o minima)> -e <email por 
        elque se realizara la busqueda> -d <Base de datos que quieres
        consultar>

        EXAMPLES:

        % python entrez_busqueda.py -i ../results/genes_regulacion_negativa.txt -o ../results/genes_entrez.txt -c 10 -s menor -e ednakrz@lcg.unam.mx -d gene

        % python entrez_busqueda.py -i ../results/genes_regulacion_positiva.txt -o ../results/genes_entrez.txt -c 10 -s mayor -e ednakrz@lcg.unam.mx -d gene

PARAMETERS:

%  python entrez_busqueda.py --help

Busqueda de los genes con menor o mayor expresión diferencial

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Ruta del archivo de entrada (TSV)
  -o OUTPUT, --output OUTPUT
                        Ruta del archivo de salida
  -c CANTIDAD, --cantidad CANTIDAD
                        Cantidad de genes ha buscar
  -s {positiva,negativa}, --regulacion {mayor,menor}
                        Tipo de expresion, de mayor o menor significancia
  -e EMAIL, --email EMAIL 
                        Correo por el cual se conectara a Entrez 
  -d BASEDATOS, --basedatos BASEDATOS 
                        Base de datos en la que que quieres buscar tus  genes
                        expresados con mayor o menor significancia

    

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


def main():
    #Leer el archivo de entrada 
    args = obtener_argumentos()
    df = leer_archivo(args.input)
    
    # Filtrar los genes 
    if df is not None:
        genes_filtrados = filtrar_genes(df,args.cantidad, args.significancia)
        if genes_filtrados is not None:
            busqueda = busqueda_entrez(args.email, genes_filtrados, args.basedatos)
        
            # Generar el nombre del archivo de salida dinámicamente
            regulacion = args.significancia
            output_file = args.output.replace(".txt", f"_{regulacion}.txt")
            guardar_genes(busqueda, output_file)

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
        cantidad (int): Cantidad de genes a obtener.
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
    """
    Buscar los genes seleccionados en a base de datos querida a partir de Entrez
    Args:
        email (str): Direccion de correo electronico para acceder a Entrez. 
        genes_filtrados (list): Lista de genes filtrados segun el tipo significancia.
        database (str): Base de datos donde se buscaran los genes filtrados.

    Returns:
        DataFrame: Genes filtrados según el criterio.

    """
    # Correo para accesar a Entrez
    Entrez.email = email
    # Lista para almacenar los resultados
    resultados = [] 
    for gene_filtrado in genes_filtrados:
         try: 
                 # Realiza la búsqueda en la base de datos 
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
        print(f"Resultados de la busqueda guardados en {output_file}")
    except Exception as e:
        print(f"Error al guardar los genes buscados: {e}")

#=======================================================================#
#===                             Main                                ===#
#=======================================================================#

if __name__ == "__main__":
    main()

