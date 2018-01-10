import requests
from pprint import pprint


def search_get(q, rows=None, start=None, semanticGroup=None):
    url = 'https://www.ebi.ac.uk/ols/api/search'
    params = {
        'q': q,
        'rows': rows,
        'start': start,
        'exact': False,
    }

    r = requests.get(url=url, params=params)
    parsed_list = list()
    results = r.json()
    for result in results['response']['docs']:
        try:
            curie = None
            if 'obo_id' in result.keys():
                curie = result['obo_id']
            else:
                short_term = result['short_form'].split("_")
                curie = ":".join(short_term)
            synonym = list()
            for highlight, value in results['highlighting'].items():
                h_curie = highlight.split("/")[-1].replace('_',':')
                if curie == h_curie and 'synonym' in value.keys():
                    syn = [x.replace('<b>', '') for x in value['synonym']]
                    syn = [x.replace('</b>', '') for x in syn]
                    for sy in syn:
                        synonym.append(sy)

            parsed = {
                         "definition": result['description'],
                         "id": curie,
                         "name": result['label'],
                         "semanticGroup": '',
                         "synonyms": synonym
                     }
            parsed_list.append(parsed)

        except Exception as e:
            print(e)
    return parsed_list
