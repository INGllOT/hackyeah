import requests

_paragraphs_dochodowe = {}
_paragraphs_wydatkowe = {}


def get_dochodowe_paragraphs():
    if len(_paragraphs_dochodowe) != 0:
        return _paragraphs_dochodowe

    link = "https://bestia-api.mf.gov.pl/api/paragrafy-dochodowe?limit=100&page=1"
    while link != None:
        result = requests.get(link)
        if result.status_code == 200:
            result_json = result.json()
            # print(result_json)
            link = result_json["links"].get("next")
            for paragraph in result_json["data"]:
                _paragraphs_dochodowe[paragraph["symbol"]] = paragraph["tekst"]

    return _paragraphs_dochodowe


def get_wydatkowe_paragraphs():
    if len(_paragraphs_wydatkowe) != 0:
        return _paragraphs_wydatkowe

    link = "https://bestia-api.mf.gov.pl/api/paragrafy-wydatkowe?limit=100&page=1"
    while link != None:
        result = requests.get(link)
        if result.status_code == 200:
            result_json = result.json()
            # print(result_json)
            link = result_json["links"].get("next")
            for paragraph in result_json["data"]:
                _paragraphs_wydatkowe[paragraph["symbol"]] = paragraph["tekst"]

    return _paragraphs_wydatkowe
