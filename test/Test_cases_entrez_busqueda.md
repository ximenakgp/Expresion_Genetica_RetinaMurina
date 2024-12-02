# Casos de prueba o escenarios
Este documento describe los casos de prueba para el script de Python *entrez_busqueda.py* desarrollado para buscar en las bases de datos NCBI los genes cuyos valores de sobreexpresión estén regulados ya sea negativa o positiva mente.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.


## 1. Entrada básica y salida esperada
Objetivo: Probar si el script funciona correctamente con datos válidos.
Entrada:
- Archivo con genes y un valor de significancia (pvalue).
- Parámetros básicos con significancia=mayor y cantidad=10.
```bash
python entrez_busqueda.py -i entrada_valida.tsv -o salida_entrez.txt -c 10 -s mayor -e prueba@example.com -d gene
```
Esperado:

- Se conectará a Entrez usando el correo proporcionado.
- Buscará los 10 genes con menor pvalue en la base de datos gene.
- Guardará los resultados en salida_entrez_mayor.txt.

## 2. Archivo sin columna pvalue
Objetivo: Verificar si el script detecta la ausencia de la columna necesaria para filtrar.
Entrada:

```bash
python entrez_busqueda.py -i archivo_sin_pvalue.tsv -o salida_fallo.txt -c 5 -s menor -e prueba@example.com -d gene
```
Esperado:

- Mensaje: "La columna 'pvalue' no existe en el DataFrame."
- El script no realiza la búsqueda ni genera un archivo de salida.

## 3. Archivo vacío
Objetivo: Validar cómo el script maneja archivos sin datos.
Entrada:

```bash
python entrez_busqueda.py -i archivo_vacio.tsv -o salida_vacia.txt -c 10 -s menor -e prueba@example.com -d gene
```
Esperado:

- Mensaje: "Archivo leído correctamente", pero sin realizar búsquedas.
- No genera un archivo de salida.

## 4. Número de genes solicitado mayor al disponible
Objetivo: Manejar casos donde el número solicitado supera la cantidad de genes en el archivo.
Entrada:

```bash
python entrez_busqueda.py -i pocos_genes.tsv -o salida_pocos_genes.txt -c 100 -s mayor -e prueba@example.com -d gene
```
Esperado:

- Se realiza la búsqueda con todos los genes disponibles en el archivo.
- Mensaje: "Solo se encontraron N genes en el archivo."

## 5. Conexión fallida a Entrez
Objetivo: Verificar el manejo de errores durante la conexión a Entrez.
Entrada:

```bash
python entrez_busqueda.py -i entrada_valida.tsv -o salida_fallo_entrez.txt -c 5 -s menor -e prueba@example.com -d gene
```
Simulación:
Desconectar la red o usar un correo no válido.

Esperado:

- Mensaje: "Error al buscar <gene>: [detalles del error]."
- Se sigue intentando con los genes restantes.
- Archivo de salida incluye solo los genes exitosamente buscados.

## 6. Parámetros incompletos
Objetivo: Probar el manejo de argumentos faltantes.
Entrada:

```bash
python entrez_busqueda.py -i entrada_valida.tsv -o salida_incompleta.txt -c 10
```
Esperado:

- Mensaje: "El parámetro '-s' es obligatorio."
- El script no ejecuta la búsqueda.

## 7. Archivo con valores no numéricos en pvalue
Objetivo: Validar el manejo de datos corruptos.
Entrada: Archivo con valores no numéricos en la columna pvalue.

```bash
python entrez_busqueda.py -i valores_no_numericos.tsv -o salida_no_numericos.txt -c 5 -s mayor -e prueba@example.com -d gene
```
Esperado:

- Mensaje indicando error al intentar filtrar.
- El script no realiza búsquedas ni genera salida.

## 8. Archivo con delimitadores incorrectos
Objetivo: Probar archivos mal formateados (separados por comas).
Entrada:

```bash
python entrez_busqueda.py -i archivo_malformateado.csv -o salida_error.txt -c 5 -s menor -e prueba@example.com -d gene
```
Esperado:

- Mensaje: "Error al leer el archivo: [detalle del error]."

## 9. Pruebas de rendimiento
Objetivo: Validar la eficiencia del script con grandes volúmenes de datos.
Entrada: Archivo con 100,000 genes y cantidad=500.

```bash
python entrez_busqueda.py -i archivo_grande.tsv -o salida_grande.txt -c 500 -s mayor -e prueba@example.com -d gene
```
Esperado:

- Realiza la búsqueda y genera la salida correctamente.
- Mensajes de progreso útiles si se implementan.

## 10. Diferentes bases de datos
Objetivo: Comprobar la funcionalidad con distintas bases de datos en Entrez.
Entrada:

```bash
python entrez_busqueda.py -i entrada_valida.tsv -o salida_variada.txt -c 5 -s menor -e prueba@example.com -d protein
```
Esperado:

- El script busca genes en la base de datos protein.
- Resultados reflejan información relevante para esa base de datos.
