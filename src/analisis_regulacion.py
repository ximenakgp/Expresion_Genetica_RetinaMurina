'''
NAME: 
    
VERSION:
    
AUTHORS: 

DESCRIPTION:
            SCRIPT PARA IDENTIFICAR LOS GENES REGULADOS POSITIVAMENTE, GUARDARLOS Y 
            LUEGO EXTRAER LOS 10 QUE MAS SE REGULAN Y HACER UNA GRAFICA DE ESTOS.
            Posteriormente, podríamos complementar todo, utilizando biopython y entrez para hacer 
            consultas a NCBI y sacar información 
            sobre estos genes porque por ejemplo en esta parte del artículo se mencionan dos de ellos
            Hacer el script para ambos, que se ocupe tanto para los positivos como parea los negativos y 
            que sea funcional.
    
CATEGORY:
        Biopython: 

USAGE:
        % python
    
METHOD:
un log2FoldChange positivo generalmente indica sobreexpresión de un gen bajo ciertas condiciones
    
'''

# ===========================================================================
# =                            Imports
# ===========================================================================

import pandas as pd
import argparse


# ===========================================================================
# =                            Functions
# ===========================================================================

def leer_archivo(ruta, sep="\t"):
    """Lee un archivo en formato TSV y retorna un DataFrame."""
    try:
        df = pd.read_csv(ruta, sep=sep)
        print("Archivo leído correctamente.")
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
    """Guarda los genes filtrados en un archivo TSV."""
    try:
        df.to_csv(output_file, sep="\t", index=False)
        print(f"Genes guardados en {output_file}")
    except Exception as e:
        print(f"Error al guardar los genes: {e}")

def obtener_argumentos():
    """Obtiene argumentos desde la línea de comandos."""
    parser = argparse.ArgumentParser(description="Análisis de expresión diferencial de genes")
    parser.add_argument("-i", "--input", required=True, help="Ruta del archivo de entrada (TSV)")
    parser.add_argument("-o", "--output", required=True, help="Ruta del archivo de salida")
    parser.add_argument("-c", "--column", default="log2FoldChange", help="Columna para filtrar genes")
    parser.add_argument("-r", "--regulacion", choices=["positiva", "negativa"], required=True,
                        help="Tipo de regulación a analizar ('positiva' o 'negativa')")
    return parser.parse_args()


# Ruta del archivo
archivo = "../data/GSE131954_DESeq2_RR9_Ground_Ctrl_vs_Flight_DEGs.txt"

# Leer el archivo en un DataFrame considerando que está separado por tabulaciones (\t)
#df = pd.read_csv(archivo, sep="\t")
# Mostrar las primeras filas del archivo para verificar su contenido
#print("Contenido del archivo:")
#print(df.head())

# Ver las columnas del archivo
#print("\nColumnas disponibles:")
#print(df.columns)

# Filtrar genes regulados positivamente si hay una columna como log2FoldChange
#if "log2FoldChange" in df.columns:
    # Filtra el DataFrame para obtener solo los genes regulados positivamente
    # Esto se hace seleccionando las filas donde "log2FoldChange" sea mayor que 0
    #genes_regulados_positivamente = df[df["log2FoldChange"] > 0]
    #print("\nGenes regulados positivamente:")
    #print(genes_regulados_positivamente)

    # Contar cuántos genes están regulados positivamente 
    #cantidad_genes_positivos = len(genes_regulados_positivamente) 
    # len(genes_regulados_positivamente): Devuelve el numero de filas

    # Mostrar los resultados al usuario 
    #print(f"\nSe encontraron {cantidad_genes_positivos} genes regulados positivamente") 

# Guardar los genes regulados positivamente en un archivo separado
#output_file = "genes_regulados_positivamente.txt"
#genes_regulados_positivamente.to_csv(output_file, sep="\t", index=False)
# - `to_csv`: Método de pandas para exportar datos a un archivo
# - `sep="\t"`: Especifica que el archivo estará separado por tabulaciones (formato TSV)
# - `index=False`: Evita incluir la columna de índices del DataFrame en el archivo
#print(f"\nGenes regulados positivamente guardados en {output_file}")

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