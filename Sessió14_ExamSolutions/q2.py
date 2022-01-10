# Imports
import pandas  as pd

# -----------------------------------------------------------------------------
# Student name: WRITE YOUR NAME HERE
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question: get_total_deaths()
# -----------------------------------------------------------------------------
# 
# - You are given the fixed Tycho dataset.
# - Write a function to calculate the ranking of diseases by number of total deaths.
# 
# - Return parameters:
#   - Return a dataframe.
#   - The dataframe must have three columns in this order: ranking, disease, deaths
#   - The ranking must start at 1
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
def get_total_deaths(entries: pd.DataFrame) -> pd.DataFrame:

    deaths: pd.DataFrame = ( entries.loc[:, ['disease', 'deaths']]
                                    .groupby(by='disease') #agrupo pels diferents valors diferents de disease , com SQL
                                    .sum() #sumo la columna deaths
                                    .sort_values(by='deaths', ascending=False) #ordeno aquesta suma
                                    .reset_index() 
                                    .assign(ranking=lambda df: df.index + 1) #asigno un nou index sumant 
                                    .reindex(columns=['ranking', 'disease', 'deaths'])
    )

    return deaths


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries: pd.DataFrame = pd.read_csv("data/tycho-fixed.csv", sep=",")
    deaths:  pd.DataFrame = get_total_deaths(entries)

    print(deaths)


# -----------------------------------------------------------------------------
