# Eines de test per millorar la codificació amb Python.


### pytest_ Suite( o framework) per a relitzar test unitaris



La instal·lació , es realitza amb la següent comanda.

`conda install .n py39 -c anaconda pytest`


Per provar crearem un fitxer q1.py

```python
def sum_nums(a: int,b:int) -> int:
	return a+b;
```

Crearem un fitxer q1_test, es important que tingui la paraula **test**

```python
import p1
def test_sum_nums():
	a: int = 1
	b: int = 2
	
	resultado = p1.sum_nums(a,b)
	assert resultado==3
```

***assert* **es una paraula clau, mai es fica la comprovació entre parentesis. Si el fiquessim amb parentesis , el pendria com una tupla *assert(resultado==3,"mensaje")*

Executem amb la instrucció *pytest* amb el fitxer de test i ens mostra totes les proves realitzades, amb verd si han anat be...


<pre>(py39) <font color="#4E9A06"><b>miki@pop-os</b></font>:<font color="#3465A4"><b>~/BIO-M15/test</b></font>$ pytest p1_test.py
<b>============================= test session starts ==============================</b>
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.9.0, pluggy-0.12.0
rootdir: /home/miki/BIO-M15/test
<b>collected 1 item                                                               </b>

p1_test.py <font color="#4E9A06">.                                                             [100%]</font>

<font color="#4E9A06">============================== </font><font color="#4E9A06"><b>1 passed</b></font><font color="#4E9A06"> in 0.12s ===============================</font>
(py39) <font color="#4E9A06"><b>miki@pop-os</b></font>:<font color="#3465A4"><b>~/BIO-M15/test</b></font>$ cat p1.py
</pre>

Modifiquem el fitxer, perque les variables valguin un , i la comprovació no doni i aixi comprovem com es veu quant no passa un test.

<pre>py39) <font color="#4E9A06"><b>miki@pop-os</b></font>:<font color="#3465A4"><b>~/BIO-M15/test</b></font>$ pytest p1_test.py
<b>============================= test session starts ==============================</b>
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.9.0, pluggy-0.12.0
rootdir: /home/miki/BIO-M15/test
<b>collected 1 item                                                               </b>

p1_test.py <font color="#CC0000">F                                                             [100%]</font>

=================================== FAILURES ===================================
<font color="#CC0000"><b>________________________________ test_sum_nums _________________________________</b></font>

    <font color="#48B9C7">def</font> <font color="#73C48F">test_sum_nums</font>():
    	a: <font color="#34E2E2">int</font> = <font color="#48B9C7">1</font>
    	b: <font color="#34E2E2">int</font> = <font color="#48B9C7">1</font>
    
    	resultado = p1.sum_nums(a,b)
&gt;   	<font color="#48B9C7">assert</font> resultado==<font color="#48B9C7">3</font>
<font color="#CC0000"><b>E    assert 2 == 3</b></font>

<font color="#CC0000"><b>p1_test.py</b></font>:7: AssertionError
=========================== short test summary info ============================
FAILED p1_test.py::test_sum_nums - assert 2 == 3
<font color="#CC0000">============================== </font><font color="#CC0000"><b>1 failed</b></font><font color="#CC0000"> in 0.05s ===============================</font>
</pre>


### formatejador de codi (autopep8(més flexible), yapt, black(menys flexible))

Eines per donar un format unitari a tot el codi.

autopep8, agafa totes les regles del PEP8 i t'avisa si no compleixes les normes i les formateja

> La PEP8 és una guia que indica les convencions estilístiques que cal seguir per escriure codi Python.


Provarem el formatejar black
La instal·lació és amb el canal conda-forge

    conda install -n py39 -c conda-forge black


### Validador de tipus

El que fa revisa el codi, com si fos el llenguatge **estatic**, per veure que no li assignes diferents tipus a una mateixa variable.
El validador de tipus, més famos es MyPy

    conda install -n py39 -c conda-forge mypy

Fem una prova al fitxer p1.py

<pre>(py39) <font color="#4E9A06"><b>miki@pop-os</b></font>:<font color="#3465A4"><b>~/BIO-M15/test</b></font>$ cat p1.py
def sum_nums(a: int,b:int) -&gt; int:
	return a + b -1


a: int = 1
a: boolean = true
(py39) <font color="#4E9A06"><b>miki@pop-os</b></font>:<font color="#3465A4"><b>~/BIO-M15/test</b></font>$ mypy p1.py
p1.py:6: <font color="#CC0000"><b>error:</b></font> Name <b>&quot;a&quot;</b> already defined on line 5
p1.py:6: <font color="#CC0000"><b>error:</b></font> Name <b>&quot;boolean&quot;</b> is not defined
p1.py:6: <font color="#CC0000"><b>error:</b></font> Name <b>&quot;true&quot;</b> is not defined
<font color="#CC0000"><b>Found 3 errors in 1 file (checked 1 source file)</b></font>
</pre>

Avisa en aquest cas, avisa que una variable ja esta definida, en linees anteriors. Et troba els errors, però  no els corregeix.

Afegir-los al visual studio code,  es marca  a settings la opció de mypy.

[![Instal·lació Visual codi](mypyvisualstudio.png "Instal·lació Visual codi")](mypyvisualstudio.png "Instal·lació Visual codi")

### linter 

Validador de codi, mes rígid que els altres validadors **Pylint**

    conda install -n py39 -c anaconda pylint

per executarlo es fica pylint p1.py, posem aquí el codi i el retorn que dona el linter


<pre>py39) <font color="#4E9A06"><b>miki@pop-os</b></font>:<font color="#3465A4"><b>~/BIO-M15/test</b></font>$ cat p1.py
def sum_nums(a: int,b:int) -&gt; int:
	return a + b -1


a: int = [1,2,3]

(py39) <font color="#4E9A06"><b>miki@pop-os</b></font>:<font color="#3465A4"><b>~/BIO-M15/test</b></font>$ pylint p1.py
************* Module p1
p1.py:2:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
p1.py:6:0: C0305: Trailing newlines (trailing-newlines)
p1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
p1.py:1:0: C0103: Argument name &quot;a&quot; doesn&apos;t conform to snake_case naming style (invalid-name)
p1.py:1:0: C0103: Argument name &quot;b&quot; doesn&apos;t conform to snake_case naming style (invalid-name)
p1.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
p1.py:1:13: W0621: Redefining name &apos;a&apos; from outer scope (line 5) (redefined-outer-name)

----------------------------------------------------------------------
Your code has been rated at -13.33/10 (previous run: -13.33/10, +0.00)
</pre>

Se'ns queixa que a la linea 2, hi ha una identació incorrecta.
A la linea 6, hi ha noves linees que no quadren.
A la linea 1 es queixa de que no hi ha el format camel-case



* * * * 
**Fora de tema**

Metodologíes de treball
· **Waterfall (cascada)**, vas fent tasques i al final fiques un dia d'entrega, sense mostra anteriorment.
 ·**Agiles**, vas fent entregues, millorant-les però anant fent entregues de mini demos ,cada un lapsus de temps, on anirem informant de les funcionalitats de cadascuna de les versions. Hi ha diferents opcions:
 
1. SCRUM
2. KANBAN (Els fluxos de treball poden ser una cosa tan senzilla com “Per fer”, “En curs” i “Terminat")
3. XP PROGRAMMING, programar per parelles. S'utilitza perque normalment la qualitat es més gran, ja que 4 ulls verifiquen més validacions que un mateix.
