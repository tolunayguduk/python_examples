import requests
def hava():
    url1 = "http://212.175.180.28/api/merkezler?il="
    url2 = "http://212.175.180.28/api/sondurumlar?istno="

    response1 = requests.get(url1 + input("şehir : "))
    json_verisi1 = response1.json()

    response2 = requests.get(url2 + str(json_verisi1[0]["sondurumIstNo"]))
    json_verisi2 = response2.json()

    for key in json_verisi2[0]:
        print(key, json_verisi2[0][key])

hava()