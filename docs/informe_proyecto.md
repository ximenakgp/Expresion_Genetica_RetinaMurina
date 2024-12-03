# Influencia de los vuelos espaciales en la expresión genética de la retina murina  

Nombre: Karla Ximena González Platas (<ximenagp@lcg.unam.mx>)
 
Nombre: Edna Karen Rivera Zagal (<ednakrz@lcg.unam.mx>)

Fecha:  10/09/2024 


## Introducción

Actualmente, una parte de la humanidad está cautivada por la era de la exploración espacial, convirtiendo este ámbito en una oportunidad de negocio para numerosas empresas privadas. Sin embargo, la investigación científica en esta área es igualmente crucial, ya que el éxito comercial y el avance tecnológico dependen uno del otro. Un ejemplo de ello son las misiones espaciales que se han estado preparando en los últimos años, como los planes para establecer asentamientos permanentes en la Luna o llevar a cabo misiones tripuladas a Marte.

El entorno espacial presenta condiciones muy diferentes a las de la Tierra, lo que conlleva una serie de estresores fisiológicos únicos, como la microgravedad y la radiación ionizante, cuyos efectos aún no se comprenden completamente y representan desafíos significativos para las misiones de larga duración. Uno de los principales problemas identificados es el deterioro del funcionamiento ocular después de la exposición al entorno espacial, así como los cambios en la estructura y función de la retina.

Por esta razón, es fundamental llevar a cabo estudios que permitan comprender en profundidad las implicaciones que estos factores estresantes tienen en los astronautas durante las misiones espaciales. En el caso del proyecto presentado, se busca analizar la influencia de los vuelos espaciales en la expresión genética de la retina murina, utilizando los datos obtenidos de un experimento realizado por la NASA con ratones como organismo modelo, que fueron expuestos al entorno espacial durante 35 días a bordo de la Estación Espacial Internacional (ISS). Este estudio tiene como objetivo determinar si el entorno espacial induce daño oxidativo en la estructura ocular y caracterizar los perfiles de expresión genética de la retina expuesta al vuelo espacial, proporcionando información crucial sobre los efectos de las condiciones espaciales en la salud ocular.


![image](https://github.com/user-attachments/assets/66935ed7-0b2d-4611-b15a-adbdda2b6134)
                                   

## Planteamiento del problema

A pesar de los grandes esfuerzos que la comunidad científica está haciendo por analizar los cambios fisiológicos de organismos modelo en condiciones espaciales, para la seguridad de las futuras misiones, aún queda mucho trabajo por hacer en el área de la biología molecular.

Así como el estudio de la morfología de la retina murina, es imperativo analizar la expresión genética que tiene nuestro organismo modelo en condiciones espaciales, para saber los procesos celulares que se activan bajo estas condiciones y su relación con el posible daño oxidativo a la estructura ocular. 

Con este fin se analizarán los datos  obtenidos de la base de datos GEO(Gene Expression Omnibus), bajo el identificador de acceso GSE131954, los cuales contienen medidas de abundancia normalizada específicas para los genes diferencialmente expresados (DEGs) de los ratones espaciales.  

Con el estudio de estos datos se busca contribuir a la disminución de la falta de análisis en la expresión genética en la biología espacial y conocer la relación de los procesos biológicos sobrerrepresentados con enfermedades asociadas al daño ocular en condiciones espaciales.  


## Preguntas de investigación

En este contexto, se plantean tres principales preguntas de investigación prioritarias:

> 1. ¿Cuántos genes están regulados de forma positiva y negativa en el grupo de vuelo en comparación con el grupo de control terrestre?
> 2. ¿Qué vías biológicas y categorías funcionales se encuentran sobrerrepresentadas entre los genes regulados positivamente y negativamente en la retina murina en respuesta a la exposición al vuelo espacial?
> 3. ¿Cómo obtener información adicional sobre genes de interés?

Además, se explorará 1 pregunta adicional que complementa y enriquece el enfoque del proyecto:
 
 > 4. ¿Cuáles son los factores de transcripción expresados ​​diferencialmente (DETF) que están regulados positivamente y qué implicaciones tienen en la expresión genética de la retina murina?
Dado que de los 600 genes expresados ​​diferencialmente (DEG), 29 son factores de transcripción, esta pregunta busca identificar cuáles de estos DETF están regulados positivamente y cómo podrían influir en la regulación general de la expresión genética en la retina bajo condiciones espaciales.

Estas preguntas de investigación contribuirán a comprender las adaptaciones de la retina murina frente a los desafíos del entorno espacial, con especial énfasis en los genes regulados positivamente y sus funciones biológicas. 

## Metodología

### A. Servidor y software

> Servidor: Servidor de la Licenciatura en Ciencias Genómicas de la UNAM campus Morelos. 

> Usuario: ednakrz  y ximenagp 

> Software:
- Lenguaje de programación: Python
- Control de versiones: Git y GitHub.
- Entorno de desarrollo: VSCode.

### B. Datos de Entrada 

Los datos de entrada fueron descargados desde NCBI y se encuentran en la carpeta data del presente repositorio

```
/home/ednakrz/BioPython/Proyecto_ExpresionMurina/Expresion_Genetica_RetinaMurina/data
.
├── Datos_complementarios
│   ├── archivo_prueba.txt
│   ├── DEGS_ProteinClasses.xlsx
│   └── Gene_Disease_Associations.xlsx
├── GSE131954_DESeq2_RR9_Ground_Ctrl_vs_Flight_DEGs.txt
└── T.txt
```


#### Metadatos de la carpeta de datos


> Versión/Identificador Adhesión GEO: GSE131954

> Fecha de descarga: 25/09/2024

| Archivo | Descripción  | Tipo |
|:--      |:--           |:--  |
| GSE131954_DESeq2_RR9_Ground_Ctrl_vs_Flight_DEGs.txt  | Medidas de abundancia normalizada específicas para los genes diferencialmente expresados (DEGs) de los ratones espaciales | Formato tsv |




#### Formato de los archivos



- ` GSE131954_DESeq2_RR9_Ground_Ctrl_vs_Flight_DEGs.txt` : formato tsv


```
RefSeq Symbol	baseMean	log2FoldChange	lfcSE	stat	pvalue	padj
1110002L01Rik	756.7442416	0.214392751	0.056488755	3.795317318	0.000147455	0.007749727
1110038D17Rik	559.5329736	0.196306528	0.056424089	3.479126231	0.000503052	0.01965955
1200016B10Rik	295.1970385	0.239538839	0.066717953	3.590320548	0.000330272	0.014560608
1300018I17Rik	242.7758952	-0.221981787	0.072266793	-3.07169834	0.002128447	0.055386346
1500004A13Rik	130.6192251	0.368513591	0.08898661	4.141225176	3.45E-05	0.002676788
1700027L20Rik	54.56851159	-0.954960107	0.179418409	-5.322531361	1.02E-07	2.02E-05
1700029J07Rik	230.7086566	0.299339956	0.088130097	3.396568987	0.000682364	0.024595056

```

Formato: 

DESeq2 es una herramienta que utiliza métodos estadísticos para analizar y normalizar datos de RNA-seq
> a. La primera línea es información del análisis de DESeq2.
 > Los atributos de cada columna son: 
>   1) Identificadores de transcripción
>   2) Valores medios base
>   3) Log 2 (cambio de pliegue)
>   4) Valores de error estándar (IfcSE)
>   5) Valores estadísticos de Wald
>   6) Valores P de la prueba de Wald
>   7) Valores P ajustados (padj)


## Resultados
 

### ¿Cuántos genes están regulados de forma positiva y negativa en el grupo de vuelo en comparación con el grupo de control terrestre?

OBJETIVO: Realizar un script que permita clasificar los genes de acuerdo a su regulación considerando el log2Fold Change.

Archivo(s):
- Archivo de entrada (TSV):
           Ejemplo: GSE131954_DESeq2_RR9_Ground_Ctrl_vs_Flight_DEGs.txt
           Contiene información tabular de expresión diferencial, incluyendo una columna log2FoldChange.
            
- Archivo(s) de salida:
            Los resultados se guardarán en archivos separados para genes regulados positivamente y negativamente en la carpeta results del presente repositorio.
  
**Algoritmo:** 

1. Leer el archivo de entrada: El archivo se lee como un DataFrame utilizando pandas.

2. Filtrar genes según el valor log2FoldChange:
- log2FoldChange > 0: Genes regulados positivamente.
- log2FoldChange < 0: Genes regulados negativamente.

3. Guardar resultados en archivos: Los genes filtrados se guardan en archivos separados con nombres que indican el tipo de regulación.

4. Imprimir estadísticas: Mostrar el número total de genes regulados positivamente y negativamente

**Solución:**

Análisis de genes regulados positivamente
```bash
python analisis_regulacion.py \
    -i ../data/GSE131954_DESeq2_RR9_Ground_Ctrl_vs_Flight_DEGs.txt \
    -o ../results/genes_regulacion.txt \
    -c log2FoldChange \
    -r positiva

```
Análisis de genes regulados negativamente
```bash
python analisis_regulacion.py \
    -i ../data/GSE131954_DESeq2_RR9_Ground_Ctrl_vs_Flight_DEGs.txt \
    -o ../results/genes_regulacion.txt \
    -c log2FoldChange \
    -r negativa
```

**Desglose del código:**

1. Argumentos desde la línea de comandos:

La función obtener_argumentos permite al usuario proporcionar:
        
       -i (ruta al archivo de entrada).
       -o (ruta del archivo de salida).
       -c (nombre de la columna para filtrar, por defecto log2FoldChange).
       -r (tipo de regulación, positiva o negativa).

2. Leer el archivo:

La función leer_archivo carga el archivo de entrada como un DataFrame utilizando pandas. Esto permite una manipulación eficiente de los datos tabulares.

3. Filtrar genes:
   
La función filtrar_genes aplica un filtro basado en el valor de log2FoldChange:

    - df[df[columna] > 0] para regulación positiva.
    - df[df[columna] < 0] para regulación negativa.

4. Guardar resultados:

La función guardar_genes guarda los genes filtrados en un archivo TSV utilizando pandas.

**Consideraciones:**

- Formato del archivo: El script asume que el archivo de entrada está separado por tabulaciones (\t). Si el archivo usa otro separador, actualiza el argumento sep en leer_archivo.

- Validación: Si el archivo de entrada no contiene la columna log2FoldChange, el script imprimirá un error y terminará.

- Automatización: Puedes crear un script adicional para ejecutar ambos análisis (positivo y negativo). 

**Resultados:**

- Se encontraron 286 genes regulados positivamente.
  
- Se encontraron 314 genes regulados negativamente.

### ¿Qué vías biológicas y categorías funcionales se encuentran sobrerrepresentadas entre los genes regulados positivamente y negativamente en la retina murina en respuesta a la exposición al vuelo espacial?

OBJETIVO: Realizar un análisis de sobrerrepresentación (ORA) para los genes regulados positivamente y negativamente, lo cual permitirá identificar las vías y respuestas biológicas favorecidas como consecuencia de la exposición a las condiciones espaciales.

**Archivo(s):**

Archivo de entrada: datos_genes.tsv (contiene los genes regulados positivamente o negativamente).
Archivo de salida: resultados_ora.csv (almacena los resultados del análisis de sobrerrepresentación).

**Algoritmo:**

1. Cargar los genes regulados: Leer los genes regulados del archivo de entrada y extraer sus identificadores únicos.

2. Realizar el análisis GO: Usar la herramienta GProfiler para realizar el análisis de sobrerrepresentación considerando las categorías de GO (procesos biológicos, funciones moleculares, componentes celulares), KEGG (vías metabólicas) y HP (categorías fenotípicas).

3. Filtrar resultados significativos: Seleccionar solo aquellos términos con un valor de FDR menor a 0.05.

4. Generar resumen de resultados: Identificar y listar las categorías más significativas para cada fuente.

5. Visualizar los resultados: Generar gráficos que muestren los términos más enriquecidos en cada categoría.

6. Guardar los resultados: Exportar los resultados significativos a un archivo CSV para análisis adicional.

**Solución:**

```bash
% python gen_ontology_ora.py [-h] -i INPUT -o OUTPUT [-g ORGANISMO]
```
**Descripciones de las funciones**

- obtener_argumentos(): Maneja los argumentos proporcionados en la línea de comandos para configurar el análisis, como el archivo de entrada, archivo de salida y el organismo.

- cargar_genes_desde_archivo(ruta_archivo): Lee un archivo tabular con datos de genes regulados, extrae los símbolos RefSeq únicos y elimina duplicados y valores nulos.

- realizar_analisis_go(genes, organismo='mmusculus')}: Realiza un análisis de sobre-representación (ORA) utilizando G:Profiler, considerando diversas categorías funcionales como GO, KEGG y HP.

- obtener_top_terminos_por_fuente(resultados_go, n_top=10): Obtiene los términos más significativos (menor FDR) para cada categoría funcional del análisis GO.

- guardar_resultados_en_archivo(resultados_go, archivo_salida): Guarda los resultados del análisis GO en un archivo CSV para consulta y análisis posterior.

**Consideraciones:**
- Formato del archivo: El archivo de entrada debe ser tabular (.csv o .tsv) y contener una columna llamada RefSeq Symbol con nombres válidos de genes.
- Validación: Verifica que los genes correspondan al organismo especificado y que la conexión a internet esté activa para el análisis GO mediante G:Profiler.
- Automatización: Asegúrate de tener instaladas las dependencias necesarias (pandas, gprofiler-official) y que el módulo personalizado graficas_GO esté disponible para ejecutar correctamente el análisis y generar gráficos.

**Resultados:**

- Positivo:

Genes regulados encontrados: 286

Se encontraron 97 términos GO:BP, 54 GO:MF, 41 GO:CC, 1 vías de señalización (KEGG), y 0 categorías fenotípicas (HP) con un FDR menor a 0.05.

Resultados del análisis GO: 193 categorías enriquecidas encontradas.

Términos más significativos por fuente:

GO:BP:
  - response to abiotic stimulus
  - cellular response to stress
  - response to unfolded protein
  - apoptotic process
  - response to topologically incorrect protein
  - cell death
  - programmed cell death
  - response to light stimulus
  - protein folding
  - regulation of biological process

GO:MF:
  - ion binding
  - small molecule binding
  - binding
  - protein-folding chaperone binding
  - metal ion binding
  - heat shock protein binding
  - protein binding
  - cation binding
  - Hsp70 protein binding
  - catalytic activity

GO:CC:
  - cytoplasm
  - membrane-bounded organelle
  - intracellular anatomical structure
  - organelle
  - intracellular membrane-bounded organelle
  - nucleoplasm
  - intracellular organelle
  - cytosol
  - nucleus
  - organelle lumen

KEGG:
  Antigen processing and presentation

HP:

- Negativo:

Genes regulados encontrados: 314

Se encontraron 418 términos GO:BP, 65 GO:MF, 127 GO:CC, 2 vías de señalización (KEGG), y 5 categorías fenotípicas (HP) con un FDR menor a 0.05.

Resultados del análisis GO: 617 categorías enriquecidas encontradas.

Términos más significativos por fuente:

GO:BP:

  - system development
  - multicellular organism development
  - neurogenesis
  - biological regulation
  - nervous system development
  - anatomical structure development
  - localization
  - transport
  - regulation of biological process
  - cellular process

GO:MF:

  - protein binding
  - binding
  - adenyl ribonucleotide binding
  - ATP binding
  - adenyl nucleotide binding
  - enzyme binding
  - purine ribonucleotide binding
  - ribonucleotide binding
  - purine ribonucleoside triphosphate binding
  - purine nucleotide binding

GO:CC:

  - cytoplasm
  - neuron projection
  - cellular anatomical entity
  - cell projection
  - organelle
  - plasma membrane bounded cell projection
  - intracellular anatomical structure
  - synapse
  - membrane-bounded organelle
  - cell junction

KEGG:

  - Phototransduction
  - Thyroid hormone signaling pathway

HP:

  - Progressive night blindness
  - Macular degeneration
  - Retinal degeneration
  - Abnormal visual electrophysiology
  - Peripheral visual field loss

  Gráfica de los procesos biológicos más representativos de los genes regulados positivamente:
  
![image](https://github.com/ximenakgp/Expresion_Genetica_RetinaMurina/blob/main/src/graphs/GO_BP_top_terms.png)

### ¿Cómo obtener información adicional sobre genes de interés?

OBJETIVO: Hacer uso de herramientas como Entrez para obterner información de los genes más importantes.

**Archivo(s):**     

El archivo de entrada debe ser un archivo tabular (.txt o .tsv) con columnas que incluyan RefSeq Symbol (nombres válidos de genes) y pvalue.

**Algoritmo:** 

1. Leer un archivo tabular con datos de expresión diferencial.
2. Filtrar los genes con mayor o menor significancia estadística según el valor de pvalue.
3. Conectar a Entrez usando un correo electrónico proporcionado por el usuario.
4. Realizar búsquedas en la base de datos NCBI seleccionada (por default, "gene") para obtener detalles de los genes filtrados.
5. Guardar los resultados en un archivo de texto.


**Solución:**

```bash
# Ejemplo de ejecución
python entrez_busqueda.py -i genes_expresion.txt -o resultados_entrez.txt -c 10 -s menor -e usuario@example.com -d gene
```

**Consideraciones:**

- Formato de los archivos: El archivo debe estar separado por tabulaciones (.tsv) y contener las columnas necesarias, especialmente RefSeq Symbol y pvalue.
- Validación: Verificar la existencia de las columnas esperadas antes de ejecutar el script. Asegurar que los genes filtrados sean válidos y que el correo electrónico proporcionado permita acceso a Entrez.
- Automatización: Manejo de excepciones para capturar errores en la lectura de archivos o en las conexiones a la base de datos.

**Resultados:** 

Se obtendrán los genes mayor o menor representados, como sea el caso que se haya elegido, y se obtendrá la información general que proporcione la base de datos en la que se buscó coincidencia. 

Ejp: 
1. A12M1
adenovirus-12 chromosome modification site 1C [Homo sapiens (human)]
Other Designations: Adenovirus-12 chromosome modification site-1q1
Chromosome: 1; Location: 1q42-q43
This record was discontinued.
ID: 4

## Análisis y Conclusiones

En este proyecto, se analizaron datos de expresión génica diferencial y se obtuvo información relevante sobre los genes más significativos utilizando herramientas bioinformáticas. El trabajo se enfocó en crear scripts que permitieron clasificar los genes de acuerdo a su regulación (positiva o negativa), hacer un análisis de sobrerrepresentación (ORA) de ontología génica (GO), vías y categorías fenotípicas y graficar las categorías mas representadas. Los resultados obtenidos indican que los genes regulados positivamente están asociados con importantes procesos biológicos como:  {response to abiotic stimulus, cellular response to stress, apoptotic process, cell death, programmed cell death, response to light stimulus}. El resultado anterior coincide con estudios realizados previamente que indican que estos procesos son los que desencadenan un daño oxidativo en la retina que genera apoptosis en este tejido. 
Además, el hecho de que se hayan identificado 5 categorías fenotípicas sugiere que los genes estudiados están relacionados con alteraciones en la función y estructura de la retina, lo cual tiene un impacto directo en la visión. Estas categorías fenotípicas representan manifestaciones clínicas o síntomas comunes en trastornos genéticos o enfermedades oculares específicas.

### Conclusión de lo que aprendimos: 

Gracias a este proyecto, aprendimos nuevas funciones de Python y Biopython, y aprendimos a gestionar y organizar mejor el trabajo colaborativo utilizando herramientas como la plataforma Github, que nos permitió separar las tareas por issues y project, lo que facilitó la idea de lo que cada integrante tenía que hacer.
También aprendimos sobre la gestión de la información al embarcarnos en la búsqueda de bases de datos y aprendimos a discernir sobre la información que nos podría ayudar y la que tenemos que filtrar. Por otro lado, reforzamos la implementación de búsqueda a través de línea de comando con herramientas como Entrez, para obtener información en las distintas bases de datos de NCBI.
Para mejorar este proyecto, se podría realizar un análisis más extenso sobre los genes más representados y automatizar los scripts para que puedan generar los archivos sin tener que correr el código dos veces, es decir una vez para cada tipo de regulación que nos interese. Entre las dificultades a las que nos enfrentamos, se encuentra la falta de tiempo, ya que por esa cuestión no pudimos terminar de contestar la pregunta 4 y por ende ya no usamos los datos de los factores de transcripción que se encuentran en la carpeta data. 
Sin embargo, la realización de este proyecto nos ha servido mucho como experiencia en el manejo de Python, Biopython y Github. Por lo que, en un futuro esperamos seguir desarrollando nuestras habilides a través de estas herramientas y lenguaje de programación. 

## Referencias
Overbey, E. G., Abraham, W., Seta Stanbouly, Nishiyama, N. C., Roque-Torres, G. D., Pecaut, M. J., Zawieja, D. C., Wang, C., Willey, J. S., Delp, M. D., Hardiman, G., & Mao, X. W. (2019). Spaceflight influences gene expression, photoreceptor integrity, and oxidative stress-related damage in the murine retina. Scientific Reports, 9(1). https://doi.org/10.1038/s41598-019-49453-x

Introduction to GO annotations. (2024). Gene Ontology Resource. https://www.geneontology.org/docs/go-annotations/


‌


‌

