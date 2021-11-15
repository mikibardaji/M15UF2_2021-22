Seguirem el tutorial oficial de [pandas 10 minutes](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html "pandas 10 minutes")


Les primeres llibreries a importar son dues llibreries
 · **np** --> numerical panda, es una llibreria per a realitzar càlcul numèric
 · **pd** --> llibreria panda, es la llibreria per a gestionar i analitzar dades tabulars(dades que es troben amb forma de taula)

```python
import numpy as np 
import pandas as pd
```

 Panda utilitza dos tipus bàsics:
 1. **Series** , s'assembla a una llista.
 2. **DataFrame**, la tabla amb sí.
 
 
 *Exemple: Nem a crear una taula d'alumnes que volen fer la dual*
 
 **Series**
 ```python
names_list = ["John","Mary","Lucy","Peter"]
grades_ser=[7,9,8,4]
wants_dual_ser = [False, True, False, True]
```
**DataFrame**

| Name  | Grade  | Wants Dual   |
| ------------ | ------------ | ------------ |
|  John | 7  | False  |
|  Mary | 9  | True  |
|  Lucy | 8  | False  |
|  Peter | 4  | True  |

|Part dalt | ^Serie  | ^Serie   |
|. . . . . |


```python
ser = pd.Series([1, 3, 5, np.nan, 6, 8])
```
Dos conceptos diferentes

   ·**NaN** Not a Number (infinit, Indeterminar). La dada esta calculada. Concepte matemàtic.
   
   ·**NA**: Not Avalaible(No disponible). La dada no hi és, no existeix. Concepte estadístic.
   
   ·**None**  És un objecte, per tant no és eficient

Per eficiencia *Python* utilitza Nans quant vol dir NA.


Tipus de dades que s'utilitza a Pandas

·**dtype** = Data Type. Es un camp que utilitza NumPy.
   Numpy utilitza els seu propis tipus codificats al llenguatge de programació C, per eficiencia.
   
  *Exemple: float 64(bits)*
  
  
  #### Series
  
  Te 3 característiques principals, de les múltiples que té
  
  1. Contingut inicialment amb el mateix tipus
  2. El dtype té que cubrir tots els continguts
  3. El index el pots configurar al meu gust, per defecte es  numèric, pero podem elegir d'un altre tipus segons el  cas.

  ```python
ser = pd.Series([1, 3, 5, np.nan, 6, 8])
ser

```


No es molt normal, barrejar dades

   > 0    1.0
    1    3.0
    2    5.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64




```python
ser = pd.Series([1, 3, 5, 6, 8])
ser
```



Si son uniformes el dtype tria un tipus de dades correctes.

   > 0    1
    1    3
    2    5
    3    6
    4    8
    dtype: int64




```python
ser = pd.Series([1, 3, 5, 6, 8], dtype=np.float32)
ser
```


Es pot forçar a un tipus de dades prefixat per nosaltres.

 >   0    1.0
    1    3.0
    2    5.0
    3    6.0
    4    8.0
    dtype: float32




```python
#les notes de dawbio amb series
student_list=["John","Mary","Lucy","Peter"]
grades_list = [7,9,8,4]
wants_dual_list = [False,True,False,True]
ser = pd.Series(grades_list)
ser
```


>    0    7
>    1    9
>   2    8
>    3    4
>    dtype: int64


Creem una llista amb indexs propis.

```python
#index canviats a índex d'estudiants
ser = pd.Series(data=grades_list,index=student_list)
ser
```


 >   John     7
    Mary     9
    Lucy     8
    Peter    4
    dtype: int64


  #### DataFrame
  
  
  Podem seguir l'exemple del tutorial [aqui](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#object-creation "aqui")


![](dataframe.png)


