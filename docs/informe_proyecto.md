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

<!-- Describir la problemática que se presenta, la situación que motiva la realización del proyecto/análisis y que está causando posibles inconvenientes. -->

El análisi de los datos paleontológicos en México es un area de investigación que ha sido muy poco explorada por la cominidad científica. A pesar de que la palontología es un área de investigación de suma importancia, ya que gracias a su estudio es que podemos conocer el pasado de los seres vivios que habitaron nuestro territorio nacional, permitiendonos conocer la evolución e historia de los organismos que estuvieron antes de los que ahora habitan dentro de la república. 

Sin embargo, es importante retomar este análisis de los restoso fósiles que se han descubierto en el territorio nacional, ya que apartir de el, es posible conocer la basta diversidad de organismo que habitaron en nuestro territorio, la relación filogenética que tinen unos con otros y de esta manera poder ver la evolución que han tenido las especies en regiónes específicas del país.

**Preguntas de investigación**  

1. Analizar la distribución de los fósiles en los diversos estados, para determinar cual es el estado con la mayor cantidad de ellos y evaluar a que se debe esto. 

2. Hacer filogenias de las entidades con mayor cantidad de fósiles. En este caso planeamos utilizar los nombres de los organismos, obtenidos por estados a partir del primer punto, y buscarlos en NCBI (con esearch) para posteriormente obtener sus IDs y buscar su información en la base de datos UnitProt y así poder hacer una filogénia. Todavía no tenemos claro que gen podríamos comparar pero buscamos esclarecerlo con la clasificación de los organismos por estado. 

3. La otra opción en la que pensamos es utilizar los datos de taxonomia de los organismos encontrados en la entidad con mayor cantidad de fósiles, para analizar que nos puede decir esto acerca de su historia evolutiva y de como ha ido cambiado el habitat y la distribución de esos organismos  a lo largo del tiempo, dado que estos datos son fósiles de diferentes edades geológicas principalmente entre el Cámbrico y el Pleistoceno. 

Generar este nuevo conocimiento es de gran utilidad (falta por terminar de tunear jajajaj)  

## Metodología

<!-- [Identificar y describir los diferentes datos de entrada con los que se cuenta, así como de dónde fueron descargados, el formato de los mismos, y las columnas con las que cuenta. Especificar si se utilizará un servidor en particular para trabajar, o herramientas para el desarrollo de la solución del análsis. Formular las preguntas biológicas que se busca resolver con el análisis de los datos para determinar las tareas a realizar por cada una de ellas.]


### A. Servidor y software

> Servidor: 

> Usuario: 

> Software: 

### B. Datos de Entrada 

Entendiendo los archivos de datos 

Los datos de entrada fueron descargados desde NCBI y se encuentran en RUTA DE LA CARPETA.

```
|-- data
|   |-- coli_genomic.fna
|   |-- coli.gff
|   |-- coli_protein.fna
|   |-- directorio.txt
|   `-- flagella_genes.txt
```
-->

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
