### Lectura de fitxers amb iteradors

|  Python v3.9 |
| :------------ |
|  cheatsheets|
|   Anaconda > Environments (Jupiter Lab)|
|   python > list,dict,set|

* * *

|  Iteradors |
| :------------ |
|  **Pros:** Ocupa molt poca memoria|
|  **Contres:** Sol es pot recorrer un sol cop|
|   No admet acces directe|
|   No puc donar marxa endarrera|

* * *

|  Implementació |
| :------------ |
|  Un iterador es qualsevol objecte que te dues funcions sempre|
|  **__iter__()** > Retorna un interador |
| **__next__()** |

* * *

|  Utilització |
| :------------ |
|  Per fitxers molts grans, es recomable, al utilitzar menys memòria file.readLine()|
|  Concatena càlculs (*programació funcional*) |

* * *

|  Paradigmes de la programació |
| :------------ |
|  Procedures utilitzen funcions impures |
|  *OOP* tenen totes funcions impures |
|  *Funcional* emprar el màxim possible de funcions impures(almenys 1  segur que hi ha) |


> Funcions pures: 
>  ·Sol llegeix dels seus paràmetres d'entrada
>  ·Sol escriu desde els seus paràmetres de sortida
>  ·Si pels mateixos paràmetres d'entrada sempre retorna els mateixos paràmetres d'entrada
> **Pros** 
> Són les més reutilitzables.
> Les més testejables
> Amb general, son les que tenen menys bugs


|  Yield  |
| :------------ |
|  Substitueix al return amb la diferencia que el yield , no fa acabar la funció guarda l'estat intern de la funció recorda el punt on s'estava executant, i quant la tornes a  crida comença a partir del yield, no del inici. |

|  Generator  |
| :------------ |
|  Un iterador creat per la paraula clau "yield" |
| Es comporta igual que un iterador creat a mà (té la funció __next__()) |

* *  *

| Programació funcional  |
| :------------ |
|  Per concatenar operacions fent 3 funcions bàsiques (sol treballar amb iteracions) |
| · map |
| · filter |
| · reduce (no sutilitza)* |
