import requests

def validate_address(adresse):
    url = "https://api-adresse.data.gouv.fr/search"
    params = {
        'q': adresse,
        'limit': 1
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)

        if data['features'] and len(data['features']) > 0:
            properties = data['features'][0]['properties']
            geo = data['features'][0]['geometry']

            return {
                'valid': True,
                'latitude': geo['coordinates'][1],
                'longitude': geo['coordinates'][0],
                'label': properties['label']
            }
        
    return {'valid': False}