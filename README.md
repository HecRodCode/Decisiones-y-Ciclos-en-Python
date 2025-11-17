# Decisiones y Ciclos en Python
## Diferencias entre un bucle controlado por contador y uno controlado por condición

|         | Controlado por contador | Controlado por condición | 
|---------|-----------|-----------|
| Definicion | Se repite un numero determinado de veces | Se repite mientras se cumpla una condición lógica | 
| Control | Usa una variable contador que se incrementa o decrementa con cada iteración | Depende de una expresión booleana que puede cambiar en cualquier momento | 
| Estructura | For con Range() | while |

## Ejemplos cotidianos con ciclos for y while
#### Ciclo for
1. Un ejemplo del ciclo for en la vida cotidiana podria ser cuando tenemos una lista de compras y quieres verificar que cada producto este ahi, lo que haces es mirar uno por uno los productos de la lista.
2. Subir escaleras también lo podriamos interpretar como un ciclo for, si sabes que un edificio tiene 10 escaleras normalmente nos proponemos a subir escalon por escalon hasta llegar al 10, de esa manera recorremos todos los escalones.
#### Ciclo while
1. Esperar el bus también se puede interpretar como un ciclo while. Cuando uno está en la parada, no sabe exactamente en qué momento va a llegar, así que lo único que hace es mirar la calle una y otra vez. Mientras el bus no aparezca, seguimos repitiendo esa acción: mirar, esperar, volver a mirar. Pero en el momento en que el bus llega, ya no seguimos esperando. De esa forma, el proceso se mantiene hasta que la condición cambia.
2. Comer papitas de una bolsa también es un buen ejemplo de un ciclo while. Cuando abres una bolsa no sabes cuántas papitas trae, simplemente empiezas a sacar una, luego otra, y sigues así mientras todavía queden dentro. El “ciclo” se mantiene mientras la bolsa no esté vacía. Pero cuando metes la mano y ya no sale ninguna papita, ahí termina todo, porque la condición dejó de cumplirse.

# ¿Cuándo es más apropiado usar for o while?
- **while**:
  Usamos el bucle while cuando la decisión de repetir el ciclo esta basada en una condición y no se conoce necesariamente cuantas veces se ejecutará. Se utiliza cuando la condicion que evalúa al inicio de cada iteración y el bucle continúa hasta que la condición sea falsa.
- **for**:
  El for lo utilizamos cuando se conoce de antemano cuántas veces se debe de ejecutar el bucle. Se usa comúnmente con funciones como range() o al iterar sobre colecciones de datos como listas, diccionarios, cadenas, etc.<br>
[Khan Academy](https://support.khanacademy.org/hc/es/articles/203327020--Cu%C3%A1ndo-uso-un-bucle-for-y-cu%C3%A1ndo-un-while)
# Bucles infinitos en Python
#### **Definición:**
Un bucle infinito es un ciclo en un programa que se ejecuta indefinidamente porque su condición de salida nunca se cumple, y es fundamental prevenirlo y detectarlo para evitar bloqueos y sobreuso de recursos en una aplicación.<br>
#### **Como prevenirlos:**
1. <ins><strong>Verificar condiciones de salida clara:</strong></ins> siempre hay que asegurarnos de que el ciclo tenga una condición que pueda cumplirse y que lleve a la terminación del bucle.
2. <ins><strong>Diseñar una buena lógica del bucle:</strong><ins> evitar errores lógicos como confundir operadores de asignación = con comparativos ==.
