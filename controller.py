import json

import io

from project_utils import str_from_file

from image_processing import detect_text_from_file
from gpt_processing import chat_gpt

import logging

CHAT_GPT_PROMT = 'format the receipt to JSON. The keys should be: "timestamp", "items", "store" . The timestamp should be formatted in ISO 8601, add a new key names "category" per item, which classifies the food to a food category.'

ONLINE: bool = True


def file_input(file) -> dict:
    receipt_text: str = get_receipt_text(file)
    query: str = to_gpt_query(receipt_text)
    receipt_data: dict = get_receipt_data(query)

    return receipt_data


def to_gpt_query(text) -> str:
    return f"{text}\n{CHAT_GPT_PROMT}"


def get_receipt_data(query: str) -> dict:
    if ONLINE:
        gpt_response: str = chat_gpt(query)["content"]
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


if __name__ == '__main__':
    path = "./test-data/kassenbon-2.png"

    with io.open(path, 'rb') as image_file:
        file_input(image_file)
