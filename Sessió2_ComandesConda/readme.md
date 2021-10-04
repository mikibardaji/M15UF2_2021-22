# Comandes per Conda (Gestor de entorns/Gestor de paquets)
##              <center>Pablo Garcia, Miquel Angel Bardají</center>

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


#### Comandes bàsiques

### Introducció a python

Llenguatge interpretat. Interprets amb els que podem treballar amb python
- **python3**
- **ipython** (depen del python3), versió amb format enriquit i amb colors.
- **jupiterlab** (va al navegador i treballar amb ipython),[cheatsheet JupiterLab](https://blog.ja-ke.tech/assets/jupyterlab-shortcuts/Shortcuts.png "cheatsheet JupiterLab"), ficarem per executarlo a la consola 

```jupiter lab``` 

##### ***Punts bàsics python***

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

[Tutorial pàgina oficial Python](https://docs.python.org/es/3/tutorial/)

#### comandes bàsiques
Imprimir per pantalla
```python
print("Hello World!");
```

>Hello World!

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

· **if**
El tabulador s´utilitza al if i al else
```python
if (s=="HOLA"):
    print ("HOLA")
elif (s=="Adios"):
   print("Era adios")
else:
    print("No es hola")
```

· **Operadors lògics AND/OR/XOR/NOT**
A diferencia de java s'escriuen amb lletres
```python
if (n>2) AND (n<5):
    print ("esta entre 2 y 5")
elif (n>5) OR (n<2):
   print("Fora de 2 y 5")
else:
    print("es un altre cas")
```

· **pass**
Es la paraula per no fer cap acció dintre de un if
```python
if (n>2) AND (n<5):
    print ("esta entre 2 y 5")
else:
    pass
```

. **llistes**
```python
l1 = [0,1,2,3]
lx = [0,1,True,"Hola"]
```
Per saber la longitud d´una llista
```python
len(lx)
```
