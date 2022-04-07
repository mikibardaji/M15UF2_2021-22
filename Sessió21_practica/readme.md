## Pràctica i Examen final UF

Consistirà en diferents fitxers, a la pràctica els que vulguem, on haurem de descarregar fitxers genbank i explotar-los. Fer algunes alineacions.


### Enunciat Practica

1. Escoger organismo y gen (o genes) a comparar entre especies.
2. Descargar Genbanks usando Biopython Entrez.
3. Extraer información del GenBank, extraer alguna información usando Regexps.
4. Alinear Secuencias.
5. Mostrar resultados en forma de tablas de Pandas.

### Pe Òmiques

1. Lo mismo que la práctica
2. Saber navegar entre ficheros genBanks
3. Saber extraer información con Regexps
4. Saber alinear
5. Poner la información en tablas de Pandas.


Exemple:

Partint d'aquest, busqueu a la taxonomia, si es carnívor.
O busqueu els **autors d'aquest article amb expressions regulars**


###### Incís aclaratori

**API** - Application Program Interface

    1. Una llista de funcions que controla el programa.
    2. Exemples : 
       1. Android: ShowNotification(...,..,...)
       2. Colection de rutes: HTTP d'una aplicació web.
       3. Com es crida a una API 
    ![API](API.jpg "API")
       5. [Link metodos](https://developer.mozilla.org/es/docs/Web/HTTP/Methods "Link metodos")
       6. [github public apis](https://github.com/public-apis/public-apis "public apis")
   
   [Proves crida Api animechan](./3-apis/1-requests/animechan.py "crida animechan")


   ## NCBI BioPython

   Seguirem el tutorial de biopython, al capítol 9:

   1. [Biopython Tutorial oficial](http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec143 "biopython")
   
   Les instruccions que veurem seran

      1. **EInfo** Les instruccions 
      
   
   - [Prova 1 einfo](./3-apis/2-entrez/1-einfo/einfo-e1/einfo.py "einfo-e1")

   - [Prova 2 einfo](./3-apis/2-entrez/1-einfo/einfo-e2/einfo.py "einfo-e1")
    
      2. **ESearch** és un mètode get  (GET)
   
         1. [Prova 1 esearch](./3-apis/2-entrez/2-esearch/esearch-e1/esearch.py "esearch-e1")
   
         2. [Prova 2 esearch](./3-apis/2-entrez/2-esearch/esearch-e2/esearch.py "esearch-e2")
   
      3. **EPost** és un mètode post
   
      4. **EFetch** recoge los datos

         1. [Prova 1 efetch](./3-apis/2-entrez/3-efetch/efetch-e1/efetch.py "efetch-e1")

         2. [Prova 2 efetch](./3-apis/2-entrez/3-efetch/efetch-e2/efetch.py "efetch-e2")

         3. [Prova 3 efetch](./3-apis/2-entrez/3-efetch/efetch-e3/efetch.py "efetch-e3")

   ### Aligment (alineament)

    La teoria i les instruccions les seguirem a partir del document [python](./4-alignments/pairwise.py "pairwise")


   




