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

· [Python cheatsheets begginners](https://ehmatthes.github.io/pcc/cheatsheets/README.html)

· [10 must have python cheatsheets](https://betterprogramming.pub/10-must-have-python-cheatsheets-2b74e8097bc3)



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
* [Arrays Avançats](#arraysup)
* [Bucles e indexs Avançats](#buclessup)
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

***Exercici 2*** A partir d'una llista, que va del 1 al 10, crear amb una linea , una nova llista, amb els valors al quadrat de la primera

[Solucions exercici2](https://github.com/mikibardaji/M15UF2_2021-22/blob/main/Sessi%C3%B32_ComandesConda/exercici2.md "exercici2")



<a name="slices"></a>
##### **Slices**

Es una opció per retallar diferents llistes, de maneres diferents.

```python
#Indexes = 0..7 (8 letters)
# len -1 = últim índex

slic = ["a","b","c","d","e","f","g","h"]
len(slic)

#del 2 al 7
slic[2:7]
```

> ['c', 'd', 'e', 'f', 'g']


```python
#del 2 al final
slic[2:len(slic)]
```

> ['c', 'd', 'e', 'f', 'g', 'h']

```python
#del 2 al final
slic[2:]
```

> ['c', 'd', 'e', 'f', 'g', 'h']

```python
# Del principi a la 5 lletra
slic[:5]
```

> ['a', 'b', 'c', 'd', 'e']

```python
#Tota la llista retornant una copia
slic[:]
```

> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


```python
#Si fiques un index fora de límits del array, no dona error outofBounds del segon índex
slic[2:2000]
```

> ['c', 'd', 'e', 'f', 'g', 'h']

```python
#Llegir tota una llista saltant de X en X, es un tercer parametre "step"
slic[0:8:2]
```

> ['a', 'c', 'e', 'g']

```python
#Índex negatius, comencen pel final de la llista. El -1 és el final de la llista.
slic[-1]
```

> 'h'

```python
#Puc fer rangs amb índexs negatius
slic[-8:-1]
```

> ['a', 'b', 'c', 'd', 'e', 'f', 'g']

```python
slic[-8:] #fins la h. No puc ficar el índex final
```

> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

```python
#Exemple avançat. Invertir una secuencia
slic[::-1]
```

> ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

```python
"Hola Mundo"[::-2]
```

> 'onMao'

<a name="arraysup"></a>
##### **Arrays avançats**

Hi ha 3 o més tipus de Strings. 

####### *Arrays Normals*

```python
s = "Hola Mundo. \n ¿Que tal estas?"
print(s)
```

> Hola Mundo. 
> ¿Que tal estas?

####### *Raw Strings No interpreta els càracters de ESCAPE*

```python
r = r"Hola Mundo.\n¿Que tal estàs?"
print(r)
```

> Hola Mundo.\n¿Que tal estàs?

####### *Format Strings. Van be per imprimir variables*

```python
name = "Bardaji"
name2 = "Pablo"
print("Hello " + name + " and hello " + name2)
frase_format = f"Hello {name} and hello {name2}"
print(frase_format)
```

> Hello Bardaji and hello Pablo

> Hello Bardaji and hello Pablo

<a name="buclesup"></a>
##### **Bucles avançats, recuperar el index i crear tuples**
Utilitzem normalment els index, si vols o necessites els índexs, utilitzem el while.

Si no ens fa falta el index utilitzem el for

Pero si volem saber els índexs utilitzant la instrucció for podemo utilitzar **enumerate**

```python
lista_index = ["a","b","c","d","e","f","g","h"]

for item in enumerate(lista_index):
    print(item)
```

> (0, 'a')
 
> (1, 'b')
 
> (2, 'c')
 
> (3, 'd')
 
> (4, 'e')
 
> (5, 'f')
 
> (6, 'g')
 
> (7, 'h')

Com ho fem si volem veure, per exemple el segon element de cadascuna de les tuples.

```python
for item in enumerate(lista_index):
    print(item[1])
```

> a

> b

> ..

> h

Si volem crear una llista de tuples podem fer...

```python
el = list(enumerate(lista_index))
el
```

> [(0, 'a'),  (1, 'b'),  (2, 'c'),  (3, 'd'),  (4, 'e'),  (5, 'f'),  (6, 'g'),  (7, 'h')]

Per poder mostrar amb el for, el primer o el segon element de cadascuna de les tuples podem fer

```python
for index, elem in enumerate(lista_index):
    print(elem)
```

> a

> b

> ..

> h


o veure el index

```python
for index, elem in enumerate(lista_index):
    print(index)
```
> 0

> 1

> ..

> 7

Altres utilitats, anomenar cada element d'un array amb una variable

```python
nombre, apellido1, apellido2 = ["Pablo","Garcia","Bardaji"]
print(nombre + "-" + apellido1 + "-" + apellido2)
```
> Pablo-Garcia-Bardaji

També si algunes posicions no ens interessen,  l'assigno a _, a tantes posicions com no m'interessin
```python
nombre, apellido1, _ ,_ = ["Pablo","Garcia","Bardaji","Dawbio"]
print(nombre + "-" + apellido1 )
```

> Pablo-Garcia

***Exercici 3*** Construir la llista de tuples amb un bucle while

[Solució exercici3](https://github.com/mikibardaji/M15UF2_2021-22/blob/main/Sessi%C3%B32_ComandesConda/exercici3.md "Solució exercici3")


<a name="ajuda"></a>
**Documentació funcions**

Per saber totes les funcions associades al objecte es com java...
```
 nom_objecte. <Tab> -> Autocomplete
 nom_objecte.nom_funcio <Tab>+<Shift> Documentació de la funció
```

Comentar linees amb java dins el codi, per indicar el tipus de les variables s'utilitza :
** Important ** Els dos ':' i el tipus de darrera, per python és sol comentari, no fa cas, la variable prendrà el tipus de valor que se li asigni, en cada moment

```python
a: int = 3
b: bool = True
# Los dos : y el tipo, para java es solo comentario, no hace caso, la variable tomará el tipo de valor en lo que almacenes
```
