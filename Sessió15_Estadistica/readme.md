
# Introducción a la Estadística

## Definiciones

- Informática: Es la ciencia que estudia cómo procesar la INFORmación automMÁTICAmente.

### Definiciones relacionadas con datos.
- Información: Todo aquello que nos interese.
- Dato: Unidad de información.

### Definiciones relacionadas con predicciones.
Aleatoriedad:
- Falta aparente de predecibilidad.
- El resultado de un suceso aleatorio sólo se puede conocer DESPUÉS de que ocurra el suceso.

Probabilidad:
- Medida de la certeza de que un suceso ocurra.
- Es un número real entre 0 y 1 SIEMPRE.
- 0 significa que el suceso es imposible.
- 1 significa que el suceso ocurrirá seguro.


## Definición de Estadística

La Estadística es una rama de las matemáticas.
Estudia dos cosas:
1. La variabilidad de los DATOS.
2. Los procesos aleatorios que generan estos datos, es decir la PROBABILIDAD.

En europa por el 1663, surgen los primeros escritos de estadística.
Estos escritos se refieren a la "ciencia del estado" porque tratan de decidir la política del estado en base a datos económicos y demográficos.

Bioestadística: Estadística aplicada a las ciencias de la vida.



# La ramas de la Estadística

1. Estadística descriptiva (se centra en los DATOS)
Un resumen de los datos.

2. Estadística inferencial (se centra en las probabilidades)
Extrapolar una información que tengo de unas muestras a toda la población.



# Pipeline de análisis de datos

1. Importar los datos
2. Ponerlos en formato tidy
3. Caja grande: Visualizar -> Tranformar -> Modelar   [EDA]
4. Comunicar

EDA = Exploratory Data Analysis. Análisis exploratorio de datos.
En EDA se trabajan las dos ramas de la estadística (descriptiva + inferencial)


# Relación entre datos y probabilidad

- Si tenemos datos observados -> Podemos intentar deducir las probablidades que tenían esos sucesos antes de ocurrir.
- Si tenemos las probablidades -> Podemos intentar predecir los sucesos que veremos en un futuro.



# Definiciones

- **Población**: El conjunto de elementos o sucesos que queremos estudiar.
- **Muestra**: El subconjunto de la población que podemos observar.
- **Variable**: Característica de la muestra que podemos medir.



# Tipos de variables

Hay dos tipos.

1. **Variables cuantitativas**: Se describen con números.
  - *Contínuas*: Hay un número infinito de valores. Ejemplo: Peso, altura.
  - *Discretas*: Hay un número finito (normalmente pocos) de valores. Ej: Número de hijos.

2. **Variables cualitativas**: Se describen con texto.
  - *Ordinales*: Tienen un orden implícito. Ej: Excelente > Notable > Bien > Suf
  - *Nominales*: No tienen un orden. Cáncer, Covid19, Sida, Ébola




# Frecuencias

El valor de una variable se le puede llamar también "frecuencia".

- **Frecuencia absoluta**: El valor absoluto.
- **Frecuencia relativa**: El valor dividido por el tamaño de la muestra.



## Conceptos básicos de la estadística descriptiva

En *[estadística descriptiva](https://es.wikipedia.org/wiki/Estad%C3%ADstica_descriptiva)* se utilizan distintas medidas para intentar describir las propiedades de nuestros datos, algunos de los conceptos básicos, son:

* **Media aritmética**: La [media aritmética](https://es.wikipedia.org/wiki/Media_aritm%C3%A9tica) es el valor obtenido al sumar todos los *[datos](https://es.wikipedia.org/wiki/Dato)* y dividir el resultado entre el número total elementos. Se suele representar con la letra griega $\mu$. Si tenemos una [muestra](https://es.wikipedia.org/wiki/Muestra_estad%C3%ADstica) de $n$ valores, $x_i$, la *media aritmética*, $\mu$, es la suma de los valores divididos por el numero de elementos; en otras palabras:

![Desviación](aritmetica.png "Desviación media")


* **Desviación respecto a la media**: La desviación respecto a la media es la diferencia en valor absoluto entre cada valor de la variable estadística y la media aritmética.

![Desviación](desviacionmedia.png "Desviación respecto la media")


* **Varianza**: La [varianza](https://es.wikipedia.org/wiki/Varianza) es la media aritmética del cuadrado de las desviaciones respecto a la media de una distribución estadística. La varianza intenta describir la dispersión de los *[datos](https://es.wikipedia.org/wiki/Dato)*. Se representa como $\sigma^2$. 

![Desviación](varianza.png "Varianza")


* **Desviación típica**: La [desviación típica](https://es.wikipedia.org/wiki/Desviaci%C3%B3n_t%C3%ADpica) es la raíz cuadrada de la varianza. Se representa con la letra griega $\sigma$.

![Desviación](tipica.png "Desviación típica")


* **Moda**: La <a href="https://es.wikipedia.org/wiki/Moda_(estad%C3%ADstica)">moda</a> es el valor que tiene mayor frecuencia absoluta. Se representa con $M_0$


* **Mediana**: La <a href="https://es.wikipedia.org/wiki/Mediana_(estad%C3%ADstica)">mediana</a> es el valor que ocupa el lugar central de todos los datos cuando éstos están ordenados de menor a mayor. Se representa con $\widetilde{x}$.


* **Cuantil**: Los [cuantiles](https://es.wikipedia.org/wiki/Cuantil) son puntos tomados a intervalos regulares de la función de distribución de una variable aleatoria. Las muestras se ordenan según sus valores de menor a mayor, y el cuantil es el valor en ese punto.


* **Valor atípico**: Un [valor atípico (outlier)](https://en.wikipedia.org/wiki/Outlier) es una observación que se aleja demasiado de la moda; esta muy lejos de la tendencia principal del resto de los datos. Pueden ser causados por errores en la lectura de los datos o medidas inusuales. Generalmente se recomienda eliminarlos.


##### Webs de referencia per complementar 

- [khan Academy amb Anglés](https://www.khanacademy.org/math/statistics-probability "khan Academy amb anglés")
- [khan Academy amb Castellà](https://es.khanacademy.org/math/statistics-probability "khan Academy amb castella")
- [Web per fer editors online](https://editor.codecogs.com/ "Web per fer editors online")

```python

```
