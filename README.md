# Contador ATGC

Este es un script de Python diseñado para contar el numero de apariciónes que existen de las letras 'A,T,G,C' en un archivo .txt.

## Uso
El script acepta dos argumentos, el nombre del archivo a leer:
```
python archivo.txt
```
Donde `[archivo]` es el nombre del archivo que contiene las letras a sumar.

Y las letras específicas ha contar. 

## Salida

El script imprimirá la cantidad de pariciones que contó de las 4 letras por separado o imprimirá la aparición de la letra especificada por el usuario.

## Control de errores

Este código se centra en la rebición errores de dos tipos principalmente.

1. FileNotFoundError: Este error se maneja cuando el archivo especificado por el usuario no se puede encontrar o no existe en el sistema. En este caso, el programa imprimirá un mensaje de error indicando que no se pudo encontrar el archivo.
2. Excepciones genéricas: Se utiliza un bloque 'except' genérico para manejar cualquier otra excepción inesperada que pueda ocurrir durante la ejecución del programa. 

## Pruebas

El script no incluye un conjunto de pruebas unitarias.

## Datos
El script está diseñado para operar en archivos de texto plano. No hay restricciones en el número de líneas en el archivo.

## Metadatos y documentación
Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script, consulte [Enlace a la documentación].

## Código fuente
El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia [nombre de la licencia]. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [información de citación].

## Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: [ednakrz@lcg.unam.mx].
