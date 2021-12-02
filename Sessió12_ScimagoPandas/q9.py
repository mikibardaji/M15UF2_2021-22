# Imports
import utils
import pprint

import numpy as np
import pandas as pd

# -----------------------------------------------------------------------------
# Q9. All regions covered by all entries
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def q9():

    # Get regions
    entries:          pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")
    unique_regions:   np.ndarray   = entries.loc[:, "Region"].unique()

    # Prepare output
    num:              int          = len(unique_regions)
    sorted_regions:   list[str]    = sorted(unique_regions)

    # Print
    pprint.pp(sorted_regions)
    print(f"There are {num} regions.")


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q9()
# -----------------------------------------------------------------------------
