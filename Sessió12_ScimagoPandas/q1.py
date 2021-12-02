# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q1. How many entries are in scimago-medicine.csv?
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def q1():
    
    entries: pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")
    num:     int          = len(entries)
    
    print("Exporting all entries to html...")
    entries.to_html("scimago-medicine.html")

    print("First entry:")
    print(entries.loc[0, :])

    print(f"There are {num} entries.")


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q1()
# -----------------------------------------------------------------------------
