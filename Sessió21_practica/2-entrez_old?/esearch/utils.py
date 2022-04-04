'''Utils to be used along BioPython's Entrez.'''

import json

from pathlib import Path
from typing  import Union

from Bio               import Entrez
from Bio.Entrez.Parser import DictionaryElement, ListElement

import pygments
from   pygments.lexers.web             import JsonLexer
from   pygments.formatters.terminal256 import Terminal256Formatter



# ---------------------------------------------------------------------
# XML Functions
# ---------------------------------------------------------------------


# Write xml as a bytes string to a file in disk.
# To be used with Entrez's xml responses.
# Makes the parent dirs, if they don't exist.
# ---------------------------------------------------------------------
def write_xml(xml_bytes: bytes, filename: str):

    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    Path(filename).write_bytes(xml_bytes)


# Read xml from a file in disk
# To be used with Entrez's xml responses.
# ---------------------------------------------------------------------
def read_xml(xml_filename: str) -> Union[DictionaryElement, ListElement]:

    with Path(xml_filename).open('rb') as xml_file:
        content = Entrez.read(xml_file)

    return content



# ---------------------------------------------------------------------
# Pretty Printing Functions
# ---------------------------------------------------------------------


# Prettifies an object and returns its pretty representation as a string.
# It expects a json-able object.
# ---------------------------------------------------------------------
def prettify(something) -> str:

    pretty_str: str = json.dumps(something,
                                 sort_keys=True,
                                 indent=4)

    return pretty_str


# Print Prettily
# Uses prettify(), adds colors and prints directly to the terminal.
# List of all supported styles:  print(list(pygments.styles.get_all_styles()))
# Interesting styles: default, solarized-dark, solarized-light, zenburn
# ---------------------------------------------------------------------
def print_pretty(something, style: str):

    pretty_str: str = json.dumps(something,
                                 sort_keys=True,
                                 indent=4)

    lexer     = JsonLexer()
    formatter = Terminal256Formatter(style=style)

    colored_str: str = pygments.highlight( pretty_str,
                                           lexer=lexer,
                                           formatter=formatter )

    print(colored_str)

# ---------------------------------------------------------------------


