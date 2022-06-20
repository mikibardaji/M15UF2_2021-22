# Gràfiques amb Pandas

A estadística, existeixen 2 tipus:
  - Descriptiva (Gràfiques)
  - Inferencia (Previssions)

Per ajudar-nos en l'estadística que veurem, seria visualitzar i aprendre de la web [khan academy](https://es.khanacademy.org/ "khan academy").

Per realitzar gràfiques, tenim que instal·lar la llibreria **matplotlib**. Llibreria que utilitzara Pandas per sota, nosaltres no la cridarem

Per gràfiques utilitzarem la llibreria Matplotlib(baix nivell) que l'utilitzaran el panda's o seaBorn (alt nivell)

*Comandes d'instal·lació*

```shell
conda install -n py39 -c conda-forge matplotlib
```

A partir d'aqui seguirem el apartat de [plotting](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#plotting "plotting") al tutorial 10 minutes panda 


Codi realitzat



```python
import numpy as np 
import pandas as pd
#np --> numerical panda, es una llibreria per a realitzar càlcul numèric
#les notes de dawbio amb series
student_list=["John","Mary","Lucy","Peter"]
grades_list = [7,9,8,4]
wants_dual_list = [False,True,False,True]
datos: dict[list] = {"grade": grades_list,
                   "dual": wants_dual_list}
students_frame = pd.DataFrame(
    index=student_list,
    data = datos
)
students_frame.loc[:,"grade"].plot(kind="bar")
```




>   <AxesSubplot:>
>



![png](output_0_1.png)



```python
#no aconsellable
students_frame.loc[:,"grade"].plot(kind="pie")
```




>   <AxesSubplot:ylabel='grade'>
>



![png](output_1_1.png)



```python
# Continous vars, maje a dataframe with 2 columns
# Each column will have 100 random values (ints).
# Values will range from 0 to 100.


import numpy as np 
import pandas as pd

min_value = 0
max_value = 100

df = pd.DataFrame({ 'edad' : np.random.randint(min_value, max_value ,100),
    'nota' : np.random.randint(min_value, max_value , size=100)})
df.loc[:,"nota"].plot(kind="bar")
```




>    <AxesSubplot:>
>



![png](output_2_1.png)



