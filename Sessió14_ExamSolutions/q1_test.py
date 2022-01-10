# Imports
import pandas  as pd
import q1

# -----------------------------------------------------------------------------
# Test: test_fix_broken_tycho()
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def test_fix_broken_tycho():

    # Read input and correct result
    broken_entries: pd.DataFrame = pd.read_csv("data/tycho-broken.csv", sep=",")
    fixed_entries:  pd.DataFrame = pd.read_csv("data/tycho-fixed.csv",  sep=",")

    # Get result
    result: pd.DataFrame = q1.fix_broken_tycho(broken_entries)

    # Test
    pd.testing.assert_frame_equal(result, fixed_entries)


# -----------------------------------------------------------------------------
