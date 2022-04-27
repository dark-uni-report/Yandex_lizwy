import requests

a = 'Хабаровск, Уфа, Нижний Новгород, Калининград'.split(', ')
for i in a:
    response = requests.get(
        f'https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={i}&format=json')
    json_response = response.json()
    print(i, '-', json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
        "GeocoderMetaData"]["Address"]["Components"][1]["name"])
