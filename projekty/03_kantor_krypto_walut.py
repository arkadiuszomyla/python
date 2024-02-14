# https://www.coingecko.com/pl/api/documentation
import requests

coinsList = None
currency = 'PLN'

def getCoinList():
    global coinsList
    # {'id': '01coin', 'symbol': 'zoc', 'name': '01coin', 'platforms': {}}
    response = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    if response.ok:
        print("Lista krypto pobrana")
        data = response.json()
        # print(data[0])
        # print("Ilość kryptowalut {}". format(len(data)))
        coinsList = data
    else:
        print("nie pobrano danych")


def findCoinBySymbol(symbol):
    symbol = symbol.lower().strip()
    for coin in coinsList:
        if coin["symbol"] == symbol:
            return coin
    else:
        return None

def getCoinLastMarkedData(coinId):
    #{'pln': 122243.91065935309, 'pln_market_cap': 2367559663414.2305, 'pln_24h_vol': 91295285967.32227, 'pln_24h_change': 3.9804427937896674, 'last_updated_at': 1679602978}
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=" + coinId + "&vs_currencies=" + currency + "&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true&precision=18")
    if response.ok:
        data = response.json()
        return data
    else:
        return None


def getCoinPriceInCurrency(coinId, currency):
    currency = currency.lower().strip()
    markeData = getCoinLastMarkedData(coinId)
    return markeData[coinId][currency]  #zagniezdzony słownik


#getCoinList()
#btcData = findCoinBySymbol('btc')
#print(btcData)
#
#markedData = getCoinLastMarkedData(findCoinBySymbol('btc')['id'])
#print(markedData)
#
#currentPrice = getCoinPriceInCurrency(btcData["id"], currency)
#print("Coin price in " + currency, currentPrice)

print('Witamy w kantorze')

while True:
    coinToExchange = input("Jaką walutę chcesz wymienić???????? lub exit jak koniec ")
    if coinToExchange == 'exit':
        break

    getCoinList()
    coinData = findCoinBySymbol(coinToExchange)

    if coinToExchange == None:
        print("Nie ma takiej kryptowaluty")
        continue

    coinPrice = getCoinPriceInCurrency(coinData["id"], currency)
    print("Cena " + str(coinData["id"]), coinPrice, currency)

    moneyToBuyCrypto = float(input("Ile chcesz przeznaczyć na zakup? "))
    boughtCrypto = moneyToBuyCrypto / coinPrice

    print("\nKupiłeś " + str(boughtCrypto) + coinToExchange)