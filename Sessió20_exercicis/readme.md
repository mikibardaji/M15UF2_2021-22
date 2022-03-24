## Exercicis pràctica expressions regulars

Els exercicis els farem a partir [regex.eu](http://regex.sketchengine.eu "regex.eu")

Podem seguir l'explicació de classe o treure'l de la [tutorial regex](https://www.sketchengine.eu/guide/regular-expressions/ "tutorial regex")

Practicarem les 4 estràtegies
 1. Positiva
 2. Negativa
 3. Múltiples Regex
 4. Fer grups

#### Exercici 1

![Exercici1](ex1.png "Exercici1")

a) Ho fem inicialment ficant totes les parts positives i veiem els patrons.

 > pi, po, pat, p(espai)

b) Treure el patró d'aquestes parts úniques

 > p[aio ]t

 i d'aqui podem treure la solució

 > p.t


#### Exercici 2

![Exercici2](ex2.png "Exercici2")


a) Ho fem inicialment ficant totes les parts positives i veiem els patrons.

 > (ap.|ape|apt|ap\/|ap9|apo)[thr]

b) Treure el patró d'aquestes parts úniques

El patró positiu 

> ap.[th]

El patró negatiu

> ap.[^pd][^ ]

#### Exercici 3

![Exercici3](ex3.png "Exercici3")


