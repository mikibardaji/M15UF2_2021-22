# XXX Remove your email address!

'''Entrez: Easy access to the NCBI API through BioPython.'''

import sys
import json
import utils

from Bio               import Entrez
from Bio.Entrez.Parser import DictionaryElement, ListElement


# Entrez Global Config
Entrez.email = "mabardaji@gmail.com"
assert Entrez.email != "", "Write your email address before using Entrez."



# Request DB info Search 
# ---------------------------------------------------------------------
def request_search(db1: str, term1: str, retmax1: int,xml_filename: str):

    with Entrez.esearch(db=db1,
                        term=term1,
                        retmax=str(retmax1)             ) as response:

        xml_bytes: bytes = response.read()

    utils.write_xml(xml_bytes, xml_filename)



# Main
# ---------------------------------------------------------------------
this_module: str = __name__
main_module: str = "__main__"

if this_module == main_module:
    
    #request_search(db1="pubmed",term1="biopython[title]",retmax1=40,xml_filename="pubmed_search.xml")

    # request_db_info('',           'cache/dblist.xml')
    # request_db_info('nucleotide', 'cache/nucleotide.xml')
    # request_db_info('pubmed',     'cache/pubmed.xml')

   content: DictionaryElement= utils.read_xml('pubmed_search.xml')

   utils.print_pretty(content,'default')

# ---------------------------------------------------------------------
