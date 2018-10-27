# CMCAPI v1.0 : CoinMarketCapAPI Wrapper

**cmcapi**es un contenedor muy fácil de usar y se reduce a las siguientes funciones de recuperación de información mínima:
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

# Versión e instalación de Python

 - Desarrollar para Python 3.6.4 (Linux y Windows)
 - La instalación es anticuada, simplemente copie el archivo [cmcapi.py](https://github.com/damballah/cmcapi/blob/master/cmcapi.py) a la raíz de su proyecto.


## utilizar

Una vez que el archivo  [cmcapi.py](https://github.com/damballah/cmcapi/blob/master/cmcapi.py) se copie en la raíz de su proyecto, edite su archivo principal de Python y llame al módulo de la siguiente manera:

**`from cmcapi import cmc`**

## Crear un nuevo objeto *cmc*
Para inicializar un nuevo objeto ***cmc***, simplemente siga este ejemplo con el bitcoin:

**`btc=cmc("btc","usd")`**

No tiene que ingresar la moneda "*usd*" como parámetro y puede dejarla vacía.

ejemplo: **`btc=cmc("btc","")`**

Sin embargo, de forma predeterminada, la información estará en usd, puede elegir entre las siguientes monedas comunes:

*AUD, BRL, CAD, CHF, CLP, CNY, CZK, DKK, EUR, GBP, HKD, HUF, IDR, ILS, INR, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PKR, PLN, RUB, SEK, SGD, THB, TRY, TWD*. 

Y para las monedas criptográficas, las siguientes: *ZAR, BTC, ETH XRP, LTC, BCH*.

## Un caso concreto en uso

Quiero recuperar el tipo de cambio durante 24 horas en Ethereum: 

    eth=cmc("eth","eur")
    chg24=eth.change24h
    print(chg24)
    
Resultado en la fecha 27/10/2018 a las 10:52 ---> 0.42

## Ejemplo completo con toda la información recuperable y convertida en euros en el XRP
Copie y pegue el siguiente ejemplo para probar **cmcapi** donde puede descargar directamente el archivo [test.py](https://github.com/damballah/cmcapi/blob/master/test.py).

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
Resultado: 

![Résultat](https://github.com/damballah/cmcapi/blob/master/Capture_resultat_exemple_complet_cmcapi.PNG)



