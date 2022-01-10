# Imports
import pandas  as pd
import q3

# -----------------------------------------------------------------------------
# Test: test_get_ambiguous_cities()
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def test_get_ambiguous_cities():

    # Read input and correct result
    entries:            pd.DataFrame = pd.read_csv("data/tycho-fixed.csv", sep=",")
    ambiguous_cities:   pd.DataFrame = pd.read_csv("output/ambiguous_cities.csv", sep=",")

    # Get result
    result: pd.DataFrame = q3.get_ambiguous_cities(entries)

    # Test
    pd.testing.assert_frame_equal(result, ambiguous_cities)


# -----------------------------------------------------------------------------
