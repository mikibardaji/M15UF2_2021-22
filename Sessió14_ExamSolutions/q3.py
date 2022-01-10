# Imports
import pandas  as pd

# -----------------------------------------------------------------------------
# Student name: WRITE YOUR NAME HERE
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question: get_ambiguous_cities()
# -----------------------------------------------------------------------------
# 
# - You are given the fixed Tycho dataset.
# - Write a function to answer this question:
#   List the cities that have the same name in different states.
# 
# - Return parameters:
#   - Return a dataframe.
#   - The dataframe must have two columns in this order: city, state
#   - Rows must be ordered alphabetically. First by city, second by state.
#   - The index must be numerical, starting from 0.
# 
# - Hint:
#   - Look at the solution csv in the test.
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - Run pytest to make sure you succeeded.
# -----------------------------------------------------------------------------


# - Write your solution here.
# - This function must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def get_ambiguous_cities(entries: pd.DataFrame) -> pd.DataFrame:

    ambiguous_cities: pd.DataFrame = (entries.loc[:, ['city', 'state']]
                                             .groupby(by='city')
                                             .filter(lambda group: group.state.nunique() > 1)
                                             .drop_duplicates()
                                             .sort_values(by=['city', 'state'])
                                             .reset_index(drop=True)
    )

    return ambiguous_cities


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries:          pd.DataFrame = pd.read_csv("data/tycho-fixed.csv", sep=",")
    ambiguous_cities: pd.DataFrame = get_ambiguous_cities(entries)

    print(ambiguous_cities)


# -----------------------------------------------------------------------------
