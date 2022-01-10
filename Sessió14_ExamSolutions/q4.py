# Imports
import pandas  as pd

# -----------------------------------------------------------------------------
# Student name: WRITE YOUR NAME HERE
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question: get_diseases()
# -----------------------------------------------------------------------------
# 
# - You are given the fixed Tycho dataset.
# - Write a function to answer this question:
#   - Plot the deaths of the four most deadly diseases in 1893.
#   - The diseases are: tuberculosis, diphtheria, typhoid fever, scarlet fever
# 
# - Return parameters:
#   - Return a dataframe.
#   - The dataframe must have the following columns in the same order:
#     week, tuberculosis, diphtheria, typhoid_fever, scarlet_fever
#   - The week column must start from 1 and end in 52.
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
def get_diseases(entries: pd.DataFrame) -> pd.DataFrame:

    tuberculosis: pd.DataFrame = (entries.query("(year == 1893) and (disease == 'TUBERCULOSIS')")
                                         .loc[:, ['epi_week', 'deaths']]
                                         .groupby(by='epi_week')
                                         .sum()
    )

    diphtheria: pd.DataFrame = (entries.query("(year == 1893) and (disease == 'DIPHTHERIA')")
                                         .loc[:, ['epi_week', 'deaths']]
                                         .groupby(by='epi_week')
                                         .sum()
    )

    typhoid_fever: pd.DataFrame = (entries.query("(year == 1893) and (disease == 'TYPHOID FEVER')")
                                         .loc[:, ['epi_week', 'deaths']]
                                         .groupby(by='epi_week')
                                         .sum()
    )

    scarlet_fever: pd.DataFrame = (entries.query("(year == 1893) and (disease == 'SCARLET FEVER')")
                                         .loc[:, ['epi_week', 'deaths']]
                                         .groupby(by='epi_week')
                                         .sum()
    )

    diseases_by_epiweek: pd.DataFrame = pd.DataFrame(
                            index=tuberculosis.index,
                            data={
                                'tuberculosis':  tuberculosis.deaths,
                                'diphtheria':    diphtheria.deaths,
                                'typhoid_fever': typhoid_fever.deaths,
                                'scarlet_fever': scarlet_fever.deaths,
                            }
    )

    diseases = (diseases_by_epiweek.reset_index(drop=True)
                                    .assign(week=lambda df: df.index + 1)
                                    .reindex(columns=['week', 'tuberculosis', 'diphtheria', 'typhoid_fever', 'scarlet_fever'])
    )

    return diseases


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries:    pd.DataFrame = pd.read_csv("data/tycho-fixed.csv", sep=",")
    diseases:   pd.DataFrame = get_diseases(entries)

    diseases.set_index('week', drop=True).plot(kind='line', title='Top 4 diseases in 1893').get_figure().savefig("output/diseases.pdf")
    print(diseases)


# -----------------------------------------------------------------------------
