# Casos de prueba o escenarios *analisis_regulacion.py*
Este documento describe los casos de prueba para el script de Python *analisis_regulacion.py* desarrollado para filtrar los genes regulados según su cambio de expresión "log2foldchange", ya sea positiva o negativa, y guardarlos en un archivo de salida.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

El script permite especificar la columna de interés y el tipo de regulación ("positiva" o "negativa"). Los genes filtrados se guardan en un archivo de texto con el tipo de regulación incluido en el nombre del archivo.

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.

## 1. Entrada básica y salida esperada

Objetivo: Probar si el script funciona correctamente con datos válidos y parámetros básicos.
Entrada:

Archivo de entrada con columnas gene y log2FoldChange.
Valor positivo o negativo en la columna log2FoldChange.

```bash
python analisis_regulacion.py -i genes_expresion.tsv -o salida_genes.txt -c log2FoldChange -r positiva
```
Esperado:

Archivo salida_genes_positiva.txt con genes con log2FoldChange > 0.

## 2. Entrada con valores mixtos
Objetivo: Validar el filtrado tanto para valores positivos como negativos.

Entrada:
Archivo con valores positivos, negativos y ceros en la columna log2FoldChange.
```bash
python analisis_regulacion.py -i gen_valores_mixtos.tsv -o salida_mixtos.txt -c log2FoldChange -r negativa
```
Esperado:

Archivo salida_mixtos_negativa.txt con genes con log2FoldChange < 0.

## 3. Filtro sobre columna inexistente
Objetivo: Manejar el error cuando la columna especificada no existe en el archivo.
Entrada:

```bash
python analisis_regulacion.py -i genes_expresion.tsv -o salida_genes.txt -c expresion -r positiva
```
Esperado:

Mensaje: "La columna 'expresion' no existe en el DataFrame."
No se genera un archivo de salida.

## 4. Archivo vacío
Objetivo: Comprobar el comportamiento con un archivo vacío.
Entrada:

```bash
python analisis_regulacion.py -i genes_expresionWO.tsv -o salida_vacia.txt -c log2FoldChange -r negativa
```
Esperado:

Mensaje: "Archivo leído correctamente" seguido de "Se encontraron 0 genes regulados negativamente."
Archivo de salida vacío salida_vacia_negativa.txt.

## 5. Archivo sin valores numéricos en la columna objetivo
Objetivo: Validar manejo de datos corruptos.
Entrada: Archivo donde log2FoldChange contiene valores no numéricos.

```bash
python analisis_regulacion.py -i  genes_expresion_valores_no_numericos.tsv -o salida_invalida.txt -c log2FoldChange -r positiva
```
Esperado:

Mensaje indicando error en el procesamiento del DataFrame.

## 6. Argumentos incompletos
Objetivo: Comprobar el manejo de entradas incorrectas.
Entrada:

```bash
python analisis_regulacion.py -i genes_expresion.tsv -o salida_genes.txt
```
Esperado:

Mensaje: "El parámetro '-r' es obligatorio."
Salida del script con código de error.

## 7. Archivo de entrada con delimitadores incorrectos
Objetivo: Validar que el script maneje archivos no separados por tabulaciones.
Entrada: Archivo CSV separado por comas.

```bash
python analisis_regulacion.py -i genes_expresion_entrada_csv.csv -o salida_genes.txt -c log2FoldChange -r positiva
```
Esperado:

Mensaje indicando error al leer el archivo.

## 9. Regeneración del archivo de salida
Objetivo: Validar que el archivo de salida se sobreescribe correctamente.
Entrada:
Ejecución del mismo comando dos veces con datos diferentes.

```bash
python analisis_regulacion.py -i genes_expresion1.tsv -o salida_regen.txt -c log2FoldChange -r positiva
python analisis_regulacion.py -i genes_expresion2.tsv -o salida_regen.txt -c log2FoldChange -r positiva
```
Esperado:

Solo el contenido de genes_expresion2.tsv estará en salida_regen_positiva.txt.

