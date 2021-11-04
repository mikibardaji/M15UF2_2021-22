# Imports
import utils
import pprint
import q6

# -----------------------------------------------------------------------------
# Q7. Top 20 categories with most entries
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def get_num_entries(category: str, clean_entries: list[dict]) -> int:

    num_entries = 0

    for entry in clean_entries:
        categories_list: list[str] = entry['Categories']
        
        if category in categories_list:
            num_entries += 1

    return num_entries

# -----------------------------------------------------------------------------
def sort_ranking(ranking: dict[str, int]) -> list[tuple[str, int]]:

    ranking_items:  list[tuple[str, int]] = list(ranking.items())
    get_num:        function              = lambda item: item[1]
    sorted_ranking: list[tuple[str, int]] = sorted(ranking_items, key=get_num, reverse=True)

    return sorted_ranking

# -----------------------------------------------------------------------------
def q7():
    
    # Get clean entries
    raw_entries:   list[dict] = utils.read_csv_file("scimago-medicine.csv")
    clean_entries: list[dict] = utils.clean_entries(raw_entries)

    # Get unique categories
    unique_categories_list: list[str] = q6.get_unique_categories(clean_entries)

    # Make ranking
    category_ranking: dict[str, int] = {category: get_num_entries(category, clean_entries) for category in unique_categories_list}

    pprint(category_ranking)
    # Sort ranking
    sorted_category_ranking: list[tuple[str, int]] = sort_ranking(category_ranking)

    # Get Top 20
    top20_list: list[tuple[str, int]] = sorted_category_ranking[0:20]

    # Print top 20
    print("Top 20 Categories:")
    for item in top20_list:
        category:    str = item[0]
        num_entries: int = item[1]
        print(f"{category}: {num_entries}")

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q7()
# -----------------------------------------------------------------------------
