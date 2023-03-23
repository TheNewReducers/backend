import json

import openfoodfacts

search_result = openfoodfacts.products.advanced_search({
    "search_terms": "Nutella", 
    # "sort_by":"unique_scans_n", 
    "page_size":"2", 
    # "countries":"Germany",
    # "search_nutriment":"carbon-footprint", 
    # "nutriment_compare_0":"gt",
    # "nutriment_value_0":"0"
})

for result in search_result["products"]:
    print(result["product_name"])
    print(result["ecoscore_data"]['agribalyse']['co2_total'])

open("test.json", "w").write(json.dumps(search_result, indent=4, sort_keys=True))


# print(search_result)

##                     "ef_agriculture": "0.26394245",
                    # "ef_consumption": 0,
                    # "ef_distribution": "0.0046415086",
                    # "ef_packaging": "0.018685146",
                    # "ef_processing": "0.24201201",
                    # "ef_total": "0.5452432926",
                    # "ef_transportation": "0.015962178",
