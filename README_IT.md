# CMCAPI v1.0 : CoinMarketCapAPI Wrapper

**cmcapi**è un wrapper molto facile da usare e riduce alle seguenti funzionalità di recupero delle informazioni minime:
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

# Versione e installazione Python

 - Sviluppa per Python 3.6.4 (Linux e Windows)
 - L'installazione è obsoleta, copia semplicemente il file [cmcapi.py](https://github.com/damballah/cmcapi/blob/master/cmcapi.py) nella radice del tuo progetto.


## uso

Una volta copiato il file  [cmcapi.py](https://github.com/damballah/cmcapi/blob/master/cmcapi.py) nella root del progetto, modifica il file Python principale e chiama il modulo come segue:

**`from cmcapi import cmc`**

## Crea un nuovo oggetto *cmc*
Per inizializzare un nuovo oggetto ***cmc***, basta seguire questo esempio con il bitcoin:

**`btc=cmc("btc","usd")`**

Non devi inserire la valuta "*usd*" come parametro e puoi lasciarlo vuoto.

esempio: **`btc=cmc("btc","")`**

Tuttavia, per impostazione predefinita, le informazioni saranno in dollari, è possibile scegliere tra le seguenti valute comuni:

*AUD, BRL, CAD, CHF, CLP, CNY, CZK, DKK, EUR, GBP, HKD, HUF, IDR, ILS, INR, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PKR, PLN, RUB, SEK, SGD, THB, TRY, TWD, ZAR*. 

E per le criptovalute, le seguenti: *BTC, ETH XRP, LTC, BCH*.

## Un caso concreto in uso

Voglio recuperare il tasso di cambio per 24 ore su Ethereum:

    eth=cmc("eth","eur")
    chg24=eth.change24h
    print(chg24)
    
Risultato alla data 27/10/2018 alle 10:52 ---> 0,42

## Esempio completo con tutte le informazioni recuperabili e convertite in euro sull'XRP
Copia e incolla il seguente esempio per provare **cmcapi** dove puoi scaricare direttamente il file [test.py](https://github.com/damballah/cmcapi/blob/master/test.py).

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
Risultato: 

![Résultat](https://github.com/damballah/cmcapi/blob/master/Capture_resultat_exemple_complet_cmcapi.PNG)



