# Transport Time Calculator

Este scri en python calcula los tiempos automáticamente para los transfers de golfistas.

Encontramos los principales destinos desde los que los golfistas se suelen mover más en la zona de Murcia, Alicante y Almería.
Se calculan los tiempos entre ellos según google maps para tener en cuenta el trayecto.

La recogida se calculará según el tee time sumando el tiempo de trayecto + 1 hora para que el jugador puesta estar con 1 hora de antelación para su check-in en el campo y para practicar. 
La vuelta se calculará según el número de jugadores que son, calculando que la partida durará 5 horas y 15 minutos, 
y sumando 10 minutos más por cada tee time extra. 
(si son 4 jugadores serán 5h y 15 min, si son 7 serán 5h, 15 min + 10min extra, y así)

Nos preguntará principalmente si queremos que nos calcule el tiempo automáticamente, si no queremos esta opción
podremos poner manualmente el tiempo de espera en el campo (por si quieren comer o salir más tarde o más temprano).

El ejectuable nos pedirá el destino de salida (por ejemplo el hotel en el que se alojan) y el destino al que quieren llegar (el campo de golf). 
Escribir el número del destino de salida y el número del destino al que han de ir.
Seguidamente nos pedirá la hora del tee time (la hora a la que tienen la partida de golf contratada).
El nº de jugadores es importante para calcular el tiempo de espera en el campo, ya que a más jugadores más tendrá que esperar el autobús).
Nos pedirá la fecha para poder imprimir todos los detalles de los servicios para mandarlos al cliente y la compañía de transfers.

Ante cualquier equívoco a la hora de poner los detalles escribir "back" para volver a realizar el servicio anterior.

Una vez terminado un servicio nos preguntará si queremos seguir añadiendo y podremos añadir hasta terminar el total de servicios de un mismo cliente 
para que nos salgan juntos, poder copiarlos y enviarlos a los destinatarios.

En el caso de los aeropuertos se ha hecho un formato especial.
Cuando el destino de salida es un aeropuerto nos pedirá la hora de salida del vuelo y el destino. Dejará en blanco el nº de vuelo.
En caso de que el destino de vuelta sea un destino nos pedirá la hora de salida del vuelo y calculará el trayecto + 2 horas,
para que el cliente esté con tiempo en el aeropuerto.



```bash
python3 transport_time_calculator.py
```

## Requisitos

- Python 3 (>= 3.6)
- No se requieren dependencias adicionales

## Ejecutar el Ejemplo

Ejecuta el archivo `transport_time_calculator.py` para ver un ejemplo de cómo usar el script.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un `issue` o envía un `pull request`.

## Seguridad

El código está diseñado para ser limpio y comprensible. No realiza operaciones de red ni de sistema de archivos.
