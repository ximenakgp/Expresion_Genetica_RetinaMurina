# Casos de prueba o escenarios
Este documento describe los casos de prueba para el script de Python *gen_ontology_ora.py* desarrollado para el análisis de sobrerrepresentación (Over-Representation Analysis, ORA) utilizando datos de expresión génica. Este tipo de análisis se enfoca en determinar si ciertos términos biológicos, como procesos de ontología génica (GO), rutas metabólicas (KEGG) o categorías fenotípicas (HP), están representados significativamente en un conjunto de genes regulados.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

El script utiliza la herramienta G:Profiler para realizar un análisis que vincula los genes regulados con:
- Procesos biológicos (GO:BP): Funciones en el contexto de procesos en organismos vivos.
- Funciones moleculares (GO:MF): Actividades moleculares específicas de los genes.
- Componentes celulares (GO:CC): Ubicaciones celulares en las que los genes cumplen funciones.

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.


---

### **Casos de prueba para cargar_genes_desde_archivo**
```
python analisis_regulacion.py -i genes_regulados.tsv -o resultados_GO.csv
```
Salida esperada
- Un archivo CSV llamado resultados_GO.csv con los términos GO, rutas KEGG y categorías fenotípicas significativas.
- Impresiones en consola mostrando cuántos términos GO significativos fueron encontrados por categoría.
- Gráficos generados por la clase GraficadorTopTerminos.

1. **Archivo válido con genes duplicados y valores nulos**:
   - Entrada: Archivo con genes duplicados y valores nulos en la columna `RefSeq Symbol`.
```
python analisis_regulacion.py -i genes_regulados_DN.tsv -o resultados_GO.csv
```
   - Resultado esperado: Lista única de genes, sin valores nulos.

2. **Archivo sin columna RefSeq Symbol**:
   - Entrada: Archivo que no tiene la columna esperada.
```
python analisis_regulacion.py -i genes_regulados_WORS.tsv -o resultados_GO.csv
```
   - Resultado esperado: Error levantado, indicando la falta de la columna.

3. **Archivo vacío**:
   - Entrada: Archivo sin datos.

```
python analisis_regulacion.py -i genes_regulados_WO.tsv -o resultados_GO.csv
```

   - Resultado esperado: Lista vacía.

---
