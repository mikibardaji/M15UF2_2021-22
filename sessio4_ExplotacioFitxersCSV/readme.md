#  Exercici explotació fitxers CSV
##              <center>Pablo Garcia, Miquel Angel Bardají</center>

[Web font de dades Scimago ](https://www.scimagojr.com/journalrank.php?area=2700 "Web font de dades ")

### **Practica explotar un fitxer** i resoldre diferentes 

#####  **Practica explotar un fitxer** i resoldre diferents consultes.

Fitxer de dades : [aqui](https://github.com/mikibardaji/M15UF2_2021-22/blob/main/sessio4_ExplotacioFitxersCSV/scimagomedicine.csv "aqui")


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
csv_file_path = "scimagomedicine.csv"
entries = read_csv_file(csv_file_path)
entries[0]       
```




>    {'Rank': '1',

>     'Sourceid': '28773',

>    'Title': 'Ca-A Cancer Journal for Clinicians',
>    
>    'Type': 'journal',

>    'Issn': '15424863, 00079235',

>    'SJR': '62,937',

>    'SJR Best Quartile': 'Q1',

>    ...

>    'Categories': 'Hematology (Q1); Oncology (Q1)'}




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


```python
# Buscar cuantos tipos de entradas hay diferentes
unicos = get_unique_type(entries)
print(unicos)
```

>   ['journal', 'book series', 'conference and proceedings', 'trade journal']









