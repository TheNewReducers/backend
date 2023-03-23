import json

from image_processing import detect_text_from_file
from gpt_processing import chat_gpt

mock_text= """
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

chat_out = """
{
  "content": "\n\n{\n  \"store\": \"Ecenter\",\n  \"address\": \"OSKAR-VON-MILLER-STR.6, SCHWEINFURT\",\n  \"date\": \"08.12.07\",\n  \"time\": \"16:27\",\n  \"items\": [\n    {\n      \"name\": \"RADIESCHEN\",\n      \"price\": 0.59\n    },\n    {\n      \"name\": \"KAESEAUFSCH.\",\n      \"price\": 1.39\n    },\n    {\n      \"name\": \"BAUCHSPECK\",\n      \"price\": 1.19\n    },\n    {\n      \"name\": \"BAUCHSPECK\",\n      \"price\": 1.19\n    },\n    {\n      \"name\": \"DORNFELDER\",\n      \"price\": 0.99\n    },\n    {\n      \"name\": \"CLEMENTINEN\",\n      \"price\": 2.49\n    },\n    {\n      \"name\": \"L&M BLUE\",\n      \"price\": 3.5\n    },\n    {\n      \"name\": \"L&M BLUE\",\n      \"price\": 3.5\n    }\n  ],\n  \"total\": 14.84,\n  \"taxes\": [\n    {\n      \"rate\": \"7.00%\",\n      \"amount\": 0.45\n    },\n    {\n      \"rate\": \"19.00%\",\n      \"amount\": 1.73\n    }\n  ],\n  \"payment_method\": \"BAR\",\n  \"cashier\": \"H. SEUFERT\"\n}",
  "role": "assistant"
}
"""


def file_input(file) -> str:
    #text: str = detect_text_from_file(file)
    text = mock_text
    text += "\n Return the data as json"

    #ai_response:str = chat_gpt(text)
    ai_response = chat_out

    ai_response = ai_response.replace("\n", "")

    print(ai_response)


    json_formatted_str = json.loads(ai_response)

    print(json_formatted_str)


    return ai_response



if __name__ == '__main__':
    file_input("")