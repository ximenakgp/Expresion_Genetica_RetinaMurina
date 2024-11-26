import pandas as pd
from gprofiler import GProfiler

# 1. Cargar y extraer los nombres de los genes desde el archivo
def cargar_genes_desde_archivo(ruta_archivo):
    """
    Carga un archivo tabular con datos de genes regulados y extrae la columna 'Symbol'.
    """
    df_genes = pd.read_csv(ruta_archivo, sep="\t")
    genes_unicos = df_genes['RefSeq Symbol'].dropna().unique().tolist()
    return genes_unicos

# 2. Realizar análisis GO con G:Profiler
def realizar_analisis_go(genes, organismo='mmusculus'):
    """
    Realiza un análisis GO con G:Profiler para los genes proporcionados.
    """
    gp = GProfiler(return_dataframe=True)
    resultados_go = gp.profile(
        organism=organismo,
        query=genes,
        sources=['GO:BP', 'GO:MF', 'GO:CC'],  # Biological Process, Molecular Function, Cellular Component
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

# 3. Guardar los resultados
def guardar_resultados_en_archivo(resultados_go, archivo_salida):
    """
    Guarda los resultados del análisis GO en un archivo CSV.
    """
    resultados_go.to_csv(archivo_salida, index=False)

# 4. Script principal
if __name__ == "__main__":
    # Ruta al archivo con los datos de los genes regulados positivamente
    ruta_archivo_genes = "genes_regulados_positivamente.txt"
    
    # Cargar los genes desde el archivo tabular
    genes_regulados_positivos = cargar_genes_desde_archivo(ruta_archivo_genes)
    print(f"Genes regulados positivamente encontrados: {len(genes_regulados_positivos)}")
    
    # Realizar análisis GO
    resultados_analisis_go = realizar_analisis_go(genes_regulados_positivos, organismo='mmusculus')  
    print(f"Resultados del análisis GO: {len(resultados_analisis_go)} categorías enriquecidas encontradas.")
    
    # Guardar resultados
    archivo_resultados_salida = "resultados_go_genes_positivos.csv"
    guardar_resultados_en_archivo(resultados_analisis_go, archivo_resultados_salida)
    print(f"Resultados guardados en: {archivo_resultados_salida}")
