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

#### Comandes bàsiques

### Introducció a python

Llenguatge interpretat. Interprets de python
- **python3**
- **ipython** (depen del python3), versió amb format enriquit i amb colors.
- **jupiterlab** (va al navegador i treballar amb ipython),[cheatsheet JupiterLab](https://blog.ja-ke.tech/assets/jupyterlab-shortcuts/Shortcuts.png "cheatsheet JupiterLab"), ficarem per executarlo a la consola 

```jupiter lab``` 




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

##### ***Punts bàsics python***

- Python per defecte es **tipat dinàmic** (va be per programes petits, interactiva o exploratoria). Vol dir que una variable pot canviar de tipus durant el programa. **Exemple**

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

 Java es explícit, que vol dir que una variable durant tot el programa serà del mateix tipus durant tota l´execució.


		



		 
