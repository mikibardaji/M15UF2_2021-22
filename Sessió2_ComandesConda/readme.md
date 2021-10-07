# Comandes per Conda (Gestor de entorns/Gestor de paquets) i primeres passes Python
##              <center>Pablo Garcia, Miquel Angel Bardají</center>


* [Comandes bàsiques gestor Conda](#conda)
* [Introducció Python](#python)

<a name="conda"></a>
## Comandes bàsiques pel gestor Conda.

#### Comprovacions previes
Al arrancar el terminal et sortira la paraula (base), és el interpret de conda.
Per poder sortir de l'interpret, NO ES CTRL-C, sinò es Ctrl-D (fi d'ordres de teclat), però això tanca el terminal, al tornar a obrir sortirà.
- Per saber que tenim python d´anaconda, podem ficar la instrucció **which -a python3**, i veiem el nou python.
- Per saber on es conda, executem **which -a conda**.
- Per veure el propietari **ls -lisah /home/alumne/anaconda3/bin/conda**
- Comanda friki **ls -lisah $(which conda)**, la sortida de la comanda interior, es la entrada de la comanda més exterior.
- **Crear el teu propi entorn** [tutorial](https://www.devacademy.es/entornos-virtuales-en-python-anaconda).

```conda create -n nombreenv python=x.x```

Per activarla, un cop ja es troba creada es 

```conda activate nombreEntorno```

Per desactivar l'entorn, trobant-nos al entorn s'utilitza 

```conda deactivate```

<a name="python"></a>
## Introducció a python

Llenguatge interpretat. Interprets amb els que podem treballar amb python
- **python3**
- **ipython** (depen del python3), versió amb format enriquit i amb colors. Versió no oficial de python
- **jupiterlab** (va al navegador i treballar amb ipython),[cheatsheet JupiterLab](https://blog.ja-ke.tech/assets/jupyterlab-shortcuts/Shortcuts.png "cheatsheet JupiterLab"), ficarem per executarlo a la consola 

```jupiter lab``` 

### ***Punts bàsics python***

#### Bibliografia Python

· [Tutorial pàgina oficial Python](https://docs.python.org/es/3/tutorial/)

· [Revolunet](https://pythonbooks.revolunet.com/)

· [Pildoras informaticas](https://www.youtube.com/watch?v=G2FCfQj-9ig)

· [Python cheatsheets](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)

- Python per defecte es **tipat implicit i dinàmic** (va be per programes petits, interactiva o exploratoria). Vol dir que no ens falta declarar el tipus de la variable al utilitzar per primer cop una variable(*implicit*), i una variable pot canviar de tipus durant el programa(*dinamic*). **Exemple**

```python
    var1 = 1;
    print (var1);
```
 > 1

 Canviem posteriorment i li assignem el String "Hola"
 ```python
     var1 = "Hola";
    print(var1);
```
> Hola

 **Java** es explícit i estatic, al definir la variable tens que dir, quin tipus és, i no pot canviar el seu tipus durant el cicle de vida del programa.



#### comandes bàsiques

* [Imprimir Pantalla](#print)
* [Declaracions funcions](#funcions)
* [If](#if)
* [Bucles for/while](#bucles)
* [Funció range](#range)
* [Operadors lògics](#logics)
* [Instrucció pass](#pass)
* [Llistes](#llistes)
* [Tuples](#tuples)
* [Diccionari](#diccionari)
    * [Exercicis amb diccionaris](#exercici_diccionari)
    * [Comprenhension](#comprenhension)
    * [Exercici Llistes amb comprenhension](#exercici2_comprenhension)
* [Slices](#slices)
* [Utilitat Ajuda python](#ajuda)

<a name="print"></a>
Imprimir per pantalla
```python
print("Hello World!");
```

>Hello World!

<a name="funcions"></a>
Declaracions de funcions
```python
In [3]: def say_hello():
...:     print("Hello World!!!")
...:     print("Dawbio")
...: 
In [4]:  say_hello():

```
>Hello World!!!
>Dawbio

**Tabulacions obligatories despres dels :** 
   Els claudàtors(corchetes) dels if's i del while, es substitueix per un tabulador.

<a name="if"></a>
##### **if**
El tabulador s´utilitza al if i al else
```python
if (s=="HOLA"):
    print ("HOLA")
elif (s=="Adios"):
   print("Era adios")
else:
    print("No es hola")
```


<a name="bucles"></a>
##### **bucles (while/for)**

***while***
El while funciona exactament igual que Java.

```python
count = 1
while (count <= 10):
    print(count)
    count += 1
```

***for***
Es diferent... ja que necessita un array inicialitzat.


```python
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)
```

Inicialitzem, el array amb la funció **range()**, ficant el punt d'inici(inclusiu) i el punt final(exclusiu)

```python
# Solution 3
numbers = range(1,11)
for number in numbers:
    print(number)
``` 
Segona forma de fer la inicialització

```python
for number in range(1,11):
    print(number)
``` 
<a name="range"></a>
**Range tiene tres formas:**
 1. Con 1 parámetro
 2. Con 2 parámetros
 3. Con 3 parámetros

Range devuelve un "Generador", no una lista. Si quiero una lista, tengo que convertirla, manualmente con list(...)

```python
list(range(10))

list(range(1, 11))

list(range(1, 11, 2))
``` 

<a name="logics"></a>
##### **Operadors lògics AND/OR/XOR/NOT**
A diferencia de java s'escriuen amb lletres
```python
if (n>2) AND (n<5):
    print ("esta entre 2 y 5")
elif (n>5) OR (n<2):
   print("Fora de 2 y 5")
else:
    print("es un altre cas")
```
<a name="pass"></a>
##### **pass**
Es la paraula per no fer cap acció dintre de un if
```python
if (n>2) AND (n<5):
    print ("esta entre 2 y 5")
else:
    pass
```

<a name="llistes"></a>
##### **llistes**

Comencen per 0, com a molts llenguatges.

```python
l1 = [0,1,2,3]
lx = [0,1,True,"Hola"]
```
Per saber la longitud d´una llista
```python
len(lx)
```

Diferencies amb java, la comilla i la comilla simple és el mateix

```python
l=["a","b","c"]
```

però serveix per poder ficar cometes dobles dins de la simple

```python
msg ='Dijo "Vete de asqui!"'
msg
```

> msg ='Dijo "Vete de asqui!"'

amb python "a" == 'a' es TRUE

<a name="tuples"></a>
#### **Tuples**

Tupla es una llista de sol lectura, millor no utilitzar
```python
t = ("a","b","c")
t
```

> ('a', 'b', 'c')

<a name="diccionari"></a>
#### **Diccionari**

Diccionari, Hash, Tabla Hash, Has Map, Mapa son tots sinònims. Es diferent de Arrays...

**Arrays**
|Claus   | Valors   |
| :------------: | :------------: |
|0   | "Roger"  |
| 1  |  "Dani" |
| 2  |  "Mar" |
| 3  |  "Albert" |
| 4  |  "Carlos" |

- Amb un diccionari les claus, poden ser del tipus que vulgui, no sol enters. *exemple: Strings*
- Les claus tenen que ser uniques, no pot haver-hi repetides.

**Diccionari**
|  Claus | Valors   |
| :------------: | :------------: |
|  "Roger" | 111  |
| "Dani"  |  222 |
| "Mar" |  223 |
| "Albert" | 342  |
| "Carlos" |  782 |

Nomenclatura per diccionaris
- () Brackets
- [] Square Brackets
- {} Curly Brackets
- <> Angle Brackets

```python
d = {"Roger": 111,
    "Dani":   234,
    "Mar":    342,
    "Albert": 567,
    "Carlos": 478 }
d["Roger"]
```
> 111

```python
for keys in d:
    print(keys)
```

>Roger

>Dani

>Mar

>Albert

>Carlos

<a name="exercici_diccionari"></a>
***Exercici 1*** Crear un nou diccionari on les claus del primer siguin els valors del segon i els valors, passin a ser les claus.

Per una de les possibles solucions al exercici s'introdueix un nou concepte el de comprenhension

<a name="comprenhension"></a>
##### **Comprenhension**
·Hi ha "Dict Comprenhensions" y "List Comprenhensions"
·Per a llegir o escriure una comprenhension, es comença pel mig (pel "for")
·Dict comprenhension

    ```d2 = {key:value for key,value in dictionary_source.items()```

·List comprenhension

    ```d2 = {elem for elem in List_source```

[Solucions exercici1](https://github.com/mikibardaji/M15UF2_2021-22/blob/main/Sessi%C3%B32_ComandesConda/exercici1.md "exercici1")

<a name="exercici2_comprenhension"></a>

***Exercici 2*** A partir d'una llista, del 1 al 10, crear una nova llista, amb els valors al quadrat

[Solucions exercici2](https://github.com/mikibardaji/M15UF2_2021-22/blob/main/Sessi%C3%B32_ComandesConda/exercici2.md "exercici2")



<a name="ajuda"></a>
**Documentació funcions**

Per saber totes les funcions associades al objecte es com java...
```
 nom_objecte. <Tab> -> Autocomplete
 nom_objecte.nom_funcio <Tab>+<Shift> Documentació de la funció
```
