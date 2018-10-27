# CMCAPI v1.0 : CoinMarketCapAPI Wrapper

**cmcapi** is a very easy-to-use wrapper and reduces to the following minimal information retrieval features:
 - id
 - name
 - symbol
 - website slug
 - rank
 - circulating_supply
 - total_supply
 - max_supply
 - price
 - market_cap
 - volume_24h
 - percent_change_1h
 - percent_change_24h
 - percent_change_7d

# Python Version and Installation

 - Develop for Python 3.6.4 (Linux and Windows)
 - The installation is old-school, copy the [cmcapi.py](https://github.com/damballah/cmcapi/blob/master/cmcapi.py) file to the root of your project, simply.


## use

Once the  [cmcapi.py](https://github.com/damballah/cmcapi/blob/master/cmcapi.py) file is copied to the root of your project, edit your main Python file, and call the module as follows:

**`from cmcapi import cmc`**

## Create a new *cmc* object
To initialize a new ***cmc*** object, just follow this example with the bitcoin:

**`btc=cmc("btc","usd")`**

You do not have to enter the "*usd*" currency as a parameter and you can leave it empty.

example: **`btc=cmc("btc","")`**

Nevertheless by default, the information will be in *usd*, you can choose between the following common currencies:

*AUD, BRL, CAD, CHF, CLP, CNY, CZK, DKK, EUR, GBP, HKD, HUF, IDR, ILS, INR, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PKR, PLN, RUB, SEK, SGD, THB, TRY, TWD*. 

And for the crypto currencies, the following ones: *ZAR, BTC, ETH XRP, LTC, BCH*.

## A concrete case in use

I want to retrieve the exchange rate for 24 hours on Ethereum: 

    eth=cmc("eth","eur")
    chg24=eth.change24h
    print(chg24)
    
Result on the date 27/10/2018 at 10:52 ---> 0.42

## Exemple complet avec toutes les informations récupérables et converties en euro sur le XRP
Copy and paste the following example to test **cmcapi** where you can directly download the [test.py](https://github.com/damballah/cmcapi/blob/master/test.py) file.

    from cmcapi import cmc
    
    xrp=cmc("xrp","eur")
    
    print("")
    print("INFOS SUR LE XRP : ")
    print("------------------ ")
    print("")
    
    numId="Numéro ID dans l'API CoinMarketCap : "+ xrp.id
    classement="Classé n°" + xrp.rank
    nom="Nom : " + xrp.name
    symbol="Symbole : " + xrp.symbol
    webslug="WebsiteSlug : " + xrp.websiteslug
    marketcap="MarketCap actuel : " + xrp.marketcap + " " + xrp.devise
    circulation="Monnaie en circulation : " + xrp.circulating + " " + xrp.symbol
    coinstotal="Total monnaie : " + xrp.total + " " + xrp.symbol
    maxcreacoin="Maximum prévu : " + xrp.max + " " + xrp.symbol
    prixactuel="Prix actuel : " + xrp.price + " " + xrp.devise
    vol24="Volume échangé en 24h : " + xrp.vol24h + " " + xrp.devise
    tauxChange1h="Taux de change depuis 1h : " + xrp.change1h + "%"
    tauxChange24h="Taux de change depuis 24h : " + xrp.change24h + "%"
    tauxChange7j="Taux de change depuis 7 jours : " + xrp.change7d + "%"
    
    print(numId)
    print(classement)
    print(nom)
    print(symbol)
    print(webslug)
    print("")
    print(marketcap)
    print(circulation)
    print(coinstotal)
    print(maxcreacoin)
    print(prixactuel)
    print("")
    print(vol24)
    print(tauxChange1h)
    print(tauxChange24h)
    print(tauxChange7j)
    print("")
    print("-------------------- ")
    print("FIN DES INFORMATIONS")
    print("")
Result: 

![Résultat](https://github.com/damballah/cmcapi/blob/master/Capture_resultat_exemple_complet_cmcapi.PNG)



