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

En este contexto, se plantean dos principales preguntas de investigación prioritarias: 

> 1. ¿Qué procesos biológicos y funciones están alterados en los genes regulados positivamente en la retina murina durante la exposición al vuelo espacial, y cómo podrían estos cambios influir en la adaptación de la retina a las condiciones espaciales?
Para responder a esta pregunta, se realizará una anotación funcional de los genes regulados positivamente, con el objetivo de identificar los procesos biológicos alterados y comprender cómo estos cambios impactan la expresión genética en la retina.
> 2. ¿Qué vías biológicas y categorías funcionales se encuentran sobrerrepresentadas entre los genes regulados positivamente en la retina murina en respuesta a la exposición al vuelo espacial?
Se llevará a cabo un análisis de sobrerrepresentación (ORA) para los genes regulados positivamente, lo cual permitirá identificar las vías y respuestas biológicas favorecidas como consecuencia de la exposición a las condiciones espaciales.

 Además, se explorarán dos preguntas adicionales que complementarán y enriquecerán el enfoque del proyecto:

 > 3. ¿Cuáles de los 75 genes asociados con la retinitis pigmentosa muestran una regulación positiva en la retina murina durante la exposición al vuelo espacial y qué implicaciones podrían tener estos genes para la progresión de esta enfermedad bajo condiciones espaciales?
Esta pregunta permitirá evaluar si los genes vinculados con la retinitis pigmentosa se ven afectados por el entorno espacial, lo cual podría proporcionar nuevas perspectivas sobre la progresión de la enfermedad en este tipo de ambiente.
 > 4. ¿Cuáles son los factores de transcripción expresados ​​diferencialmente (DETF) que están regulados positivamente y qué implicaciones tienen en la expresión genética de la retina murina?
Dado que de los 600 genes expresados ​​diferencialmente (DEG), 29 son factores de transcripción, esta pregunta busca identificar cuáles de estos DETF están regulados positivamente y cómo podrían influir en la regulación general de la expresión genética en la retina bajo condiciones espaciales.

Estas preguntas de investigación contribuirán a comprender las adaptaciones de la retina murina frente a los desafíos del entorno espacial, con especial énfasis en los genes regulados positivamente y sus funciones biológicas.


## Metodología

<!-- [Identificar y describir los diferentes datos de entrada con los que se cuenta, así como de dónde fueron descargados, el formato de los mismos, y las columnas con las que cuenta. Especificar si se utilizará un servidor en particular para trabajar, o herramientas para el desarrollo de la solución del análsis. Formular las preguntas biológicas que se busca resolver con el análisis de los datos para determinar las tareas a realizar por cada una de ellas.] -->


### A. Servidor y software

> Servidor: Servidor de la Licenciatura en Ciencias Genómicas de la UNAM campus Morelos. 

> Usuario: ednakrz  y ximenagp 

> Software: Chaac 

### B. Datos de Entrada 

Los datos de entrada fueron descargados desde NCBI y se encuentran en RUTA DE LA CARPETA.

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
 > -Los atributos de cada columna son: 
>   1) Identificadores de transcripción
>   2) Valores medios base
>   3) Log 2 (cambio de pliegue)
>   4) Valores de error estándar (IfcSE)
>   5) Valores estadísticos de Wald
>   6) Valores P de la prueba de Wald
>   7) Valores P ajustados (padj)


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
