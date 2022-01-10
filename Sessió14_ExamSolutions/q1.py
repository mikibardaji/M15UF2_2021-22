# Imports
import pandas  as pd

# -----------------------------------------------------------------------------
# Student name: WRITE YOUR NAME HERE
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question: fix_broken_tycho()
# -----------------------------------------------------------------------------
# 
# - You are given a broken Tycho dataset. Write a function to fix it.
# - The function fix_broken_tycho() must do the following:
#   1. Drop 'country' and 'url' columns
#   2. Rename 'evnt' to 'event'
#   3. Cleanup the diseases removing the names in square brackets. (See hint below)
#   4. Add a new column called 'year' of type 'int' with the year from the epi_week.
#   5. Select rows where the year is 1890, 1891, 1892, 1893, 1894 or 1895.
#   6. Add a new column called 'id' with a numerical unique identifier starting from 0
#   7. Rename 'loc' to 'city', 'number' to 'deaths'
#   8. Reorder columns as follows: ['id', 'year', 'epi_week', 'from_date', 'to_date', 'state', 'city', 'disease', 'deaths']
# 
# - Return parameters:
#   - Return the fixed entries as a dataframe.
#   - The index must be numerical, starting from 0.
# 
# - Hints:
#   .str.replace(pat=r' \[.*\]', repl='', regex=True)
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - Run pytest to be sure you succeeded.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
def get_year(epi_week: int) -> int:

    epi_week_str: str = str(epi_week)
    year_str:     str = epi_week_str[0:4]
    year_int:     int = int(year_str)

    return year_int


# - Write your solution here.
# - This function must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def fix_broken_tycho(entries: pd.DataFrame) -> pd.DataFrame:

    alt_name_reg:   str       = r' \[.*\]'
    sorted_columns: list[str] = ['id', 'year', 'epi_week', 'from_date', 'to_date', 'state', 'city', 'disease', 'deaths']

    fixed_entries: pd.DataFrame = (entries.drop(  columns=['country', 'url'])
                                          .rename(columns={'evnt': 'event'})
                                          .assign(disease=lambda df: df.disease.str.replace(pat=alt_name_reg, repl='', regex=True)) #elimina square brackets, seleccionas misma columna
                                          .assign(year   =lambda df: df.epi_week.apply(get_year) )
                                          .query('1890 <= year <= 1895') #incovenient, el error es il·legible, però si es fa bé , es pràctica.
                                          .reset_index(drop=True)
                                          .assign(id=lambda df: df.index) #copio a "mà" el index, a una nova columna id
                                          .rename(columns={'loc': 'city', 'number': 'deaths'})
                                          .reindex(columns=sorted_columns)
    )

    return fixed_entries


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    broken_entries: pd.DataFrame = pd.read_csv("data/tycho-broken.csv", sep=",")
    fixed_entries:  pd.DataFrame = fix_broken_tycho(broken_entries)
    
    print(fixed_entries)

# -----------------------------------------------------------------------------
