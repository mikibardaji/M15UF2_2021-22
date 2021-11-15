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
|-------------|


```python
ser = pd.Series([1, 3, 5, np.nan, 6, 8])
```
Dos conceptos diferentes
   ·**NaN** Not a Number (infinit, Indeterminar). La dada esta calculada. Concepte matemàtic.
   ·**NA**: Not Avalaible(No disponible). La dada no hi és, no existeix. Concepte estadístic.
   ·**None**  És un objecte, per tant no és eficient

Per eficiencia *Python* utilitza Nans quant vol dir NA