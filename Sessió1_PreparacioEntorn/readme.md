# Instalació disc dur SSD USB bootable amb Linux
## Pablo Garcia, Miquel Angel Bardají

### Hardware necessari
 - USB(3.0) de >= 4 gb Linux
 - ISO  (iso és un fitxer que té l'estructura d´un cd) El ordinador creurà que la ISO és un CD. → Instal·lador y un modo live(de prueba). 
 - HDD/SSD >= 256 GB → Aconsellats Crucial, SanDisk , Kingston, Samsung
 - Cable Sata 3.0 → USB 3.0

### Programari necessari (2 opcions)
1. **Màquina arranca en mode UEFI**, baixar la ISO de --> [Pop_Os](https://pop.system76.com/)   Instalador fàcil, No usa GRUB, sino systemd-boot. Alternativa Espanyola [Slimbook](https://slimbook.es/). El SystemBoot de la BIOS ha d'estar desactivat.

2. **Màquina NO arranca en mode UEFI o no es vol popups** baixar la ultima  [ISO de Ubuntu LTS ](https://ubuntu.com/download/desktop) 

 - [BalenaEtcher](https://www.balena.io/etcher/), per fer la còpia de la ISO al disc dur extraïble

### Passos a seguir per l'USB bootable

 1. Descarregar iso escollida.
 2. Executar el [BalenaEtcher](https://www.balena.io/etcher/), esculleixes la ISO(elegida) i t'assegures de triar el disc de 4 GB, **no el disc dur del PC**
 3. Arrancar amb el usb en lloc del disc dur. Amb la tecla que sigui per arrancar bios(F2/F1/F8/F9)
> **Firmware**, el software dins del hardware perquè funcioni.
>
> **Bios** - Basci Input/Output System - Mort al 2013 - Tabla Particions MBR
>
> **UEFI** - Universal EFI = EFI 20 Extensible Firmware Interface - Live - 
>  Tabla Particiones GPT: GUID Partition table
> UUID: Universal Unique ID
 3. Arrancar en **mode UEFI el usb** → Hi ha l´opció try demo, que és recomanable per provar si funciona el sistema operatiu abans de fer la còpia al ssd,  i les opcions a escollir, preferentment serien 
    · Software  Angles-Irlanda
    · Elegir keyboard-Español amb especificació català si volem
    - Escollir l´opciò **Clean Storm**, borra tots els fitxers , aquí agafes el disc dur extern. Aquest moment has de triar el disc dur (SSD) i no equivocar-te
    - No escollir l´opció encriptar el password, perque si hi ha un problema, des de fora es pot ajudar una mica més.

## Utilitats i comandes ubuntu

- INXI --> és una ordre que trobem en l'última versió d'Ubuntu i que ens mostra totes les especificacions de l´equip, des del sòcol del processador fins al nucli de sistema operatiu que estem fent servir passant pels processos oberts que està executant el sistema operatiu.

## Instal·lació d´una versió de Python diferent del sistema linux.
- Per saber la versió que tenim de Python,  escriure a la línia de terminal **python3 --version**.
   -  Per saber on és l'executable del teu python **which -a python3**. 
      - Es pot utilitzar **ls -lisah /bin/python3**, i es veu on es localitza l'executable i es veu quin executable realment utilitza, quant a la terminal escrivim python3. Al llistat pot sortir ***blau claret***, que vol dir que és executable.
	  
	  - Per poder instal·lar la nostra versió de python, necessitem saber on es troben els python de sistema, per no fer-los malbé. Posarem la comanda **echo $PATH | sed -E "s/:/\n/g"**.
	  
	  Per poder instal·lar la nostra pròpia versió de python, instal·larem [**Conda - Anaconda**](https://docs.conda.io/en/latest/ "**Conda**"), que és un software que ens permet dues coses:
	  
	     - **Gestor d'entorns**(virtual): Un directori amb llibreries i executables, aïllats de la resta.
	     - **Gestor de paquets** (*conjunt d´arxius necessaris per a un executable o llibreria(codi que es pot executar des de un executable)*).
	       
	L´instal·larem perque no permet requerir permis d'administrador (ideal per empreses)
	
	1.  Baixarem l'instal·lador de la pagina oficial de [Anaconda](https://www.anaconda.com/products/individual "Python") - **64-Bit (x86) Installer (544 MB)** *64-Bit(la quantitat de memoria que podem dirigir) (x86 *(Arquitectura Intel)*) Installer (544 MB)* .  Extensió sh (shell)
	2. Al instal·lador podem mirar dins el fitxer amb *less nom_fitxer*, i veiem quin codi hi ha.
	3. Executem "sh nom_fitxer.sh" i hem de fer: 
		> Do you accept the license terms? [yes|no]
		>[no] >>> yes
		>Anaconda3 will now be installed into this location:
		>/home/alumne/anaconda3
		>
		>  - Press ENTER to confirm the location
		>  - Press CTRL-C to abort the installation
		>  - Or specify a different location below
		> ...
		>Preparing transaction: done
		>Executing transaction: done
		>installation finished.
		>Do you wish the installer to initialize Anaconda3
		>by running conda init? [yes|no]
		>[no] >>> **yes**
		
	Un cop instal·lat i perquè s'adoni del canvi, **tanquem la terminal i la tornem a obrir**. Sinò et surt pots seguir aquest [tutorial](https://www.solvetic.com/tutoriales/article/8876-instalar-anaconda-en-ubuntu-20-04/)
		>Ajuda --> Ctrl-C (tancar proces amb linux)
		 
	 Si sense voler no ens ha parat a la pregunta conda init (hem apretat el enter mentre s´estaven descomprimint arxius) --> Llavors fiquem ./ conda_init (executable al directori actual, ens hem de ficar a "~/anaconda3/bin")
			
## Comandes bàsiques pel gestor Conda.

· [CheatSheet Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html) 


#### Comandes comprovacions previes a la instal·lació de python3
A l'arrancar el terminal et sortirà la paraula (base), és el intèrpret de Conda, i l'entorn base que crea sempre per defecte. Per poder sortir de l'intèrpret, NO ES *CTRL-C*, sinò es *Ctrl-D* (fi d'ordres de teclat), però això tanca el terminal, en tornar a obrir sortirà.

*Comprovacions*

- Per saber que tenim python d´anaconda, podem ficar la instrucció **which -a python3**, i veiem el nou python.
- Per saber on es conda, executem **which -a conda**.
- Per veure el propietari **ls -lisah /home/alumne/anaconda3/bin/conda**
- Comanda friki **ls -lisah $(which conda)**, la sortida de la comanda interior, es la entrada de la comanda més exterior.

**Comandes instal·lació**

· Instal·lació python --> 

    ```sudo conda install -n BIO anaconda python (directori oficial)```
    

#### Entorn JupiterLab

JupyterLab és una interfície d'usuari basada en web per a Júpiter del projecte i està estretament integrat a Adobe Experience Platform. Proporciona un entorn de desenvolupament interactiu perquè els científics de dades treballin amb Jupyter Notebooks, codi i dades.

· Instal·lació [Jupyter Lab](https://jupyter.org/). Comanda: 

    ```sudo conda install -n BIO conda-forge jupyter-lab (directori no oficial)```
    
**Area de treball** 

  2 modes de treball:
  
  --> 1 Edició
  
  --> 2 Comandes
				   
  2 tipus de cel·la: 
  
  --> Python (tecla ESC i despres'y'), serveix per codificar
  
  --> Markdown (tecla ESC i despres 'm'), serveix per documentar la codificació
		   
		   
**Abreviaturas**

	Shift+Intro --> Executar una cel·la i anar a la següent
	Ctrl + Intro --> Executar una cel·la i es queda a la mateixa.
	 

