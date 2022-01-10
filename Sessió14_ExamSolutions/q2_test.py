# Imports
import pandas  as pd
import q2

# -----------------------------------------------------------------------------
# Test: test_get_total_deaths()
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def test_get_total_deaths():

    # Read input and correct result
    entries:  pd.DataFrame = pd.read_csv("data/tycho-fixed.csv",  sep=",")
    deaths:   pd.DataFrame = pd.read_csv("output/deaths.csv", sep=",")

    # Get result
    result: pd.DataFrame = q2.get_total_deaths(entries)

    # Test
    pd.testing.assert_frame_equal(result, deaths)


# -----------------------------------------------------------------------------
