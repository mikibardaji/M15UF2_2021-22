import re
from   pathlib import Path

"""
Read fasta files without using BioPython.
"""

# -----------------------------------------------------------------------------
def read_fasta_v1(filename: str) -> str:
    """Reads a .fasta file with a single sequence.
       Uses a regexp with a single match.
       Removes whitespace using string .replace()"""

    # Regex setup    
    txt: str = Path(filename).read_text()
    reg: str = r'(>[^\n]{0,})(.{0,})'
    pat: re.Pattern = re.compile(reg, re.DOTALL)

    # Get matches
    match_list: list[re.Match] = list(pat.finditer(txt))

    # If there is a sequence, there is a match
    assert len(match_list) == 1
    match: re.Match = match_list[0]
    lines: str      = match.group(2)

    # Remove newlines
    seq: str = lines.replace('\n', '')

    return seq


# -----------------------------------------------------------------------------
def remove_whitespace(txt: str) -> str:
    """Removes whitespace everywhere using a regex."""

    # Regex setup
    reg: str = r'\s'
    pat: re.Pattern = re.compile(reg)

    # Remove whitespaces
    result: str = pat.sub('', txt)

    return result


# -----------------------------------------------------------------------------
def read_fasta_v2(filename: str) -> str:
    """Reads a .fasta file with a single sequence.
       Uses a regexp with a single match.
       Removes whitespace using another regex."""

    # Regex setup
    txt: str = Path(filename).read_text()
    reg: str = r'(>[^\n]{1,})(.{0,})'
    pat: re.Pattern = re.compile(reg, re.DOTALL)

    # Get matches
    match_list: list[re.Match] = list(pat.finditer(txt))

    # If there is a sequence, there is a match
    assert len(match_list) == 1
    match: re.Match = match_list[0]
    lines: str      = match.group(2)

    # Remove newlines
    seq: str = remove_whitespace(lines)

    return seq


# -----------------------------------------------------------------------------
def read_fasta_v3(filename: str) -> str:
    """Reads a .fasta file with a single sequence.
       Uses a regexp with a single match.
       Removes whitespace using another regex.
       Pretty version."""

    # Regex setup
    txt: str = Path(filename).read_text()
    reg: str = r'''(>           # Header starts
                    [^\n]{0,}   # Not a newline, zero or more times
                   )
                   (.{0,})      # All Lines. re. DOTALL => The dot matches \n
                '''
    pat: re.Pattern = re.compile(reg, re.DOTALL | re.VERBOSE)

    # Get matches
    match_list: list[re.Match] = list(pat.finditer(txt))

    # If there is a sequence, there is a match
    assert len(match_list) == 1
    match: re.Match = match_list[0]
    lines: str      = match.group(2)

    # Remove newlines
    seq: str = remove_whitespace(lines)

    return seq


# Main
# -----------------------------------------------------------------------------
print(read_fasta_v3('test1-single.fasta'))

# -----------------------------------------------------------------------------
