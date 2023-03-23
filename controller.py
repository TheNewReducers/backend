import json

import io

from image_processing import detect_text_from_file
from gpt_processing import chat_gpt

mock_text = """
Ecenter
EDEKA
nated anism sael SCHWEINFURT
RADIESCHEN
KAESEAUFSCH.
BAUCHSPECK
BAUCHSPECK
DORNFELDER
CLEMENTINEN
L&M BLUE
L&M BLUE
brom SUMME
BAR
OSKAR-VON-MILLER-STR.6
EUR
RÜCKGELD EUR
ENTHALTENE
MWST
7,00 %
19,00 %
SUMME MWST
MEHRWERTSTEUER
0,45
1,28
1,73
eõisp istabmoq
STEUERNUMMER: 257/115/30471
QUITTUNG
08.12.07 16:27 37589
0,59
1,39
1,19
1,19
0,99
2,49
ES BEDIENTE SIE: H. SEUFERT
3,50
3,50
EDEKA HANDELSGESELLSCHAFT
NORDBAYERN-SACHSEN-THÜRINGEN MBH
14,84 *
50,00
35,16
NETTO
6,40
6,71
13,11
blueNUTZEN SIE DIE EDECARD
PUNKTE SAMMELN+PRAMIEN ERWERBEN
IHR EINKAUF WÄRE UNS
1 BONUSPUNKTE WERT GEWESEN !
48 4 8500
VIELEN DANK FÜR IHREN EINKAUF!
AUF WIEDERSEHEN IM E-CENTER
UNSERE ÖFFNUNGSZEITEN FÜR SIE:
MONTAG-SAMSTAG: 08.00-20.00UHR
"""

chat_mock_out = """
{
  "items": [
    {"name": "EDEKA", "price": 14.84},
    {"name": "nated anism sael SCHWEINFURT", "price": 0.59},
    {"name": "RADIESCHEN", "price": 1.39},
    {"name": "KAESEAUFSCH.", "price": 1.19},
    {"name": "BAUCHSPECK", "price": 1.19},
    {"name": "BAUCHSPECK", "price": 0.99},
    {"name": "DORNFELDER", "price": 2.49},
    {"name": "CLEMENTINEN", "price": 3.5},
    {"name": "L&M BLUE", "price": 3.5},
    {"name": "L&M BLUE", "price": 6.4},
    {"name": "brom SUMME", "price": 6.71}
  ],
  "taxes": [
    {"type": "7.00%", "amount": 0.45},
    {"type": "19.00%", "amount": 1.28},
    {"type": "SUMME MWST", "amount": 1.73},
    {"type": "MEHRWERTSTEUER", "amount": 1.73}
  ],
  "total": 35.16,
  "receipt_data": {
    "date": "08.12.07",
    "time": "16:27",
    "receipt_num": "37589",
    "served_by": "H. SEUFERT",
    "store_info": {
      "name": "EDEKA HANDELSGESELLSCHAFT NORDBAYERN-SACHSEN-THÜRINGEN MBH",
      "address": "OSKAR-VON-MILLER-STR.6"
    }
  },
  "extras": {
    "card_bonus_points": 1,
    "message": "NUTZEN SIE DIE EDECARD PUNKTE SAMMELN+PRAMIEN ERWERBEN IHR EINKAUF WÄRE UNS 1 BONUSPUNKTE WERT GEWESEN !",
    "opening_hours": "MONTAG-SAMSTAG: 08.00-20.00UHR"
  }
}
"""


def file_input(file) -> dict:
    text: str = detect_text_from_file(file)
    # text = mock_text
    text += "\n Extract the data to json and classify food catigoeries"

    ai_response: dict = chat_gpt(text)["content"]

    print(ai_response)

    ai_response = json.loads(ai_response)

    return ai_response


if __name__ == '__main__':
    path = "./test-data/kassenbon-1.jpg"

    with io.open(path, 'rb') as image_file:
        file_input(image_file)
