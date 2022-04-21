
# Enunciats Examen



### Exercici 1

- You are given a broken Tycho dataset. Write a function to fix it.
 - The function fix_broken_tycho() must do the following:
   1. Drop 'country' and 'url' columns
   2. Rename 'evnt' to 'event'
   3. Cleanup the diseases removing the names in square brackets. (See hint below)
   4. Add a new column called 'year' of type 'int' with the year from the epi_week.
   5. Select rows where the year is 1890, 1891, 1892, 1893, 1894 or 1895.
   6. Add a new column called 'id' with a numerical unique identifier starting from 0
   7. Rename 'loc' to 'city', 'number' to 'deaths'
   8. Reorder columns as follows: ['id', 'year', 'epi_week', 'from_date', 'to_date', 'state', 'city', 'disease', 'deaths']
 
 - Return parameters:
   - Return the fixed entries as a dataframe.
   - The index must be numerical, starting from 0.
 
 - Hints:
   .str.replace(pat=r' \[.*\]', repl='', regex=True)
 
 - Remember:
   - Write your solution inside the given function.
   - Functions must be pure. Remember to delete your print() calls when done.
   - Run pytest to be sure you succeeded.

**Solution** ![q1.py](q1.py "q1.py")

------------
### Exercici 2

 Question: get_total_deaths()
 -----------------------------------------------------------------------------
 
 - You are given the fixed Tycho dataset.
 - Write a function to calculate the ranking of diseases by number of total deaths.
 
 - Return parameters:
   - Return a dataframe.
   - The dataframe must have three columns in this order: ranking, disease, deaths
   - The ranking must start at 1
   - The index must be numerical, starting from 0.
 
 - Hint:
   - Look at the solution csv in the test.
 
 - Remember:
   - Write your solution inside the given function.
   - Functions must be pure. Remember to delete your print() calls when done.
   - Run pytest to make sure you succeeded.
 -----------------------------------------------------------------------------

**Solution** ![q2.py](q2.py "q2.py")

------------
### Exercici 3

 -----------------------------------------------------------------------------
 Question: get_ambiguous_cities()
 -----------------------------------------------------------------------------
 
 - You are given the fixed Tycho dataset.
 - Write a function to answer this question:
   List the cities that have the same name in different states.
 
 - Return parameters:
   - Return a dataframe.
   - The dataframe must have two columns in this order: city, state
   - Rows must be ordered alphabetically. First by city, second by state.
   - The index must be numerical, starting from 0.
 
 - Hint:
   - Look at the solution csv in the test.
 
 - Remember:
   - Write your solution inside the given function.
   - Functions must be pure. Remember to delete your print() calls when done.
   - Run pytest to make sure you succeeded.
  
**Solution** ![q3.py](q1.py "q3.py")

------------

### Exercici 4

 -----------------------------------------------------------------------------
 Question: get_diseases()
 -----------------------------------------------------------------------------
 
 - You are given the fixed Tycho dataset.
 - Write a function to answer this question:
   - Plot the deaths of the four most deadly diseases in 1893.
   - The diseases are: tuberculosis, diphtheria, typhoid fever, scarlet fever
 
 - Return parameters:
   - Return a dataframe.
   - The dataframe must have the following columns in the same order:
     week, tuberculosis, diphtheria, typhoid_fever, scarlet_fever
   - The week column must start from 1 and end in 52.
 
 - Hint:
   - Look at the solution csv in the test.
 
 - Remember:
   - Write your solution inside the given function.
   - Functions must be pure. Remember to delete your print() calls when done.
   - Run pytest to make sure you succeeded.

**Solution** ![q4.py](q4.py "q4.py")