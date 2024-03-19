## Introducción

Mientras seguias tu camino por el laberinto, Minios vuelve a aparecer frente a ti. Minos, enojado al ver que avanzas sin dificultad te dice: "De ahora en adelante no será tan sencillo avanzar". Se cierran los caminos y comienza a aparecer un grupo de soldados de piedra dispuestos a atacarte.


## Objetivo

Ahora no solo avanzarás, sino que también tendrás que luchar. Para esto debes separar cada suceso como un **evento** disinto. Por lo que tendrás que modificar el código que hiciste en la pregunta anterior. Ese código debe ser usado cuando se entregue como _input_ el evento **cartel**, mientras que cuando se entregue el evento **asalto** se debe luchar con los soldados.

Al inicio de tu código debes recibir tu **ataque** y **vida**, se entregará como un _input_ del tipo entero. luego de esto comenzarás a recibir **infinitos eventos** (hasta que se entregue el input **"FIN"**), los cuales como se mencionó con anterioridad se dividirán entre "asalto" y "cartel".

Cuado se entregue el evento **cartel** se mantendrá la lógica de la pregunta anterior, o sea si se recibe un evento cartel, se entregara un _input_ que indicara que hay escrito en el cartel y debes imprimir el texto corresponiente. Será un solo cartel por cada evento "cartel". 

Pero cuando se entregue el evento **asalto** se desencadenará la siguiente secuencia:

Primero se te entregará un entero que indicará la **cantidad de soldados** que te van a atacar, esta cantidad siempre será mayor o igual a 1. Los soldados atacaran en foma de iteración. Por cada iteración se te entregará el **ataque del soldado** con el que lucharás, este será un número entero. 
La condición de victoria es que **si tu ataque es mayor o igual al del soldado ganarás** y no pasará nada. En caso contrario, tendrás que **restarle a tu vida la diferencia obtenida entre el ataque del soldado y tu ataque** y pasaras a luchar con el siguiente soldado.

Si durante el evento de asalto **tu vida llega a 0 o menos** debes imprimir: 
```
Tal y como se menciona, nadie que haya entrado ha vuelto a salir...
```
y **terminar el loop de eventos** asi como el de las iteraciones de asaltos.  
**(Considerar que en este caso no se entregara un _input_ "FIN")**

En caso contrario, si superas el asalto con una **vida mayor a 0**, debes imprimir:
```
Logre superar el asalto!, seguire avanzando
```

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
