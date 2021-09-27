# Comandes per Conda (Gestor de entorns/Gestor de paquets)
## Pablo Garcia, Miquel Angel Bardají

## Comandes bàsiques pel gestor Conda.

#### Comprovacions previes
Al arrancar el terminal et sortira la paraula (base), és el interpret de conda.
Per poder sortir de l'interpret, NO ES CTRL-C, sinò es Ctrl-D (fi d'ordres de teclat), però això tanca el terminal, al tornar a obrir sortirà.
- Per saber que tenim python d´anaconda, podem ficar la instrucció **which -a python3**, i veiem el nou python.
- Per saber on es conda, executem **which -a conda**.
- Per veure el propietari **ls -lisah /home/alumne/anaconda3/bin/conda**
- Comanda friki **ls -lisah $(which conda)**, la sortida de la comanda interior, es la entrada de la comanda més exterior.

#### Comandes

Les treurem d´un [[cheatsheet de Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html# "cheatsheet de Conda")]
- Per saber tota la informació de la instal·lació de conda.

`conda info`
- Per actualitzar l'ultima versió

 `conda update -n base conda `
- Per crear un entorn de BIO 

      `conda create --name BIO `
- Per canviar d´entorn, i canvies a l'entorn que has creat.

    `conda activate BIO`
- Per desactivar 

  `conda deactivate`
- Per instal·lar paquets, per exemple de **python**,  La instrucció la trobem a google posant "install python en conda" i surt la instrucció. Aquesta instrucció es troba també al apartat *Using Packages and Channels del CheatSheet*

  `conda install -n BIO -c anaconda python`
- Per ***instal·lar jupiterLab***, busquem la instrucció també a google i l'apliquem al nostre entorn BIO 
- 
    `conda install -n BIO -c conda-forge jupyterlab`


		 
