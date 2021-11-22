# PANDAS

###### Instal·lacio Pandas a conda: [Instruccions](https://anaconda.org/anaconda/pandas)


Per fer una introducció a Pandas seguirem el tutorial oficial de [pandas 10 minutes](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html "pandas 10 minutes")


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
| . . . .|


***

  
  #### Series
  
  Te 3 característiques principals, de les múltiples que té
  
  1. Contingut inicialment amb el mateix tipus
  2. El dtype té que cubrir tots els continguts
  3. El index el pots configurar al meu gust, per defecte es  numèric, pero podem elegir d'un altre tipus segons el  cas.


No es molt normal, barrejar dades

Tres conceptes de dades diferents:

   ·**NaN**: Not a Number (infinit, Indeterminar). La dada esta calculada. Concepte matemàtic.
   
   ·**NA**:  Not Avalaible(No disponible). La dada no hi és, no existeix. Concepte estadístic.
   
   ·**None**:  És un objecte, per tant no és eficient.


Per eficiencia *Python* utilitza Nans quant vol dir NA.


Tipus de dades que s'utilitza a Pandas

 ·**dtype** = Data Type. Es un camp que utilitza NumPy.
   Numpy utilitza els seu propis tipus codificats al llenguatge de programació C, per eficiencia.
   
  *Exemple: float 64(bits)*
  

  ```python
ser = pd.Series([1, 3, 5, np.nan, 6, 8])
ser

```

>   0    1.0
>   
>   1    3.0
>   
>   2    5.0
>   
>   3    NaN
>   
>   4    6.0
>   
>   5    8.0
>   
>   dtype: float64




```python
ser = pd.Series([1, 3, 5, 6, 8])
ser
```



Si son uniformes el dtype tria un tipus de dades correctes.

 >   0    1
 >   
 >   1    3
 >   
 >   2    5
 >   
 >   3    6
 >   
 >   4    8
 >   
 >   dtype: int64
 >   




```python
ser = pd.Series([1, 3, 5, 6, 8], dtype=np.float32)
ser
```


Es pot forçar a un tipus de dades prefixat per nosaltres.

 >   0    1.0
 >   
 >   1    3.0
 >   
 >   2    5.0
 >   
 >   3    6.0
 >   
 >   4    8.0
 >   
 >   dtype: float32
 >   




```python
#les notes de dawbio amb series
student_list=["John","Mary","Lucy","Peter"]
grades_list = [7,9,8,4]
wants_dual_list = [False,True,False,True]
ser = pd.Series(grades_list)
ser
```


>    0    7
>    
>    1    9
>    
>    2    8
>    
>    3    4
>    
>    dtype: int64
>    


Creem una llista amb indexs propis.

```python
#index canviats a índex d'estudiants
ser = pd.Series(data=grades_list,index=student_list)
ser
```


 >   John     7
 >   
 >   Mary     9
 >   
 >   Lucy     8
 >   
 >   Peter    4
 >   
 >   dtype: int64
 >   

* * * 

  #### DataFrame
  
  
  Podem seguir l'exemple del tutorial [aqui](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#object-creation "aqui")

Com poder crear un dataframe a partir de 6 mesos diferents

![](dataframe.png)

Un altra forma de crear datasets, es nombrar totes les columnes i ficar la seva llista respectiva, que mostrarà aquesta columna.

![](dataframe2.png)

**Una excepció diferent a Java, al final veieu que hi ha una coma, que amb JAva donaria error, al python l'obvia i no li fa cas**

Aquesta segona dataframe, podem modificar-la perquè, alguna serie, exemple la A, no sigui sempre igual,  sinò que tingui alguns valors diferents.


```python
df3 = pd.DataFrame(

    {

        "A": [1.0] + [np.nan] * 3,

        "B": pd.Timestamp("20130102"),

        "C": pd.Series(1, index=list(range(4)), dtype="float32"),

        "D": np.array([3] * 4, dtype="int32"),

        "E": pd.Categorical(["test", "train", "test", "train"]),

        "F": "foo",

    }

)
df3
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>2013-01-02</td>
      <td>1.0</td>
      <td>3</td>
      <td>test</td>
      <td>foo</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>2013-01-02</td>
      <td>1.0</td>
      <td>3</td>
      <td>train</td>
      <td>foo</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>2013-01-02</td>
      <td>1.0</td>
      <td>3</td>
      <td>test</td>
      <td>foo</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>2013-01-02</td>
      <td>1.0</td>
      <td>3</td>
      <td>train</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>


A partir del exemple creat per nosaltres, amb les notes dels estudiants de DAWBIO i si volen fer dual, veurem les principals funcions del dataframe.

### Cheatsheet instruccions bàsiques.

* [DataFrame - Creació DataFrame a partir de les diferents llistres](#dataframe)
* [DTYPES - Obtenir el tipus de dades de totes les columnes](#dtypes)
* [HEAD - Obtenir les primeres files](#head)
* [TAIL - Obtenir les ultimes files](#tail)
* [SAMPLE - Obtenir una fila aleatoria](#sample)
* [T - Trasposar la taula, les columnes per taules i a la inversa](#T)
* [SORT_INDEX - Ordenar els indexs, tant per fila com per columna](#sort_index)
* [SORT_VALUES - Ordenar els valors, per la columna triada](#sort_values)
* [LOC - Cercar un valor concret dins la dataframe](#loc)
* [Coordenades - Sistema de coordenades](#coordenades)
* [MASKS - Mascares de sel·lecció](#mask)
* [Exemples: Treballant amb pandas i fitxer scimago](#scimagoexample)


<a name="dataframe"></a>


```python
#les notes de dawbio amb dataframe
student_list=["John","Mary","Lucy","Peter"]
grades_list = [7,9,8,4]
wants_dual_list = [False,True,False,True]
datos: dict[list] = {"grade": grades_list,
      "dual": wants_dual_list}
students_frame = pd.DataFrame(
    index=student_list,
    data = datos
)
students_frame
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


<a name="dtypes"></a>


```python
#Obtenim el tipus  de dades de cadascuna de les columnes.
students_frame.dtypes
```




    grade    int64
    dual      bool
    dtype: object


<a name="head"></a>

```python
#Obtindre les primeres 5 linees de la taula
students_frame.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>






```python
# Les primeres 2 files
students_frame.head(2)
```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


<a name="tail"></a>


```python
# Les últimes 2 files
students_frame.tail(2)
```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


<a name="sample"></a>


```python
# Linea aleatoria
students_frame.sample()
```




<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>

<a name="T"></a>



```python
# Trasposar la matriu
students_frame.T
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>John</th>
      <th>Mary</th>
      <th>Lucy</th>
      <th>Peter</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>grade</th>
      <td>7</td>
      <td>9</td>
      <td>8</td>
      <td>4</td>
    </tr>
    <tr>
      <th>dual</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Recupera el index (row names) i les columnes (column names)
# Atenció! No son funcions son atributs
print(type(students_frame.index))
```

    <class 'pandas.core.indexes.base.Index'>

<a name="sort_index"></a>



```python
#Ordenació per index axis=0 el index de la primera columna, axis=1 ordena els index de la primera columna (dual,grade)
students_frame_sorted = students_frame.sort_index(axis=1, 
                                                  ascending=True)
students_frame_sorted
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dual</th>
      <th>grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>False</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>True</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>False</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>True</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>


<a name="sort_values"></a>


```python
#Ordenació per valors axis=0 columnes 
students_grade_sorted = students_frame.sort_values(by=['grade'], 
                                                   axis=0, 
                                                   ascending=False)
students_grade_sorted
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>






<a name="coordenades"></a>

###### Sistema coordenades

El sistema de coordenades, amb dataframes comencen pel 0 i per indicar una coordenada es posa la fila primer  i llavors la columna.

** Regla nemotècnica (enfonsar-se i nedar)**  Primer et tires de cap i llavors vas nedant fins la columna.

```python
# Utilitzar sempre localització d'un atribut
# .loc rep 2 parametres('enfonsar-se','bucejar')
students_frame.loc["Lucy","grade"]
```

>  8




<a name="loc"></a>


###### busqueda de varis valors de diferents columnes


```python
#busqueda de mes d'una columna
students_frame.loc["Lucy",["grade","dual"]]
```




    grade        8
    dual     False
    Name: Lucy, dtype: object




```python
#si vull totes les columnes de Lucy fico un slice buit
students_frame.loc["Lucy",:]
```




    grade        8
    dual     False
    Name: Lucy, dtype: object




```python
#si vull totes les notes dels estudiants
students_frame.loc[:,"grade"]
```




    John     7
    Mary     9
    Lucy     8
    Peter    4
    Name: grade, dtype: int64




Ja hem utilitzat la funció **loc** , ficant el nom directamente de les files primer i les columnes despŕes. 

Amb les coordenades numèriques, tenim que anomenar el primer numero per columna i el segon per files.


```python
#La primera coordenada capbusada | i despres bucejo -> però amb numèrics.
students_frame.iloc[0,1]
```




    False




```python
#Les comandes at e iat son sinònimes de loc e iloc, però sol poden retornar un sol valor.
#at es una optimització

students_frame.at["Lucy","grade"]
```




>  8



```python
students_frame.iat[2,0]
```




>  8




```python
#Podemos devolver una lista de varias filas, devuelve una lista
students_frame.loc[["Mary","Lucy"],"grade"]
```




>    Mary    9
>    Lucy    8
>    Name: grade, dtype: int64




```python
type(students_frame.loc[["Mary","Lucy"],"grade"])
```


>    pandas.core.series.Series



```python
#Podem retornar una llista de varies files, i retorna una llista
students_frame.loc[["Mary","Lucy"],
                   ["grade","dual"]]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
students_frame.loc[students_frame.index,["grade","dual"]]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
#seleccionar totes les columnes i files
students_frame.loc[:,:]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
#no es recomanable, ficar el interval de columnes, encara que es po fer
students_frame["John":"Lucy"]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>


<a name="mask"></a>

###### Masks

```python

# Mask = Objecte que amaga tota la informació que no volem

students_pass = students_frame.loc[:,"grade"] >= 5
#creo mask amb estudiants que compleixen criteris
students_pass
```




>    John      True
>
>    Mary      True
>
>   Lucy      True
>
>   Peter    False
>
>   Name: grade, dtype: bool







```python
#a la mascara anterior la puc ficar per que seleccioni, sols els de la mask
students_frame.loc[students_pass,:]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
#sinonim
students_frame.loc[[True,True,True,False],:]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



<a name="scimagoexample"></a>


```python
# Read scimago ranking
entries: pd.DataFrame = pd.read_csv("scimagomedicine.csv", sep=";")
entries
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Sourceid</th>
      <th>Title</th>
      <th>Type</th>
      <th>Issn</th>
      <th>SJR</th>
      <th>SJR Best Quartile</th>
      <th>H index</th>
      <th>Total Docs. (2020)</th>
      <th>Total Docs. (3years)</th>
      <th>Total Refs.</th>
      <th>Total Cites (3years)</th>
      <th>Citable Docs. (3years)</th>
      <th>Cites / Doc. (2years)</th>
      <th>Ref. / Doc.</th>
      <th>Country</th>
      <th>Region</th>
      <th>Publisher</th>
      <th>Coverage</th>
      <th>Categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>28773</td>
      <td>Ca-A Cancer Journal for Clinicians</td>
      <td>journal</td>
      <td>15424863, 00079235</td>
      <td>62,937</td>
      <td>Q1</td>
      <td>168</td>
      <td>47</td>
      <td>119</td>
      <td>3452</td>
      <td>15499</td>
      <td>80</td>
      <td>126,34</td>
      <td>73,45</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Wiley-Blackwell</td>
      <td>1950-2020</td>
      <td>Hematology (Q1); Oncology (Q1)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>19434</td>
      <td>MMWR Recommendations and Reports</td>
      <td>journal</td>
      <td>10575987, 15458601</td>
      <td>40,949</td>
      <td>Q1</td>
      <td>143</td>
      <td>10</td>
      <td>9</td>
      <td>1292</td>
      <td>492</td>
      <td>9</td>
      <td>50,00</td>
      <td>129,20</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Centers for Disease Control and Prevention (CDC)</td>
      <td>1990-2020</td>
      <td>Epidemiology (Q1); Health Information Manageme...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>18991</td>
      <td>Nature Reviews Genetics</td>
      <td>journal</td>
      <td>14710056, 14710064</td>
      <td>26,214</td>
      <td>Q1</td>
      <td>365</td>
      <td>106</td>
      <td>325</td>
      <td>7332</td>
      <td>6348</td>
      <td>149</td>
      <td>21,22</td>
      <td>69,17</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Nature Publishing Group</td>
      <td>2000-2020</td>
      <td>Genetics (Q1); Genetics (clinical) (Q1); Molec...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>21318</td>
      <td>Nature Reviews Immunology</td>
      <td>journal</td>
      <td>14741741, 14741733</td>
      <td>20,529</td>
      <td>Q1</td>
      <td>390</td>
      <td>230</td>
      <td>436</td>
      <td>9421</td>
      <td>8200</td>
      <td>202</td>
      <td>17,33</td>
      <td>40,96</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Nature Publishing Group</td>
      <td>2001-2020</td>
      <td>Immunology (Q1); Immunology and Allergy (Q1); ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>71056</td>
      <td>MMWR. Surveillance summaries : Morbidity and m...</td>
      <td>journal</td>
      <td>15458636, 15460738</td>
      <td>19,961</td>
      <td>Q1</td>
      <td>100</td>
      <td>32</td>
      <td>48</td>
      <td>499</td>
      <td>2235</td>
      <td>48</td>
      <td>57,77</td>
      <td>15,59</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Centers for Disease Control and Prevention (CDC)</td>
      <td>2002-2020</td>
      <td>Epidemiology (Q1); Health Information Manageme...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7120</th>
      <td>7121</td>
      <td>25412</td>
      <td>Zhonghua kou qiang yi xue za zhi = Zhonghua ko...</td>
      <td>journal</td>
      <td>10020098</td>
      <td>NaN</td>
      <td>-</td>
      <td>14</td>
      <td>150</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>China</td>
      <td>Asiatic Region</td>
      <td>Zhonghua Yixuehui Zazhishe</td>
      <td>1987-2016, 2020</td>
      <td>Medicine (miscellaneous)</td>
    </tr>
    <tr>
      <th>7121</th>
      <td>7122</td>
      <td>21485</td>
      <td>Zhonghua liu xing bing xue za zhi = Zhonghua l...</td>
      <td>journal</td>
      <td>02546450</td>
      <td>NaN</td>
      <td>-</td>
      <td>31</td>
      <td>292</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>China</td>
      <td>Asiatic Region</td>
      <td>Zhonghua Yixuehui Zazhishe</td>
      <td>1982-2016, 2020</td>
      <td>Medicine (miscellaneous)</td>
    </tr>
    <tr>
      <th>7122</th>
      <td>7123</td>
      <td>26726</td>
      <td>Zhonghua nei ke za zhi [Chinese journal of int...</td>
      <td>journal</td>
      <td>05781426</td>
      <td>NaN</td>
      <td>-</td>
      <td>18</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>China</td>
      <td>Asiatic Region</td>
      <td>Zhonghua Yixuehui Zazhishe</td>
      <td>1957-1959, 1979-1997, 1999-2016, 2020</td>
      <td>Medicine (miscellaneous)</td>
    </tr>
    <tr>
      <th>7123</th>
      <td>7124</td>
      <td>19324</td>
      <td>Zhonghua wai ke za zhi [Chinese journal of sur...</td>
      <td>journal</td>
      <td>05295815</td>
      <td>NaN</td>
      <td>-</td>
      <td>16</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>China</td>
      <td>Asiatic Region</td>
      <td>Zhonghua Yixuehui Zazhishe</td>
      <td>1957, 1959-1964, 1979-2016, 2020</td>
      <td>Medicine (miscellaneous)</td>
    </tr>
    <tr>
      <th>7124</th>
      <td>7125</td>
      <td>20906</td>
      <td>Zhurnal Mikrobiologii Epidemiologii i Immunobi...</td>
      <td>journal</td>
      <td>03729311</td>
      <td>NaN</td>
      <td>-</td>
      <td>12</td>
      <td>53</td>
      <td>0</td>
      <td>1264</td>
      <td>0</td>
      <td>0</td>
      <td>0,00</td>
      <td>23,85</td>
      <td>Russian Federation</td>
      <td>Eastern Europe</td>
      <td>Izdatel'stvo S-Info</td>
      <td>1945-1947, 1954-2016</td>
      <td>Immunology; Medicine (miscellaneous); Microbio...</td>
    </tr>
  </tbody>
</table>
<p>7125 rows × 20 columns</p>
</div>




```python
entries.loc[:,"Rank"]
```




    0          1
    1          2
    2          3
    3          4
    4          5
            ... 
    7120    7121
    7121    7122
    7122    7123
    7123    7124
    7124    7125
    Name: Rank, Length: 7125, dtype: int64




```python
entries.loc[:,"Rank"].dtype
```




    dtype('int64')




```python
entries.dtypes
```




 >   Rank                       int64
 >   
 >  Sourceid                   int64
 >  
 >  Title                     object
 >  
 >  Type                      object
 >  
 >  Issn                      object
 >  
 >  SJR                       object
 >  
 >  SJR Best Quartile         object
 >  
 >  H index                    int64
 >  
 >  Total Docs. (2020)         int64
 >  
 >  Total Docs. (3years)       int64
 >  
 >  Total Refs.                int64
 >  
 >  Total Cites (3years)       int64
 >  
 >  Citable Docs. (3years)     int64
 >  
 >  Cites / Doc. (2years)     object
 >  
 >  Ref. / Doc.               object
 >  
 >  Country                   object
 >  
 >  Region                    object
 >  
 >  Publisher                 object
 >  
 >  Coverage                  object
 >  
 >  Categories                object
 >  
 >  dtype: object




```python
#us mostra els index de cada fila
entries.index
```




 >   RangeIndex(start=0, stop=7125, step=1)
 >




```python
#seleccionar i mostrar les entries amb H index superior
entries_high = entries.loc[:,"H index"] >= 450
entries_ok = entries.loc[entries_high,:]
entries_ok
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Sourceid</th>
      <th>Title</th>
      <th>Type</th>
      <th>Issn</th>
      <th>SJR</th>
      <th>SJR Best Quartile</th>
      <th>H index</th>
      <th>Total Docs. (2020)</th>
      <th>Total Docs. (3years)</th>
      <th>Total Refs.</th>
      <th>Total Cites (3years)</th>
      <th>Citable Docs. (3years)</th>
      <th>Cites / Doc. (2years)</th>
      <th>Ref. / Doc.</th>
      <th>Country</th>
      <th>Region</th>
      <th>Publisher</th>
      <th>Coverage</th>
      <th>Categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>15847</td>
      <td>New England Journal of Medicine</td>
      <td>journal</td>
      <td>00284793, 15334406</td>
      <td>19,889</td>
      <td>Q1</td>
      <td>1030</td>
      <td>1671</td>
      <td>4312</td>
      <td>15715</td>
      <td>82469</td>
      <td>1842</td>
      <td>19,08</td>
      <td>9,40</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Massachussetts Medical Society</td>
      <td>1945-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>15819</td>
      <td>Nature Medicine</td>
      <td>journal</td>
      <td>1546170X, 10788956</td>
      <td>19,536</td>
      <td>Q1</td>
      <td>547</td>
      <td>452</td>
      <td>953</td>
      <td>10601</td>
      <td>22548</td>
      <td>664</td>
      <td>23,52</td>
      <td>23,45</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Nature Publishing Group</td>
      <td>1995-2020</td>
      <td>Biochemistry, Genetics and Molecular Biology (...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>16590</td>
      <td>Lancet, The</td>
      <td>journal</td>
      <td>01406736, 1474547X</td>
      <td>13,103</td>
      <td>Q1</td>
      <td>762</td>
      <td>1488</td>
      <td>4593</td>
      <td>16580</td>
      <td>45581</td>
      <td>1227</td>
      <td>9,45</td>
      <td>11,14</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Elsevier Ltd.</td>
      <td>1823-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>29949</td>
      <td>Journal of Clinical Oncology</td>
      <td>journal</td>
      <td>15277755, 0732183X</td>
      <td>10,482</td>
      <td>Q1</td>
      <td>548</td>
      <td>583</td>
      <td>1890</td>
      <td>17448</td>
      <td>23642</td>
      <td>1221</td>
      <td>12,29</td>
      <td>29,93</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>American Society of Clinical Oncology</td>
      <td>1983-2020</td>
      <td>Cancer Research (Q1); Medicine (miscellaneous)...</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>22581</td>
      <td>Circulation</td>
      <td>journal</td>
      <td>00097322, 15244539</td>
      <td>7,795</td>
      <td>Q1</td>
      <td>607</td>
      <td>778</td>
      <td>2685</td>
      <td>22242</td>
      <td>26532</td>
      <td>1702</td>
      <td>9,48</td>
      <td>28,59</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Lippincott Williams and Wilkins Ltd.</td>
      <td>1950-2020</td>
      <td>Cardiology and Cardiovascular Medicine (Q1); P...</td>
    </tr>
    <tr>
      <th>69</th>
      <td>70</td>
      <td>15870</td>
      <td>Journal of Clinical Investigation</td>
      <td>journal</td>
      <td>00219738, 15588238</td>
      <td>6,278</td>
      <td>Q1</td>
      <td>488</td>
      <td>611</td>
      <td>1446</td>
      <td>32961</td>
      <td>16569</td>
      <td>1418</td>
      <td>10,27</td>
      <td>53,95</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>The American Society for Clinical Investigation</td>
      <td>1945-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>89</th>
      <td>90</td>
      <td>25454</td>
      <td>Blood</td>
      <td>journal</td>
      <td>15280020, 00064971</td>
      <td>5,515</td>
      <td>Q1</td>
      <td>465</td>
      <td>853</td>
      <td>2755</td>
      <td>26498</td>
      <td>22558</td>
      <td>2041</td>
      <td>7,41</td>
      <td>31,06</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>American Society of Hematology</td>
      <td>1946-2020</td>
      <td>Biochemistry (Q1); Cell Biology (Q1); Hematolo...</td>
    </tr>
    <tr>
      <th>113</th>
      <td>114</td>
      <td>85291</td>
      <td>JAMA - Journal of the American Medical Associa...</td>
      <td>journal</td>
      <td>15383598, 00987484, 00029955</td>
      <td>4,688</td>
      <td>Q1</td>
      <td>680</td>
      <td>1793</td>
      <td>5000</td>
      <td>14369</td>
      <td>30016</td>
      <td>2627</td>
      <td>5,46</td>
      <td>8,01</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>American Medical Association</td>
      <td>1883-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
  </tbody>
</table>
</div>




```python
#ensenyar les 5 primeres
#Ordenació per valors axis=0 columnes 
entries_top = entries_ok.sort_values(by=['H index'], 
                                                   axis=0, 
                                                   ascending=False)
entries_top = entries_top[0:5]
entries_top
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Sourceid</th>
      <th>Title</th>
      <th>Type</th>
      <th>Issn</th>
      <th>SJR</th>
      <th>SJR Best Quartile</th>
      <th>H index</th>
      <th>Total Docs. (2020)</th>
      <th>Total Docs. (3years)</th>
      <th>Total Refs.</th>
      <th>Total Cites (3years)</th>
      <th>Citable Docs. (3years)</th>
      <th>Cites / Doc. (2years)</th>
      <th>Ref. / Doc.</th>
      <th>Country</th>
      <th>Region</th>
      <th>Publisher</th>
      <th>Coverage</th>
      <th>Categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>15847</td>
      <td>New England Journal of Medicine</td>
      <td>journal</td>
      <td>00284793, 15334406</td>
      <td>19,889</td>
      <td>Q1</td>
      <td>1030</td>
      <td>1671</td>
      <td>4312</td>
      <td>15715</td>
      <td>82469</td>
      <td>1842</td>
      <td>19,08</td>
      <td>9,40</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Massachussetts Medical Society</td>
      <td>1945-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>16590</td>
      <td>Lancet, The</td>
      <td>journal</td>
      <td>01406736, 1474547X</td>
      <td>13,103</td>
      <td>Q1</td>
      <td>762</td>
      <td>1488</td>
      <td>4593</td>
      <td>16580</td>
      <td>45581</td>
      <td>1227</td>
      <td>9,45</td>
      <td>11,14</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Elsevier Ltd.</td>
      <td>1823-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>113</th>
      <td>114</td>
      <td>85291</td>
      <td>JAMA - Journal of the American Medical Associa...</td>
      <td>journal</td>
      <td>15383598, 00987484, 00029955</td>
      <td>4,688</td>
      <td>Q1</td>
      <td>680</td>
      <td>1793</td>
      <td>5000</td>
      <td>14369</td>
      <td>30016</td>
      <td>2627</td>
      <td>5,46</td>
      <td>8,01</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>American Medical Association</td>
      <td>1883-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>22581</td>
      <td>Circulation</td>
      <td>journal</td>
      <td>00097322, 15244539</td>
      <td>7,795</td>
      <td>Q1</td>
      <td>607</td>
      <td>778</td>
      <td>2685</td>
      <td>22242</td>
      <td>26532</td>
      <td>1702</td>
      <td>9,48</td>
      <td>28,59</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Lippincott Williams and Wilkins Ltd.</td>
      <td>1950-2020</td>
      <td>Cardiology and Cardiovascular Medicine (Q1); P...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>29949</td>
      <td>Journal of Clinical Oncology</td>
      <td>journal</td>
      <td>15277755, 0732183X</td>
      <td>10,482</td>
      <td>Q1</td>
      <td>548</td>
      <td>583</td>
      <td>1890</td>
      <td>17448</td>
      <td>23642</td>
      <td>1221</td>
      <td>12,29</td>
      <td>29,93</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>American Society of Clinical Oncology</td>
      <td>1983-2020</td>
      <td>Cancer Research (Q1); Medicine (miscellaneous)...</td>
    </tr>
  </tbody>
</table>
</div>
