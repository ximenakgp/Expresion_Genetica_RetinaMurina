# SCRIPT PARA IDENTIFICAR LOS GENES REGULADOS POSITIVAMENTE 

import pandas as pd

# Ruta del archivo

archivo = "../data/GSE131954_DESeq2_RR9_Ground_Ctrl_vs_Flight_DEGs.txt"

# Leer el archivo en un DataFrame considerando que está separado por tabulaciones (\t)
df = pd.read_csv(archivo, sep="\t")

# Mostrar las primeras filas del archivo para verificar su contenido
print("Contenido del archivo:")
print(df.head())

# Ver las columnas del archivo
print("\nColumnas disponibles:")
print(df.columns)

# Filtrar genes regulados positivamente si hay una columna como log2FoldChange
if "log2FoldChange" in df.columns:
    genes_regulados_positivamente = df[df["log2FoldChange"] > 0]
    print("\nGenes regulados positivamente:")
    print(genes_regulados_positivamente)
# Falta contar estos genes y dejar solo columnas que nos interesen 

# Guardar los genes regulados positivamente en un archivo separado
output_file = "genes_regulados_positivamente.txt"
genes_regulados_positivamente.to_csv(output_file, sep="\t", index=False)
print(f"\nGenes regulados positivamente guardados en {output_file}")
