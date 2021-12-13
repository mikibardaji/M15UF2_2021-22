# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q9. All regions covered by all entries
# -----------------------------------------------------------------------------

# .size() equals to (len) in Series. In DataFrames it is the total count.
# -----------------------------------------------------------------------------
def q9():

    # Get regions
    entries:          pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")
    unique_regions:   pd.Series    = (entries.loc[:, "Region"]
                                             .drop_duplicates()
                                             .sort_values()
                                             .reset_index(drop=True)
    )

    # Print
    print(unique_regions)
    print(f"There are {unique_regions.size} regions.")


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q9()
# -----------------------------------------------------------------------------
