# Influencia de los vuelos espaciales en la expresión genética de la retina murina 

## Descripción del proyecto

El presente proyecto tiene como objetivo analizar la influencia de los vuelos espaciales en la expresión genética de la retina murina, utilizando datos obtenidos de un experimento realizado por la NASA con ratones como organismo modelo, los cuales fueron expuestos al entorno espacial durante 35 días a bordo de la Estación Espacial Internacional (ISS). Se busca determinar si el entorno espacial induce daño oxidativo en la estructura ocular y caracterizar los perfiles de expresión genética de la retina expuesta al vuelo espacial, proporcionando información crucial sobre los efectos de las condiciones espaciales en la salud ocular.

En este contexto, se plantean tres principales preguntas de investigación prioritarias:

1. ¿Cuántos genes están regulados de forma positiva y negativa en el grupo de vuelo en comparación con el grupo de control terrestre?

OBJETIVO: Realizar un script que permita clasificar los genes de acuerdo a su regulación considerando el log2Fold Change.
 
2. ¿Qué vías biológicas y categorías funcionales se encuentran sobrerrepresentadas entre los genes regulados positivamente y negativamente en la retina murina en respuesta a la exposición al vuelo espacial?  

OBJETIVO: Realizar un análisis de sobrerrepresentación (ORA) para los genes regulados positivamente y negativamente, lo cual permitirá identificar las vías y respuestas biológicas favorecidas como consecuencia de la exposición a las condiciones espaciales.
    
3. ¿Cómo obtener información adicional sobre genes de interés?

OBJETIVO: Hacer uso de herramientas como Entrez para obterner información de los genes más importantes.

Además, se explorará 1 pregunta adicional que complementa y enriquece el enfoque del proyecto:

4. ¿Cuáles son los factores de transcripción expresados diferencialmente (DETF) que están regulados positivamente y qué implicaciones tienen en la expresión genética de la retina murina?  
Dado que de los 600 genes expresados diferencialmente (DEG), 29 son factores de transcripción, esta pregunta busca identificar cuáles de estos DETF están regulados positivamente y cómo podrían influir en la regulación general de la expresión genética en la retina bajo condiciones espaciales.
 
Estas preguntas de investigación contribuirán a comprender las adaptaciones de la retina murina frente a los desafíos del entorno espacial, con especial énfasis en los genes regulados positivamente y sus funciones biológicas.

## Uso

```
python nombre_script.py
```

## Salida

El script imprimirá las categorías mas representadas o generará archivos con información relevante  

## Control de errores

Si el archivo proporcionado no existe, el script generará un mensaje de error. Del mismo modo, si el archivo contiene entradas que no son las adecuadas, el script generará un error.

## Pruebas

El script incluye un conjunto de pruebas unitarias almacenadas en la carpeta test.

## Datos

Los datos utilizados para este proyecto fueron obtenidos del noveno experimento de investigación de roedores de la NASA (RR-9), en el cual se llevaron ratones macho adultos C57BL/6 de diez semanas a bordo de la ISS durante 35 días y regresaron vivos a la Tierra, horas después a su amerizaje se recogieron tejidos oculares de los ratones para su análisis. Además se utilizaron ratones de control en tierra con condiciones ambientales idénticas. 

Utilizando RNA sequencing se detectaron 600 genes expresados diferencialmente (DEGs)  entre los grupos de vuelo espacial y control terrestre utilizando DESeq2. Dentro de los DEGs encontrados, se obtuvo que el grupo de vuelo espacial tuvo 286 genes regulados positivamente y 314 genes regulados negativamente en comparación con el control terrestre. Además se encontraron 75 genes asociados con la retinitis pigmentosa de los cuales se obtuvieron 12 que se expresaban de forma diferencial, siendo un resultado relevante para analizar esta enfermedad asociada a la retina.

Los conjuntos de datos generados y analizados durante el estudio están disponibles en el repositorio GEO, bajo el identificador de acceso GSE131954.

## Metadatos y documentación

Los datos de entrada fueron descargados desde NCBI

> Versión/Identificador Adhesión GEO: GSE131954

> Fecha de descarga: 25/09/2024

| Archivo | Descripción  | Tipo |
|:--      |:--           |:--  |
| GSE131954_DESeq2_RR9_Ground_Ctrl_vs_Flight_DEGs.txt  | Medidas de abundancia normalizada específicas para los genes diferencialmente expresados (DEGs) de los ratones espaciales | Formato tsv |

Para mayor información de los datos, favor de consultar el **informe del proyecto** ubicado en este repositorio GitHub. 


## Términos de uso

Este script está disponible bajo la licencia [MIT]. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [González,K.& Rivera,E.(2024)Expresion_Genetica_RetinaMurina. GitHub.https://github.com/ximenakgp/Expresion_Genetica_RetinaMurina.git].

## Integrantes del equipo
- Edna Karen Rivera Zagal
- Karla Ximena González Platas

## Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: [ximenagp@lcg.unam.mx][ednakrz@lcg.unam.mx].
