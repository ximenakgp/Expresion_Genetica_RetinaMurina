'''
NAME: 
        ANÁLISIS DE EXPRESIÓN DIFERENCIAL DE GENES 
    
VERSION: 
        1
    
AUTHORS: 
        Edna Karen Rivera Zagal 
        Karla Ximena González Platas

DESCRIPTION:
            Script para filtrar los genes regulados según su cambio de expresión 
            "log2foldchange", ya sea positiva o negativa, y guardarlos en un archivo de 
            salida. El script permite especificar la columna de interés y el tipo de 
            regulación ("positiva" o "negativa"). Los genes filtrados se guardan en 
            un archivo de texto con el tipo de regulación incluido en el nombre del archivo.
    
CATEGORY:
        Proyecto de Biopython: Expresion_Genetica_RetinaMurina

USAGE:
        % python analisis_regulacion.py -i <ruta al archivo> -o <ruta a donde se guardaran los resultados> 
          -c <nombre de la columna> -r <tipo de regulación>

        EXAMPLES:

        % python analisis_regulacion.py -i ../data/GSE131954_DESeq2_RR9_Ground_Ctrl_vs_Flight_DEGs.txt -o ../results/genes_regulacion.txt -c log2FoldChange  -r positiva

        % python analisis_regulacion.py -i ../data/GSE131954_DESeq2_RR9_Ground_Ctrl_vs_Flight_DEGs.txt -o ../results/genes_regulacion.txt -c log2FoldChange  -r negativa

PARAMETERS:

%  python analisis_regulacion.py --help

Análisis de expresión diferencial de genes

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Ruta del archivo de entrada (TSV)
  -o OUTPUT, --output OUTPUT
                        Ruta del archivo de salida
  -c COLUMN, --column COLUMN
                        Columna para filtrar genes
  -r {positiva,negativa}, --regulacion {positiva,negativa}
                        Tipo de regulación a analizar ('positiva' o 'negativa')
    
'''

# ===========================================================================
# =                            Imports
# ===========================================================================

import pandas as pd
import argparse


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
    parser.add_argument("-c", "--column", default="log2FoldChange", help="Columna para filtrar genes")
    parser.add_argument("-r", "--regulacion", choices=["positiva", "negativa"], required=True,
                        help="Tipo de regulación ('positiva' o 'negativa')")
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

def filtrar_genes(df, columna="log2FoldChange", regulacion="positiva"):

    """
    Filtra genes regulados según el criterio especificado.

    Args:
        df (DataFrame): DataFrame con los datos de expresión.
        columna (str): Columna para aplicar el filtro (por defecto, "log2FoldChange").
        regulacion (str): Tipo de regulación ("positiva" o "negativa").

    Returns:
        DataFrame: Genes filtrados según el criterio.

    """
    if columna not in df.columns:
        print(f"La columna '{columna}' no existe en el DataFrame.")
        return None
    
    if regulacion == "positiva":
        genes_filtrados = df[df[columna] > 0]
        print(f"Se encontraron {len(genes_filtrados)} genes regulados positivamente.")
    
    elif regulacion == "negativa":
        genes_filtrados = df[df[columna] < 0]
        print(f"Se encontraron {len(genes_filtrados)} genes regulados negativamente.")
    else:
        print(f"Regulación desconocida: {regulacion}. Use 'positiva' o 'negativa'.")
        return None
    
    return genes_filtrados

def guardar_genes(df, output_file):
    """
    Guarda los genes filtrados en un archivo
    
    """
    try:
        df.to_csv(output_file, sep="\t", index=False)
        print(f"Genes guardados en {output_file}")
    except Exception as e:
        print(f"Error al guardar los genes: {e}")


#=======================================================================#
#===                             Main                                ===#
#=======================================================================#

def main():
    args = obtener_argumentos()
    df = leer_archivo(args.input)
    if df is not None:
        genes_filtrados = filtrar_genes(df, args.column, args.regulacion)
        if genes_filtrados is not None:
            # Generar el nombre del archivo de salida dinámicamente
            regulacion = args.regulacion
            output_file = args.output.replace(".txt", f"_{regulacion}.txt")
            guardar_genes(genes_filtrados, output_file)

if __name__ == "__main__":
    main()