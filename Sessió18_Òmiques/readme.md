# M15_UF2 Ciencies Òmiques
## Pablo Garcia, Miquel Angel Bardají

Omicas , es un sufix grec que significa molts, per treballar lleis de la genètica.


#### Introducció Òmiques


##### DOGMA CENTRAL DE LA BIOLOGIA MOLECULAR

La transcripció es ADN(**ATCG**) a ARN(**UTCG**) (doble sentit), mes la tradució que es de ARN a proteinas.

![[Dogma]](dogma.png "Dogma")



Com s'edita l'ADN, amb pyvers i amb la polimerasa que duplica la cadena.
Nosaltres tenim

* PCR: Per duplicar cadenes.

Diferències entre diferents assajos clínics.


- *in silico*: la més innovadora, es tracta de mètodes de simulació (ordinador). Es recullen dades, s'emmagatzemen i es creen models computacionals que permeten observar què passa si es canvien les condicions externes.

- *in vitro*: es fan sobre teixit aïllat, òrgans i/o cèl·lules i no impliquen l'ús d'organismes vius (animals/humans)
- *in vivo*: es realitzen sobre organismes vius (animals/humans).
En el cas de la indústria cosmètica no es permet l'experimentació en animals segons la normativa Regulation (EC) N° 1223/2009 (Capítol V, Art. 18), però si es realitzen a la indústria farmacèutica/productes sanitaris/medicina. En cosmètica, s'usen voluntaris (panellistes) que ofereixen, per dir-ho així, la seva pell perquè es realitzin assajos (test dermatològics, tape stripping, insult patch test)
- *ex viu*: en aquest cas s'usa teixit viu que ha estat creat de manera artificial al laboratori o donat per organismes vius. És una de les tècniques que reemplaça les tècniques in vivo en animals al sector de la cosmètica. Parlem d'algunes d'aquestes tècniques aquí, a l'article sobre les tècniques d'experimentació alternativa al testatge en animals



#### Python amb bio informàtica

La llibreria que utilitzarem es la [biopython](https://biopython.org/ "biopython"). Podem partir de la seva documentació que esta plantejada com un [Tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html "Tutorial")

S'utilizen dos tipus de fitxers

	1.- *BioPython.*
		- .fasta
		- .gb (gen basic)
	
	2.- *Busqueda de secuencias.* Expressiones regulares (Regexp)

	3.- *Alineamiento de secuencias.* 3 algoritmos principales

		- **Lineal**

		- **Global**

		- ** [BLAST](https://es.wikipedia.org/wiki/BLAST "BLAST") ** utilitza una matriu de substitució d'aminoàcids o nucleòtids per qualificar els seus alineaments. Aquesta matriu conté la puntuació (també anomenada score) que se li dóna en alinear un nucleòtid o un aminoàcid X de la seqüència A amb un altre aminoàcid I de la seqüència B.