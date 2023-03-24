import json
import io
from product import Product
from project_utils import str_from_file
from image_processing import detect_text_from_file
from gpt_processing import chat_gpt
from food import get_food_facts_by_name
import logging

# CHAT_GPT_PROMT = 'format the receipt to JSON. The keys should be: "timestamp", "items", "store",  "name", "price", ' \
#                  '"number", "weight", "category", "is_food". The timestamp should be formatted in ISO 8601, ' \
#                  'add a new key names "category" per item, which classifies the food to a food category. For the ' \
#                  'category, select one from these: Meat, Pet Food, Snacks, Fruits, Vegetables, Dairy, Beverages, ' \
#                  'Tobacco, Alcohol. If there is no suitable one, create a new one. If no number is specified, enter "1".' \
#                  'If it is a food, the key "is_food" should be set to true ' \
#                  'otherwise to false. All keys should be in english language. If there is no weight, then insert "null".,' \


TRAIN_CAT_PROMT = "FoodData: ['Ananas', 'Apfel', 'Aubergine', 'Avocado', 'Banane', 'Birne', 'Blumenkohl', 'Bohnen', 'Brokkoli', 'Champignons', 'Erbsen', 'Erdbeeren', 'Feldsalat', 'Fenchel', 'Grünkohl', 'Karotten', 'Kartoffeln', 'Kartoffelpüreepulver', 'Kichererbsen', 'Kohlrabi', 'Kürbis', 'Lauch', 'Leinsamen', 'Linsen', 'Mais', 'Orange / Apfelsine', 'Paprika', 'Pfirsich', 'Rettich', 'Rosenkohl', 'Rote Beete', 'Rotkohl', 'Rucola', 'Salatgurke', 'Salatmischung', 'Sellerie', 'Spargel', 'Spinat', 'Tomaten', 'Tomaten, passiert', 'Tomatenmark', 'Trauben', 'Weißkohl', 'Zucchini', 'Zwiebeln', 'Butter', 'Ei', 'Joghurt', 'Käse', 'Käse-Ersatz', 'Milch', 'Dinkelmilch', 'Hafermilch', 'Mandelmilch', 'Sojamilch', 'Quark', 'Soja', 'Sahne', 'Sahne-Ersatz, Hafer Cuisine', 'Saure Sahne', 'Bratling/Veggieburger/Patty auf Sojabasis', 'Bratling/Veggieburger/Patty auf Erbsenbasis', 'Fisch', 'Gemüsenugget /-schnitzel', 'Hähnchen', 'Lupinenmehl', 'Rindfleisch', 'Rinder-Hackfleisch', 'Rinder-Patty/-Bratling', 'Schweinefleisch', 'Seitan', 'Sojagranulat', 'Tempeh', 'Tofu', 'Wildfleisch', 'Wurst, Bratwurst, Thüringer Rostbratwurst', 'Vegane Bratwurst', 'Wurstaufschnitt vom Rind', 'Brot', 'Bulgur', 'Dinkel', 'Erdnüsse, in Schale', 'Erdnussbutter', 'Feinbackwaren', 'Gnocchi', 'Haferflocken', 'Honig', 'Kokosöl', 'Margarine', 'Nudeln', 'Olivenöl', 'Palmfett', 'Pommes', 'Rapsöl', 'Reis', 'Schokolade', 'Sonnenblumenkerne', 'Sonnenblumenöl', 'Walnüsse', 'Zucker'])"
CHAT_GPT_PROMT = "Given is a receipt. Present the data on the receipt in JSON format. There should be the keys: timestamp, items and store. The items should be formatted as a list. Each item should have the keys: name, price, amount, weight, category. Only food items should appear in the list. The timestamp should be formatted in ISO 8601. Add for each item a new key 'data_name', which assigns to each item name exactly one food from given 'FoodData' list, if nothing matching is found 'undefined' should be assigned."

ONLINE: bool = True


def file_input(file) -> dict:
    receipt_text: str = get_receipt_text(file)
    query: str = to_gpt_query(receipt_text)
    receipt_data: dict = get_receipt_data(query)

    map_json_to_food_data(receipt_data)


    return receipt_data


def to_gpt_query(text) -> str:
    return f"{text}\n{CHAT_GPT_PROMT}"


def search_for_all_product_info(receipt_data):
    for item in receipt_data["items"]:
        p: Product = get_food_facts_by_name(item["name"])
        if p is None:
            continue
        item["product"] = p.toJSON()

    print(receipt_data)


def get_receipt_data(query: str) -> dict:
    if ONLINE:
        gpt_response: str = chat_gpt(query, train_data=TRAIN_CAT_PROMT)["content"]
    else:
        gpt_response: str = str_from_file("./test-data/receipt_mock_data.txt")

    logging.info(gpt_response)

    gpt_response_json: dict = {"state": "error"}

    gpt_response_json = json.loads(gpt_response)

    print(gpt_response_json)

    return gpt_response_json


def get_receipt_text(file) -> str:
    if ONLINE:
        return detect_text_from_file(file)
    return str_from_file("./test-data/receipt_mock_text.txt")



def map_json_to_food_data(receipt_data:dict):
    with open("./food_data.json", "r") as file:
        food_data:dict = json.loads(file.read())

        for item in receipt_data["items"]:

            if item["data_name"] == "undefined" or food_data.get(item["data_name"]) is None:
                item["co2_item"] = None
                continue

            data = food_data[item["data_name"]]
            co2 = data["co2"] * (data["base_weigth"] / 1000)
            item["co2_item"] = co2

    print(receipt_data)







if __name__ == '__main__':
    path = "./test-data/kassenbon-2.png"

    with io.open(path, 'rb') as image_file:
        file_input(image_file)
