#  Exercici explotació fitxers CSV
##              <center>Pablo Garcia, Miquel Angel Bardají</center>

[Web font de dades Scimago ](https://www.scimagojr.com/journalrank.php?area=2700 "Web font de dades ")

#####  **Practica explotar un fitxer** i resoldre diferents consultes.

Fitxer de dades : [aqui](https://github.com/mikibardaji/M15UF2_2021-22/blob/main/sessio4_ExplotacioFitxersCSV/scimagomedicine.csv "aqui")


# Entries from SciMago

Para leer un fichero en python, utilizaremos una función que le pasaremos la ruta y retornarà una lista con todas las lineas del fichero.

```python
# How to define a function in python with the word key
# the type date after the : is only documentation for Python
def read_csv_file(csv_file_path: str) -> list:
    
    with open(csv_file_path, newline='') as csvfile:
        csv_reader=csv.DictReader(csvfile, delimiter=";")
        result = [row_dict for row_dict in csv_reader]
        
    return result
```

De esta forma llamamos a la función que nos devolverà el contenido.

```python
# Import notebook
# How to import a notebook a file

import csv
csv_file_path = "scimagomedicine.csv"
entries = read_csv_file(csv_file_path)
entries[0]       
```




>    {'Rank': '1',

>    'Sourceid': '28773',

>    'Title': 'Ca-A Cancer Journal for Clinicians',
   
>    'Type': 'journal',

>    'Issn': '15424863, 00079235',

>    'SJR': '62,937',

>    'SJR Best Quartile': 'Q1',

>    ...

>    'Categories': 'Hematology (Q1); Oncology (Q1)'}


** Exercici 1 ** Detectar tots els valors diferents de la columna Type.


```python
# Función que devuelve una lista de valores unicos de una lista con valores repetidos
def get_unique_type(lista:list) -> list:
    unique = []
    for entrada in entries:
        # print(entrada['Type'])
        if (not (entrada['Type'] in unique)):
            unique.append(entrada['Type'])
            
    return unique
```

I la crida seria... 

```python
# Buscar cuantos tipos de entradas hay diferentes
unicos = get_unique_type(entries)
print(unicos)
```

>   ['journal', 'book series', 'conference and proceedings', 'trade journal']


# Entries from SciMago



```python
# How to define a function in python with the word key
# the type date after the : is only documentation for Python
def read_csv_file(csv_file_path: str) -> list:
    
    with open(csv_file_path, newline='') as csvfile:
        csv_reader=csv.DictReader(csvfile, delimiter=";")
        result = [row_dict for row_dict in csv_reader]
        
    return result
```


```python
# Import notebook
# How to import a notebook a file

import csv
import re
csv_file_path = "scimagomedicine.csv"
entries = read_csv_file(csv_file_path)
# entries = entries[0:10]
entries[0]


```




>    {'Rank': '1',
>     'Sourceid': '28773',
>     'Title': 'Ca-A Cancer Journal for Clinicians',
>     'Type': 'journal',
>     'Issn': '15424863, 00079235',
>     'SJR': '62,937',
>     'SJR Best Quartile': 'Q1',
>     'H index': '168',
>     'Total Docs. (2020)': '47',
>     'Total Docs. (3years)': '119',
>     'Total Refs.': '3452',
>     'Total Cites (3years)': '15499',
>     'Citable Docs. (3years)': '80',
>     'Cites / Doc. (2years)': '126,34',
>     'Ref. / Doc.': '73,45',
>     'Country': 'United States',
>     'Region': 'Northern America',
>     'Publisher': 'Wiley-Blackwell',
>     'Coverage': '1950-2020',
>     'Categories': 'Hematology (Q1); Oncology (Q1)'}
>     




```python
# Función que devuelve una lista de valores unicos de una lista con valores repetidos
def get_unique_type(entries:list) -> list:
    unique = []
    for entrada in entries:
        # print(entrada['Type'])
        if (not (entrada['Type'] in unique)):
            unique.append(entrada['Type'])
            
    return unique
```


```python
# Buscar cuantos tipos de entradas hay diferentes
unicos = get_unique_type(entries)
print(unicos)
```

    ['journal', 'book series', 'conference and proceedings', 'trade journal']



```python
# Función que devuelve diccionario con los diferentes tipos y el numero de veces que aparece
def get_num_type(lista:list) -> dict:
    num_type = {}
    for entrada in lista:
        # print(entrada['Type'])
        if (not (entrada['Type'] in num_type)):
            num_type[entrada['Type']]=1
        else:
            num_type[entrada['Type']] = num_type[entrada['Type']] + 1
            
    return num_type
```


```python
diccionario = get_num_type(entries)
print(diccionario)
```

    {'journal': 6823, 'book series': 35, 'conference and proceedings': 262, 'trade journal': 5}



```python
# Función que devuelve una lista de valores unicos de una lista con valores repetidos
def get_unique_type2(entries:list) -> list:
    unique = []
    for entrada in entries:
        # print(entrada['Type'])
        if (not (entrada in unique)):
            unique.append(entrada)
            
    return unique
```


```python
#type(entries)
#type(entries[0])

listaTipos = [d["Type"] for d in entries]
l = get_unique_type2(listaTipos)
print(l)
```

    ['journal', 'book series', 'conference and proceedings', 'trade journal']



```python
#Buscar cuantas publicaciones de españa hay
#buscar cuabntas superan una tasa
#buscar cuantas publicaciones de cada tipo hay

import re

text = "python is, an easy;language; to, learn."
print(re.split('; |, ', text))

```

    ['python is', 'an easy;language', 'to', 'learn.']


### Exercici 6: Llistar totes les categories


```python
categorias: set = set() #Mejor así. Desambigua
for entrada in entries:
    lista = re.split(';', entrada['Categories']) #Separa, en función de los delimitadores que le pongas
    for cate in lista:
        posicion=cate.find(" (Q")
        if (posicion!=-1):
            cate = cate[:posicion]
        categorias.add(cate.strip())
        
#print(categorias)
#mylist = [x for x in iterable]
mylist = list(categorias)
mylist.sort()
i=1
for item in mylist:
    print(i,item,)
    i=i+1
```

   > 1 Acoustics and Ultrasonics
   > 2 Advanced and Specialized Nursing
   > ..
   > 286 Waste Management and Disposal
   > 287 Water Science and Technology


### Exercici 7: Categoría con más entradas


```python
categorias: dict = set() #Mejor así. Desambigua
dictionary = {}
for entrada in entries:
    lista = re.split(';', entrada['Categories']) #Separa, en función de los delimitadores que le pongas
    for cate in lista:
        posicion=cate.find(" (Q") # Elimino el texto trimestre
        if (posicion!=-1):
            cate = cate[:posicion]
        cate = cate.strip() #Elimino espacios por delante
        if cate in dictionary:
            dictionary[cate]+=1
        else:
            dictionary[cate]=1
dictionary2=dict(sorted(dictionary.items(), key=lambda item: item[1],reverse=True))
dictionary2
i=0
for key in dictionary2:
    i = i + 1
    if (i<=20):
        print((i),'-', key,':',dictionary2[key])
    else:
        break;
```




    {'Medicine (miscellaneous)': 2447,
     'Public Health, Environmental and Occupational Health': 560,
     'Psychiatry and Mental Health': 537,
     'Surgery': 456,
     'Neurology (clinical)': 373,
     'Oncology': 354,
     'Cardiology and Cardiovascular Medicine': 349,
     'Radiology, Nuclear Medicine and Imaging': 338,
     'Pediatrics, Perinatology and Child Health': 301,
     'Infectious Diseases': 292,
     'Orthopedics and Sports Medicine': 288,
     'Health Informatics': 274,
     'Health Policy': 256,
     'Pharmacology (medical)': 253,
     'Endocrinology, Diabetes and Metabolism': 232,
     'Pathology and Forensic Medicine': 206,
     'Immunology and Allergy': 197,
     'Pharmacology': 197,
     'Health (social science)': 195,
     'Clinical Psychology': 195,
     'Cancer Research': 184,
     'Obstetrics and Gynecology': 181,
     'Immunology': 176,
     'Biomedical Engineering': 172,
     'Computer Science Applications': 171,
     'Physical Therapy, Sports Therapy and Rehabilitation': 160,
     'Molecular Biology': 151,
     'Neurology': 146,
     'Genetics': 145,
     'Gastroenterology': 144,
     'Pulmonary and Respiratory Medicine': 139,
     'Dermatology': 138,
     'Internal Medicine': 131,
     'Cell Biology': 130,
     'Rehabilitation': 130,
     'Hematology': 129,
     'Computer Networks and Communications': 129,
     'Biochemistry': 128,
     'Ophthalmology': 124,
     'Anesthesiology and Pain Medicine': 122,
     'Microbiology (medical)': 121,
     'Biochemistry, Genetics and Molecular Biology (miscellaneous)': 120,
     'Geriatrics and Gerontology': 108,
     'Urology': 107,
     'Otorhinolaryngology': 107,
     'Physiology': 104,
     'Physiology (medical)': 103,
     'Endocrinology': 101,
     'Education': 98,
     'Epidemiology': 97,
     'Nutrition and Dietetics': 97,
     'Genetics (clinical)': 96,
     'Complementary and Alternative Medicine': 93,
     'Microbiology': 89,
     'Critical Care and Intensive Care Medicine': 88,
     'Sports Science': 87,
     'Artificial Intelligence': 87,
     'Molecular Medicine': 85,
     'Emergency Medicine': 85,
     'Developmental and Educational Psychology': 81,
     'Clinical Biochemistry': 78,
     'Neuroscience (miscellaneous)': 77,
     'Health, Toxicology and Mutagenesis': 76,
     'Information Systems': 74,
     'Biotechnology': 74,
     'Reproductive Medicine': 74,
     'Law': 69,
     'Toxicology': 68,
     'Instrumentation': 67,
     'Nephrology': 66,
     'Hepatology': 65,
     'Histology': 64,
     'Drug Discovery': 63,
     'Biophysics': 61,
     'Biochemistry (medical)': 59,
     'Rheumatology': 58,
     'Nursing (miscellaneous)': 57,
     'Pharmaceutical Science': 55,
     'Applied Psychology': 55,
     'Pharmacology, Toxicology and Pharmaceutics (miscellaneous)': 55,
     'Radiological and Ultrasound Technology': 53,
     'Signal Processing': 51,
     'Virology': 50,
     'Computer Vision and Pattern Recognition': 50,
     'Parasitology': 49,
     'Information Systems and Management': 49,
     'Bioengineering': 48,
     'Psychology (miscellaneous)': 48,
     'Food Science': 48,
     'Arts and Humanities (miscellaneous)': 47,
     'Safety, Risk, Reliability and Quality': 47,
     'Dentistry (miscellaneous)': 47,
     'Immunology and Microbiology (miscellaneous)': 45,
     'Electrical and Electronic Engineering': 45,
     'Cellular and Molecular Neuroscience': 44,
     'Family Practice': 43,
     'Transplantation': 42,
     'Health Information Management': 41,
     'Veterinary (miscellaneous)': 41,
     'Agricultural and Biological Sciences (miscellaneous)': 40,
     'Anatomy': 39,
     'Social Psychology': 39,
     'Biological Psychiatry': 37,
     'Advanced and Specialized Nursing': 37,
     'Ecology, Evolution, Behavior and Systematics': 37,
     'Cognitive Neuroscience': 37,
     'Issues, Ethics and Legal Aspects': 37,
     'Hardware and Architecture': 36,
     'Applied Microbiology and Biotechnology': 33,
     'Sensory Systems': 33,
     'Developmental Biology': 33,
     'Behavioral Neuroscience': 33,
     'Gerontology': 33,
     'Plant Science': 32,
     'Experimental and Cognitive Psychology': 32,
     'Neuropsychology and Physiological Psychology': 32,
     'Psychiatric Mental Health': 31,
     'Control and Optimization': 31,
     'Pollution': 30,
     'Community and Home Care': 29,
     'Biomaterials': 28,
     'Oral Surgery': 28,
     'Modeling and Simulation': 28,
     'Sociology and Political Science': 27,
     'Aging': 27,
     'Speech and Hearing': 27,
     'Animal Science and Zoology': 27,
     'Analytical Chemistry': 26,
     'Medical Laboratory Technology': 25,
     'Leadership and Management': 25,
     'Human-Computer Interaction': 25,
     'Chemistry (miscellaneous)': 24,
     'Philosophy': 24,
     'Management, Monitoring, Policy and Law': 23,
     'Environmental Science (miscellaneous)': 22,
     'Radiation': 22,
     'Social Sciences (miscellaneous)': 22,
     'Energy Engineering and Power Technology': 22,
     'Software': 21,
     'Mechanical Engineering': 21,
     'Organic Chemistry': 20,
     'Safety Research': 20,
     'Pharmacy': 20,
     'Emergency Nursing': 19,
     'History and Philosophy of Science': 19,
     'Anthropology': 19,
     'Engineering (miscellaneous)': 18,
     'Waste Management and Disposal': 18,
     'Pediatrics': 18,
     'Materials Science (miscellaneous)': 17,
     'Social Work': 17,
     'Endocrine and Autonomic Systems': 17,
     'Health Professions (miscellaneous)': 17,
     'Maternity and Midwifery': 17,
     'Applied Mathematics': 16,
     'Environmental Chemistry': 16,
     'Statistics and Probability': 16,
     'Ecology': 16,
     'Physical and Theoretical Chemistry': 16,
     'Medical and Surgical Nursing': 16,
     'Insect Science': 15,
     'Embryology': 15,
     'Media Technology': 15,
     'Developmental Neuroscience': 14,
     'Spectroscopy': 14,
     'History': 14,
     'Life-span and Life-course Studies': 13,
     'Environmental Engineering': 13,
     'Atomic and Molecular Physics, and Optics': 13,
     'Oncology (nursing)': 13,
     'Communication': 13,
     'Business, Management and Accounting (miscellaneous)': 13,
     'Computer Science (miscellaneous)': 13,
     'Electronic, Optical and Magnetic Materials': 13,
     'Nanoscience and Nanotechnology': 12,
     'Computer Graphics and Computer-Aided Design': 12,
     'Structural Biology': 12,
     'Industrial and Manufacturing Engineering': 12,
     'Agronomy and Crop Science': 12,
     'Computational Mathematics': 11,
     'Water Science and Technology': 11,
     'Strategy and Management': 11,
     'Critical Care Nursing': 11,
     'Occupational Therapy': 10,
     'Linguistics and Language': 10,
     'Control and Systems Engineering': 10,
     'Physics and Astronomy (miscellaneous)': 9,
     'Optometry': 9,
     'Renewable Energy, Sustainability and the Environment': 8,
     'Economics, Econometrics and Finance (miscellaneous)': 8,
     'Acoustics and Ultrasonics': 8,
     'Geography, Planning and Development': 8,
     'Gender Studies': 8,
     'Library and Information Sciences': 8,
     'Language and Linguistics': 8,
     'Chemical Engineering (miscellaneous)': 7,
     'Human Factors and Ergonomics': 7,
     'Aquatic Science': 7,
     'Management of Technology and Innovation': 7,
     'Cultural Studies': 7,
     'Management Science and Operations Research': 7,
     'Complementary and Manual Therapy': 7,
     'Religious Studies': 7,
     'Materials Chemistry': 6,
     'Inorganic Chemistry': 6,
     'Organizational Behavior and Human Resource Management': 6,
     'Public Administration': 6,
     'Multidisciplinary': 6,
     'Economics and Econometrics': 6,
     'Fundamentals and Skills': 6,
     'Pharmacology (nursing)': 6,
     'Research and Theory': 6,
     'Aerospace Engineering': 6,
     'Nuclear and High Energy Physics': 6,
     'Automotive Engineering': 6,
     'Computational Theory and Mathematics': 5,
     'Statistics, Probability and Uncertainty': 5,
     'Tourism, Leisure and Hospitality Management': 5,
     'Building and Construction': 5,
     'Assessment and Diagnosis': 5,
     'Care Planning': 5,
     'Condensed Matter Physics': 5,
     'LPN and LVN': 5,
     'Chemical Health and Safety': 5,
     'Chiropractics': 5,
     'Nuclear Energy and Engineering': 5,
     'Civil and Structural Engineering': 5,
     'Electrochemistry': 4,
     'Decision Sciences (miscellaneous)': 4,
     'Demography': 4,
     'Orthodontics': 4,
     'Food Animals': 4,
     'Development': 4,
     'Transportation': 4,
     'Mathematics (miscellaneous)': 4,
     'Podiatry': 4,
     'Emergency Medical Services': 4,
     'Nature and Landscape Conservation': 3,
     'Space and Planetary Science': 3,
     'Surfaces and Interfaces': 3,
     'Periodontics': 3,
     'Geochemistry and Petrology': 3,
     'Business and International Management': 3,
     'Marketing': 3,
     'Drug Guides': 3,
     'Mechanics of Materials': 3,
     'Ceramics and Composites': 2,
     'Analysis': 2,
     'Catalysis': 2,
     'Industrial Relations': 2,
     'Urban Studies': 2,
     'Soil Science': 2,
     'Colloid and Surface Chemistry': 2,
     'Surfaces, Coatings and Films': 2,
     'Visual Arts and Performing Arts': 2,
     'Process Chemistry and Technology': 2,
     'Music': 2,
     'Small Animals': 2,
     'Review and Exam Preparation': 2,
     'Earth and Planetary Sciences (miscellaneous)': 2,
     'Fluid Flow and Transfer Processes': 2,
     'Architecture': 2,
     'Discrete Mathematics and Combinatorics': 2,
     'Political Science and International Relations': 2,
     'Energy (miscellaneous)': 1,
     'Polymers and Plastics': 1,
     'Oceanography': 1,
     'Mathematical Physics': 1,
     'Statistical and Nonlinear Physics': 1,
     'Global and Planetary Change': 1,
     'Equine': 1,
     'Horticulture': 1,
     'Metals and Alloys': 1,
     'Archeology (arts and humanities)': 1,
     'E-learning': 1,
     'Computational Mechanics': 1,
     'Finance': 1,
     'Archeology': 1,
     'Ocean Engineering': 1,
     'Algebra and Number Theory': 1,
     'Medical Terminology': 1,
     'Astronomy and Astrophysics': 1,
     'Paleontology': 1,
     'Medical Assisting and Transcription': 1,
     'Management Information Systems': 1,
     'Geotechnical Engineering and Engineering Geology': 1,
     'Respiratory Care': 1}



    1 - Medicine (miscellaneous) : 2447
    2 - Public Health, Environmental and Occupational Health : 560
    3 - Psychiatry and Mental Health : 537
    4 - Surgery : 456
    5 - Neurology (clinical) : 373
    6 - Oncology : 354
    7 - Cardiology and Cardiovascular Medicine : 349
    8 - Radiology, Nuclear Medicine and Imaging : 338
    9 - Pediatrics, Perinatology and Child Health : 301
    10 - Infectious Diseases : 292
    11 - Orthopedics and Sports Medicine : 288
    12 - Health Informatics : 274
    13 - Health Policy : 256
    14 - Pharmacology (medical) : 253
    15 - Endocrinology, Diabetes and Metabolism : 232
    16 - Pathology and Forensic Medicine : 206
    17 - Immunology and Allergy : 197
    18 - Pharmacology : 197
    19 - Health (social science) : 195
    20 - Clinical Psychology : 195



```python
#5.- Ranking de paises por H-Index
#4.- Cual es publisher más antigui que aún publica, (tiene publicación el último año)
#3.- Agrupar publisher por numero de tipo de publicaciones
```

# Exercici 8 Todas las entradas de "Sports Medicine" o "Sports science"


```python
i=0
for entrada in entries:
    #if entrada['Categories'].find("Sports")!=-1:
    if "Sports" in entrada['Categories']:
        i=i+1
        print(entrada)
        
```

>    {'Rank': '121', 'Sourceid': '19817', 'Title': 'British Journal of Sports Medicine', 'Type': 'journal', 'Issn': '03063674, 14730480', 'SJR': '4,329', 
>    'SJR  Best Quartile': 'Q1', 'H index': '171', 'Total Docs. (2020)': '394', 'Total Docs. (3years)': '1156', 'Total Refs.': '11234', 'Total Cites (3years)': 
>    '7715', >'Citable Docs. (3years)': '668', 'Cites / Doc. (2years)': '5,97', 'Ref. / Doc.': '28,51', 'Country': 'United Kingdom', 'Region': 'Western Europe', 
>    'Publisher': >'BMJ Publishing Group', 'Coverage': '1964, 1974-2020', 'Categories': 'Medicine (miscellaneous) (Q1); Orthopedics and Sports Medicine (Q1); 
>    Physical Therapy, Sports Therapy and Rehabilitation (Q1); Sports Science (Q1)'}
>    ...

> {'Rank': '7091', 'Sourceid': '21101013588', 'Title': 'Journal of Spine Surgery', 'Type': 'journal', 'Issn': '2414469X, 24144630', 'SJR': '', 
> 'SJR Best Quartile': '-', 'H index': '4', 'Total Docs. (2020)': '127', 'Total Docs. (3years)': '0', 'Total Refs.': '4501', 'Total Cites (3years)': '0',
>  'Citable Docs. (3years)': '0', 'Cites / Doc. (2years)': '0,00', 'Ref. / Doc.': '35,44', 'Country': 'China', 'Region': 'Asiatic Region', 'Publisher': 
>  'AME Publishing Company', 'Coverage': '2020', 'Categories': 'Orthopedics and Sports Medicine; Surgery'}


# Exercici 9 Todas las regiones cubiertas por todas las entries


```python
regiones: dict = set() #Mejor así. Desambigua
for entrada in entries:
    regiones.add(entrada['Region'])
regiones
```




 >   {'Africa',
 >    'Africa/Middle East',
 >    'Asiatic Region',
 >    'Eastern Europe',
 >    'Latin America',
 >    'Middle East',
 >    'Northern America',
 >    'Pacific Region',
 >    'Western Europe'}



# Exercici 10 Media del H-Index por region


```python
# Función que devuelve una lista de valores unicos de una lista con valores repetidos
def actualizar_lista(entrada:list, valor:int) -> list:
    entrada[0] = entrada[0] + 1
    entrada[1] = entrada[1] + valor
    
            
    return entrada

def media(entrada:list) -> float:        
    return entrada[1]/entrada[0]


dictionary = {}
for entrada in entries:
    region = entrada['Region']
    if region in dictionary:
        dictionary[region] = actualizar_lista(dictionary[region], int(entrada['H index']))
    else:
        dictionary[region]=[1]
        dictionary[region].append(int(entrada['H index']))

for entrada_diccionario in dictionary:
    print(entrada_diccionario,'-', media(dictionary[entrada_diccionario]))

```

>    Northern America - 65.21652816251154
>    Western Europe - 54.08188428706924
>    Asiatic Region - 21.913719943422915
>    Pacific Region - 28.87704918032787
>    Eastern Europe - 12.408415841584159
>    Middle East - 19.862962962962964
>    Africa/Middle East - 26.017241379310345
>    Latin America - 18.331550802139038
>    Africa - 17.75


# Exercici 5 -  Ranking de paises por H-Index



```python

```

# Exercici 4.- Cual es publisher más antiguo que aún publica (tiene publicación el último año)



```python
# 'Publisher': 'Wiley-Blackwell',
  #'Coverage': '1950-2020',
import datetime

#Obtains the current year of execution
def current_year() -> int:  
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = int(date.strftime("%Y"))      
    return year


categorias: dict = set() #Mejor así. Desambigua
dictionary = {}
year_min = current_year()
year = year_min
name = [] 

for entrada in entries:
    anyos = re.split('-|,', entrada['Coverage']) #Separa, en fu
    anyos = [int(i) for i in anyos]
    if (year_min > anyos[0] and anyos[-1]==(year-1)):
        name.append(entrada['Publisher'])
        year_min = anyos[0]
    elif (year_min== anyos[0] and anyos[-1]==(year-1)):

        name.append(entrada['Publisher'])

print('The publishers -> ' ,name, ' first publish in ', year_min)


```

  
 >   The publishers ->  ['Wiley-Blackwell', 'Massachussetts Medical Society', 'American Physiological Society', 'Elsevier Ltd.']  first publish in  1823


# Exercici 3 Agrupar publisher por numero de tipo de publicaciones






