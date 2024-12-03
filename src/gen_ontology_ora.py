'''
NAME: 
        Análisis de sobrerrepresentación (ORA) de ontología génica (GO), vías y categorías fenotípicas.
    
VERSION: 
        1
    
AUTHORS: 
        Edna Karen Rivera Zagal 
        Karla Ximena González Platas

DESCRIPTION:
          El código realiza un análisis de sobrerrepresentación (Over-Representation Analysis, ORA) utilizando dat
          os de expresión génica. Este tipo de análisis se enfoca en determinar si ciertos términos biológicos, co
          mo procesos de ontología génica (GO), rutas metabólicas (KEGG) o categorías fenotípicas (HP), están repr
          esentados significativamente en un conjunto de genes regulados.  
    
CATEGORY:
        Proyecto de Biopython: Expresion_Genetica_RetinaMurina

USAGE:
        % python gen_ontology_ora.py -i ..\results\genes_regulacion_positiva.txt -o ../results/ora_genes_positiva.txt
        % python gen_ontology_ora.py -i ..\results\genes_regulacion_negativa.txt -o ../results/ora_genes_negativa.txt

        % gen_ontology_ora.py [-h] -i INPUT -o OUTPUT [-g ORGANISMO]
        EXAMPLES:       

PARAMETERS:
            Análisis GO de genes regulados

            options:
            -h, --help            show this help message and exit
            -i INPUT, --input INPUT
                                    Ruta del archivo de entrada con los genes regulados
            -o OUTPUT, --output OUTPUT
                                    Ruta del archivo de salida para los resultados GO
            -g ORGANISMO, --organismo ORGANISMO
                                    Organismo para el análisis GO (default: mmusculus)
'''

# =========================================================================== 
# =                            Imports 
# =========================================================================== 

import pandas as pd  
from gprofiler import GProfiler  # Para realizar análisis GO
import argparse  
from graficas_GO import GraficadorTopTerminos  # Importar la función del primer script

# =========================================================================== 
# =                              Functions
# =========================================================================== 

def obtener_argumentos():
    """
    Maneja los argumentos de la línea de comandos para especificar los parámetros del programa.
    
    Retorna:
        argparse.Namespace: Objeto con los argumentos proporcionados.
    """
    # Crear el parser para los argumentos
    parser = argparse.ArgumentParser(description="Análisis GO de genes regulados")
    # Argumento para la ruta del archivo de entrada
    parser.add_argument("-i", "--input", required=True, help="Ruta del archivo de entrada con los genes regulados")
    # Argumento para la ruta del archivo de salida
    parser.add_argument("-o", "--output", required=True, help="Ruta del archivo de salida para los resultados GO")
    # Argumento para especificar el organismo (default: ratón)
    parser.add_argument("-g", "--organismo", default="mmusculus", help="Organismo para el análisis GO (default: mmusculus)")
    # Retornar los argumentos parseados
    return parser.parse_args()


def cargar_genes_desde_archivo(ruta_archivo):
    """
    Carga un archivo tabular con datos de genes regulados y extrae la columna 'RefSeq Symbol'.
    
    Parámetros:
        ruta_archivo (str): Ruta al archivo de entrada con datos de genes.
    
    Retorna:
        list: Lista de nombres únicos de genes (sin valores nulos).
    """
    # Leer el archivo de entrada usando pandas
    df_genes = pd.read_csv(ruta_archivo, sep="\t")
    # Extraer los nombres de los genes de la columna 'RefSeq Symbol', eliminando valores nulos y duplicados
    genes = df_genes['RefSeq Symbol'].dropna().unique().tolist()
    return genes

def realizar_analisis_go(genes, organismo='mmusculus'):
    """
    Realiza un análisis de Ontología Génica (GO), vías de señalización y categorías fenotípicas usando G:Profiler.

    Parámetros:
        genes (list): Lista de nombres de genes para el análisis.
        organismo (str): Organismo de referencia para el análisis (default: 'mmusculus').

    Retorna:
        pd.DataFrame: DataFrame con los resultados significativos (FDR < 0.05).
    """
    # Validación de entrada
    if not genes or not isinstance(genes, list):
        raise ValueError("La lista de genes está vacía o no es válida. Debe ser una lista no vacía.")
    
    try:
        # Inicializamos G:Profiler
        gp = GProfiler(return_dataframe=True)
        
        # Realizamos el análisis GO, incluyendo vías y fenotipos
        resultados_go = gp.profile(
            organism=organismo,
            query=genes,
            sources=['GO:BP', 'GO:MF', 'GO:CC', 'KEGG', 'HP'],  # Agregamos KEGG y HP
            significance_threshold_method='fdr'
        )
        
        # Validación de resultados
        if 'p_value' not in resultados_go.columns:
            raise ValueError("La columna 'p_value' no se encuentra en los resultados. Verifica la salida de G:Profiler.")
        
        # Filtrar resultados significativos
        resultados_significativos = resultados_go[resultados_go['p_value'] < 0.05]
        
        # Contar categorías significativas
        num_bp = resultados_significativos[resultados_significativos['source'] == 'GO:BP'].shape[0] # "GO:BP" (Biological Processes)
        num_mf = resultados_significativos[resultados_significativos['source'] == 'GO:MF'].shape[0] # "GO:MF" (Molecular Functions)
        num_cc = resultados_significativos[resultados_significativos['source'] == 'GO:CC'].shape[0] # "GO:CC" (Cellular Components)
        num_kegg = resultados_significativos[resultados_significativos['source'] == 'KEGG'].shape[0] # "KEGG" (Metabolic Pathways)
        num_hp = resultados_significativos[resultados_significativos['source'] == 'HP'].shape[0] # "HP" (Phenotypic Categories)
        
        # Mostrar resumen al usuario
        print(
            f"Se encontraron {num_bp} términos GO:BP, {num_mf} GO:MF, {num_cc} GO:CC, "
            f"{num_kegg} vías de señalización (KEGG), y {num_hp} categorías fenotípicas (HP) con un FDR menor a 0.05."
        )
        return resultados_significativos
    
    except Exception as e:
        print(f"Error durante el análisis: {e}")
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error

def obtener_top_terminos_por_fuente(resultados_go, n_top=10):
    """
    Obtiene los términos más significativos (por FDR) de cada categoría de GO y KEGG.
    
    Parámetros:
        resultados_go (pd.DataFrame): DataFrame con los resultados del análisis GO.
        n_top (int): Número de términos a extraer por fuente.
    
    Retorna:
        dict: Diccionario con listas de términos más significativos por fuente.
    """
    categorias = ['GO:BP', 'GO:MF', 'GO:CC', 'KEGG', 'HP']
    top_terminos = {}

    for categoria in categorias:
        top = (
            resultados_go[resultados_go['source'] == categoria]
            .sort_values(by='p_value')
            .head(n_top)
        )
        top_terminos[categoria] = top[['name', 'p_value', 'query_size']].to_dict('records')
    
    return top_terminos

def guardar_resultados_en_archivo(resultados_go, archivo_salida):
    """
    Guarda los resultados del análisis GO en un archivo CSV.
    
    Parámetros:
        resultados_go (pd.DataFrame): DataFrame con los resultados del análisis GO.
        archivo_salida (str): Ruta al archivo donde se guardarán los resultados.
    """
    # Guardar el DataFrame como un archivo CSV
    resultados_go.to_csv(archivo_salida, index=False)

# =================================================================== 
# =                              Main
# =================================================================== 

if __name__ == "__main__":
    # Obtener los argumentos desde la línea de comandos
    args = obtener_argumentos()
    
    # Cargar los genes desde el archivo especificado por el usuario
    genes_regulados = cargar_genes_desde_archivo(args.input)
    print(f"Genes regulados encontrados: {len(genes_regulados)}")
    
    # Realizar el análisis GO para los genes cargados
    resultados_analisis_go = realizar_analisis_go(genes_regulados, organismo=args.organismo)
    print(f"Resultados del análisis GO: {len(resultados_analisis_go)} categorías enriquecidas encontradas.")
    
    # Obtener los términos más significativos por categoría
    top_terminos = obtener_top_terminos_por_fuente(resultados_analisis_go)
    print("Términos más significativos por fuente:")
    for fuente, terminos in top_terminos.items():
        print(f"\n{fuente}:")
        for termino in terminos:
            print(f"  {termino['name']}")

    # Crear el objeto graficador y graficar los términos
    graficador = GraficadorTopTerminos()
    graficador.graficar(top_terminos) 
    

    # Guardar los resultados del análisis en el archivo de salida especificado
    guardar_resultados_en_archivo(resultados_analisis_go, args.output)



