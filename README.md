# Sistema de Supresión de Ruido de Red Eléctrica

> Presente su reporte aquí

1. Fs = 48000 Hz
2. La imagen prob2_a.png muestra el espectro completo, por otro lado al aumentar una region del mismo, en la figura prob2_b.png. Se observa que el espectro tiene simetría lo cual es esperado para una señal real.

3. La imagen prob3.png muestra los posibles armónicos de 60 Hz (n*60) como lineas punteadas. Se observa que las componentes en estos valores tienen un valor alto debido al ruido.

5. Se propone utilizar una cascada de varios filtros de orden 2 tipo 'notch' centrados en los distintos armónicos. Cada bloque tiene una respuesta en frecuencia 

H(z) = 1-2cos(w_o)z^-1+z^-2
       --------------------
       1-2*r*cos(w_o)z^-1+r^2*z^-2

se hace que r sea cercano a la unidad para que los polos y ceros se encuentren cercanos.

6. La respuesta en frecuencia se muestra en la figura prob5.png. Se observa como la magnitud cae en los valores armónicos deseados.

7. Utilizando la cascada de filtros se obtiene el audio en 'result.wav'

8. De una manera cualitativa se nota una disminución considerable del ruido de la línea de potencia, sin embargo si se compara con la señal de referencia, es posible escuchar aún la componente de 60 Hz, esto puede deberse a que la magnitud de ese bloque no es lo suficientemente baja para eliminarlo del todo como lo muestra la figura prob5.png