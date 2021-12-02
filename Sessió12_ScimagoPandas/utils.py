# Imports
import copy

import numpy as np
import pandas as pd

# -----------------------------------------------------------------------------
# Read CSV File
# -----------------------------------------------------------------------------

# See 'open' docs to understand the newline parameter
# DictReader converts each row in csv_file in a dictionary.
# The dictionary keys are the column names.
# -----------------------------------------------------------------------------
def read_csv_file(csv_file_path: str) -> pd.DataFrame:
    
    entries: pd.DataFrame = pd.read_csv("scimago-medicine.csv", sep=";")
    return entries

# -----------------------------------------------------------------------------
