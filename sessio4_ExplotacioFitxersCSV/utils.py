# Imports
import csv
import copy


# See 'open' docs to understand the newline parameter
# DictReader converts each row in csv_file in a dictionary.
# The dictionary keys are the column names.
# -----------------------------------------------------------------------------
def read_csv_file(csv_file_path: str):
    
    with open(csv_file_path, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        result     = [row_dict for row_dict in csv_reader]

    return result




# Uses unnecessary copy(). replace() returns a new copy each time.
# Instead of replace() you can use a regexp.
# -----------------------------------------------------------------------------
def remove_quarter(category: str) -> str:
    "Returns the category string without the quarter id: (Q1), (Q2), (Q3) or (Q4)"

    result = copy.copy(category)

    result = result.replace("(Q1)", "")
    result = result.replace("(Q2)", "")
    result = result.replace("(Q3)", "")
    result = result.replace("(Q4)", "")

    return result


# -----------------------------------------------------------------------------
def clean_entry(entry: dict) -> dict:
    "Returns a copy of the original entry with Categories as a list of clean strings."

    # Get categories
    categories_str = entry['Categories']

    # Split categories
    categories_list = categories_str.split(';')

    # Remove quarter ids
    categories_merged_list = [remove_quarter(category) for category in categories_list]

    # Trim whitespaces
    categories_clean_list = [category.strip() for category in categories_merged_list]

    # Make a copy of the entry. Hace la copia de lista recursiva.
    result = copy.deepcopy(entry)

    # Categories: str -> Categories: list[str]
    result['Categories'] = categories_clean_list

    # Return the result with Categories as a list of clean strings
    return result


# -----------------------------------------------------------------------------
def clean_entries(raw_entries):
    "Returns a copy of the entries with Categories as a list of clean strings."

    clean_entries: list[dict] = [clean_entry(entry) for entry in raw_entries]

    return clean_entries

# -----------------------------------------------------------------------------
