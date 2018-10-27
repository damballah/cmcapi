# CMCAPI : CoinMarketCapAPI v0.1

**cmcapi** est un wrapper très simple d'utilisation et réduit aux fonctionnalités de récupérations d'informations minimales suivantes :
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

# Version Python et Installation

 - Développer pour le Python 3.6.4
 - L'installation est à l'ancienne, copier le fichier [cmcapi.py](https://github.com/damballah/cmcapi/blob/master/cmcapi.py) à la racine de votre projet, tout simplement.


## Utilisation

Une fois le fichier  [cmcapi.py](https://github.com/damballah/cmcapi/blob/master/cmcapi.py) copié à la racine de votre projet, éditer votre fichier Python principal, et appelez le module de la façon suivante : 

**`from cmcapi import cmc`**

## Créer un nouvel objet *cmc*
Pour initialiser un nouvel objet ***cmc***, il vous suffit de suivre cette exemple avec le bitcoin : 

**`btc=cmc("btc","usd")`**

Vous n'êtes pas obligé de saisir en paramètre la devise "*usd*" et vous pouvez laisser celui ci vide.

exemple : **`btc=cmc("btc","")`**

Néanmoins par défaut, les informations seront en *usd*, vous pouvez choisir entre les devises communes suivantes : 

*AUD, BRL, CAD, CHF, CLP, CNY, CZK, DKK, EUR, GBP, HKD, HUF, IDR, ILS, INR, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PKR, PLN, RUB, SEK, SGD, THB, TRY, TWD*. 

Et pour les devises crypto, les suivantes : *ZAR, BTC, ETH XRP, LTC, BCH*.

## Un cas concret dans l'utilisation

Je désire récupérer le taux de change depuis 24h sur de l'Ethereum : 

    eth=cmc("eth","eur")
    chg24=eth.change24h
    print(chg24)
    
Résultat à la date du 27/10/2018 à 10:52 ---> 0.42

## Exemple complet avec toutes les informations récupérables et converties en euro sur le XRP
Copiez-collez l'exemple suivant pour tester **cmcapi** où téléchargez directement le fichier [test.py](https://github.com/damballah/cmcapi/blob/master/test.py).

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
Résultat : 

![Résultat](https://github.com/damballah/cmcapi/blob/master/Capture_resultat_exemple_complet_cmcapi.PNG)



