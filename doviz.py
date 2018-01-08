import requests

def doviz():
    url = "http://api.fixer.io/latest?base="

    birinci = input("Birinci Döviz : ").upper()
    ikinci = input("İkinci Döviz : ").upper()
    miktar = float(input("Miktar : "))

    response = requests.get(url + birinci)

    json_verisi = response.json()

    print(float(json_verisi["rates"][ikinci]) * miktar)



doviz()