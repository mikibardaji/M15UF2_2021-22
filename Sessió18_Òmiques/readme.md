# M15_UF2 Ciencies Òmiques
## Pablo Garcia, Miquel Angel Bardají

Omicas , es un sufix grec que significa molts, en aquest cas moltes opcions per treballar sobre les lleis de la genètica.


#### Introducció Òmiques


##### DOGMA CENTRAL DE LA BIOLOGIA MOLECULAR

La transcripció es ADN(**ATCG**) que dona pas a les cadenes ARN(**UTCG**) (doble sentit), més la traducció que és la creació de proteïnes a partir de les cadenes d'ARN.

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
		- .gb (gen bank)
	
	2.- *Busqueda de secuencias.* Expressiones regulares (Regexp)

	3.- *Alineamiento de secuencias.* 3 algoritmos principales

		- **Lineal**

		- **Global**

		- ** [BLAST](https://es.wikipedia.org/wiki/BLAST "BLAST") ** utilitza una matriu de substitució d'aminoàcids o nucleòtids per qualificar els seus alineaments. Aquesta matriu conté la puntuació (també anomenada score) que se li dóna en alinear un nucleòtid o un aminoàcid X de la seqüència A amb un altre aminoàcid I de la seqüència B.


### Fichero fasta

	###  Ficheros Fasta

- Conté una(*archivo fasta*) o més(*archivo multifasta*) seqüències.

- Escritas como secuencias de ADN
| bases nitrogenades  |  Combinacions de totes  |
| ------------ | ------------ |
|  A T C G |  N· K · I |


Extreuem  fitxers FASTA de la web [NCBI](https://www.ncbi.nlm.nih.gov/ "NCBI")

Buscar al cercador de nucleòtids, la paraula COVID, per exemple

- **ORF** Open Reading Frame. ORFx , el numero x indica per quina base, tinc que començar per llegir una seqüència.

Cadena (Orf1)**G**(Orf2)**A**(Orf3)**TAGATA**

Per cada seqüència, hi ha dos coses:
1. Un comentari/descripció que comença per > i es una sola linea
2. La seqüència de bases dividides per línies de ...[70] caràcters pot variar.

Si es un fitxer MULTI-FASTA, és separa seqüència amb seqüència amb una linea de capçalera ( > ), 


#### Proves amb Mòdul Biopython 

 -->[biopython.ipynb](biopython.ipynb "biopython.ipynb")

 Tindrem que recordar la nomenclatura de -->[biopython.ipynb](https://iupac.org/ "biopython.ipynb")

 Per alguns dels exercicis, tindrem que tenir present la **traducció** [aminoacids_table](https://upload.wikimedia.org/wikipedia/commons/7/70/Aminoacids_table.svg"biopython.ipynb")

 Treballarem també amb el GENBANK de coronavirus.

 ### Fitxer GENBANK del coronaviurs

 Explicació de la fitxa general del fitxer de coronavirus, extret de ... [ncbi coronavirus](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512 "ncbi coronavirus")

 ![[severeacute]](severeacute.png "severeacute")
 
 **Locus** identificació

 · **29903** posició de la seqüencia en la que acaba la seqüència.
 · **DBLINK** projecte d'on ha sortit aquesta seqüència.
 · **ORGANISM** Diferents classificacions del coronavirus.
 · **Reference Authors** tots els que l'han seqüenciat
 · **Title** Títol del article on han publicat.
 · **JOURNAL** Mitjà on ho han publicat 
 · **PUBMED** link del article (si el volem llegir podem intentar buscar a SCI HUB)
 · **REFERENCE** de otras personas que han estat treballant sobre el tema.
 · **FEATURES** les diferents anotacions que tenen el fitxer.
  ![[anotacions]](anotacions.png "anotacions")
 · **ORIGIN** On comença la seqüencia

El fitxer // es el final d'un fitxer genbank

#### Aclaracions de la part de Features concret

 *5'UTR           1..265* no ho ha codificat
 *gene*                   
 *CDS*            Cadena codificant
 */translation*    Cadena proteïna