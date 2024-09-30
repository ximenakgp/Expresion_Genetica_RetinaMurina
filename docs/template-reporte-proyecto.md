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

Con el estudio de estos datos se busca contribuir a la disminución de la falta de análisis en los procesos de expresión genética en la biología espacial y conocer la relación de los procesos moleculares que tienen los ratones con las enfermedades retinales desarrolladas en el orbe. 

## Preguntas de investigación 
Las preguntas de investigación que proponemos para el análisi de los datos son las sigueintes: 

1. ¿Qué procesos biológicos y funciones están alterados en los genes regulados positivamente en la retina murina durante la exposición al vuelo espacial, y cómo podrían estos cambios influir en la adaptación de la retina a las condiciones espaciales?

2. ¿Qué vías biológicas y categorías funcionales se encuentran sobrerrepresentadas entre los genes regulados positivamente en la retina murina en respuesta a la exposición al vuelo espacial?

3. ¿Cuáles de los 75 genes asociados con la retinitis pigmentosa muestran una regulación positiva en la retina murina durante la exposición al vuelo espacial y qué implicaciones podrían tener estos genes para la progresión de esta enfermedad bajo condiciones espaciales?

## Metodología

<!-- [Identificar y describir los diferentes datos de entrada con los que se cuenta, así como de dónde fueron descargados, el formato de los mismos, y las columnas con las que cuenta. Especificar si se utilizará un servidor en particular para trabajar, o herramientas para el desarrollo de la solución del análsis. Formular las preguntas biológicas que se busca resolver con el análisis de los datos para determinar las tareas a realizar por cada una de ellas.] -->


### A. Servidor y software

> Servidor: Servidor de la Licenciatura en Ciencias Genómicas de la UNAM campus Morelos. 

> Usuario: ednakrz  y ximenagp 

> Software: Chaac 

### B. Datos de Entrada 

Entendiendo los archivos de datos 

Los datos de entrada fueron descargados desde NCBI y se encuentran en RUTA DE LA CARPETA.

```
.
├── Datos_complementarios
│   ├── archivo_prueba.txt
│   ├── DEGS_ProteinClasses.xlsx
│   └── Gene_Disease_Associations.xlsx
├── GSE131954_DESeq2_RR9_Ground_Ctrl_vs_Flight_DEGs.txt
├── GSE131954_DESeq_RR9_Ground_Ctrl_vs_Flight_All.txt
└── T.txt
```


#### Metadatos de la carpeta de datos

<!-- 
> Versión/Identificador del genoma:  NC_000913.3

> Fecha de descarga: dd/mm/aaaa

>| Archivo | Descripción  | Tipo |
|:--      |:--           |:--  |
| coli_genomic.fna  | Secuencia de nucleotidos de E. coli  | Formato FastA |
| coli.gff.   | Anotación del genoma de E. coli  | Formato gff |
| coli_protein.faa | Secuencia de aminoacidos de las proteinas de E. coli | formato FastA|
| flagella_genes.txt | Genes con función relacionada al flagello en E. coli | lista |
| directorio.txt. | Archivo con nombres de personas | lista |

-->

#### Formato de los archivos

<!-- 

- `coli_genomic.fna` : formato FastA


```
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTG
GTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGAC
AGATAAAAATTACAGAGTACACAACATCCATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGT
```

Formato: 

> a. La primera línea es información de la secuencia. Primero viene el identificador del genoma.

> b. Después vienen varias líneas con la secuencia de nuclótidos del genoma completo.



- `coli.gff`: anotación de features en el genoma


El contenido del archivo es:

```
##gff-version 3
#!gff-spec-version 1.21
#!processor NCBI annotwriter
#!genome-build ASM584v2
#!genome-build-accession NCBI_Assembly:GCF_000005845.2
##sequence-region NC_000913.3 1 4641652
##species https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=511145

NC_000913.3     RefSeq  region  1       4641652 .       +       .       ID=NC_000913.3:1.>
NC_000913.3     RefSeq  gene    190     255     .       +       .       ID=gene-b0001;Dbx>
NC_000913.3     RefSeq  CDS     190     255     .       +       0       ID=cds-NP_414542.>
NC_000913.3     RefSeq  gene    337     2799    .       +       .       ID=gene-b0002;Dbx>
NC_000913.3     RefSeq  CDS     337     2799    .       +       0       ID=cds-NP_414543.>

```

Formato: 

> a. Es un formato gff tabular, es decir, cada dato es separado por tabulador.
> 
> b. Cada renglón en el formato gff es una elemento genético anotado en el genoma, que se le denomina `feature`, éstos features pueden ser genes, secuencias de inserción, promotores, sitios de regulación, todo aquello que este codificado en el DNA y ocupe una región en el genoma de  E. coli.

> c. Los atributos de cada columna par cada elemento genético son

>```
1. seqname. Nombre del cromosoma
2. source. Nombre del programa que generó ese elemento
3. feature. Tipo de elemento
4. start. Posición de inicio
5. end. Posición de final
6. score. Un valor de punto flotante
7. strand. La cadena (+ , - )
8. frame. Marco de lectura
9.  attribute. Pares tag-value, separados por coma, que proveen información adicional
```


#### Preguntas de investigación
> ¿Pregunta X?
Respuesta: Describir el trabajo que implica o pasos a seguir para resolver esta pregunta.



-->


## Resultados
 

<!-- ### X. Pregunta 

Archivo(s):     

Algoritmo: 

1. 

Solución: Describir paso a paso la solución, incluyendo los comandos correspondientes

```bash

```

-->




## Análisis y Conclusiones

 <!-- Describir todo lo que descubriste en este análisis -->


## Referencias
<!-- Registrar todas las referencias consultadas. Se sugiere formato APA. Ejemplo:
 
 [1] Frederick R. Blattner et al., The Complete Genome Sequence of <i>Escherichia coli</i> K-12.Science277,1453-1462(1997).DOI:10.1126/science.277.5331.1453
 
 -->
