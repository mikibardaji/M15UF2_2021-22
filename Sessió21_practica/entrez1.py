from unittest import result
from Bio import Entrez

# Entrez Config
Entrez.email = "mabardajiprofe@gmail.com"

handle = Entrez.einfo();

print(type(handle)) # es un <class 'http.client.HTTPResponse'>
result = handle.read()
print(type(result)) # <<class 'bytes'>
print(result)


# EInfo 
# ESearch és un mètode getl  (GET)
# EPost és un mètode post
# EFetch recoge los datos
