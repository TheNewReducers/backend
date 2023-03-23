import json

import openfoodfacts

search_result = openfoodfacts.products.search("Nutella", sort_by="unique_scans_n", page_size=2)

print(search_result)
