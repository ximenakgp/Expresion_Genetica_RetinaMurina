'''
NAME: 
        
    
VERSION: 
        1
    
AUTHORS: 
        Edna Karen Rivera Zagal 
        Karla Ximena González Platas

DESCRIPTION:
            
    
CATEGORY:
        Proyecto de Biopython: Expresion_Genetica_RetinaMurina

USAGE:
        % python analisis_regulacion.py -i <ruta al archivo> -o <ruta a donde se guardaran los resultados> 
          -c <nombre de la columna> -r <tipo de regulación>

        EXAMPLES:

        

PARAMETERS:

    
'''

# ===========================================================================
# =                            Imports
# ===========================================================================

import pandas as pd
from gprofiler import GProfiler
import argparse

# Cargar y extraer los nombres de los genes desde el archivo
def cargar_genes_desde_archivo(ruta_archivo):
    """
    Carga un archivo tabular con datos de genes regulados y extrae la columna 'Symbol'.
    """
    df_genes = pd.read_csv(ruta_archivo, sep="\t")
    genes = df_genes['RefSeq Symbol'].dropna().unique().tolist()
    return genes


def realizar_analisis_go(genes, organismo='mmusculus'):
    """
    Realiza un análisis GO con G:Profiler para los genes proporcionados.
    """
    gp = GProfiler(return_dataframe=True)
    resultados_go = gp.profile(
        organism=organismo,
        query=genes,
        sources=['GO:BP', 'GO:MF', 'GO:CC', 'KEGG', 'HP'],  # Biological Process, Molecular Function, Cellular Component
        significance_threshold_method='fdr'  # Control de tasa de descubrimiento falso
    )
    
    # Filtrar resultados con FDR < 0.05
    resultados_significativos = resultados_go[resultados_go['p_value'] < 0.05]
    
    # Contar el número de GO, vías y categorías fenotípicas
    num_go = resultados_significativos[resultados_significativos['source'] == 'GO:BP'].shape[0]
    num_vias = resultados_significativos[resultados_significativos['source'] == 'KEGG'].shape[0]  # Si se usan vías de KEGG
    num_fenotipos = resultados_significativos[resultados_significativos['source'] == 'HP'].shape[0]  # Si se usan categorías fenotípicas
    
    print(f"Se encontraron {num_go} GO, {num_vias} vías y {num_fenotipos} categorías fenotípicas con un FDR menor a 0.05.")
    
    return resultados_significativos

def guardar_resultados_en_archivo(resultados_go, archivo_salida):
    """
    Guarda los resultados del análisis GO en un archivo CSV.
    """
    resultados_go.to_csv(archivo_salida, index=False)

def obtener_argumentos():
    """Obtiene los argumentos desde la línea de comandos"""
    parser = argparse.ArgumentParser(description="Análisis GO de genes regulados")
    parser.add_argument("-i", "--input", required=True, help="Ruta del archivo de entrada con los genes regulados")
    parser.add_argument("-o", "--output", required=True, help="Ruta del archivo de salida para los resultados GO")
    parser.add_argument("-g", "--organismo", default="mmusculus", help="Organismo para el análisis GO (default: mmusculus)")
    return parser.parse_args()

if __name__ == "__main__":
    # Obtener los argumentos desde la línea de comandos
    args = obtener_argumentos()
    
    # Cargar los genes desde el archivo
    genes_regulados = cargar_genes_desde_archivo(args.input)
    print(f"Genes regulados encontrados: {len(genes_regulados)}")
    
    # Realizar análisis GO
    resultados_analisis_go = realizar_analisis_go(genes_regulados, organismo=args.organismo)  
    print(f"Resultados del análisis GO: {len(resultados_analisis_go)} categorías enriquecidas encontradas.")
    
    # Guardar resultados
    guardar_resultados_en_archivo(resultados_analisis_go, args.output)
    print(f"Resultados guardados en: {args.output}")


