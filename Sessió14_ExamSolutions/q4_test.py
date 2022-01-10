# Imports
import pandas  as pd
import q4

# -----------------------------------------------------------------------------
# Test: test_get_diseases()
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def test_get_diseases():

    # Read input and correct result
    entries:    pd.DataFrame = pd.read_csv("data/tycho-fixed.csv", sep=",")
    disaeases:  pd.DataFrame = pd.read_csv("output/diseases.csv",  sep=",")

    # Get result
    result: pd.DataFrame = q4.get_diseases(entries)

    # Test
    pd.testing.assert_frame_equal(result, disaeases)


# -----------------------------------------------------------------------------
