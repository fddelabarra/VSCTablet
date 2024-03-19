## Introducción

Escribir un texto que sirva como introducción o historia relacionada con el ejercicio. Esta sección debe ser omitida dentro de las interrogaciones. Debe ser contenido irrelevante para el desarrollo del ejercicio en sí, es decir, un texto o párrafo completamente opcional en su lectura.

## Objetivo

Descripción de lo que se busca realice el alumno, como realizar un algoritmo, definir una función o un objeto.

* Al escribir el nombre de una función u objeto, se debe usar monospace para ello. Además, se debe usar snake_case para funciones: ``nombre_de_funcion(parametro)`` y CamelCase para nombres de objetos: ``NombreDeObjeto``.

* Se debe **destacar en negrita** tan solo lo de vital importancia para el desarrollo del un algoritmo o funcionamiento de un ejercicio.

* Se debe evitar el "spanglish" y de usar términos necesarios en inglés como _input_ u _output_, utilizar cursivas.

Se debe mencionar si el _input_ será manejado de forma automática o no, utilizando el siguiente párrafo:

_"Los llamados a inputs serán manejados por nosotros, por lo que no debes preocuparte de recibir inputs. Solo deberás encargarte de definir la función/objeto ``nombre_funcion/NombreObjeto``. De todas formas, un ejemplo del flujo del programa sería:"_

En caso de entregar un archivo y que el alumno deba leerlo, el contenido del archivo será entregado como un input del ejercicio SOLO con fines de que el alumno pueda visualizarlo directamente en cada _test case_.

Además, este tipo de ejercicio debe mencionar en enunciado este comprotamiento de la siguiente forma:

_"En este ejercicio no se entregará un input. Sin embargo, en el campo de input se te mostrará el contenido de los archivos que debes leer."_

## Ejemplos

### Ejemplo 1

#### Input
```py
numero = 1234567
indice = 2
nuevo = 1
reversa = True
print(cantidad_de_digitos(numero))
print(en_posicion(numero, indice, reversa))
print(reemplazar(numero, indice, nuevo, reversa))
```

#### Output
```
J1 2
J1 4
J1 7
J1 0
```
**Explicación:** Se explica la lógica detrás de cómo se llegó a dicho _output_

### Ejemplo 2

#### Input
```
2
4
7
0
```

#### Output
```
J1 2
J1 4
J1 7
J1 0
```
**Explicación:** Se explica la lógica detrás de cómo se llegó a dicho _output_
