import openfoodfacts
from product import Product


def get_food_facts_by_name(name: str) -> Product:
    search_result = openfoodfacts.products.advanced_search({
        "search_terms": name,
        "page_size": "2",
    })

    if len(search_result["products"]) == 0:
        print("errr")
        return None

    item = search_result["products"][0]

    print(item)

    name = item["product_name"]

    keys = [
        "ef_agriculture",
        "ef_consumption",
        "ef_distribution",
        "ef_packaging",
        "ef_processing",
        "ef_total",
        "ef_transportation"
    ]

    values = []

    for key in keys:

        try:
            values.append(item["ecoscore_data"]["agribalyse"][key])
        except KeyError:
            values.append(None)

    product = Product(name, *values)

    print(product.toJSON())

    return product
